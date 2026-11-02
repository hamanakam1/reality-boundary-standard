# Development and verification

Python 3.10+ runs the reference tools. Only the optional full schema engine needs an installed package. No tool retrieves evidence, executes submitted code, or grants operating authority.

## Checks and their boundaries

| Check | Command | Establishes |
|---|---|---|
| Source package integrity | `python3 tools/check_repository.py` | Strict JSON parsing, local Markdown targets/heading anchors, 118 requirement inventory, exact catalog/explorer generation, file-byte manifest |
| Direct record structure and policy | `python3 tools/validate_records.py examples/claims.json examples/evidence.json --as-of 2026-10-27` | The documented direct checks at the fixed fixture date |
| Behavioral tests | `python3 -m unittest discover -s tests -v` | Tested parser, policy, assessment-generation and integrity boundaries; optional schema tests explicitly skip if dependencies are absent |
| Full schema engine | `.venv/bin/python tools/check_schemas.py` | The supplied Draft 2020-12 schemas accept the supplied examples, with date/date-time/URI format checking enabled |
| Complete suite with schema tests | `.venv/bin/python -m unittest discover -s tests -v` | Behavioral checks plus schema contract tests, with dependencies installed |

Every row is narrower than factual verification or substantive RBS conformance. Repository link checking covers inline relative Markdown links outside fenced code; it does not crawl external sites or validate every HTML link. The file manifest checks bytes, not authorship or rights.

The schema engine and direct checker are separate implementations. The engine evaluates the schema documents; the checker additionally applies declared record-reference, chronology, freshness, and operational-use policy. Their accepted inputs need not be identical: the direct checker intentionally imposes stricter timestamp range checks. A schema pass with a missing evidence relationship can still fail policy.

The schema checker uses a registry without remote retrieval. Missing schema dependencies or unavailable required format checkers fail explicitly. It does not inspect evidence sources.

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/check_schemas.py
.venv/bin/python -m unittest discover -s tests -v
```

The package is pinned in [requirements-dev.txt](../requirements-dev.txt). Schema-engine behavior follows the [jsonschema validation API](https://python-jsonschema.readthedocs.io/en/stable/validate/), with explicit format validation rather than relying on its default annotation behavior.

## Edit and regenerate

Edit normative wording in [STANDARD.md](../standard/STANDARD.md), retain stable IDs, and follow [governance](../GOVERNANCE.md). Do not edit derived requirements or explorer output directly.

```bash
python3 tools/build_catalog.py
python3 tools/check_repository.py --write-manifest
python3 tools/check_repository.py
```

Regenerate the manifest after all intentional source edits. It excludes itself, Git internals, local environments, caches and verification-output directories. A changed, added, or missing source file fails verification until the manifest is intentionally refreshed. Symlinks are rejected. Keep verification receipts under `.artifacts/` or outside the repository so they do not create a self-referential manifest.

## CI

The [verification workflow](../.github/workflows/verify.yml) declares Python 3.10, 3.12 and 3.14 jobs. Each installs the schema engine and runs repository, schema, policy and behavioral checks. GitHub Action revisions are pinned, checkout does not persist credentials, permissions are read-only, and there is no deployment or publication job. Syntax follows the [GitHub workflow reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

A configured workflow is not a successful run. Report actual remote results against the exact published commit after publication. Local browser inspection of the explorer is a separate check from generated-byte verification and JavaScript parsing.
