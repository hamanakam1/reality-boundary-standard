# Reality Boundary Standard

**Make the claim. Show its boundary.**

RBS helps teams turn ambitious ideas into defensible technical claims, bounded experiments, and accountable operations. State what the evidence supports, at the scope it supports, and keep the next proposal visible as a proposal.

**0.1.0-draft · Proposed project standard · 118 requirements · No certification program**

> “Zero disclosures in 400 specified tests on revision X” is a bounded result. “Tenant isolation is guaranteed” needs a different evidentiary basis. RBS makes that boundary explicit.

| Start here | Use it for |
|---|---|
| [Getting started](docs/GETTING_STARTED.md) | Adopt RBS for one claim or workflow |
| [Read the standard](standard/STANDARD.md) | The normative requirements and definitions |
| [Requirement explorer](docs/EXPLORER.md) | Search all 118 requirements offline |
| [Assess conformance](standard/CONFORMANCE.md) | Scope, applicability, evidence review, and outcomes |
| [Worked adoption example](examples/release-review/README.md) | Follow a synthetic claim from wording to review |
| [Boundary examples](docs/BOUNDARY_EXAMPLES.md) | Rewrite misleading claims and define promotion tests |

## Three independent axes

| Axis | Values | Meaning |
|---|---|---|
| Claim class | OBSERVED · DEMONSTRATED · PROPOSED · RESEARCH · SPECULATIVE · UNKNOWN | The kind of statement |
| Support (`truth_status`) | SUPPORTED · UNVERIFIED · DISPUTED · CONTRADICTED | What current evidence supports |
| Deployment | NOT_APPLICABLE · CONCEPT · PROTOTYPE · PILOT · PRODUCTION · RETIRED | Where the implementation is used |

A production service can have an unsupported performance claim. A lab demonstration can support a narrow result without establishing production readiness. A supported design rationale does not establish the proposed implementation.

## Try the reference tools

Python 3.10 or later is required. The record checker, catalog builder, and assessment generator use only the Python standard library.

```bash
# Validate synthetic examples at their deliberately fixed evidence date.
python3 tools/validate_records.py examples/claims.json examples/evidence.json --as-of 2026-10-27

# Create all 118 assessment rows without assigning a passing result.
python3 tools/new_assessment.py /tmp/rbs-assessment.csv \
  --scope "Export workflow, revision to be recorded" --as-of 2026-11-01

# Check the source package and run behavioral tests.
python3 tools/check_repository.py
python3 -m unittest discover -s tests -v
```

The first command reports **structure PASS**, **declared-policy PASS**, and **full conformance NOT_ASSESSED**. All included claim/evidence examples are synthetic. The fixed date makes the example reproducible; evaluate real records at the actual decision date and review overdue evidence.

Record-checker exit codes: `0` for structure/policy pass; `1` for invalid input or policy failure; `2` for incomplete policy review. None establishes factual truth or full RBS conformance.

For full JSON Schema engine checks, install the development dependencies and run the separate schema suite:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/check_schemas.py
```

See [development and CI](docs/DEVELOPMENT.md) for exact check scopes and regeneration commands.

## Use a small record before building a system

1. Choose a consequential claim and split statements with different evidence.
2. Record its scope, three axes, owner, evidence, limitations, and next test.
3. Inspect actual evidence and the requirements triggered by that scope.
4. Publish bounded wording and retain review triggers.

Start with the [claim record](templates/claim-record.md), [experiment record](templates/experiment-record.md), and [assessment template](templates/conformance-assessment.md). A file in an existing repository is enough. The optional JSON format does not capture every normative obligation; retain narrative fields and actual evidence needed for review.

## Coverage

The standard covers provenance, freshness, measurement, inference, research promotion, integration boundaries, authority, recovery, security and privacy, cryptographic evidence, AI evaluation, physical systems, commercial claims, portability, publication, and maintenance. [Applicability guidance](docs/APPLICABILITY.md) helps locate requirements without silently excluding other triggered conditions.

## Project status and participation

RBS is a proposed project standard. It does not claim standards-body recognition, external endorsement, or an authorized “RBS certified” badge. A checker pass is not a conformance assessment.

Source repository: [hamanakam1/reality-boundary-standard](https://github.com/hamanakam1/reality-boundary-standard). Copyright (c) 2026 Michael Hamanaka. The standard and prose use **CC BY 4.0**; reference software, schemas, synthetic JSON examples and configuration use **MIT**. Copied standard paragraphs in generated output retain their prose license. See [LICENSING.md](LICENSING.md), [NOTICE.md](NOTICE.md), and [release-manifest.json](release-manifest.json) for scope and publication records.

Use [CONTRIBUTING.md](CONTRIBUTING.md) for corrections, proposals, and adoption reports; [GOVERNANCE.md](GOVERNANCE.md) for decisions and versioning; and the [roadmap](ROADMAP.md) for the path toward a stable standard. Private engagement material and original speculative narratives stay outside this repository.
