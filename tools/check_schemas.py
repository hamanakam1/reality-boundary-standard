#!/usr/bin/env python3
"""Validate supplied schemas and records with a JSON Schema 2020-12 engine.

This checks structure and formats only, not declared policy or conformance.
"""

import argparse
import json
import sys
from pathlib import Path

from validate_records import strict_load

ROOT = Path(__file__).resolve().parents[1]


def schema_errors(schema, records):
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry

    Draft202012Validator.check_schema(schema)
    checker = FormatChecker()
    # Missing optional format dependencies must not silently skip date/URI checks.
    for name, invalid in (("date-time", "not-a-timestamp"), ("date", "2026-02-30"), ("uri", "not a uri")):
        if checker.conforms(invalid, name):
            raise ValueError("format checker unavailable for " + name + "; install requirements-dev.txt")
    validator = Draft202012Validator(schema, format_checker=checker, registry=Registry())
    return [{"path": list(error.absolute_path), "message": error.message}
            for error in validator.iter_errors(records)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claims", type=Path, default=ROOT / "examples/claims.json")
    parser.add_argument("--evidence", type=Path, default=ROOT / "examples/evidence.json")
    args = parser.parse_args(argv)
    report = {"schema_engine": "JSON Schema Draft 2020-12", "schema_validation": "NOT_RUN",
              "errors": [], "policy": "NOT_RUN", "full_conformance": "NOT_ASSESSED"}
    try:
        for kind, path in (("claim", args.claims), ("evidence", args.evidence)):
            errors = schema_errors(strict_load(ROOT / f"schemas/{kind}.schema.json"), strict_load(path))
            report["errors"].extend({"record_type": kind, **error} for error in errors)
        report["schema_validation"] = "FAIL" if report["errors"] else "PASS"
    except ImportError:
        report["errors"].append({"message": "Missing development dependencies; install requirements-dev.txt"})
    except (OSError, UnicodeError, ValueError) as exc:
        report["errors"].append({"message": str(exc)})
    print(json.dumps(report, indent=2))
    return 0 if report["schema_validation"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
