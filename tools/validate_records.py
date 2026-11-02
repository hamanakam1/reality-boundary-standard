#!/usr/bin/env python3
"""Limited RBS record checker. No network, execution of evidence, or truth claims.

This is a direct checker for version 0.1.0 claim/evidence records. It is not a
general JSON Schema evaluator and does not establish full RBS conformance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


SCHEMA_VERSION = "0.1.0"
VALIDATOR_VERSION = "0.1.1"
CLAIM_CLASSES = {"OBSERVED", "DEMONSTRATED", "PROPOSED", "RESEARCH", "SPECULATIVE", "UNKNOWN"}
TRUTH_STATUSES = {"SUPPORTED", "UNVERIFIED", "DISPUTED", "CONTRADICTED"}
DEPLOYMENT_STATUSES = {"NOT_APPLICABLE", "CONCEPT", "PROTOTYPE", "PILOT", "PRODUCTION", "RETIRED"}
SOURCE_TYPES = {"OBSERVATION", "TEST_RUN", "PRIMARY_DOCUMENT", "SOURCE_REVIEW", "ATTESTATION", "SIMULATION", "SYNTHETIC_FIXTURE"}
ACCESS_TYPES = {"PUBLIC", "RESTRICTED", "SYNTHETIC"}
REVIEW_STATUSES = {"NOT_REVIEWED", "SELF_REVIEWED", "INDEPENDENT_REVIEW"}
EXECUTION_STATUSES = {"NOT_EXECUTED", "EXECUTED"}


def instant(timestamp):
    """Parse an explicit-offset timestamp and ensure its UTC instant is usable.

    Python normalizes invalid offset minutes such as +00:99, so lexical
    component bounds must be checked before parsing. UTC conversion can also
    overflow at the datetime range boundaries despite a valid local date.
    """
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?(?:Z|[+-](?:[01][0-9]|2[0-3]):[0-5][0-9])", timestamp):
        raise ValueError("invalid explicit-offset timestamp")
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(timezone.utc)


class Structure:
    """Small direct shape checks; deliberately not a schema interpreter."""

    def __init__(self):
        self.errors = []

    def issue(self, path, message):
        self.errors.append({"path": path, "message": message})

    def obj(self, value, path, fields):
        if type(value) is not dict:
            self.issue(path, "expected an object")
            return False
        missing = set(fields) - set(value)
        extra = set(value) - set(fields)
        if missing:
            self.issue(path, "missing fields: " + ", ".join(sorted(missing)))
        if extra:
            self.issue(path, "unknown fields: " + ", ".join(sorted(extra)))
        return not missing

    def text(self, value, path, nullable=False):
        if value is None and nullable:
            return True
        if type(value) is not str or not value.strip():
            self.issue(path, "expected a nonempty string" + (" or null" if nullable else ""))
            return False
        return True

    def boolean(self, value, path):
        if type(value) is not bool:
            self.issue(path, "expected a boolean")

    def enum(self, value, path, values, nullable=False):
        if nullable and value is None:
            return
        if type(value) is not str or value not in values:
            self.issue(path, "expected one of: " + ", ".join(sorted(values)))

    def strings(self, value, path, minimum=0):
        if type(value) is not list:
            self.issue(path, "expected an array")
            return
        if len(value) < minimum:
            self.issue(path, f"expected at least {minimum} item(s)")
        for index, item in enumerate(value):
            self.text(item, f"{path}[{index}]")
        if all(type(x) is str for x in value) and len(set(value)) != len(value):
            self.issue(path, "duplicate array items")

    def timestamp(self, value, path, nullable=False):
        if value is None and nullable:
            return
        if not self.text(value, path):
            return
        try:
            instant(value)
        except (ValueError, OverflowError):
            self.issue(path, "expected an ISO 8601 date-time with an explicit time-zone offset, representable in UTC")

    def day(self, value, path):
        if not self.text(value, path):
            return
        try:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError
            date.fromisoformat(value)
        except ValueError:
            self.issue(path, "expected a valid YYYY-MM-DD date")

    def scope(self, value, path):
        fields = {"system", "environment", "version", "population", "time_window", "conditions", "exclusions"}
        if not self.obj(value, path, fields):
            return
        for key in ("system", "environment", "population", "time_window"):
            self.text(value[key], f"{path}.{key}")
        self.text(value["version"], f"{path}.version", nullable=True)
        self.strings(value["conditions"], f"{path}.conditions")
        self.strings(value["exclusions"], f"{path}.exclusions")

    def base(self, value, path):
        if value["schema_version"] != SCHEMA_VERSION:
            self.issue(f"{path}.schema_version", f"unsupported schema_version; expected {SCHEMA_VERSION}")
        self.text(value["id"], f"{path}.id")
        self.boolean(value["synthetic"], f"{path}.synthetic")

    def claim(self, value, path):
        fields = {"schema_version", "id", "synthetic", "statement", "claim_class", "truth_status", "deployment_status", "scope", "owner", "as_of", "review_by", "evidence_ids", "conflicting_evidence_ids", "limitations", "verification", "operational", "authority", "authority_not_applicable_reason", "usage", "classification_rationale", "decision_history"}
        if not self.obj(value, path, fields):
            return
        self.base(value, path)
        for key in ("statement", "owner", "classification_rationale"):
            self.text(value[key], f"{path}.{key}")
        self.enum(value["claim_class"], f"{path}.claim_class", CLAIM_CLASSES)
        self.enum(value["truth_status"], f"{path}.truth_status", TRUTH_STATUSES)
        self.enum(value["deployment_status"], f"{path}.deployment_status", DEPLOYMENT_STATUSES)
        self.scope(value["scope"], f"{path}.scope")
        self.timestamp(value["as_of"], f"{path}.as_of")
        self.day(value["review_by"], f"{path}.review_by")
        for key in ("evidence_ids", "conflicting_evidence_ids"):
            self.strings(value[key], f"{path}.{key}")
        self.strings(value["limitations"], f"{path}.limitations", minimum=1)
        self.boolean(value["operational"], f"{path}.operational")
        self.text(value["authority_not_applicable_reason"], f"{path}.authority_not_applicable_reason", nullable=True)
        authority = value["authority"]
        if authority is not None:
            keys = {"actions", "actor", "scope", "budget", "revocation", "rollback"}
            if self.obj(authority, f"{path}.authority", keys):
                self.strings(authority["actions"], f"{path}.authority.actions", minimum=1)
                for key in keys - {"actions"}:
                    self.text(authority[key], f"{path}.authority.{key}")
        verification = value["verification"]
        keys = {"method", "acceptance", "actual_result", "reproduction", "execution_status"}
        if self.obj(verification, f"{path}.verification", keys):
            for key in ("method", "acceptance"):
                self.text(verification[key], f"{path}.verification.{key}")
            for key in ("actual_result", "reproduction"):
                self.text(verification[key], f"{path}.verification.{key}", nullable=True)
            self.enum(verification["execution_status"], f"{path}.verification.execution_status", EXECUTION_STATUSES)
        usage = value["usage"]
        keys = {"customer_promise", "production_dependency", "research_only"}
        if self.obj(usage, f"{path}.usage", keys):
            for key in keys:
                self.boolean(usage[key], f"{path}.usage.{key}")
        history = value["decision_history"]
        if type(history) is not list or not history:
            self.issue(f"{path}.decision_history", "expected a nonempty array")
        else:
            keys = {"at", "from_class", "to_class", "reason", "evidence_ids", "decider"}
            for index, item in enumerate(history):
                here = f"{path}.decision_history[{index}]"
                if not self.obj(item, here, keys):
                    continue
                self.timestamp(item["at"], f"{here}.at")
                self.enum(item["from_class"], f"{here}.from_class", CLAIM_CLASSES, nullable=True)
                self.enum(item["to_class"], f"{here}.to_class", CLAIM_CLASSES)
                self.text(item["reason"], f"{here}.reason")
                self.text(item["decider"], f"{here}.decider")
                self.strings(item["evidence_ids"], f"{here}.evidence_ids")

    def evidence(self, value, path):
        fields = {"schema_version", "id", "synthetic", "title", "source_type", "source", "collected_at", "review_by", "scope", "method", "summary", "artifact_digest", "supports_claim_ids", "contradicts_claim_ids", "transformations", "limitations", "provenance"}
        if not self.obj(value, path, fields):
            return
        self.base(value, path)
        for key in ("title", "method", "summary"):
            self.text(value[key], f"{path}.{key}")
        self.enum(value["source_type"], f"{path}.source_type", SOURCE_TYPES)
        self.timestamp(value["collected_at"], f"{path}.collected_at")
        self.day(value["review_by"], f"{path}.review_by")
        self.scope(value["scope"], f"{path}.scope")
        digest = value["artifact_digest"]
        if digest is not None and (type(digest) is not str or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest)):
            self.issue(f"{path}.artifact_digest", "expected null or sha256: followed by 64 lowercase hex digits; bytes are not verified")
        for key in ("supports_claim_ids", "contradicts_claim_ids", "transformations"):
            self.strings(value[key], f"{path}.{key}")
        self.strings(value["limitations"], f"{path}.limitations", minimum=1)
        provenance = value["provenance"]
        keys = {"collector", "origin", "independence_group"}
        if self.obj(provenance, f"{path}.provenance", keys):
            for key in keys:
                self.text(provenance[key], f"{path}.provenance.{key}")
        source = value["source"]
        if self.obj(source, f"{path}.source", {"uri", "access", "review"}):
            if self.text(source["uri"], f"{path}.source.uri"):
                try:
                    uri = urlsplit(source["uri"])
                    if re.search(r"\s", source["uri"]) or not uri.scheme or not (uri.netloc or uri.path):
                        raise ValueError
                except ValueError:
                    self.issue(f"{path}.source.uri", "expected an absolute URI; no URI is fetched")
            self.enum(source["access"], f"{path}.source.access", ACCESS_TYPES)
            review = source["review"]
            keys = {"status", "reviewer", "reviewed_at", "scope", "limitations"}
            if self.obj(review, f"{path}.source.review", keys):
                self.enum(review["status"], f"{path}.source.review.status", REVIEW_STATUSES)
                self.text(review["reviewer"], f"{path}.source.review.reviewer", nullable=True)
                self.timestamp(review["reviewed_at"], f"{path}.source.review.reviewed_at", nullable=True)
                self.text(review["scope"], f"{path}.source.review.scope")
                self.strings(review["limitations"], f"{path}.source.review.limitations", minimum=1)


def utc_day(timestamp):
    return instant(timestamp).date()


def validate_records(claims, evidence, as_of):
    """Return declared structure/policy results; never claim factual truth."""
    if type(as_of) is not date:
        raise TypeError("as_of must be a datetime.date")
    structure = Structure()
    for name, records, validator in (("claims", claims, structure.claim), ("evidence", evidence, structure.evidence)):
        if type(records) is not list:
            structure.issue(name, "expected a top-level array")
            continue
        if name == "claims" and not records:
            structure.issue(name, "at least one claim is required; empty validation cannot pass")
        for index, record in enumerate(records):
            validator(record, f"{name}[{index}]")
        ids = [x.get("id") for x in records if type(x) is dict and type(x.get("id")) is str]
        if len(ids) != len(set(ids)):
            structure.issue(name, "duplicate record identifiers")
    report = {
        "validator_version": VALIDATOR_VERSION,
        "checked_as_of": as_of.isoformat(),
        "structure": {"status": "FAIL" if structure.errors else "PASS", "errors": structure.errors},
        "policy": {"status": "NOT_RUN", "errors": [], "incomplete": []},
        "full_conformance": "NOT_ASSESSED",
        "limits": "Direct shape and declared-policy checks only. No general JSON Schema evaluation, source retrieval, factual validation, authority verification, or full RBS conformance assessment.",
    }
    if structure.errors:
        return report
    errors, incomplete = report["policy"]["errors"], report["policy"]["incomplete"]

    def fail(path, message):
        errors.append({"path": path, "message": message})

    def unknown(path, message):
        incomplete.append({"path": path, "message": message})

    claim_map = {x["id"]: x for x in claims}
    evidence_map = {x["id"]: x for x in evidence}
    all_records = claims + evidence
    report["data_mode"] = "SYNTHETIC_DEMONSTRATION" if all(x["synthetic"] for x in all_records) else "DECLARED_RECORDS"
    report["counts"] = {"claims": len(claims), "evidence": len(evidence)}
    if report["data_mode"] == "SYNTHETIC_DEMONSTRATION":
        report["synthetic_notice"] = "These fixtures demonstrate validator behavior only; they are not operating evidence or a product assessment."

    for item in evidence:
        here = "evidence:" + item["id"]
        collected_day = utc_day(item["collected_at"])
        if collected_day > as_of:
            fail(here, "evidence was collected after the evaluation date")
        if date.fromisoformat(item["review_by"]) < collected_day:
            fail(here, "review_by precedes collection")
        if date.fromisoformat(item["review_by"]) < as_of:
            unknown(here, "evidence review is overdue; freshness requires human reassessment")
        for key, inverse in (("supports_claim_ids", "evidence_ids"), ("contradicts_claim_ids", "conflicting_evidence_ids")):
            for claim_id in item[key]:
                if claim_id not in claim_map:
                    fail(here + "." + key, "references a missing claim: " + claim_id)
                elif item["id"] not in claim_map[claim_id][inverse]:
                    fail(here + "." + key, "claim lacks the reciprocal declared relationship: " + claim_id)
        review = item["source"]["review"]
        if review["status"] != "NOT_REVIEWED":
            if review["reviewer"] is None or review["reviewed_at"] is None:
                fail(here + ".source.review", "a declared review requires a reviewer and review timestamp")
            elif utc_day(review["reviewed_at"]) > as_of:
                fail(here + ".source.review", "review is dated after the evaluation date")
            elif instant(review["reviewed_at"]) < instant(item["collected_at"]):
                fail(here + ".source.review", "review precedes collection")
        elif review["reviewer"] is not None or review["reviewed_at"] is not None:
            fail(here + ".source.review", "NOT_REVIEWED conflicts with a declared completed reviewer/timestamp")
        if item["source"]["access"] == "RESTRICTED" and review["status"] == "NOT_REVIEWED":
            unknown(here + ".source.review", "restricted evidence has no disclosed review; access alone is not verification")
        if item["source_type"] == "SYNTHETIC_FIXTURE" and not item["synthetic"]:
            fail(here, "a synthetic fixture must declare synthetic=true")
        if item["source"]["access"] == "SYNTHETIC" and not item["synthetic"]:
            fail(here, "synthetic source access must declare synthetic=true")

    for item in claims:
        here = "claim:" + item["id"]
        observed_day = utc_day(item["as_of"])
        if observed_day > as_of:
            fail(here, "claim as_of is after the evaluation date")
        if date.fromisoformat(item["review_by"]) < observed_day:
            fail(here, "review_by precedes claim as_of")
        if date.fromisoformat(item["review_by"]) < as_of:
            unknown(here, "claim review is overdue; freshness requires human reassessment")
        history = item["decision_history"]
        if history[-1]["to_class"] != item["claim_class"]:
            fail(here + ".decision_history", "last classification does not match claim_class")
        history_times = [datetime.fromisoformat(x["at"].replace("Z", "+00:00")) for x in history]
        if history_times != sorted(history_times):
            fail(here + ".decision_history", "decision history is not chronological")
        for decision in history:
            if utc_day(decision["at"]) > as_of:
                fail(here + ".decision_history", "decision is dated after the evaluation date")
            for evidence_id in decision["evidence_ids"]:
                if evidence_id not in evidence_map:
                    fail(here + ".decision_history", "references missing evidence: " + evidence_id)
        for key, inverse in (("evidence_ids", "supports_claim_ids"), ("conflicting_evidence_ids", "contradicts_claim_ids")):
            for evidence_id in item[key]:
                related = evidence_map.get(evidence_id)
                if related is None:
                    fail(here + "." + key, "references missing evidence: " + evidence_id)
                elif item["id"] not in related[inverse]:
                    fail(here + "." + key, "evidence lacks the reciprocal declared relationship: " + evidence_id)
                elif not item["synthetic"] and related["synthetic"] and item["claim_class"] in {"OBSERVED", "DEMONSTRATED"}:
                    fail(here, "synthetic evidence cannot establish a real observational or demonstrated claim")
        if item["truth_status"] == "SUPPORTED" and not item["evidence_ids"]:
            fail(here, "SUPPORTED requires at least one supporting evidence reference")
        if item["truth_status"] in {"DISPUTED", "CONTRADICTED"} and not item["conflicting_evidence_ids"]:
            fail(here, "DISPUTED or CONTRADICTED requires counterevidence")
        if item["claim_class"] in {"OBSERVED", "DEMONSTRATED"}:
            if not item["evidence_ids"]:
                fail(here, "observed/demonstrated claims require evidence")
            matching = [evidence_map[eid] for eid in item["evidence_ids"] if eid in evidence_map and all(evidence_map[eid]["scope"][key] == item["scope"][key] for key in ("system", "environment", "version"))]
            if not matching:
                fail(here, "no supporting evidence declares the same system, environment, and version")
            verification = item["verification"]
            if verification["execution_status"] != "EXECUTED" or verification["actual_result"] is None:
                fail(here + ".verification", "observed/demonstrated claims require declared execution and an actual result")
            if item["claim_class"] == "DEMONSTRATED" and verification["reproduction"] is None:
                fail(here + ".verification", "a demonstration requires reproduction instructions or access procedure")
        usage = item["usage"]
        operational_use = usage["customer_promise"] or usage["production_dependency"]
        if operational_use:
            if item["truth_status"] != "SUPPORTED" or item["claim_class"] not in {"OBSERVED", "DEMONSTRATED"}:
                fail(here + ".usage", "a production dependency or customer capability promise requires a SUPPORTED OBSERVED/DEMONSTRATED claim")
            if usage["research_only"]:
                fail(here + ".usage", "research_only cannot also be a production dependency or customer promise")
        if item["authority"] is None:
            if item["authority_not_applicable_reason"] is None:
                fail(here + ".authority", "null authority requires an explicit non-action rationale")
            if item["operational"]:
                fail(here + ".authority", "operational action claims require declared authority, limits, revocation, and recovery")
        elif item["authority_not_applicable_reason"] is not None:
            fail(here + ".authority", "authority and a not-applicable rationale are mutually exclusive")
        if item["deployment_status"] == "PRODUCTION":
            if item["scope"]["version"] is None:
                fail(here + ".scope.version", "production claims need an identified version")
            if item["claim_class"] in {"PROPOSED", "RESEARCH", "SPECULATIVE", "UNKNOWN"} and item["operational"]:
                fail(here, "split an unverified proposed/research capability from the production action claim")
        for relationship in ("evidence_ids", "conflicting_evidence_ids"):
            for evidence_id in item[relationship]:
                related = evidence_map.get(evidence_id)
                if related and instant(related["collected_at"]) > instant(item["as_of"]):
                    fail(here + "." + relationship, "referenced evidence was collected after the claim evidence cutoff")

    report["policy"]["status"] = "FAIL" if errors else "INCOMPLETE" if incomplete else "PASS"
    return report


def strict_load(path):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON object key: " + key)
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError("non-finite JSON number is not permitted: " + value)

    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique_object, parse_constant=reject_constant)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("claims", help="JSON array of claim records")
    parser.add_argument("evidence", help="JSON array of evidence records")
    parser.add_argument("--as-of", required=True, type=date.fromisoformat, help="YYYY-MM-DD; freshness evaluated by UTC calendar date")
    args = parser.parse_args(argv)
    try:
        report = validate_records(strict_load(args.claims), strict_load(args.evidence), args.as_of)
    except (OSError, UnicodeError, ValueError) as exc:
        report = {
            "validator_version": VALIDATOR_VERSION,
            "structure": {"status": "FAIL", "errors": [{"path": "input", "message": str(exc)}]},
            "policy": {"status": "NOT_RUN", "errors": [], "incomplete": []},
            "full_conformance": "NOT_ASSESSED",
        }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if report["structure"]["status"] != "PASS" or report["policy"]["status"] == "FAIL":
        return 1
    if report["policy"]["status"] != "PASS":
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
