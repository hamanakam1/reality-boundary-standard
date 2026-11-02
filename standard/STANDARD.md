# Reality Boundary Standard

**Identifier:** RBS  
**Version:** 0.1.0-draft  
**Status:** Proposed project standard for public review  
**Prepared:** 27 October 2026  
**Applicability:** Technical claims, engineering decisions, autonomous operations, product commitments, and research communication

## 1. Purpose

The Reality Boundary Standard defines how an organization distinguishes what it has observed, what it has demonstrated, what it proposes to build, what remains research, and what belongs to speculative fiction. It gives useful ideas a path into engineering without allowing ambition, a convincing narrative, or an attractive diagram to substitute for evidence.

The standard applies to statements about software, artificial intelligence, cloud services, customer workflows, physical systems, commercial readiness, and the relationships among them. Its central unit is a scoped claim attached to evidence, limitations, and an accountable owner. Its central operating rule is that a claim earns stronger wording and broader deployment through relevant evidence and authorized decisions.

This document is a proposed standard maintained by its project contributors. It is not an ISO standard, an IETF standard, a government rule, a product certification, an audit opinion, or approval from any marketplace or cloud provider. Publication on a source-control platform does not change that status. Organizations may adopt this standard for their own work and make the limited conformance statements described in [CONFORMANCE.md](CONFORMANCE.md).

The standard is deliberately thorough. Adoption should be proportionate: a small internal experiment needs a small claim record; a public guarantee or autonomous action affecting customers needs stronger evidence and controls. Exhaustiveness means accounting for the material boundaries of a claim, including unknowns. It does not mean collecting every available piece of data or delaying reversible work until all uncertainty disappears.

## 2. Normative language and applicability

**RBS-GOV-01.** Uppercase **MUST** and **MUST NOT** identify requirements for conformance. **SHOULD** and **SHOULD NOT** identify recommendations that may be departed from with a recorded reason and understood consequences. **MAY** identifies an option. Lowercase uses carry their ordinary meaning. This convention follows the requirement-level and capitalization approach of RFC 2119 and RFC 8174.[1][2]

**RBS-GOV-02.** An adopter MUST state its assessment scope, version of this standard, applicable profiles, exclusions, and assessment date. A requirement applying to a material capability cannot be omitted merely because it is inconvenient to verify. A legitimate not-applicable decision needs an explanation of the absent condition and a reconsideration trigger.

**RBS-GOV-03.** Examples, templates, references, and explanatory paragraphs are informative unless they contain an explicit normative requirement identifier. External sources do not silently incorporate all their requirements into this standard. Any adopted external requirement MUST be identified by source, version, applicability, and effective date.

**RBS-GOV-04.** This standard MUST NOT be used to create authority that the operator does not possess, override applicable policies or agreements, or authorize access, purchases, messages, deployment, destructive testing, or physical action. An evidence record explains why an action is justified; authorization establishes who may permit or perform it. Both are necessary where applicable.

**RBS-GOV-05.** Routine work already covered by a valid authorization SHOULD proceed without repeated confirmation. Additional review gates SHOULD be tied to a concrete change in risk, scope, cost, reversibility, or decision rights. A stream of unnecessary approvals can obscure the few decisions that actually need human attention.

## 3. Terms and records

A **claim** is a statement that a reader might use to make a decision. Claims include existence, behavior, performance, security, commercial availability, readiness, expected outcomes, and assertions that a system can act autonomously.

An **observation** is a recorded occurrence under stated conditions. A **demonstration** is an executed method intended to test a stated proposition. An **inference** connects evidence to a conclusion through an explicit argument. A **proposal** describes intended work or a possible design. A **hypothesis** is a statement that can be challenged by a feasible observation or experiment. **Speculative fiction** explores a scenario without an established, testable implementation path at the claimed scope.

**Evidence** is material relevant to evaluating a claim. The existence of evidence does not guarantee its accuracy, independence, completeness, or applicability. A **requirement** defines an obligation or acceptance condition. A **finding** compares a scoped current state with a requirement or objective. A **decision** selects or rejects an option under an accountable authority. A **task** implements a selected outcome. An **assumption** is a proposition being used before it has adequate confirmation.

**RBS-REC-01.** Implementations MUST keep claims, evidence, requirements, findings, decisions, and tasks distinguishable, even when one lightweight file stores them. A task marked complete does not automatically establish its originating claim; an acceptance observation is needed.

**RBS-REC-02.** Material records MUST have stable identifiers, a responsible owner or owner role, creation and review timestamps with time zones, and a revision history. Corrections MUST preserve a discoverable relationship to the superseded statement. Removed sensitive content may be represented by a restricted correction record instead of publicly retained payloads.

**RBS-REC-03.** Authors MUST split compound claims when their parts have different evidence or maturity. For example, model availability, local execution, low latency, privacy, financial viability, and autonomous deployment are separate propositions. Demonstrating one does not establish the others.

## 4. Three independent classification axes

**RBS-CLS-01.** Each material claim MUST carry a claim class, support status, and deployment status. These axes MUST remain separate. Deployment does not establish correctness; a well-supported experiment does not establish production readiness; an interesting research question does not become a delivery commitment through repetition.

### 4.1 Claim class

| Class | Meaning | Minimum basis | Permitted reading |
|---|---|---|---|
| **OBSERVED** | A specific event, state, or measurement was directly recorded. | Identifiable observation with scope, time, method, and source. | “This occurred under these conditions.” |
| **DEMONSTRATED** | An explicit proposition was tested by an executed method. | Method, acceptance conditions, execution evidence, results, and limitations. | “This test supports this bounded proposition.” |
| **PROPOSED** | A design, planned capability, target, or engineering change. | Defined intended outcome, dependencies, assumptions, and a verification plan. | “We propose to build or test this.” |
| **RESEARCH** | A technical uncertainty requiring investigation beyond an established implementation path. | Research question, relevant prior work, uncertainty, and a falsifiable or discriminating test where feasible. | “This remains an open research question at this scope.” |
| **SPECULATIVE** | A fictional or exploratory scenario without an established evidentiary implementation path. | Explicit labeling and separation from delivery commitments. | “This is an imaginative scenario.” |
| **UNKNOWN** | Available information is insufficient to assign another class responsibly. | A precise account of what is missing. | “We do not yet know.” |

These classes describe the claim being made, not the reputation of its author. An observed failed experiment remains an observation. A research technology may include demonstrated subcomponents. A speculative scenario may contain ordinary deployed components. Break the scenario into claims before evaluating its parts.

### 4.2 Support status

| Status | Meaning |
|---|---|
| **SUPPORTED** | The current evidence reasonably supports the exact scoped statement, with limitations disclosed. |
| **UNVERIFIED** | Adequate verification has not been completed or the available basis cannot be assessed. |
| **DISPUTED** | Material conflicting evidence or unresolved expert disagreement exists. |
| **CONTRADICTED** | Identified evidence defeats the statement as worded within its stated scope. |

**RBS-CLS-02.** “Supported” MUST NOT mean certain, universal, complete, independent, safe, approved, or commercially viable unless the claim specifically covers that property and adequate evidence supports it. A proposed design can have a supported rationale while its operational capability remains a separate, unverified claim.

**RBS-CLS-03.** “Contradicted” MUST identify the defeated proposition and the conflicting evidence. Lack of demonstration alone MUST NOT be described as proof of impossibility. A conflict with a well-established constraint should be stated at the relevant level, without pretending to settle unrelated research questions.

### 4.3 Deployment status

| Status | Meaning |
|---|---|
| **NOT_APPLICABLE** | Deployment is not meaningful for the claim. |
| **CONCEPT** | No operational implementation has been established. |
| **PROTOTYPE** | An implementation exists for controlled development or evaluation. |
| **PILOT** | A bounded implementation operates with defined participants, limits, and monitoring. |
| **PRODUCTION** | The capability is used in an intended operational environment with identified ownership. |
| **RETIRED** | The implementation or commitment is no longer active. |

**RBS-CLS-04.** Deployment status MUST include the environment and version to which it applies. A claim about production behavior requires deployment evidence. Source code, a build artifact, a screenshot, a successful local test, and a proposed infrastructure manifest are not substitutes for that evidence.

**RBS-CLS-05.** A class/status combination that could mislead a reader MUST be explained or split into separate claims. A fictional archive entry may have verified provenance as a piece of writing; that does not make its fictional physical capabilities SUPPORTED.

## 5. The minimum claim record

**RBS-CLM-01.** Every material claim MUST identify: its exact statement; intended use; the three classification axes; scope; relevant evidence and counterevidence; assumptions; remaining uncertainty; owner; last-reviewed date; review triggers; and the next verification or decision step. Quantitative claims additionally require units, denominator, time window, measurement method, and comparison basis.

Scope includes whichever of the following affects interpretation: product, component, tenant or population, environment, jurisdiction, configuration, identity/role, data category, hardware, model and version, software revision, deployment revision, dependency versions, operating conditions, observation interval, and audience. Missing values are recorded as unknown, not silently filled from a convenient default.

**RBS-CLM-02.** Claims used in public communication, contractual commitments, access decisions, billing, safety decisions, or material investment MUST identify the permitted wording and the stronger wording that the evidence does not justify. This can be a short field rather than a separate essay.

**RBS-CLM-03.** Records MUST distinguish observed fact, attributed statement, inference, and proposed action. If a vendor states that a feature is available, the supported statement may be “the vendor announced the feature”; account access and successful operation require their own evidence.

**RBS-CLM-04.** A claim owner MUST identify what would change their conclusion. “No possible evidence could change this classification” is unsuitable for an empirical claim. Where no feasible test exists, describe the limitation and keep the claim outside an evidence-backed implementation commitment.

Records SHOULD be concise enough to maintain. A link to an exact evidence artifact is more useful than copying it into several reports. A synthesis MAY group closely related claims if their distinct assumptions, status, and evidence remain visible.

## 6. Evidence provenance, collection, and access

**RBS-EVD-01.** Each evidence item MUST record its origin, collection method, collector or generating system, capture time, relevant scope, artifact identifier, and any transformations. Appropriate identifiers include a source URL and retrieval time, repository commit and path, immutable artifact digest, test-run identifier, document revision, or controlled record reference.

**RBS-EVD-02.** Evidence collection MUST respect existing access rights and data-use permissions. Collection MUST be limited to what the claim needs. Credentials, session secrets, unnecessary personal records, and unrelated customer information MUST NOT be copied into a reusable public record.

**RBS-EVD-03.** Redactions, sampling, conversions, summaries, and synthetic replacements MUST be declared. A screenshot can establish what was displayed; it usually cannot establish backend persistence, authorization enforcement, a complete schema, or the absence of another execution path. A synthetic fixture establishes behavior on the fixture, not the prevalence of that behavior in customers.

**RBS-EVD-04.** Sources with a shared origin MUST NOT be counted as independent corroboration. Several articles repeating one announcement, several agents reading the same log, or two dashboards driven by one pipeline do not create independent measurement.

**RBS-EVD-05.** Private evidence MAY remain private. A public claim relying on restricted evidence MUST disclose that limitation and identify an appropriate review arrangement or redacted summary. A reviewer’s attestation MUST state what they inspected, under which scope, and which conclusions remain outside their assessment.

**RBS-EVD-06.** Missing, inaccessible, inconsistent, or incomplete evidence MUST be recorded as such. A collection failure is not a passed test, a failed product requirement, or evidence that a feature does not exist. Preserve the distinction so the next operator can request the correct input.

## 7. Freshness, versions, and historical truth

**RBS-TIM-01.** Claims MUST have an as-of date and a freshness policy proportionate to their volatility and consequence. Current prices, API behavior, account eligibility, supported models, quotas, legal obligations, and production deployments need revalidation when used for a new decision. Stable background concepts do not require arbitrary daily refresh.

**RBS-TIM-02.** A material change in a claim’s dependencies MUST trigger review before the claim is reused outside its preserved scope. Triggers include deployments, model updates, schema changes, configuration changes, role changes, contract amendments, outages, incidents, and contrary evidence.

**RBS-TIM-03.** Historical evidence MUST retain its historical meaning. A revoked capability, expired entitlement, retired model, changed business rule, or deleted record may be relevant to reconstructing earlier behavior. Updating the current record MUST NOT rewrite what was known or authorized at the earlier time.

**RBS-TIM-04.** Systems using time-based decisions MUST specify the authoritative clock, time-zone handling, ordering assumptions, acceptable clock skew, and treatment of late or duplicate events. Event time, processing time, approval time, and effective time MUST remain distinguishable when they affect billing, authorization, scheduling, or compliance reconstruction.

Evidence freshness is not simply age. A yesterday screenshot may already be obsolete after a deployment. An older mathematical derivation may remain applicable. Review policies should identify the mechanism that could invalidate the conclusion rather than attach an unexplained expiration date.

## 8. Measurement, uncertainty, and benchmarks

**RBS-MET-01.** Quantitative claims MUST define the measured quantity, units, denominator, sampling method, population, interval, instrumentation, aggregation, exclusions, and uncertainty or its absence. Sources of uncertainty SHOULD include measurement error, missing records, selection effects, environmental variation, and model variability. The JCGM measurement guidance provides a primary reference for expressing measurement uncertainty; adoption here does not assert formal metrological conformity.[3]

**RBS-MET-02.** Comparisons MUST identify the baseline and keep relevant conditions comparable. A faster model on a smaller task, a lower-cost configuration with lower quality, or a test with preloaded caches is not an equivalent comparison unless the changed conditions are part of the stated conclusion.

**RBS-MET-03.** Reports MUST distinguish single-run results, repeated-run distributions, simulation estimates, extrapolations, targets, and contractual guarantees. Percentiles require a defined sample and collection interval. A mean alone SHOULD NOT be used where tail behavior drives the decision.

**RBS-MET-04.** A zero-result claim MUST be bounded. “Zero observed cross-tenant disclosures in 400 specified tests on revision X” is different from “cross-tenant disclosure is impossible.” Similarly, “no external requests observed during a ten-minute instrumented run” does not establish permanent network isolation.

**RBS-MET-05.** Performance targets MUST NOT be represented as measurements. Ticket counts, token throughput, code volume, synthetic benchmark scores, and closed tasks MUST NOT be substituted for validated customer outcomes without explaining the relationship and its limitations.

**RBS-MET-06.** Evaluations SHOULD predeclare their acceptance conditions where feasible and retain failures, excluded runs, and parameter changes. If acceptance conditions change after observing results, the change and rationale MUST be disclosed. This prevents accidental selection of a favorable story from a large set of experiments.

## 9. Inference, causal claims, and unknowns

**RBS-INF-01.** An inference MUST identify its evidence, reasoning basis, important alternatives, and remaining verification. Confidence labels MAY be used, but unexplained percentages MUST NOT imply calibrated statistical certainty.

**RBS-INF-02.** Correlation, temporal sequence, and expert judgment MUST NOT be silently promoted to causal proof. For causal claims, identify the intervention or method that distinguishes the explanation from plausible alternatives. Where this is unavailable, use wording that accurately reflects the weaker basis.

**RBS-INF-03.** Material unknowns MUST be visible at the point of decision. An unknown that could reverse a decision needs an owner and a next step. Lower-impact unknowns MAY remain in an assumption register without blocking unrelated work.

**RBS-INF-04.** Absence of access, absence of a menu item, absence of a log entry, and absence of a capability are distinct. Reports MUST explain which absence was established. Claims that something never occurs require a justified observation boundary or formal argument, not a failed search alone.

**RBS-INF-05.** A forecast MUST identify assumptions, time horizon, scenario, uncertainty, and a review trigger. Forecasts about technology availability, throughput, revenue, autonomous capability, or regulatory acceptance MUST remain forecasts until relevant observations support a different claim.

A useful unknown is specific: “the deployment revision is unavailable, so source enforcement cannot yet be matched to the live endpoint.” An unhelpful unknown is an unbounded statement that nothing can be trusted. The standard favors bounded conclusions that enable the next worthwhile action.

## 10. Promotion, demotion, and the boundary between ideas and commitments

**RBS-PRM-01.** Reclassifying a claim MUST be an explicit recorded decision based on new evidence or a corrected interpretation. Additional persuasive prose, a later roadmap date, the passage of time, a larger budget, or a new generation number does not provide that evidence.

**RBS-PRM-02.** A speculative concept MAY enter research when its proposer identifies a bounded question, known constraints, relevant prior work, and a useful investigative method. A research idea MAY become an engineering proposal when its dependencies and implementation path are sufficiently understood for a bounded experiment. These transitions do not require the whole imagined system to become feasible.

**RBS-PRM-03.** A proposal MAY gain a demonstrated claim only after the relevant experiment is executed and its results reviewed. A demonstration MAY support a pilot only after the intended environment, rights, failure handling, monitoring, and operating authority are addressed. Production status requires evidence of the actual deployment and its operational scope.

**RBS-PRM-04.** Failed replication, contrary evidence, a stale dependency, an incident, or an unsupported expansion of scope MUST trigger reassessment. Demotion MUST preserve the earlier scope and explain what changed. It is a correction mechanism, not a penalty for honest experimentation.

**RBS-PRM-05.** Release plans MUST separate current capabilities, committed implementation work, conditional experiments, research, and speculative material. A research item MUST NOT become a customer delivery dependency without explicit acceptance of its uncertainty by the responsible decision maker.

This process is not a one-way maturity ladder. An observation may need more research. A production system may fail a specific property. A contradicted universal claim may yield a valuable narrower proposal. A speculative archive can inspire useful engineering while staying outside the release’s factual claims.

## 11. Architecture and integration claims

**RBS-ARC-01.** Architecture diagrams MUST label observed, source-verified, inferred, planned, and external components. Arrows MUST identify meaningful flows such as data, control, identity, events, or commercial relationships. An arrow labeled “integrates” is insufficient when the decision depends on authentication, delivery semantics, or responsibility.

**RBS-ARC-02.** Material integration claims MUST identify actual interfaces, version compatibility, request and event contracts, identities, authorization checks, storage boundaries, error handling, rate limits, retries, idempotency, observability, ownership, and unresolved dependencies. A product’s API availability does not establish compatibility with a proposed workflow.

**RBS-ARC-03.** Source review, configuration review, build verification, deployment verification, and runtime observation MUST remain distinguishable. A repository can contain unused, unreachable, disabled, historical, or unshipped code. A current user interface may conceal a manual backend process.

**RBS-ARC-04.** Cross-instance comparisons MUST record differences in tenant, role, version, data, configuration, and time. Similar appearance or matched behavior across two instances MUST NOT establish a universal platform guarantee or common backend implementation without appropriate additional evidence.

**RBS-ARC-05.** Critical business-state transitions SHOULD be specified as explicit contracts with preconditions, permitted transitions, invariants, outcomes, and failure handling. State labels such as active, provisioned, subscribed, entitled, suspended, and deleted MUST be defined where conflating them could affect access, money, retention, or customer expectations.

## 12. Autonomous authority and accountable action

**RBS-AUT-01.** Each autonomous action class MUST have an identified authority, permitted scope, eligible identities, operational limits, and an accountable human or organizational owner. An agent’s confidence, a model’s recommendation, and the ability to call a tool are not grants of authority.

**RBS-AUT-02.** Action policy MUST distinguish observation, drafting, reversible internal changes, externally visible changes, financial commitments, changes to access, destructive operations, and physical actions as relevant to the system. Approval requirements MUST follow actual consequences and existing authorization rather than a blanket rule that every operation needs confirmation.

**RBS-AUT-03.** Autonomous systems MUST provide effective means to revoke credentials or delegated authority, suspend new work, contain affected workloads, and identify in-flight actions. “Impossible to turn off” MUST NOT be adopted as an operating requirement. Resilience and decentralization need accountable containment and recovery designs.

**RBS-AUT-04.** Action records MUST distinguish proposed intent, policy evaluation, approval where required, attempted execution, accepted request, completed state transition, and observed outcome. A queued request or a success response from one component does not establish completion of the entire business process.

**RBS-AUT-05.** Agents MUST NOT expand their own spending, access, replication, external communication, or physical authority merely to achieve a task. Any authorized adaptive behavior MUST operate within predefined limits and record the applicable decision.

**RBS-AUT-06.** Escalations SHOULD include the exact blocker, evidence, options, consequences, recommended action, and required decision. Existing authorization SHOULD be reused while valid. Repeatedly asking the same question without a changed condition is not an additional control.

## 13. Reliability, recovery, and partial failure

**RBS-REL-01.** Operational capability claims MUST consider partial failure, delayed outcomes, duplicate delivery, out-of-order events, dependency outage, quota exhaustion, stale state, and operator unavailability where relevant. The selected test coverage and remaining gaps MUST be stated.

**RBS-REL-02.** High-impact retried operations MUST have an explicit replay and idempotency strategy or a documented reason retries are disallowed. The strategy MUST identify the business operation, deduplication scope, retention window, concurrency behavior, and recovery from a partially completed action.

**RBS-REL-03.** Recovery claims MUST distinguish detection, mitigation, restoration, reconciliation, and customer recovery. A backup’s existence does not establish that it can restore the complete service. Recovery objectives and measured recovery results MUST be reported separately.

**RBS-REL-04.** Claims of self-healing MUST specify the failure classes detected, allowed interventions, recovery success criteria, escalation conditions, retry limits, and consequences of a failed repair. An unbounded loop of automated modifications is not evidence of resilience.

**RBS-REL-05.** Distributed operation MUST state its ordering, partition, reconciliation, authority, and conflict assumptions. A cryptographic record of two conflicting actions does not decide which business action should prevail. Reconnection requires a defined policy for state and consequences, including cases that need human adjudication.

**RBS-REL-06.** Background jobs MUST have sufficient visibility to establish their current state and operational impact. Where a job cannot be safely interrupted or reversed, that limitation MUST influence its authorization, scheduling, and recovery design.

## 14. Security, privacy, sovereignty, and tenant isolation

**RBS-SEC-01.** Security claims MUST specify assets, threat actors, trust boundaries, tested conditions, versions, and exclusions. A threat model identifies plausible risks; it does not establish that an exploit exists. A vulnerability finding requires supporting evidence appropriate to the claim.

**RBS-SEC-02.** Multi-tenant claims MUST cover relevant secondary surfaces, including caches, queues, background jobs, search indexes, files, observability, analytics, shared configuration, exports, model context, and administrative operations. Primary database filtering alone MUST NOT be described as complete tenant isolation.

**RBS-SEC-03.** Adversarial tests MUST use authorized scope, controlled data, bounded load, appropriate environments, stop conditions, and a cleanup plan. A designed test, an executed test, and a passed test MUST have distinct statuses. Unsafe production testing MUST NOT be performed merely to satisfy a checklist.

**RBS-SEC-04.** Claims of local operation, data residency, data sovereignty, privacy, and confidentiality MUST each state their own boundary. Local model inference alone does not establish that telemetry, downloads, credentials, backups, remote tools, or downstream actions remain local. Verify the relevant flows and agreements before adopting broader wording.

**RBS-SEC-05.** Data-use claims MUST identify the data categories, purpose, access, retention, deletion, onward transfer, training use, and relevant ownership or permission basis. De-identification and synthetic substitution MUST state their limits where re-identification or sensitive inference remains material.

**RBS-SEC-06.** The publication process MUST prevent accidental disclosure of secrets, customer information, unpublished vulnerabilities, private topology, restricted source code, and engagement-specific access identifiers. General lessons MAY be published only with suitable abstraction, provenance, and rights.

## 15. Cryptographic records and the limits of proof

**RBS-CRY-01.** A claim about hashes, signatures, append-only logs, attestations, or proofs MUST identify exactly what property is being verified, under which algorithms, keys, trust roots, retention controls, and verification procedure. The word “cryptographic” MUST NOT substitute for that explanation.

**RBS-CRY-02.** Receipts MUST distinguish the integrity and attribution of recorded data from the truth and completeness of the underlying event. A signed assertion that a test passed does not by itself establish that the test was adequate, executed honestly, or representative of deployed behavior.

**RBS-CRY-03.** Append-only and immutable claims MUST identify the enforcement mechanism, privileged actors, storage and replication assumptions, deletion policies, and detectable tampering limits. A hash chain in a writable database MUST NOT be described as unconditionally immutable.

**RBS-CRY-04.** Provenance records SHOULD connect inputs, build or action process, output artifacts, and verification results. Software supply-chain provenance can describe where, when, and how an artifact was produced; it is not a universal proof of product correctness.[4]

**RBS-CRY-05.** A formal proof or zero-knowledge proof claim MUST identify the proposition, model or circuit, assumptions, trusted inputs, and verification boundary. A proof about a specified computation MUST NOT be generalized to “the complete product is perfect” or “the customer’s business outcome is guaranteed.”

**RBS-CRY-06.** Key rotation, compromise, revocation, verification failure, timestamp interpretation, and missing receipts MUST have defined handling. Cryptographic evidence that can no longer be verified needs an explicit status; silently treating it as current assurance is nonconforming.

## 16. Artificial intelligence, evaluation, and learning

**RBS-AI-01.** Model capability claims MUST identify the actual model/version where available, interface, inference settings, tool access, context preparation, evaluation data, and relevant hardware or service conditions. A model-family name alone is insufficient for a reproducible performance claim.

**RBS-AI-02.** Evaluation MUST distinguish model output quality from end-to-end workflow outcomes. The system includes prompts, retrieval, tools, policies, data, operators, and downstream effects. Strong results on a benchmark do not automatically establish reliability on the deployment task.

**RBS-AI-03.** Context preparation, retrieval, structured output, model routing, and greater reasoning effort MUST NOT be advertised as eliminating hallucination, guaranteeing correctness, or removing all cold-start cost. Their benefits MUST be measured for the claimed workload.

**RBS-AI-04.** Automated evaluations SHOULD include difficult cases, refusal or abstention cases, long-tail inputs, adverse conditions, and meaningful failure categories. Human evaluation MUST identify the rubric, reviewer selection, disagreement handling, and whether review was independent of the authors.

**RBS-AI-05.** Human corrections MUST distinguish preference, policy judgment, factual correction, implementation change, approval, and observed outcome. A correction log MUST NOT automatically become a training dataset. Training requires appropriate data rights, curation, protection of sensitive information, an evaluation plan, and a separate deployment decision.

**RBS-AI-06.** Model substitution or adaptive routing MUST preserve task contracts, relevant context, data-use constraints, and action authority. A system MUST NOT silently expand cloud data transfer or tool permissions because a preferred model is unavailable.

**RBS-AI-07.** Drift monitoring MUST address changes in inputs, labels, business rules, retrieval sources, tools, models, and outcomes where relevant. Monitoring without an actionable owner and response policy does not establish ongoing reliability. NIST AI RMF 1.0 provides a useful lifecycle framing for governance and evaluation; this standard does not claim that conformance to RBS establishes conformance to that framework.[5]

## 17. Physical systems, simulation, energy, and resources

**RBS-PHY-01.** Physical capability claims MUST identify the hardware, operating envelope, instrumentation, environmental conditions, interfaces, and tested task. A visual simulation, generated design, or plausible video MUST NOT be represented as evidence that the physical operation succeeded.

**RBS-PHY-02.** Simulation results MUST state model assumptions, validation against observations, unmodeled effects, and the conditions under which transfer to physical operation is expected. Simulation success does not remove the need for staged real-world verification appropriate to consequence.

**RBS-PHY-03.** Energy, power, heat, latency, storage, bandwidth, material yield, and manufacturing-rate claims MUST use explicit quantities and boundaries. Stored energy and power delivery, local computation and communication delay, recycling and complete material recovery, and theoretical limits and achievable engineering performance MUST remain distinguishable.

**RBS-PHY-04.** Claims of zero latency, infinite capacity, zero heat, perfect recycling, instantaneous global synchronization, or total independence from supply chains MUST be challenged as stated. The review MUST identify the relevant constraint and credible evidence rather than simply use an “impossible” label. A bounded experimental zero, a mathematical idealization, and a universal physical guarantee are different claims.

**RBS-PHY-05.** Autonomous physical actions MUST have appropriate human authority, operating limits, hazard analysis, emergency controls, and qualified review for the task. Software approval or a successful digital test is not authorization to alter electrical wiring, mechanical systems, vehicles, or industrial equipment.

**RBS-PHY-06.** A self-replication or self-provisioning claim MUST enumerate its seed assets, external inputs, manufacturing dependencies, power, materials, tools, transport, credentials, and maintenance. Autonomous use of an existing provider is not self-replication from raw matter.

## 18. Commercial, marketplace, and legal claims

**RBS-COM-01.** Commercial readiness claims MUST distinguish technical feasibility, implementation readiness, account eligibility, product approval, contract execution, operational launch, customer adoption, and demonstrated economic sustainability. Evidence for one stage MUST NOT imply completion of another.

**RBS-COM-02.** Requirements from marketplaces, providers, regulators, contracts, and customers MUST be tracked with authoritative sources, effective dates, applicability conditions, and verification methods. Engineering recommendations and optional differentiators MUST remain distinguishable from mandatory requirements.

**RBS-COM-03.** Programmatic submission templates MUST distinguish placeholder manifests, schema-validated payloads, account-specific complete payloads, submitted changes, accepted changes, and published listings. A syntactically valid file is not evidence of external acceptance.

**RBS-COM-04.** Rights to inspect a product, collaborate without charge, learn a design pattern, resell a service, publish source, reuse customer data, and white-label a product MUST be evaluated separately. Technical integration does not establish commercial permission.

**RBS-COM-05.** Legal, compliance, and certification statements MUST identify the responsible entity, jurisdiction, scope, source, period, and actual status. A control mapping, risk assessment, signed log, or readiness report MUST NOT be represented as an independent audit opinion or regulatory approval.

**RBS-COM-06.** Economics claims MUST distinguish measured costs from allocations, estimates, scenarios, pricing decisions, and revenues. Cost-to-serve calculations SHOULD account for infrastructure, provider charges, labor, onboarding, support, exceptions, failed work, data movement, and ongoing maintenance where material. Sensitivity to volume, quality, and unusual customers MUST be visible.

**RBS-COM-07.** A pilot used as commercial evidence MUST specify what commercial proposition it tests. A purely technical pilot needs a technical proposition and must not be presented as commercial validation. Free internal use, enthusiasm from collaborators, a technically successful integration, and repeated paid demand are different evidence. Revenue and margin projections MUST remain scenario-based until supported by appropriately scoped operating results.

## 19. Portability, continuity, and exit

**RBS-EXT-01.** Export, backup, replication, disaster recovery, escrow, migration, and account termination MUST have separate definitions where they are offered. A data export MUST NOT be described as complete tenant portability without evidence that a recipient can interpret and use the relevant data and configuration.

**RBS-EXT-02.** A portability claim MUST define its completeness boundary: records, relationships, attachments, configuration, custom fields, history, identifiers, permissions, business rules, schemas, deletions, and external dependencies as applicable. Missing categories MUST be disclosed.

**RBS-EXT-03.** Restore and migration demonstrations MUST identify the target environment, consistency point, validation rules, excluded dependencies, elapsed time, and observed results. A daily export schedule is an intended cadence, not proof that every scheduled export completed successfully.

**RBS-EXT-04.** Operating designs MUST identify customer exit rights, authority revocation, retained records, deletion timing, and responsibility after handoff. A system that depends indefinitely on an unavailable original operator does not establish maintainable ownership transfer.

**RBS-EXT-05.** Documentation, schemas, knowledge models, and automation contracts SHOULD have owners and update triggers. A useful handoff includes enough evidence and operational context for another authorized operator to diagnose failures and safely continue the work.

## 20. Publication, narrative, and the speculative archive

**RBS-PUB-01.** Public documents MUST make the status of material claims visible where a reader encounters them. A disclaimer at the end MUST NOT be used to excuse unqualified capability claims in a headline, diagram, demo, or sales statement.

**RBS-PUB-02.** Speculative material MUST live in a clearly identified archive or section with its own purpose and boundary. It MUST NOT be included in current capability tables, conformance evidence, release acceptance, customer commitments, or investment assumptions without explicit reclassification and supporting evidence.

**RBS-PUB-03.** The archive SHOULD retain useful inspiration in a structured way: original concept, claim decomposition, research questions, practical engineering analogues, known constraints, and requirements for reconsideration. Archiving is not endorsement or permanent rejection.

**RBS-PUB-04.** Roadmap generations, maturity branding, fictional dates, and invented product names MUST NOT be used as evidence. Named products, model versions, release dates, capacities, prices, and availability MUST be verified from appropriate sources before being represented as current facts.

**RBS-PUB-05.** Published corrections MUST identify the affected statement, its prior use, the new evidence, and the corrected wording. Material customers or decisions affected by the claim SHOULD be identified through an authorized notification process. This standard does not authorize sending the notification itself.

**RBS-PUB-06.** A public release MUST include its standard version, change history, ownership or maintainership information, contribution process, applicable licensing information, and the scope of any conformance statement. Publication MUST NOT imply endorsement by referenced organizations or customers.

## 21. Review, assurance, and independence

**RBS-REV-01.** Review effort MUST be proportionate to the consequences of the claim. A low-impact internal proposal may use author review; a consequential external guarantee or autonomous operation requires review with suitable expertise and independence from the implementation where feasible.

**RBS-REV-02.** A reviewer MUST inspect the actual evidence needed for their conclusion. Agreement between language models, repeated summaries, and checklist completion alone MUST NOT be described as independent validation of an underlying empirical claim.

**RBS-REV-03.** Review MUST consider counterexamples, alternative explanations, edge conditions, source rights, missing populations, stale evidence, and unintended consequences. It SHOULD distinguish disagreement about facts from disagreement about acceptable risk or priorities.

**RBS-REV-04.** Conflicts of interest and limits of reviewer access MUST be disclosed when they materially affect the assurance statement. A self-assessment MAY be useful, but MUST be labeled as a self-assessment.

**RBS-REV-05.** Automated validators MAY check record completeness, references, identifiers, status consistency, redaction rules, and evidence freshness. They MUST NOT claim to establish factual truth, legal compliance, product safety, or complete security merely because structural checks pass.

## 22. Release gates and exceptions

**RBS-RELSE-01.** A release using this standard MUST have a scoped evidence manifest linking material published claims to their records and current support. The manifest MUST identify unresolved material unknowns and the decisions that accept or avoid them.

**RBS-RELSE-02.** A release MUST NOT claim conformance while an applicable MUST requirement has an unresolved failure or has not been established by the required assessment. An organization MAY release a product with explicitly accepted limitations under its own authority, but it must describe RBS status accurately rather than silently waive the standard. Where failed and unassessed requirements coexist, report NONCONFORMING and disclose the incomplete coverage; otherwise unresolved assessment prevents an affirmative conformance statement.

**RBS-RELSE-03.** Exceptions to SHOULD recommendations MUST state their scope, rationale, consequences, owner, review trigger, and compensating measures if relevant. An exception MUST NOT erase the underlying evidence or change the truth status of a claim.

**RBS-RELSE-04.** Publication readiness, implementation readiness, deployment authorization, and external approval MUST be separate release decisions. A document can be ready for review while its proposed architecture is unimplemented. A tested implementation can still lack authorization for production.

**RBS-RELSE-05.** Release records SHOULD be reproducible from versioned inputs. Record the standard version, material artifact versions, evidence cutoff, scope, review decisions, and outcome. Sensitive evidence may be referenced through access-controlled identifiers rather than copied into public source control.

## 23. Adoption and maintenance

**RBS-ADP-01.** An adoption plan MUST identify the responsible maintainer, the workflows in scope, the initial claim inventory, and where records will be maintained. Existing systems MAY be adapted; this standard does not require a new platform, ledger, database, model, or agent framework.

**RBS-ADP-02.** Adoption SHOULD begin with the claims that most affect customers, access, money, safety, or architectural investment. Routine factual details can be handled through shared evidence references. The absence of a perfect organization-wide inventory MUST NOT prevent correction of a material unsupported claim.

**RBS-ADP-03.** Changes to the standard MUST retain stable requirement identifiers where their meaning is preserved. Changed, superseded, or removed requirements MUST have a migration note. A later standard release MUST NOT retroactively redefine an earlier conformance statement.

**RBS-ADP-04.** A proposal to weaken a requirement MUST explain the problem, affected assurance, alternatives, and expected consequences. A proposal to add a requirement MUST identify the failure it prevents and the evidence an adopter can realistically produce. Exhaustiveness does not justify requirements with no useful decision or verification function.

**RBS-ADP-05.** Maintainers SHOULD review reported ambiguity, adoption cost, false confidence, and operational friction. Measure whether the standard improves decisions, corrects unsupported claims, and enables reliable handoffs; the number of forms completed is not the intended outcome.

## 24. Worked examples

The examples below are hypothetical. They establish no facts about a real product, organization, provider account, or customer.

| Original statement | Defensible replacement | Classification consequence |
|---|---|---|
| “The agent cannot make mistakes.” | “On the defined evaluation set, revision A met the recorded acceptance threshold; failures and exclusions are linked.” | A bounded demonstration can be SUPPORTED. A universal guarantee remains unsupported. |
| “The local model guarantees complete privacy.” | “Inference ran locally in the observed test; tool calls, telemetry, backups, and data-use permissions require separate review.” | Split inference locality from privacy and sovereignty. |
| “The signed receipt proves the customer’s feature is running.” | “The receipt identifies the build and verification event. Deployment and customer-visible behavior have separate evidence.” | Split provenance, deployment, and outcome claims. |
| “The application is marketplace-ready.” | “The scoped technical prerequisites passed; account eligibility and external listing review remain open.” | Readiness dimensions stay separate. |
| “This system repairs itself.” | “The controller recovered from the three specified failure classes within stated limits; other failures escalate.” | Bound the operational capability and authority. |
| “The factory can reproduce itself from raw material.” | “A provisioning script reproduced the software environment using listed provider services and credentials.” | Preserve a demonstrated software result without inheriting the fictional physical claim. |
| “Every tenant is isolated.” | “The specified authorization and secondary-isolation checks passed for the tested roles, tenants, and revision; remaining coverage is listed.” | Report observed coverage without universal proof. |
| “The platform’s economics work.” | “The pilot scenario produces the stated estimated margin under explicit cost and support assumptions; paid demand is not yet established.” | Separate a model, a forecast, and operating evidence. |

A productive review asks: what is the smallest statement the available evidence supports, what decision does it enable, and what is the next test that could justify a broader statement? The answer should create useful work, preserve imagination, and prevent a proposal from quietly becoming a fact.

## References

References support specific concepts; they do not endorse this project standard. Consult the applicable versions and current requirements when using them for a new decision.

1. S. Bradner. **RFC 2119: Key words for use in RFCs to Indicate Requirement Levels**. RFC Editor, March 1997. https://www.rfc-editor.org/rfc/rfc2119 . Accessed 27 October 2026. Used for the meaning of requirement levels.
2. B. Leiba. **RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words**. RFC Editor, May 2017. https://www.rfc-editor.org/rfc/rfc8174 . Accessed 27 October 2026. Used for uppercase-only normative interpretation.
3. Joint Committee for Guides in Metrology. **JCGM publications and Guide to the Expression of Uncertainty in Measurement**. Bureau International des Poids et Mesures. https://www.bipm.org/en/committees/jc/jcgm/publications . Accessed 27 October 2026. The page identifies JCGM 100:2008 and its 2026 amendment; the adopter should select the document applicable to its measurement problem.
4. SLSA project. **SLSA v1.2: Provenance**. https://slsa.dev/spec/v1.2/provenance . Accessed 27 October 2026. Used for the scoped meaning of artifact provenance.
5. National Institute of Standards and Technology. **Artificial Intelligence Risk Management Framework (AI RMF 1.0)**, NIST AI 100-1, January 2023. https://doi.org/10.6028/NIST.AI.100-1 . Primary document: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf . Accessed 27 October 2026. Used as a lifecycle risk-governance reference, not a certification scheme.
