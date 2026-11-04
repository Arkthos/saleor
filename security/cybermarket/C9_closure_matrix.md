# C9 experimental closure plan — executable hypotheses

This checkpoint replaces vague caveats with explicit technical questions, test methods and closure criteria. It does not claim unexecuted results.

## Established by source inspection
- `saleor/graphql/order/resolvers.py::resolve_order` resolves an existing order by UUID or legacy number without an actor-level permission check in that function. Authorization/redaction may occur downstream and must be tested at GraphQL field level.
- CM-T05/06 already compare raw email and both street fields for synthetic anonymous/unrelated actors using a known UUID.
- CM-T22 currently asserts only email redaction (or null order), despite the three-field proposed policy.
- A passing characterization is an established behavior for the tested fixture, not evidence of compliance.

## Closure matrix

| Question | Next test | Technical close criterion |
|---|---|---|
| Is each sensitive field accessible with known UUID to anonymous/peer? | Parametrize 2 actors x 3 fields, retain raw-value assertions and response status | Six independently reported field/actor outcomes |
| Does owner retain legitimate access? | Owner control on same order/fields | Three owner fields verified, no policy regression |
| Does legacy number actually redact sufficiently? | Assert exact permitted masking representation and detect partial leakage, separately for all fields | Defined expected outputs and three per-actor outcomes |
| Is a UUID itself intended as a bearer capability? | Source trace plus order-by-token, sharing and token-specific test coverage | Documented implementation contract; business entitlement remains a distinct decision |
| Is UUID exposure practically obtainable? | Authorized end-to-end flow using fixture IDs, no guessing assumptions | Verified source of ID or explicit environmental block |
| Are roles/staff/apps exceptional? | Test permission matrix including scoped delegated app | Observed per-role authorization and field-level visibility |
| Can artifacts support a verdict? | JUnit case IDs + per-variant matrix, SHA256, run SHA, focused + general CI | Reproducible evidence, no unmapped variants |

## Decision rules
- A technical behavior can be CLOSED—VERIFIED even when business authorization remains BLOCKED—POLICY.
- Under provisional P-ORDER-01, a field that exposes raw data to a nonowner with only a known UUID is a reproducible **provisional requirement mismatch**; do not assert a confirmed Saleor vulnerability.
- An approved policy and independently reproduced mismatch permit a CyberMarket-specific nonconformance finding, not automatic generalization to deployed Saleor.
- XFAIL must not obscure field-level failures: retain distinct, strict assertions and report each actor/field independently.
- No modification to Saleor product code, historical oracles, Avance 1 or PR merge.

## Execution
Implement the missing independent cases in the research suite, run in isolated GitHub Actions, compare JUnit with coverage and review failures before any interpretation. Current document is a checkpoint only; execution and acceptance remain pending.
