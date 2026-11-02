# Change log

## Unreleased repository foundation — 2026-11-01

- Preserved standard 0.1.0-draft, all 118 requirement meanings/IDs, record schemas 0.1.0, and reference checker 0.1.1.
- Added a focused adoption guide, applicability guide, and synthetic export-review walkthrough.
- Added a reproducible requirement catalog and standalone offline explorer derived from the normative source.
- Added an assessment CSV generator with every row initially unreviewed/unknown and exclusive file creation.
- Added a separate full JSON Schema engine check, schema contract tests, and repository-tool boundary tests.
- Added source/derived-file/link/hash verification, a pinned read-only CI workflow, and contributor issue forms.
- Recorded the existing target repository and owner while retaining the unresolved rights/license decision. Historical October preparation results remain dated historical records.
- Compatibility: informative tooling and documentation only; no normative, schema, or declared record-policy changes. Generated assessment CSVs are new working aids, not record-checker inputs.

## Draft maintenance — 2026-10-28

- Updated the reference checker to 0.1.1; record schemas remain 0.1.0 and normative standard remains 0.1.0-draft.
- Rejected invalid timezone components that Python's parser otherwise normalizes, including `+00:99`.
- Converted UTC range overflow and underflow into structural failures with policy status NOT_RUN instead of an uncaught exception.
- Unified instant parsing and added six behavioral regression tests, including CLI error reporting and valid offset/range preservation. All 51 tests pass locally.
- Refreshed the local verification report and file hashes. Publication inputs remain unresolved; no public release was made.

## 0.1.0-draft — 2026-10-27

- Introduced a three-axis claim classification and 118 stable requirements.
- Added evidence scope/freshness, promotion/demotion, operating authority, and cryptographic/AI/physical-system boundaries.
- Added conformance procedure separating structural checks, policy checks, evidence review, and scoped conformance.
- Added claim/evidence schemas, synthetic examples, a limited reference validator, and misuse-focused checks.
- Added contribution/governance/publication procedures and a maintainer execution prompt.
- Kept client-specific execution materials and speculative source narratives outside the public repository package.

Status: proposed draft; repository owner, maintainers, license, and public publication decision remain to be recorded.
