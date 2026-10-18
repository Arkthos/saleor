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
legacy order number. Owner A is expected to retrieve the fields; actor B
and anonymous C are expected to be denied on the selected query.
This is a bounded contract for legacy-ID behavior, not global proof of
object-level security.

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
- **PENDING:** focused test run and general CI on the final C3 commit; do not inherit C2's 8/8 verdict.
- **PENDING:** EvidenceSynth MAP/GAP/AUDIT on any failing or surprising cases.
- **PENDING:** decide authorized intended behavior for new UUIDs versus legacy numbers, including possession of ID and customer entitlement.
- **PENDING:** staff permission matrix and field-level tests, token audience/type, cookie settings and bounded GraphQL limits.
- **PENDING:** retain and review artifacts; only finalize C3 result once run+SHA+JUnit checks are verified.

Keep the user-validated Avance 1 unchanged. No merge before review, CI closure and interpretation.
