# CyberMarket CR — C4 test implementation and evidence checkpoint

**State:** IMPLEMENTED; first targeted CI run required before any claim of success.
**Date:** 2026-10-18 UTC.
**Source baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090` (Saleor).
**PR:** https://github.com/Arkthos/saleor/pull/1 (draft).

## Experiment design

| Case | Runtime condition | Expected behavior | Academic interpretation |
| --- | --- | --- | --- |
| CM-T08 | Login with synthetic correct credentials and `audience` | Access/refresh type, TTL and prefixed audience match configured values | Contract in fixture |
| CM-T09 | Known account invalid password vs absent account | Same `INVALID_CREDENTIALS` code and no issued token | Narrow error-code check, not full user-enumeration test |
| CM-T10 | Signed access JWT passed to `tokenRefresh` | Error `JWT_INVALID_TOKEN` | Wrong-type rejection |
| CM-T11 | Refresh with custom audience | New access token preserves `aud` | Claim continuity, **not audience enforcement** |
| CM-T12 | `user(id:)` by unrelated customer and anonymous | Permission denied | Cross-actor object access |
| CM-T13 | `MANAGE_USERS` versus `MANAGE_STAFF` | Customer/staff selection partitions | Privilege boundary |
| CM-T14 | Cookie emission under `DEBUG=False` and `DEBUG=True` | `HttpOnly`, `Secure`, `SameSite` values match code | **Characterization only**; production transport unverified |
| CM-T15 | Two aliases with configured limit 1 | GraphQL request validation error | Bounded alias gate |
| CM-T16 | Two mutations with configured limit 1 | Validation error before execution | Bounded mutation-count gate |

All conditions use ephemeral test databases and synthetic data. No third-party endpoints, production credentials or unbounded load are used.

## Static scope

Separate GitHub Actions `Scoped Python SAST evidence` job:
- Bandit 1.8.6 pinned at invocation (not introduced as a Saleor production dependency).
- Scope: `saleor/core/auth.py`, `auth_backend.py`, `jwt.py`, `jwt_manager.py`, `saleor/graphql/account/mutations/authentication`, `saleor/graphql/order/{schema,resolvers,types}.py`.
- Only medium-or-higher severity and confidence scanner matches included (`-ll -ii`); capture `bandit.json`, run metadata and checksum.
- Bandit exit 1 from findings is **not** automatically a failed security requirement. Parser/runner errors are workflow failures. Classify each match only after line-level code and exploitability review.
- The project's preexisting Semgrep pre-commit hook is an additional source but not a substitute for a captured, triaged SAST report.

## Evidence standard

The focused pytest workflow writes a `cybermarket-junit.xml` and a deterministic redacted `cybermarket-summary.json` containing source SHA, case IDs, classification, risk IDs, observation IDs and raw outcomes; artifact includes `SHA256SUMS`.

For each evaluation: preserve workflow run URL and ID, tested commit, artifact IDs, SHA-256, tool versions, expected/observed behavior, limitations, and reasons for fixing test harness versus production code.

**Critical:** CM-T05 and CM-T06 are characterization tests and CM-T14 is configuration characterization. A green result is NOT an ASVS conformance decision. New-UUID order field disclosure remains a pending security-policy question (R11/H12).

## Follow-on after C4

1. Fix CI/lint/test defects and retain both original and corrected run references.
2. Investigate R01 header normalization, R02 throttling semantics, R13 app permission intersections using synthetic fixtures without speculative claims.
3. Triaging static results: `confirmed`, `false positive`, `needs context`, `out of scope` with code anchors.
4. Produce a final execution coverage matrix and EvidenceSynth MAP/GAP/AUDIT.
5. **No Avance 2 manuscript drafting in this phase; no merge while checks are failing.**
