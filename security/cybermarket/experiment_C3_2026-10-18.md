# CyberMarket CR — Experiment checkpoint C3 (cross-customer access)

**Date:** 2026-10-18 UTC
**Repository / PR:** [Arkthos/saleor PR #1](https://github.com/Arkthos/saleor/pull/1) (draft)
**Pinned academic baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090`
**C2 measured implementation SHA:** `f66c7ad83a43573d862331a4c4727391d30ed651` — [8/8 successful](https://github.com/Arkthos/saleor/actions/runs/39127189591)
**C3 test-code commit SHA:** `95d344b7db601b6901df4bb4703f8c9b79481f23` (later commits update only traceability/docs)

## Scope and method

Question R11/H12: How does this Saleor revision handle selected order PII fields
(`userEmail`, `billingAddress.streetAddress1`,
`shippingAddress.streetAddress1`) across three actor states?

- **Actor A:** authenticated owner (fixture `user_api_client` / `customer_user`).
- **Actor B:** distinct authenticated customer (fixture `user2_api_client` / `customer_user2`).
- **Actor C:** anonymous client (`api_client`).
- **Resource:** one synthetic order that belongs to actor A; the test asserts ownership and distinct identity.
- **Operation:** GraphQL `order(id:)` with the same selected fields.
- **ID modes:** new UUID (CM-T06) and legacy order number (CM-T07).

### CM-T06 — Characterization only (not a security conformance test)

Existing upstream tests confirm that the new-UUID route returns
address/email fields for anonymous users in the pinned revision.
CM-T06 additionally compares a *different authenticated customer*.
It intentionally asserts equal selected fields across A, B and C to
reproduce the existing behavior in a controlled synthetic fixture.

**Important:** A PASS on CM-T06 documents field disclosure given a known
order UUID; it is NOT approval of that behavior, a proof that order UUIDs
are guessable, an assertion of exploitability or ASVS compliance. Whether
cross-customer field disclosure violates product policy remains
**UNDETERMINED** without authoritative ownership/access requirements and
context for UUID possession.

### CM-T07 — Legacy order-number security contract

Switch the same order to `use_old_id=True` and address it by the
legacy order number. Owner A should receive complete selected fields;
actor B and anonymous C should receive masked email/address fields.
This is a bounded *field-redaction* contract for legacy-ID behavior, not
a claim that access to the whole order is denied.

## Traceability and evidence handling

| Test | Risk | Observation | Evidence type | Security verdict before C3 execution |
| --- | --- | --- | --- | --- |
| CM-T06 | R11 | H12 | `characterization_only` | NO_DETERMINADO |
| CM-T07 | R11 | H12 | `security_contract` | NO_DETERMINADO |

- Source: `saleor/graphql/tests/test_cybermarket_security_contracts.py`.
- Matrix: `security/cybermarket/test_matrix.csv`.
- Preliminary ASVS candidates: 5.0.0 §8.2.2/8.2.3; WSTG 4.2 ATHZ-04. Mapping is not compliance certification.
- Evidence: dedicated GitHub Actions run JUnit; record run ID, code SHA, timestamps, results, JUnit test properties and SHA-256.
- No sensitive production records or live credentials. In-memory fixtures only. JUnit must not contain address values.

## Status and next decisions

- **IMPLEMENTED:** CM-T06 and CM-T07 code committed; README and matrix updated.
- **OBSERVED (initial C3):** run [39128224126](https://github.com/Arkthos/saleor/actions/runs/39128224126) against original C3 source produced 10 tests: 9 PASS, 1 FAIL, 0 errors/skips. CM-T06 passed (characterization). CM-T07 failed because the test assumed full-object denial for customer B; actual response contained the order with selected email and address fields **obfuscated**. This is a test-oracle mismatch, not by itself a security finding. Original JUnit artifact ID 12136982575 (ZIP SHA-256 `dfcfec96d00d2a8d8ff5ed2049a04b843c4658b0519fafa7be62afe594fa95a1`; JUnit SHA-256 `15e2955d0f32da42c22996bfb5e0d44ad353437eb21fafdd6ca91d7f1700da29`).
- **CORRECTED:** commit `3b8064b08b07d71e2fd3a0e8c89c572de7e36c4e` updates CM-T07 to verify that the owner receives complete selected fields and other customers/anonymous actors receive masked fields. This is a bounded field-level contract, not a general object-denial assertion.
- **VALIDATED:** corrected C3 code passed [run 39128693170](https://github.com/Arkthos/saleor/actions/runs/39128693170), checked-out code commit `1c5bb613d68817c5829fa5a953e2618bfb531979`: 10/10 tests passed, 0 failed, 0 errors and 0 skipped; reported duration 166.383 seconds. JUnit artifact 12137387020 (ZIP SHA-256 `a3a2cf98ebd929703da2061e489bdb6721104fc18b2cea2551599c2839cc8083`; JUnit XML SHA-256 `763148af9946595b661f9cadd703aaaef04ac7d7bde4f0350d1d7cb72c9a968b`). Raw results were manually parsed to verify all 10 case entries and metadata.
- **PENDING:** general repository CI (linters/full unit/e2e) on the latest documentation commit; the original C3 failure remains retained as historical evidence.
- **INTERPRETATION:** 10/10 PASS is an execution outcome, **not** a security/compliance decision. CM-T05/CM-T06 remain `NO_DETERMINADO_CHARACTERIZATION` while intended new-UUID order-data exposure is unresolved.
- **DONE (initial AUDIT):** CM-T07's failure was traced to the wrong test oracle. The actual masked response was confirmed in JUnit and the corresponding `Order` field resolvers. Updated the test to assert owner-vs-nonowner field masking; rerun is green.
- **PENDING:** complete EvidenceSynth MAP/GAP/AUDIT for R11/H12, including the new UUID policy gap, scope and threat model.
- **PENDING:** decide authorized intended behavior for new UUIDs versus legacy numbers, including possession of ID and customer entitlement.
- **PENDING:** staff permission matrix and field-level tests, token audience/type, cookie settings and bounded GraphQL limits.
- **PENDING:** retain and review artifacts; only finalize C3 result once run+SHA+JUnit checks are verified.

Keep the user-validated Avance 1 unchanged. No merge before review, CI closure and interpretation.
