"""Behavioral tests for the limited reference checker, using synthetic records."""

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("rbs_validator", ROOT / "tools/validate_records.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RecordValidationTests(unittest.TestCase):
    def setUp(self):
        self.claims = json.loads((ROOT / "examples/claims.json").read_text())
        self.evidence = json.loads((ROOT / "examples/evidence.json").read_text())
        self.as_of = date(2026, 10, 27)

    def run_check(self):
        return VALIDATOR.validate_records(self.claims, self.evidence, self.as_of)

    def assert_policy_failure(self, fragment):
        result = self.run_check()
        self.assertEqual(result["structure"]["status"], "PASS")
        self.assertEqual(result["policy"]["status"], "FAIL")
        self.assertIn(fragment, json.dumps(result["policy"]["errors"]))
        self.assertEqual(result["full_conformance"], "NOT_ASSESSED")

    def assert_structure_failure(self, fragment):
        result = self.run_check()
        self.assertEqual(result["structure"]["status"], "FAIL")
        self.assertEqual(result["policy"]["status"], "NOT_RUN")
        self.assertIn(fragment, json.dumps(result["structure"]["errors"]))

    def make_production_action(self):
        claim = self.claims[0]
        claim["operational"] = True
        claim["deployment_status"] = "PRODUCTION"
        claim["scope"]["environment"] = "production"
        self.evidence[0]["scope"]["environment"] = "production"
        claim["usage"]["production_dependency"] = True
        claim["authority_not_applicable_reason"] = None
        claim["authority"] = {
            "actions": ["simulate a bounded configuration change"],
            "actor": "synthetic-operator-role",
            "scope": "synthetic fixture only; no real system access",
            "budget": "zero financial spend; one synthetic attempt",
            "revocation": "cancel fixture job and revoke simulated credentials",
            "rollback": "restore the initial fixture state",
        }

    def test_synthetic_scoped_zero_result_is_allowed(self):
        result = self.run_check()
        self.assertEqual(result["structure"]["status"], "PASS")
        self.assertEqual(result["policy"]["status"], "PASS")
        self.assertEqual(result["data_mode"], "SYNTHETIC_DEMONSTRATION")
        self.assertEqual(result["full_conformance"], "NOT_ASSESSED")

    def test_supported_proposal_rationale_is_not_forced_to_claim_execution(self):
        self.assertEqual(self.claims[1]["verification"]["execution_status"], "NOT_EXECUTED")
        self.assertEqual(self.run_check()["policy"]["status"], "PASS")

    def test_proposal_cannot_be_relied_on_as_established_capability(self):
        self.claims[1]["usage"]["customer_promise"] = True
        self.assert_policy_failure("requires a SUPPORTED OBSERVED/DEMONSTRATED claim")

    def test_research_speculative_unknown_cannot_be_established_production_dependency(self):
        original = copy.deepcopy(self.claims[2])
        for kind in ("RESEARCH", "SPECULATIVE", "UNKNOWN"):
            with self.subTest(kind=kind):
                self.claims[2] = copy.deepcopy(original)
                self.claims[2]["claim_class"] = kind
                self.claims[2]["decision_history"][-1]["to_class"] = kind
                self.claims[2]["usage"]["production_dependency"] = True
                self.assert_policy_failure("requires a SUPPORTED OBSERVED/DEMONSTRATED claim")

    def test_unverified_current_capability_cannot_be_customer_promise(self):
        self.claims[0]["truth_status"] = "UNVERIFIED"
        self.claims[0]["usage"]["customer_promise"] = True
        self.assert_policy_failure("requires a SUPPORTED OBSERVED/DEMONSTRATED claim")

    def test_research_only_conflicts_with_established_reliance(self):
        self.claims[0]["usage"]["research_only"] = True
        self.claims[0]["usage"]["customer_promise"] = True
        self.assert_policy_failure("research_only cannot also")

    def test_demonstrated_requires_executed_status_and_result(self):
        self.claims[0]["verification"]["execution_status"] = "NOT_EXECUTED"
        self.claims[0]["verification"]["actual_result"] = None
        self.assert_policy_failure("require declared execution and an actual result")

    def test_demonstrated_requires_reproduction_information(self):
        self.claims[0]["verification"]["reproduction"] = None
        self.assert_policy_failure("requires reproduction instructions")

    def test_supporting_evidence_requires_declared_scope_match(self):
        self.evidence[0]["scope"]["version"] = "different-version"
        self.assert_policy_failure("no supporting evidence declares the same")

    def test_missing_evidence_reference_fails(self):
        self.claims[0]["evidence_ids"] = ["MISSING-EVIDENCE"]
        self.assert_policy_failure("references missing evidence")

    def test_evidence_reference_to_missing_claim_fails(self):
        self.evidence[0]["supports_claim_ids"].append("MISSING-CLAIM")
        self.assert_policy_failure("references a missing claim")

    def test_missing_reciprocal_relationship_fails(self):
        self.evidence[0]["supports_claim_ids"] = []
        self.assert_policy_failure("lacks the reciprocal declared relationship")

    def test_disputed_and_contradicted_need_counterevidence(self):
        for status in ("DISPUTED", "CONTRADICTED"):
            with self.subTest(status=status):
                self.claims[0]["truth_status"] = status
                self.assert_policy_failure("requires counterevidence")

    def test_contradicted_claim_with_counterevidence_can_be_recorded(self):
        self.claims[0]["truth_status"] = "CONTRADICTED"
        self.claims[0]["conflicting_evidence_ids"] = ["EX-EVID-COUNTER"]
        counter = copy.deepcopy(self.evidence[0])
        counter["id"] = "EX-EVID-COUNTER"
        counter["supports_claim_ids"] = []
        counter["contradicts_claim_ids"] = [self.claims[0]["id"]]
        counter["summary"] = "Synthetic counterexample; this record is not permitted as a current operational guarantee."
        self.evidence.append(counter)
        self.assertEqual(self.run_check()["policy"]["status"], "PASS")

    def test_duplicate_record_ids_fail_structure(self):
        self.evidence.append(copy.deepcopy(self.evidence[0]))
        self.assert_structure_failure("duplicate record identifiers")

    def test_duplicate_reference_items_fail_structure(self):
        self.claims[0]["evidence_ids"].append(self.claims[0]["evidence_ids"][0])
        self.assert_structure_failure("duplicate array items")

    def test_unknown_fields_are_not_silently_ignored(self):
        self.claims[0]["hidden_authorization"] = True
        self.assert_structure_failure("unknown fields")

    def test_unknown_nested_fields_are_not_silently_ignored(self):
        self.claims[0]["scope"]["secret_override"] = True
        self.assert_structure_failure("unknown fields")

    def test_boolean_integer_is_not_a_boolean(self):
        self.claims[0]["usage"]["customer_promise"] = 1
        self.assert_structure_failure("expected a boolean")

    def test_missing_required_field_fails(self):
        del self.evidence[0]["method"]
        self.assert_structure_failure("missing fields")

    def test_bad_enum_fails(self):
        self.claims[0]["truth_status"] = "ABSOLUTELY_TRUE"
        self.assert_structure_failure("expected one of")

    def test_unsupported_schema_version_fails(self):
        self.claims[0]["schema_version"] = "99.0"
        self.assert_structure_failure("unsupported schema_version")

    def test_timezone_is_required(self):
        self.claims[0]["as_of"] = "2026-10-27T12:00:00"
        self.assert_structure_failure("explicit time-zone offset")

    def test_invalid_timezone_components_fail_structure(self):
        for offset in ("+00:60", "+00:99", "-00:99", "+23:60", "+24:00", "-24:00"):
            with self.subTest(offset=offset):
                self.claims[0]["as_of"] = "2026-10-27T12:00:00" + offset
                self.assert_structure_failure("explicit time-zone offset")

    def test_unrepresentable_utc_timestamp_fails_structure(self):
        for timestamp in ("0001-01-01T00:00:00+14:00", "9999-12-31T23:59:59-14:00"):
            with self.subTest(timestamp=timestamp):
                self.claims[0]["as_of"] = timestamp
                self.assert_structure_failure("representable in UTC")

    def test_timestamp_boundary_checks_apply_to_all_record_fields(self):
        fields = (
            (self.claims[0], "as_of"),
            (self.claims[0]["decision_history"][0], "at"),
            (self.evidence[0], "collected_at"),
            (self.evidence[0]["source"]["review"], "reviewed_at"),
        )
        for record, key in fields:
            original = record[key]
            for timestamp in ("2026-10-27T12:00:00+00:99", "0001-01-01T00:00:00+14:00"):
                with self.subTest(field=key, timestamp=timestamp):
                    record[key] = timestamp
                    self.assert_structure_failure("explicit time-zone offset")
            record[key] = original

    def test_valid_offsets_preserve_instant_and_utc_date(self):
        expected = VALIDATOR.instant("2026-10-27T00:15:00Z")
        for timestamp in ("2026-10-27T05:45:00+05:30", "2026-10-26T20:45:00-03:30"):
            with self.subTest(timestamp=timestamp):
                structure = VALIDATOR.Structure()
                structure.timestamp(timestamp, "timestamp")
                self.assertEqual(structure.errors, [])
                self.assertEqual(VALIDATOR.instant(timestamp), expected)
                self.assertEqual(VALIDATOR.utc_day(timestamp), date(2026, 10, 27))

    def test_representable_utc_range_boundaries_are_allowed(self):
        for timestamp in ("0001-01-01T14:00:00+14:00", "9999-12-31T09:59:59-14:00"):
            with self.subTest(timestamp=timestamp):
                structure = VALIDATOR.Structure()
                structure.timestamp(timestamp, "timestamp")
                self.assertEqual(structure.errors, [])

    def test_invalid_calendar_date_fails(self):
        self.evidence[0]["review_by"] = "2026-02-31"
        self.assert_structure_failure("valid YYYY-MM-DD")

    def test_stale_evidence_is_incomplete_not_a_pass(self):
        self.as_of = date(2026, 11, 28)
        result = self.run_check()
        self.assertEqual(result["policy"]["status"], "INCOMPLETE")
        self.assertIn("overdue", json.dumps(result["policy"]["incomplete"]))

    def test_future_evidence_fails(self):
        self.evidence[0]["collected_at"] = "2026-10-28T10:00:00Z"
        self.assert_policy_failure("collected after the evaluation date")

    def test_same_day_evidence_after_cutoff_fails(self):
        self.evidence[0]["collected_at"] = "2026-10-27T13:00:00Z"
        self.evidence[0]["source"]["review"]["reviewed_at"] = "2026-10-27T14:00:00Z"
        self.assert_policy_failure("after the claim evidence cutoff")

    def test_counterevidence_after_claim_cutoff_fails(self):
        self.claims[0]["truth_status"] = "DISPUTED"
        self.claims[0]["conflicting_evidence_ids"] = ["EX-EVID-LATE-COUNTER"]
        counter = copy.deepcopy(self.evidence[0])
        counter["id"] = "EX-EVID-LATE-COUNTER"
        counter["supports_claim_ids"] = []
        counter["contradicts_claim_ids"] = [self.claims[0]["id"]]
        counter["collected_at"] = "2026-10-27T13:00:00Z"
        counter["source"]["review"]["reviewed_at"] = "2026-10-27T14:00:00Z"
        self.evidence.append(counter)
        self.assert_policy_failure("after the claim evidence cutoff")
        errors = self.run_check()["policy"]["errors"]
        self.assertTrue(any(error["path"].endswith(".conflicting_evidence_ids") for error in errors))

    def test_review_before_collection_fails(self):
        self.evidence[0]["source"]["review"]["reviewed_at"] = "2026-10-27T09:00:00Z"
        self.assert_policy_failure("review precedes collection")

    def test_restricted_evidence_pointer_with_disclosed_review_is_allowed(self):
        source = self.evidence[0]["source"]
        source["uri"] = "restricted://example-review-vault/fixture-001"
        source["access"] = "RESTRICTED"
        source["review"]["limitations"] = ["Synthetic access restriction example; public users cannot inspect the imagined underlying artifact."]
        self.assertEqual(self.run_check()["policy"]["status"], "PASS")

    def test_unreviewed_restricted_evidence_is_incomplete(self):
        source = self.evidence[0]["source"]
        source["access"] = "RESTRICTED"
        source["review"]["status"] = "NOT_REVIEWED"
        source["review"]["reviewer"] = None
        source["review"]["reviewed_at"] = None
        result = self.run_check()
        self.assertEqual(result["policy"]["status"], "INCOMPLETE")
        self.assertIn("no disclosed review", json.dumps(result["policy"]["incomplete"]))

    def test_null_authority_needs_rationale(self):
        self.claims[0]["authority_not_applicable_reason"] = None
        self.assert_policy_failure("null authority requires")

    def test_operational_claim_needs_authority(self):
        self.claims[0]["operational"] = True
        self.assert_policy_failure("operational action claims require")

    def test_production_fixture_with_declared_controls_passes_only_limited_checks(self):
        self.make_production_action()
        result = self.run_check()
        self.assertEqual(result["policy"]["status"], "PASS")
        self.assertEqual(result["full_conformance"], "NOT_ASSESSED")

    def test_production_version_cannot_be_unknown(self):
        self.make_production_action()
        self.claims[0]["scope"]["version"] = None
        self.evidence[0]["scope"]["version"] = None
        self.assert_policy_failure("production claims need an identified version")

    def test_production_action_cannot_omit_revocation(self):
        self.make_production_action()
        del self.claims[0]["authority"]["revocation"]
        self.assert_structure_failure("missing fields")

    def test_synthetic_evidence_does_not_establish_real_claim(self):
        self.claims[0]["synthetic"] = False
        self.assert_policy_failure("synthetic evidence cannot establish a real")

    def test_synthetic_access_cannot_be_disguised_as_real_test_run(self):
        self.claims[0]["synthetic"] = False
        self.evidence[0]["synthetic"] = False
        self.evidence[0]["source_type"] = "TEST_RUN"
        self.evidence[0]["source"]["access"] = "SYNTHETIC"
        self.assert_policy_failure("synthetic source access must declare synthetic=true")

    def test_empty_claim_set_cannot_pass(self):
        self.claims = []
        self.evidence = []
        self.assert_structure_failure("at least one claim")

    def test_top_level_object_is_rejected(self):
        self.evidence = {"records": self.evidence}
        self.assert_structure_failure("expected a top-level array")

    def test_history_classification_must_match(self):
        self.claims[0]["decision_history"][-1]["to_class"] = "PROPOSED"
        self.assert_policy_failure("last classification does not match")

    def test_json_duplicate_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id":"one","id":"two"}')
            with self.assertRaisesRegex(ValueError, "duplicate JSON object key"):
                VALIDATOR.strict_load(path)

    def test_json_nonfinite_numbers_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nan.json"
            path.write_text('[NaN]')
            with self.assertRaisesRegex(ValueError, "non-finite JSON number"):
                VALIDATOR.strict_load(path)

    def test_cli_bad_json_exits_nonzero_and_reports_not_assessed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{broken')
            process = subprocess.run([sys.executable, str(ROOT / "tools/validate_records.py"), str(path), str(ROOT / "examples/evidence.json"), "--as-of", "2026-10-27"], capture_output=True, text=True)
            self.assertEqual(process.returncode, 1)
            result = json.loads(process.stdout)
            self.assertEqual(result["policy"]["status"], "NOT_RUN")
            self.assertEqual(result["full_conformance"], "NOT_ASSESSED")

    def test_cli_stale_records_exit_two(self):
        process = subprocess.run([sys.executable, str(ROOT / "tools/validate_records.py"), str(ROOT / "examples/claims.json"), str(ROOT / "examples/evidence.json"), "--as-of", "2026-11-28"], capture_output=True, text=True)
        self.assertEqual(process.returncode, 2)
        self.assertEqual(json.loads(process.stdout)["policy"]["status"], "INCOMPLETE")

    def test_cli_timestamp_boundaries_report_structured_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "claims.json"
            for timestamp in ("2026-10-27T12:00:00+00:99", "0001-01-01T00:00:00+14:00", "9999-12-31T23:59:59-14:00"):
                with self.subTest(timestamp=timestamp):
                    self.claims[0]["as_of"] = timestamp
                    path.write_text(json.dumps(self.claims))
                    process = subprocess.run([sys.executable, str(ROOT / "tools/validate_records.py"), str(path), str(ROOT / "examples/evidence.json"), "--as-of", "2026-10-27"], capture_output=True, text=True)
                    self.assertEqual(process.returncode, 1)
                    self.assertEqual(process.stderr, "")
                    result = json.loads(process.stdout)
                    self.assertEqual(result["structure"]["status"], "FAIL")
                    self.assertEqual(result["policy"]["status"], "NOT_RUN")
                    self.assertEqual(result["full_conformance"], "NOT_ASSESSED")


if __name__ == "__main__":
    unittest.main()
