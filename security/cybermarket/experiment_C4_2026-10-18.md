# CyberMarket CR — C4 test implementation and evidence checkpoint

**State:** EXECUTED AND VERIFIED for the scoped C4 focused workflow. This is an execution verdict, not full ASVS compliance.
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

## Verified C4 runtime and SAST evidence

- Workflow: [CyberMarket GraphQL security evidence #39130431874](https://github.com/Arkthos/saleor/actions/runs/39130431874).
- PR branch head associated with this execution: `0a5d3539e1b2e6b5841d0dcf09e9472f05c9bf1f`; GitHub's PR synthetic checkout/merge commit recorded in the JUnit summary as `7767beaef5e3d06d02ded614af23325e3c849cbd`. These are distinct GitHub refs; do not silently collapse them.
- Focused pytest: **21 executions / 21 PASS / 0 FAIL / 0 ERROR / 0 SKIP**, across 16 identified cases CM-T01–T16.
- JUnit artifact: `cybermarket-security-junit`, ID `12138186188`.
- JUnit XML SHA-256: `68eba0f4595a82b02465154916453b5666d668673439cf46614724255dc0ef46`.
- Sanitized summary SHA-256: `64e7bee10df5179eb4fc4d697610eb006a4dfadbb0e6058607c10d42fca26572`.
- Artifact ZIP SHA-256: `71c167f2b05d238cd6a527038b9f55d5e21233bcf5c8f18b64c9a743304db269`.
- SAST artifact: `cybermarket-static-review`, ID `12137616867`.
- Bandit 1.8.6: finished with exit code 0; **4,629 lines measured**, 0 reported matches at the specified medium-or-greater severity **and** confidence threshold, one low-severity signal present in aggregated metrics but not reported under `-ll -ii`.
- Bandit JSON SHA-256: `e2867e7a1a6d10f5c75d744245f64f18b2e6f28b60b989e48983e88395addcae`.
- Static artifact ZIP SHA-256: see retained artifact, do not treat a zero count as evidence of no vulnerabilities.

**Interpretation:** This verifies the behavior of selected code paths and SAST scan execution. It does **not** prove correct use of proxies, configured production values, cross-origin browser behavior, an exhaustive risk assessment or ASVS compliance. CM-T05/CM-T06/CM-T14 remain characterization-only.

## Follow-on after C4

1. Fix CI/lint/test defects and retain both original and corrected run references.
2. Investigate R01 header normalization, R02 throttling semantics, R13 app permission intersections using synthetic fixtures without speculative claims.
3. Triaging static results: `confirmed`, `false positive`, `needs context`, `out of scope` with code anchors.
4. Produce a final execution coverage matrix and EvidenceSynth MAP/GAP/AUDIT.
5. **No Avance 2 manuscript drafting in this phase; no merge while checks are failing.**
