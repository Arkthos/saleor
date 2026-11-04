# C9 — Durable audit evidence snapshot (2026-10-18)

This file preserves a verified research checkpoint in Git, independent of expiring GitHub Actions artifacts. It is not a declaration of product vulnerability or approval of provisional P-ORDER-01.

## Provenance and reproducibility

- PR: https://github.com/Arkthos/saleor/pull/1 (draft; do not merge automatically)
- Experiment source branch: `research/cybermarket-security-tests-v1`
- Tested source head: `d920eaa9e678b1e5514fda7f278f69e42fdab287`
- Focused CI: https://github.com/Arkthos/saleor/actions/runs/39141812626
- CI merge SHA reported in summary: `d24895d67d4a8815614e90faa966add82e6eb4f1`
- JUnit evidence artifact ID: `12141901833`; archive digest `sha256:fbcfcf7e160fee18cc6360fbf72f37b16e9378cc248c83884501e3975bd58e0e`
- JUnit, summary and coverage hashes: verified against artifact `SHA256SUMS` during prior audit. Exact per-file digests are not reproduced here; retrieve the artifact to audit them independently. Artifact retention expires 2026-11-17.

## Actual C9 results

- 55 pytest executions: **53 PASS, 2 expected XFAIL, 0 FAIL/ERROR/SKIP**.
- 26 unique case IDs mapped to all 13 research risk IDs; mapping is not risk certification.
- CM-T23: 6 PASS; anonymous and unrelated authenticated actors, each against `userEmail`, billing street and shipping street, receive the raw synthetic values when possessing the order UUID.
- CM-T24: 3 PASS; owner positive control for the same three fields.
- CM-T25: 6 PASS; legacy-number path returns values different from raw values to both nonowner actors. **Not proof that the mask is sufficient.**
- CM-T26: 2 PASS; nonexistent UUID returns no order to either nonowner actor.
- CM-T22: 2 strict XFAIL; provisional email-focused owner-only expectation remains unmet. Not a confirmed Saleor vulnerability.

## Source-supported interpretation

- `saleor/graphql/order/resolvers.py::resolve_order` resolves a UUID or legacy number; actor-level authorization must be assessed across the downstream GraphQL field resolvers.
- `saleor/graphql/order/types.py` applies a different disclosure path for new UUID orders versus legacy-number orders; `saleor/core/anonymize.py` is used in legacy redaction.
- Legacy email obfuscation retains its domain and the first local-part character; street obfuscation retains the first character and length. This describes residual information, not an approved privacy verdict.
- Knowing a UUID is not proof that UUIDs are guessable, discoverable, or exploited in a deployment.

## Other checks at tested source head

- General tests: SUCCESS; E2E: SUCCESS; changelog: SUCCESS.
- Linters: FAILURE solely because Ruff reformatted the new C9 test file; formatter output was recorded in run 39141812700.
- Ruff-only correction committed in `39955108fd148c571aab8aba959b1ae30203a2e4` and later `e3a1d5c1a66795560fc48f09fff72ae3c6afbcbe` (check history for actual current head).
- On `e3a1d5c1a66795560fc48f09fff72ae3c6afbcbe`, CI showed changelog SUCCESS and E2E SUCCESS, while focused security, linters and general tests were CANCELLED. **Do not claim final green CI at that SHA.**

## Remaining closure gates

1. Revalidate all required CI checks at one final SHA, with no cancellations.
2. Independently test exact legacy redaction representations and remaining residual disclosure.
3. Complete staff/app/delegated permission matrix and intended UUID bearer/share-link semantics.
4. Reconcile each executed JUnit variant with the test matrix, artifact hashes, and interpretation.
5. Seek explicit policy-owner adoption/rejection of P-ORDER-01 before calling a CyberMarket requirement nonconformance; do not treat it as an official Saleor requirement.
6. Deployed HTTPS/proxy/browser risk remains outside this isolated fixture-based suite without an authorized target.

Scope: research tests, workflow and documentation only; no Saleor product code, Avance 1, or PR merge.
