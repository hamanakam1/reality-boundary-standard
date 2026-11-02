"""Meaningful schema-engine checks, separate from the direct policy checker."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_schemas import schema_errors

try:
    import jsonschema
    HAS_ENGINE = True
except ImportError:
    HAS_ENGINE = False


@unittest.skipUnless(HAS_ENGINE, "optional schema suite requires requirements-dev.txt; run tools/check_schemas.py explicitly")
class SchemaContractTests(unittest.TestCase):
    def setUp(self):
        self.schemas = {kind: json.loads((ROOT / f"schemas/{kind}.schema.json").read_text()) for kind in ("claim", "evidence")}
        self.records = {kind: json.loads((ROOT / f"examples/{kind}s.json").read_text()) if kind == "claim" else json.loads((ROOT / "examples/evidence.json").read_text()) for kind in self.schemas}

    def test_examples_pass_both_complete_schemas(self):
        for kind in self.schemas:
            with self.subTest(kind=kind):
                self.assertEqual(schema_errors(self.schemas[kind], self.records[kind]), [])

    def test_invalid_dates_and_timezones_are_rejected_with_formats_enabled(self):
        for field, value in (("as_of", "2026-10-27T12:00:00+00:99"), ("review_by", "2026-02-30")):
            records = copy.deepcopy(self.records["claim"])
            records[0][field] = value
            self.assertTrue(schema_errors(self.schemas["claim"], records))

    def test_unknown_fields_and_missing_required_fields_are_rejected(self):
        for kind in self.schemas:
            for change in ("extra", "missing"):
                records = copy.deepcopy(self.records[kind])
                if change == "extra":
                    records[0]["unexpected"] = True
                else:
                    del records[0]["scope"]
                with self.subTest(kind=kind, change=change):
                    self.assertTrue(schema_errors(self.schemas[kind], records))

    def test_empty_claims_fail_while_empty_evidence_can_be_structurally_valid(self):
        self.assertTrue(schema_errors(self.schemas["claim"], []))
        self.assertEqual(schema_errors(self.schemas["evidence"], []), [])

    def test_schema_pass_does_not_check_references_or_establish_policy(self):
        records = copy.deepcopy(self.records["claim"])
        records[0]["evidence_ids"] = ["MISSING-EVIDENCE"]
        self.assertEqual(schema_errors(self.schemas["claim"], records), [])


if __name__ == "__main__":
    unittest.main()
