# CyberMarket CR — C5 selected trust and delegated-permission contracts

**State:** IMPLEMENTED; targeted GitHub Actions result pending.
**Research code baseline:** `4cb1609a90eade14b6275a407bc7a00c35698090`
**Pull request:** https://github.com/Arkthos/saleor/pull/1 (draft)

## Hypotheses and oracles

| ID | Code boundary under test | Expected result | Claim limits |
| --- | --- | --- | --- |
| CM-T17 | `get_token_from_request` special/fallback Authorization headers | Separate prioritized header, valid JWT/Bearer fallback; reject Basic header | Characterizes parsing only; no upstream intermediary tested |
| CM-T18 | `get_client_ip` with `X-Forwarded-For` and `REMOTE_ADDR` | First syntactically valid forwarded IP, otherwise remote address | Characterizes an IP trust assumption; cannot prove an actual proxy permits spoofing |
| CM-T19 | `get_delay_time` on small and boundary attempt counts | IP and IP/user exponential backoff with cap `MAX_DELAY` | Does not validate cache, concurrent requests, header trust, or production throttling effectiveness |
| CM-T20 | `create_access_token_for_app` under overlapping and disjoint user/app perms | Delegated token permissions equal set intersection | Does not check all downstream permission consumers |
| CM-T21 | JWT verification of `alg=none` payload | Reject unsigned credential | Narrow negative algorithm test, not cryptographic certification |

**Preconditions:** Isolated fixture-backed Django tests. Actor keys, clients, addresses and identifiers are synthetic. No open network scanning, brute force, remote proxy, or third-party credentials.

**Execution:** The dedicated workflow `.github/workflows/cybermarket-security.yaml` executes all `saleor/graphql/tests/test_cybermarket_security_*.py` tests, emits XML, sanitized JSON and SHA-256. C5 source file: `saleor/graphql/tests/test_cybermarket_security_trust_boundaries.py`.

**ASVS/WSTG mappings:** `security/cybermarket/test_matrix.csv` contains *candidate mappings requiring human validation against the normative texts*. Passing is not ASVS conformance.

## Results gate

No C5 results may be announced before verifying GitHub run ID, source/checkout commit SHA, parsed JUnit case count, outcome distribution, artifact IDs and integrity hashes. Record any failure, reproduce, determine whether test expectation, fixture, infrastructure or code caused it; do not silently rewrite observations.

## Remaining external-environment evidence gaps

- R01/R02: header spoofability and rate limiting behind a **specific trusted-proxy deployment** remain untested.
- R04/R06: secure cookie transport, CSRF in an actual browser and deployment flags remain only locally characterized.
- R11: new-UUID order PII access policy is **UNRESOLVED**. CM-T05/T06 must never be classified as compliance.
- R13: app delegated permission consumers and external token audience enforcement beyond claims remain only partly covered.
- C5 does not execute a full browser/DAST scanner; deterministic GraphQL requests are in-process integration/dynamic tests.

## Next

Review all C2–C5 run artifacts and classify findings through EvidenceSynth MAP/GAP/AUDIT. Decide which gaps require a separately deployed, explicitly authorized laboratory. No academic article drafting and no PR merge at this stage.
