# Governance and versioning

## Maintainers and decision rights

The target repository is owned by the GitHub account `hamanakam1`. Its repository owner is the initial decision contact; additional maintainers have not been appointed. Use repository issues and pull requests after publication. Do not infer organization membership, an independent standards committee, or external endorsement from repository ownership. Maintainers own the normative text, schemas, release history, and review process; contributors remain responsible for the provenance and rights of their submissions.

No maintainer can turn absent evidence into proof by approving a pull request. Maintainers can decide the wording, applicability, and procedure of this proposed standard. Empirical claims remain subject to the evidence and its limitations. Publication decisions do not authorize deployments or client actions elsewhere.

## Contribution types

Use a change proposal for normative requirements, schema/policy behavior, or conformance wording. Use a correction for factual errors, broken references, and examples that overstate what evidence establishes. Use an adoption report for ambiguous requirements, disproportionate overhead, or a case where the standard failed to prevent misleading claims.

Each material proposal should identify the problem, affected stable requirement IDs, proposed change, alternatives, expected benefit, adoption cost, evidence an adopter could reasonably supply, and compatibility impact. Include a concrete example and counterexample when they clarify the rule.

## Review

Normative changes should receive a review from someone other than the author where practical. The reviewer checks coherence with the full standard, consequences for existing claim records, realistic applicability, and whether the rule can be assessed. Subject-matter claims may need a qualified domain reviewer. Record the reviewer's access and expertise limits.

Changes to evidence thresholds should be justified by the decision risk and the available verification method. Neither adding forms nor reducing all checks is automatically an improvement. A new requirement should answer a real failure mode; an exception should retain the uncertainty it accepts.

## Disagreement and appeals

Preserve the challenged wording, supporting evidence, counterevidence, and decision rationale. Distinguish factual disagreements from tradeoffs and value judgments. Do not resolve a factual conflict by voting that the desired result is true. Where evidence remains insufficient, keep the claim disputed or unverified and state what would resolve it.

A contributor may request reconsideration by supplying new evidence, a missed counterexample, or a clear applicability problem. Review should focus on the proposition and method rather than the author's status or confidence.

## Versioning

The initial release candidate is `0.1.0-draft`. During the draft series, normative behavior may change; every change still requires a migration note. A published `1.0.0` should follow actual adoption feedback and a coherent conformance review rather than a calendar target.

For this project, major versions change normative meaning or break record compatibility; minor versions add compatible requirements/profiles or capabilities with explicit adoption notes; patch versions correct wording or implementation defects without changing intended conformance. If a change effectively invalidates previously conforming records, treat it as a breaking change regardless of how small the diff looks.

Keep stable IDs for unchanged meanings. Deprecate/supersede an ID when its meaning materially changes; do not recycle it. Pin the standard version in an assessment and preserve historical results under the version actually used.

## Release package

A release includes the normative documents, schema/validator versions, examples and their synthetic status, change log, applicable licensing, maintainers, validation result, unresolved material issues, and a release manifest. Do not include confidential evidence solely to make the repository look complete.

The project may publish an explicitly incomplete draft for review. That is different from claiming scoped conformance or releasing a product under it. Any later badge or assessment service needs separate governance and must not imply an existing certification program.
