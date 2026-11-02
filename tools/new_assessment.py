#!/usr/bin/env python3
"""Create an unassessed CSV matrix covering every requirement; never assigns PASS."""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

from build_catalog import ROOT, catalog

FIELDS = ["standard_version", "requirement_id", "scope", "evidence_cutoff", "applicability",
          "applicability_rationale", "result", "claim_ids", "evidence_ids", "reviewer",
          "reviewed_at", "gap_or_exception", "next_action", "requirement_text"]


def write_matrix(output, scope, cutoff):
    if not scope.strip():
        raise ValueError("scope cannot be blank")
    data = catalog((ROOT / "standard/STANDARD.md").read_bytes())
    # Exclusive creation prevents overwriting an existing assessment or symlink target.
    with Path(output).open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for row in data["requirements"]:
            writer.writerow({"standard_version": data["standard_version"], "requirement_id": row["id"],
                             "scope": scope, "evidence_cutoff": cutoff.isoformat(),
                             "applicability": "UNREVIEWED", "result": "UNKNOWN",
                             "next_action": "Determine applicability and inspect relevant evidence",
                             "requirement_text": row["text"]})
    return len(data["requirements"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--as-of", required=True, type=date.fromisoformat,
                        help="UTC evidence-cutoff day; add exact timestamp in the assessment narrative")
    args = parser.parse_args(argv)
    try:
        count = write_matrix(args.output, args.scope, args.as_of)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(f"Created {count} UNKNOWN rows at {args.output}. Overall conformance: NOT ASSESSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
