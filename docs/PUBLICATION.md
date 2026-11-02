# GitHub publication plan

## Current destination — 1 November 2026

The owner supplied `https://github.com/hamanakam1/reality-boundary-standard` as the destination. Repository metadata confirms account `hamanakam1`, public visibility, administrative write permission for the authenticated session, and an empty repository at inspection. The new foundation is prepared in a clean local clone without importing the preparation workspace's Git history.

The repository owner is the initial decision contact through GitHub issues and pull requests after publication. The remaining owner input is confirmation of rights and the selected license scope. No public branch, tag, or release has been published by this local preparation. The live source of candidate state is [release-manifest.json](../release-manifest.json) and current verification is [VERIFICATION.md](VERIFICATION.md).

The sections below retain the publication procedure; their original proposed inputs are superseded by the confirmed destination and contact above where applicable.

## Concrete release candidate

- Proposed repository name: `reality-boundary-standard`.
- Proposed visibility: public.
- Initial version: `0.1.0-draft`.
- Release purpose: public review and initial adoption feedback.
- Normative source: `standard/STANDARD.md`.
- Conformance status of a product: not assessed by publishing this repository.
- Repository owner: `hamanakam1`.
- Initial decision contact: repository owner, through repository issues/pull requests; no additional maintainers appointed.
- License and rights holder: decision pending; see `../LICENSING.md`.

These are the remaining publication inputs, not reasons to stop preparing or reviewing the content. Resolve them against the actual authenticated GitHub account and the owner's instruction before creating or pushing a public remote. Do not guess an organization or grant a license on its behalf.

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
