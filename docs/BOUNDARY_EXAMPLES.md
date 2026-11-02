# Boundary examples: from compelling language to testable claims

These are **hypothetical teaching examples**, not reports of completed tests or evaluations of a named vendor. The rewritten statements show how to scope a claim; replace every example quantity, date, environment, and result with actual evidence before using it as a capability statement.

## 1. A receipt and an operating result

**Overclaim:** “A cryptographic receipt proves the requested feature is running correctly and meeting its SLA.”

**Separate claims:** the receipt bytes verify against a named key; the receipt refers to a particular build and deployment; an authorized observer measured specified health signals; the stated user-visible behavior met a defined acceptance test; a service-level measure met its defined observation window.

**Boundary:** integrity and provenance are valuable evidence properties. They do not erase failures in instrumentation, authorization, omitted events, semantics, or the surrounding system. A valid signature can authenticate an inaccurate assertion. Design a verification chain whose final conclusion is no broader than its weakest relevant observation.

**Promotion test:** verify the receipt, identify its issuer and scope, trace the deployment artifact, execute the behavior check, compare service measures against a declared window/denominator, and retain failures. Record the separate result of each step.

## 2. Local inference and privacy

**Overclaim:** “Running the model locally guarantees complete privacy and independence.”

**Bounded proposal:** “Run a defined inference workload locally, inventory network dependencies and telemetry, control which data may leave the device, and test its behavior when external services are unavailable.”

**Boundary:** execution location, data handling, account access, update supply chain, retrieval, tools, licensing, and operator control are separate properties. Measure the relevant ones. Do not represent a local model process as an audited end-to-end privacy guarantee.

## 3. Context preparation and model accuracy

**Overclaim:** “The context loader eliminates hallucinations and guarantees zero startup time.”

**Bounded proposal:** “Prepare a versioned task context with permitted source references, freshness checks, and missing-context indicators; measure task startup latency and unsupported-claim rate against a comparable baseline.”

**Promotion test:** use held-out tasks, stale/missing/contradictory context, access denials, and a reproducible scoring method. Report the distribution and remaining failure cases. The preparation process may reduce errors without eliminating them.

## 4. Tenant isolation

**Overclaim:** “Our adversarial suite proves tenant leakage is impossible.”

**Bounded demonstration wording:** “On revision X, the specified negative tests using synthetic tenants A and B produced no observed unauthorized reads in the declared environment.”

**Boundary:** include background jobs, caches, logs, exports, indexes, roles, restore paths, and relevant shared configuration in the test inventory. State untested paths and the evidence that the deployed revision matches the tested one. A finite test result is useful without becoming a universal theorem.

## 5. Continuous compliance

**Overclaim:** “The audit ledger makes the company compliant.”

**Bounded proposal:** “Collect permissioned evidence for identified controls, track evidence freshness and population coverage, record exceptions, and present a readiness view for review.”

**Boundary:** control design, implementation, operating effectiveness, applicable obligations, reviewer scope, and an independent opinion are separate. A signed record of a change does not show that the change was authorized or appropriate. State exactly which control assertion each artifact supports.

## 6. Simulated robotics

**Overclaim:** “A successful simulation means the robot can safely perform the physical task.”

**Bounded proposal:** “Test a defined manipulation task in simulation, document fidelity and distribution limits, then use a controlled physical evaluation with appropriate supervision, instrumentation, stopping conditions, and a qualified safety process.”

**Boundary:** simulation is evidence about the model under its assumptions. Physical performance and safe operation need evidence appropriate to the real environment. Do not use this standard as a substitute for domain-specific physical-safety engineering.

## 7. Digital twins

**Overclaim:** “The twin perfectly mirrors the business and physical world in real time.”

**Bounded proposal:** “Model selected assets and state variables, document sensor coverage, update rates, timestamps, missing observations, estimation error, and use cases for which the model is validated.”

**Promotion test:** compare defined predictions against observed outcomes, test stale/absent sensors, and show the error and lag that users can expect. Make model uncertainty visible at the decision point.

## 8. Throughput targets

**Overclaim:** “The cluster completes thousands of valuable engineering tickets every day.”

**Bounded proposal:** “Benchmark specified task classes on the actual hardware/model/tool configuration, including validation, retries, operator interventions, review/repair time, and accepted outcomes.”

**Boundary:** ticket count depends on task granularity. Hardware specifications and token throughput do not establish useful completed work. State throughput, quality, operating costs, thermal/power constraints where relevant, and the definition of acceptance together.

## 9. Decentralization and recovery

**Overclaim:** “The swarm is impossible to turn off and always heals instantly.”

**Bounded requirement:** “Define fault tolerance for specified failures while preserving cancellation, credential revocation, tenant containment, resource limits, recovery ownership, and an acceptable convergence interval.”

**Boundary:** resilience is an operating property to test. Removing accountable shutdown is an authority-design choice, not evidence of quality. A partitioned node cannot be assumed to receive an online revocation immediately; design the offline authority envelope and reconciliation explicitly.

## 10. Purchasing and corporate authority

**Overclaim:** “The autonomous system can negotiate, buy, incorporate, and govern itself without people.”

**Bounded proposal:** “Prepare purchasing or commercial recommendations, and permit only explicitly delegated transactions within a named principal's scope, budget, verification, revocation, and review arrangements.”

**Boundary:** technical API capability does not create legal authority, corporate personhood, contract rights, or acceptance by counterparties. Establish these through applicable sources and accountable decisions rather than a software generation label.

## 11. Model self-improvement

**Overclaim:** “Every correction automatically trains the system into a better model.”

**Bounded proposal:** “Capture the original proposal, human correction, reason, executed action, and observed outcome separately. Curate permissioned evaluation data first; test any training candidate on held-out and regression tasks before controlled deployment.”

**Boundary:** a correction is not necessarily an optimal answer; human preferences and outcomes may conflict. Protect tenant boundaries, data rights, privacy, evaluation independence, reproducibility, and rollback. More training data does not automatically establish better behavior.

## 12. Advanced scientific technologies

**Overclaim:** “Because a scientific technique has been demonstrated, an integrated industrial platform using it is available now.”

**Bounded research statement:** “A primary source reports a result for a specific technique under stated conditions. Availability, scale, integration, cost, reliability, and suitability for this use case remain separate questions.”

**Boundary:** do not label an entire field fictional because a particular scenario is unsupported. Conversely, do not use a real field name to support unrelated guarantees. Named product releases and capacities must be verified as of the decision date.

## 13. Zero latency, infinite resources, and perfect outcomes

**Overclaim:** “Communication has zero latency, compute is infinite, and all failures are eliminated.”

**Boundary treatment:** first identify whether the language is a metaphor, measurement rounding, a bounded zero observation, or an asserted physical guarantee. A fictional narrative may retain it with clear labeling. An engineering claim requires units, measurement resolution, distance/environment, resource boundary, conditions, and evidence for the exact statement.

Do not manufacture a numerical result or an impossibility proof to fill the gap. Where an established scientific constraint defeats the literal claim, cite an appropriate primary source for that specific conclusion. Otherwise label the unsupported claim and request the missing evidence. Replace broad promises with measurable service objectives, resource envelopes, and disclosed failure cases.

## 14. Marketplace readiness and business demand

**Overclaim:** “The application is marketplace-ready, so customers will buy the enablement service.”

**Separate claims:** applicable requirements were identified; specified technical tests passed; seller/commercial prerequisites are complete; the marketplace approved the listing; the operator authorized launch; target customers want the offer; delivery can be repeated at a sustainable margin.

**Promotion test:** use authoritative requirement evidence, integration results, commercial decisions, actual approval status, customer discovery or paid-pilot evidence, and measured delivery/support economics. A no-charge internal success can establish learning and feasibility without proving demand.

## 15. Promotion from archive to engineering

Start with one archived idea. Remove the fictional certainty and choose a narrow useful outcome. Create a separate proposed claim with owner, user need, dependencies, authority envelope, resource assumptions, success/failure criteria, and a stop rule. Identify the smallest discriminating experiment. Record its actual result; retain negative evidence.

Promote only the bounded claim that the evidence supports. The original narrative may remain in the archive. Its scope does not automatically shrink to match the successful experiment, and the experiment does not automatically validate the rest of the narrative.
