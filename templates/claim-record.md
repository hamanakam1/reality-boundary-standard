# Claim record template

This human-readable template is not an executable JSON fixture. For the exact machine record fields, including `synthetic`, `operational`, and `authority_not_applicable_reason`, use [the claim schema](../schemas/claim.schema.json), [synthetic examples](../examples/claims.json), and [validator contract](../docs/VALIDATOR.md). A completed template still requires substantive evidence review.

**Template version:** RBS 0.1.0-draft  
**Purpose:** Maintain a scoped claim without confusing evidence, intent, and deployment.  
**Usage:** Replace placeholders with actual information. Use `unknown` where appropriate. This template is not itself a verified claim or a conformance assessment.

## 1. Identity and statement

| Field | Value |
|---|---|
| `schema_version` | Version expected by the selected machine-readable schema |
| `id` | Stable claim identifier |
| `statement` | One precise statement that can be evaluated |
| `owner` | Accountable person or role |
| `as_of` | Evidence cutoff with time zone |
| `review_by` | Next scheduled review, or an explicit rationale if only event-triggered review applies |
| Intended decision | What someone will decide using this claim |
| Permitted wording | Exact language the evidence supports |
| Stronger wording not established | Important claims that must not be inferred |

Split the record if it combines distinct propositions such as model availability, local execution, privacy, latency, economics, and production deployment.

## 2. Classification

| Field | Choose one and explain |
|---|---|
| `claim_class` | `OBSERVED`, `DEMONSTRATED`, `PROPOSED`, `RESEARCH`, `SPECULATIVE`, or `UNKNOWN` |
| `truth_status` | `SUPPORTED`, `UNVERIFIED`, `DISPUTED`, or `CONTRADICTED` |
| `deployment_status` | `NOT_APPLICABLE`, `CONCEPT`, `PROTOTYPE`, `PILOT`, `PRODUCTION`, or `RETIRED` |
| `classification_rationale` | Why these values fit this exact statement; include limitations |

The axes are independent. `PRODUCTION` does not mean correct. `SUPPORTED` does not mean certain. `PROPOSED` does not mean implemented. A speculative story with verified authorship is not evidence that its fictional capabilities exist.

## 3. Scope

| Scope field | Value or explicit unknown |
|---|---|
| `scope.system` | Product/component/workflow being evaluated |
| `scope.environment` | Development, test, pilot, production, simulation, or another defined environment |
| `scope.version` | Relevant source/build/deployment/model/configuration revisions |
| `scope.population` | Tenants, users, roles, records, tasks, or equipment covered |
| `scope.time_window` | Observation, test, or effective interval with time zones |
| `scope.conditions` | Workload, hardware, dependencies, inputs, setup, rights, or other conditions |
| `scope.exclusions` | Explicit boundaries of the conclusion |

If a location, jurisdiction, data category, identity role, provider account, or business rule affects interpretation, record it in the appropriate scope field. Do not place secrets or unnecessary personal data here.

## 4. Evidence and counterevidence

| Field | Value |
|---|---|
| `evidence_ids` | Stable references to supporting evidence records |
| `conflicting_evidence_ids` | Stable references to contrary or conflicting evidence; empty only after considering the issue |
| Attributed statements | Who reported what, and whether independent verification occurred |
| Inference | Explicit reasoning from evidence to conclusion |
| Source independence | Whether evidence shares an origin, pipeline, author, or instrument |
| Redactions and access | What is withheld, why, and who can review it |
| `limitations` | Missing coverage, uncertainty, known failure modes, inaccessible evidence, and alternative explanations |

Each linked evidence record should identify provenance, capture time, method, relevant version/scope, exact artifact reference, transformations, and access restrictions. A URL by itself may be insufficient if content changes or the cited page does not support the claim.

## 5. Verification

| Field | Value |
|---|---|
| `verification.method` | Executed or proposed method; label which |
| `verification.acceptance` | Conditions that would support the claim, defined before execution where feasible |
| `verification.actual_result` | Actual observed result; use “not executed” for a plan |
| `verification.reproduction` | Inputs, versions, procedure, expected outputs, and access needed to repeat the check |
| Quantities | Units, denominator, sample/population, baseline, interval, and uncertainty |
| Contrary result | What finding would weaken, dispute, or contradict the claim |
| Next verification | Smallest useful test or evidence request |

Record failures and excluded runs. Do not substitute a proposed test, a generated screenshot, a schema pass, or an agent’s confidence for an executed evaluation.

## 6. Authority and operation

Fill this section when the claim concerns actions. For a static conceptual claim, `authority` may be null with an explicit rationale in `classification_rationale` or `limitations`.

| Field | Value |
|---|---|
| `authority.actions` | Actions contemplated or executed |
| `authority.actor` | Authorized identity and accountable operator |
| `authority.scope` | Tenant/environment/resource/operation boundaries and source of authority |
| `authority.budget` | Financial, resource, time, concurrency, and retry limits where relevant |
| `authority.revocation` | How authority, credentials, and new work can be stopped or contained |
| `authority.rollback` | Reversal, compensation, reconciliation, or documented irreversibility |
| Outcome observation | How completion and business effect will be established |

Existing valid authorization should be reused. An observed ability to perform an action is not permission to perform it.

## 7. Permitted use

| Field | Value and conditions |
|---|---|
| `usage.customer_promise` | Whether the claim is intended to support an external commitment; identify relevant approval |
| `usage.production_dependency` | Whether live operations rely on the claim; identify consequences if false |
| `usage.research_only` | Whether the claim is restricted to research/exploration |
| Publication boundary | Public, internal, restricted, or another defined audience; actual permissions still govern |

If the values conflict—for example, research-only work is also treated as an unconditional customer promise—resolve the inconsistency before release. Changing a boolean does not supply the missing evidence or authority.

## 8. Decision history and review triggers

| Timestamp | Prior classification | New classification | Evidence/change | Decision owner | Consequence |
|---|---|---|---|---|---|
| Placeholder | Initial record | Placeholder | Evidence IDs or reason | Owner role | Permitted use and next action |

Record this history under `decision_history` in machine-readable records. Review after relevant changes to implementation, deployment, model, provider behavior, business rules, permissions, contract, operating conditions, or contrary evidence. Preserve the historical scope of earlier conclusions.

## 9. Reviewer conclusion

- Record completeness: not reviewed / reviewed, with limitations.
- Structural validation: not run / passed / failed / incomplete, with tool version and result reference.
- Evidence review: not performed / performed, with reviewer and scope.
- Claim wording approved for the stated use: yes / no / conditional, with reason.
- Full RBS conformance: not assessed here unless a separate scoped assessment explicitly covers it.

A structurally valid record can contain false or inadequate evidence. This template organizes judgment; it does not replace it.
