# Assessing conformance to the Reality Boundary Standard

**Version:** 0.1.0-draft  
**Status:** Proposed assessment procedure for public review  
**Normative source:** [STANDARD.md](STANDARD.md)

## 1. What a conformance statement means

A conformance statement says that an identified body of work was assessed against the applicable requirements of a specific version of the Reality Boundary Standard (RBS), under a disclosed scope and evidence cutoff. It does not certify that the product is universally correct, secure, safe, legally compliant, commercially successful, or approved by a marketplace. It does not establish the factual truth of every supplied evidence item.

RBS is a proposed project standard. Self-assessment is permitted when labeled. Independent assessment requires an identified assessor and a description of their independence, expertise, access, method, and limits. No contributor may imply that a standards body, government agency, cloud provider, or customer endorses this project merely because its materials cite that organization.

The requirements of STANDARD.md control if this procedure or a template is inconsistent. The public reference schemas and validator support only part of the assessment. Their scope is explained in Section 7 below.

## 2. Define the assessment boundary first

Create an assessment record before assigning an outcome. Include:

| Field | Required meaning |
|---|---|
| Assessment ID | Stable identifier for this assessment, not a product version. |
| Standard version | Exact version or immutable release/commit of RBS used. |
| Assessed artifact | Product, document, release, service, operating workflow, or research package being reviewed. |
| Artifact versions | Source, build, deployment, document, model, configuration, and data revisions relevant to conclusions. |
| Intended decisions | How the findings may be used: publication, experiment, pilot, deployment, procurement, or another stated purpose. |
| Environments and populations | Relevant tenants, roles, users, jurisdictions, hardware, operating conditions, and limits. |
| Claim inventory | Material claims in scope and how they were identified. |
| Evidence cutoff | Latest included evidence, expressed with time zone. |
| Reviewer | Person or accountable role, expertise, independence, access limits, and conflicts. |
| Applicable requirements | Requirement IDs and profile/applicability decisions. |
| Exclusions | What is excluded, why, and how the exclusion limits conclusions. |
| Review triggers | Changes or events that require reassessment. |

An assessment may focus on one release or one workflow. It must not be presented as a whole-company or whole-product guarantee if its scope is narrower. Where a future dependency has not been implemented, the assessment can evaluate the quality of the proposal without asserting operational conformance for that future system.

## 3. Applicability profiles

Profiles help identify relevant requirements; they do not create a maturity ranking. More profiles do not automatically mean a better product. Each assessment applies the foundational requirements plus the domain requirements triggered by its scope.

| Profile | When it applies | Main requirement families |
|---|---|---|
| **Claims and publication** | A document, website, report, demo, release note, or public statement uses technical claims. | GOV, REC, CLS, CLM, EVD, TIM, MET, INF, PRM, PUB, REV, RELSE, ADP |
| **Software and integration** | Claims concern implementation, APIs, deployment, data flows, or application workflows. | ARC, REL; relevant SEC, AI, CRY, EXT |
| **Autonomous operations** | Software makes or executes decisions without a fresh human instruction for every action. | AUT, REL; relevant ARC, SEC, AI, CRY |
| **Security, privacy, and multi-tenancy** | Claims concern protection, isolation, sensitive data, local operation, or data rights. | SEC; relevant ARC, EVD, CRY, EXT |
| **AI capability and learning** | Claims concern models, agents, evaluation, prediction, feedback, or training. | AI; relevant MET, INF, AUT, SEC |
| **Cryptographic evidence** | Claims rely on signatures, receipts, provenance, append-only logs, or formal proof. | CRY; relevant EVD, TIM, REL |
| **Commercial and marketplace** | Claims concern listing, pricing, contracts, approvals, compliance, resale, or unit economics. | COM; relevant AUT, SEC, EXT |
| **Physical and resource systems** | Claims concern energy, matter, robotics, fabrication, hardware control, or simulation-to-reality. | PHY; relevant MET, AUT, REL, SEC |
| **Portability and continuity** | Claims concern export, backup, restore, escrow, migration, ownership transfer, or exit. | EXT; relevant REL, SEC, COM |

A profile’s “main families” are navigation aids. Review every requirement whose condition applies. For example, publishing a software export claim can trigger security, commercial rights, and portability requirements even if the assessment initially selected only the software profile.

## 4. Requirement-by-requirement outcomes

Use one of these statuses for each applicable requirement:

| Status | Meaning | Effect on conformance |
|---|---|---|
| **PASS** | Relevant evidence supports satisfaction within the assessment scope. | Counts toward satisfaction of the requirement. |
| **FAIL** | Evidence shows a requirement is not satisfied. | An applicable MUST failure prevents a conformance claim. |
| **UNKNOWN** | Required evidence is missing, unavailable, stale, or insufficient. | An applicable MUST with unknown satisfaction prevents a conformance claim. |
| **NOT_APPLICABLE** | The triggering condition is absent, with a documented rationale. | Excluded from the applicable denominator; disclose material exclusions. |
| **SHOULD_EXCEPTION** | A recommendation is intentionally not followed, with consequences and rationale recorded. | Permitted when the exception is documented; cannot waive a MUST. |

Do not substitute “mostly compliant” or a numeric score for an unresolved mandatory requirement. Counts may summarize review progress, but the denominator and material open items must remain visible. A document can be useful and ready for discussion while its assessment remains incomplete.

Each result should link to its evidence and reviewer notes. A narrative saying “we use least privilege” does not establish an actual authority boundary. A report that includes a backup diagram does not establish a successful restore. Review the property being claimed rather than the existence of a document about it.

## 5. Evidence review procedure

The following sequence supports a rigorous assessment without requiring a separate tool or platform:

1. **Inventory claims.** Identify material statements in text, diagrams, demonstrations, pricing pages, manifests, and operational policies. Split claims that mix existence, performance, privacy, autonomy, and commercial approval.
2. **Classify each claim.** Assign `claim_class`, `truth_status`, and `deployment_status` independently. Check that wording, evidence, and status agree.
3. **Trace provenance.** Inspect the exact sources, observation methods, timestamps, versions, transformations, and redactions supporting the claim. Distinguish an announcement from demonstrated account access.
4. **Examine contrary evidence.** Look for failed tests, obsolete assumptions, excluded populations, conflicting logs, reviewer disagreement, and conditions that would reverse the conclusion.
5. **Check scope and freshness.** Confirm that evidence describes the environment and version actually being discussed. Historical evidence may still be useful while no longer supporting a current claim.
6. **Evaluate measurement.** Check units, denominator, baseline, workload, uncertainty, repeated runs where needed, and whether reported precision is justified.
7. **Evaluate authority and operation.** For action-capable systems, inspect who may authorize actions, applicable limits, credential revocation, containment, retries, recovery, and observation of actual outcomes.
8. **Evaluate publication rights.** Confirm that public artifacts contain appropriate abstractions, synthetic examples, citations, and authorized material. Private evidence stays appropriately controlled.
9. **Record outcomes.** Assign requirement statuses, explain exclusions, retain accepted limitations, and identify the next useful verification step for each material unknown.
10. **Issue a bounded assessment statement.** State the assessed scope, result, evidence cutoff, limitations, and review triggers. Preserve enough provenance for a later reviewer to understand the conclusion.

Verification depth follows consequence. Repeating a low-impact check until it produces an impressive volume of evidence adds little. A new contradictory observation or an untested critical failure path is a concrete reason to expand the review.

## 6. Assessment outcomes and wording

Use one of four overall outcomes. If applicable requirements include both FAIL and UNKNOWN, NONCONFORMING takes precedence and the report must also disclose incomplete coverage. Otherwise, an applicable UNKNOWN or unfinished required review yields ASSESSMENT INCOMPLETE. NOT ASSESSED applies when no substantive conformance assessment has begun; running structural checks alone does not begin that assessment.

- **CONFORMING WITHIN STATED SCOPE:** Every applicable MUST has PASS; all not-applicable decisions and SHOULD exceptions are justified; the evidence and assessment record are complete enough to support the stated scope.
- **NONCONFORMING:** At least one applicable MUST has FAIL. The report identifies the failed requirements and needed changes.
- **ASSESSMENT INCOMPLETE:** At least one applicable MUST is UNKNOWN or the required review has not been completed. This is not a failed product claim unless evidence establishes failure.
- **NOT ASSESSED:** The materials are prepared, structurally checked, or proposed, but a conformance assessment has not been performed.

Suggested wording for a completed assessment:

> This is a [self-assessment / independent assessment] against Reality Boundary Standard 0.1.0-draft. It covers [exact artifacts, versions, environments, and intended use] using evidence through [timestamp]. The result is [outcome]. Material exclusions, accepted recommendation exceptions, unresolved issues, and review triggers are listed in [assessment reference]. This statement does not certify general product correctness, security, regulatory compliance, or external approval.

Suggested wording for structural validation only:

> The supplied records passed the reference validator’s structural and declared-policy checks. Their factual accuracy, evidence sufficiency, operating effectiveness, and full conformance to the Reality Boundary Standard have not been established by that result.

Do not issue an unqualified “RBS certified” badge. This project does not operate a certification authority. Any future independent certification program would need its own governance, assessor qualifications, dispute process, scope rules, and rights to use its marks.

## 7. Limits of the reference schemas and validator

The reference `claim.schema.json` and `evidence.schema.json` support consistent data records. A policy validator can use those records to flag missing fields, invalid enums, unresolved evidence references, declared contradictory status, missing authority information, or a research-only item incorrectly marked as an established capability promise. Exact checks are defined by the versioned validator, not inferred from this document.

The reference operational-claim policy is deliberately conservative: its production-dependency and customer-promise flags mean reliance on an already established operational capability. An explicitly qualified experiment, accepted research uncertainty, or conditional future milestone belongs in a separate accountable decision record. RBS-PRM-05 permits such a research dependency only with explicit acceptance of uncertainty; the limited reference checker does not evaluate that acceptance. A reference-policy failure therefore must not automatically be labeled normative RBS nonconformance. Identify the actual normative requirement and review its evidence and applicability separately.

These checks are deliberately limited. An automated pass cannot establish that:

- a claimed test was actually executed;
- an evidence artifact is authentic, complete, independent, or representative;
- a claim’s support status is correctly assigned;
- private evidence has been reviewed by a competent person;
- a test covers the relevant failure modes or affected population;
- an authority grant is valid or an operational control is effective;
- customer, contractual, regulatory, or publication rights exist;
- a cryptographic record establishes truth beyond its verification boundary;
- every applicable requirement of STANDARD.md has been assessed.

Structural validity, declared-policy validity, evidence review, and full conformance are separate results. Record each separately. The reference validator must fail or report incomplete checks honestly; a successful process exit must not conceal skipped schemas, missing dependencies, missing files, or an unparsed evidence record.

## 8. Minimal assessment matrix

The following columns are sufficient for a small assessment and can be expanded as needed:

| Requirement ID | Applies? and rationale | Claim/artifact IDs | Evidence IDs | Result | Reviewer and date | Gap or exception | Next action |
|---|---|---|---|---|---|---|---|
| RBS-CLS-01 | Yes: technical claim published | EX-CLAIM-001 | EX-EVID-001 | UNKNOWN | Reviewer role / date | Classification not reviewed | Inspect record and basis |
| RBS-PHY-05 | No: no physical action in scope | Scope record | Scope record | NOT_APPLICABLE | Reviewer role / date | Reassess if physical control is added | None now |

The rows are illustrative, not an assessment of a real system. An organization must replace them with its actual scope and evidence.

## 9. Corrections, reassessment, and appeals

Preserve prior assessment statements with their original scope and date. If new evidence undermines a conclusion, record the affected claims, revise their current statuses, identify dependent decisions, and issue a corrected assessment where material. Do not rewrite the previous record to imply that the new evidence was always known.

A challenged classification should be reviewed against the exact proposition and its evidence. Maintain the challenger’s material evidence and the reason for the final decision. A disagreement about acceptable risk belongs in a decision record; a disagreement about what happened belongs in the claim/evidence review. Either may require a qualified reviewer outside the original team.

An assessment remains a dated judgment. Maintenance requires attention to changes that matter: deployments, dependencies, models, business rules, accounts, contracts, incidents, and new measurements. A copied badge or unchanged checklist is not evidence that the underlying conclusion remains current.
