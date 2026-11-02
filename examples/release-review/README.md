# Synthetic walkthrough: an export readiness claim

**Informative, fictional scenario. No application, customer, test run, or independent review is asserted.** This teaches review decisions; it is not operating evidence or a completed assessment.

Initial wording: “Customers can move their entire workspace to any provider in one click.”

The fictional team has a proposed export design and a hypothetical staging demonstration. That basis mixes design, extraction, recipient interoperability, completeness, permissions, attachments, and restoration. Split those propositions before assigning status.

| Claim | Three axes in this scenario | Evidence needed next |
|---|---|---|
| Proposed manifest lists schema version and omitted categories | PROPOSED / SUPPORTED rationale / CONCEPT | Inspect the design; implementation remains separate |
| One staging run emitted declared categories for two fixture tenants | DEMONSTRATED / SUPPORTED in the fictional run / PROTOTYPE | Actual receipt, revision, counts, exclusions and failure cases |
| A recipient can independently restore a full workspace | PROPOSED / UNVERIFIED / CONCEPT | Authorized restore in a specified target with integrity and permissions checks |
| Arbitrary providers support the format in one click | UNKNOWN / UNVERIFIED / NOT_APPLICABLE | Defined provider set, compatibility checks and measured user journey |

These labels describe the fiction, not real results. The machine-readable [proposal fixture](../claims.json) uses the same distinction between supported rationale and unexecuted implementation.

Use the [claim template](../../templates/claim-record.md). A real demonstration would record source/build/deployment revisions, fixture population, exact record denominator, categories and omissions, method, actual results, failures, artifact identity, cutoff, reviewer, and next restore test. Claims do not inherit one another's evidence.

Permitted wording in the fictional scenario: “A specified staging run exported the listed fixture records. Attachments, permissions, historical revisions, and independent restoration have not been demonstrated.”

Stronger wording to withhold: “Complete portability is available to all customers.”

| Requirement | Review focus | Current result |
|---|---|---|
| RBS-REC-03 | Split independent propositions | UNKNOWN |
| RBS-CLS-04 | Actual deployment evidence | UNKNOWN |
| RBS-EVD-03 | Declared synthetic inputs and transformations | UNKNOWN |
| RBS-EXT-01 | Export versus portability | UNKNOWN |
| RBS-EXT-02 | Completeness boundary | UNKNOWN |
| RBS-EXT-03 | Observed independent restore | UNKNOWN |
| RBS-COM-04 | Reuse and publication permissions | UNKNOWN |
| RBS-PUB-01 | Boundary visible at point of use | UNKNOWN |

This teaching subset exempts no other requirement. Generate all rows for a real assessment and justify applicability. Overall status remains **NOT ASSESSED**, even if example record checks pass.

The next bounded experiment uses the [experiment template](../../templates/experiment-record.md): predeclare target, data, identities, scope and authority; export declared categories; restore under an independent operator; compare relationships and permissions; retain failures and omissions. Record the observed result without assuming it. Broader interoperability and commercial availability still need their own evidence and decisions.
