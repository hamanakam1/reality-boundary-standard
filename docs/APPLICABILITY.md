# Find the requirements triggered by a claim

This informative guide follows the profiles in [CONFORMANCE.md](../standard/CONFORMANCE.md#3-applicability-profiles). It adds no requirements or exemptions. Read every requirement whose condition applies, including families outside the initial profile.

| If the claim concerns | Begin with | Review focus |
|---|---|---|
| Any technical statement or release | GOV, REC, CLS, CLM, EVD, TIM, MET, INF, PRM, PUB, REV, RELSE, ADP | Bounded wording, ownership, freshness, traceability |
| APIs, deployment, interfaces, integrations | ARC, REL | Versions, dependencies, failures, end-to-end behavior |
| Agents acting without a fresh instruction | AUT, REL | Authority, limits, revocation, recovery |
| Privacy, tenancy, security, local execution | SEC | Identities, paths, environments, data and observation boundary |
| Models, evaluations, feedback, training | AI, MET, INF | Workload, baseline, denominator, evaluation |
| Signatures, receipts, logs, proofs | CRY, EVD, TIM | Verified property and cryptographic boundary |
| Availability, pricing, approvals, contracts | COM | Account, period, jurisdiction, external decisions |
| Robotics, hardware, energy, simulation | PHY, MET, AUT | Actual physical operations versus simulated results |
| Export, backup, migration, restoration | EXT, REL | Independent restore, configuration, ownership transfer |

Search the [explorer](EXPLORER.md) or [derived catalog](../standard/requirements.json), then read the source paragraph. Literal keyword filters do not label a paragraph as optional or mandatory; one paragraph can contain both obligations and recommendations.

For an export claim, a team may exclude physical control because no hardware action is involved. It still needs security review if the export crosses a tenant boundary, commercial rights if it promises an exit capability, and continuity review if it promises an independent restore.

The assessment generator includes all 118 rows. Document an absent triggering condition and a reconsideration trigger instead of silently dropping a family. Profiles are starting points for review, not maturity rankings or shortened conformance standards.
