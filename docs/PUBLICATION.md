# Source publication and release procedure

## Current destination — 1 November 2026

The owner supplied `https://github.com/hamanakam1/reality-boundary-standard` as the destination. Repository metadata confirms account `hamanakam1`, public visibility, administrative write permission for the authenticated session, and an empty repository at inspection. The new foundation is prepared in a clean local clone without importing the preparation workspace's Git history.

The repository owner is the initial decision contact through GitHub issues and pull requests. The owner confirmed control of the draft's rights and approved initial source publication with CC-BY-4.0 for prose and MIT for software/supporting records on 1 November 2026 (America/Los_Angeles). [LICENSING.md](../LICENSING.md) defines the exact scope and contribution terms.

The target branch is `main`. Publication is verified by reading back the exact remote commit and file contents after the push. The source manifest records the initial published revision once observed; a revision cannot contain its own Git commit hash. Exact current-head delivery receipts and CI results are therefore captured after publication. A tagged release and hosted website are separate actions from publishing source.

## Concrete release candidate

- Repository: `hamanakam1/reality-boundary-standard`.
- Visibility: public.
- Initial version: `0.1.0-draft`.
- Release purpose: public review and initial adoption feedback.
- Normative source: `standard/STANDARD.md`.
- Conformance status of a product: not assessed by publishing this repository.
- Repository owner: `hamanakam1`.
- Initial decision contact: repository owner, through repository issues/pull requests; no additional maintainers appointed.
- Rights holder: Michael Hamanaka; license scope: CC-BY-4.0 prose / MIT software and supporting records, with mixed generated output retaining both scopes.

The initial publication inputs are resolved. Future publications still require authority over their destination, content and rights; this approval does not extend rights over new third-party submissions.

## Public-content boundary

The candidate contains only the standard, procedure, templates, generic examples, schemas, limited validator, tests, governance, contribution material, and publication instructions. The original creative narratives and client-specific assessment prompt pack remain outside this source tree.

Before publication, review the exact candidate tree and Git history, not merely the visible working files. Exclude private client names/identifiers, document IDs, customer data, raw observations, credentials, access tokens, private repository pointers, proprietary source/assets, and unpublished findings. If a file was previously committed and then removed, deletion from the working tree alone does not establish a clean public history.

The preparation package is intended to start a clean public repository. Do not push an existing engagement repository and change its visibility to public. Reuse an existing public standard repository only after verifying its owner, contents, and intended destination.

## Review sequence

1. Check the exact artifact version and file inventory.
2. Review normative definitions, examples, requirement IDs, conformance wording, and source relevance.
3. Run the supplied structural/policy validator and meaningful tests. Record their scope; do not call them full conformance.
4. Verify public-content rights and privacy. Ensure references support only the claims attributed to them.
5. Resolve owner, maintainers, license, visibility, repository name, and release description.
6. Produce a reviewable release manifest with file hashes, version, checks, limitations, and the selected publication target.
7. If publication is already explicitly authorized for that exact destination and content, carry it out using the authenticated tooling. Otherwise ask for the narrowly remaining publication decision, with the concrete candidate attached.
8. Read back the resulting repository metadata, default branch, exact commit, release/tag if created, and key file content. Report the observed URL and commit; do not invent a URL before the operation succeeds.

## Release description draft

> Initial draft of the Reality Boundary Standard: a proposed evidence and governance standard for technical claims, autonomous operations, and engineering decisions. It distinguishes observed and demonstrated results from proposals, research, and speculation using separate support and deployment fields. The package includes 118 requirements, a scoped conformance procedure, record schemas, generic examples, and a limited reference validator. Public review is requested on clarity, applicability, adoption cost, missing failure modes, and misleading conformance interpretations. This is not an external certification program.

## What to ask reviewers

Does the classification let a small team work without excessive bureaucracy? Can a reviewer see exactly what a claim means and what would invalidate it? Are scoped demonstrations allowed without inviting universal promises? Are governance and physical/commercial boundaries realistic? Are the schemas and validator clearly narrower than the full normative standard? Which requirement is ambiguous or impossible to verify in its intended scope?

Use actual adoption reports to refine a future stable release. Do not claim widespread adoption, industry consensus, or third-party endorsement from the first publication.
