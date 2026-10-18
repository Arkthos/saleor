# CyberMarket CR — C5 selected trust and delegated-permission contracts

**State:** EXECUTED AND VERIFIED with a scoped, fixture-based runtime contract. No general security certification.
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

## Verified C5 artifacts and outcomes

- GitHub Actions: [run 39131023314](https://github.com/Arkthos/saleor/actions/runs/39131023314).
- PR branch SHA evaluated: `27f900ad937f15eaa1af06e1f1534424f88bf3ce`; GitHub PR synthetic merge SHA in source manifest: `9ef6c4ab8532fa5a7a2f3ca5102f2e0db3dba4a3`.
- Pytest results: **36 PASS / 0 FAIL / 0 ERROR / 0 SKIP**; 21 case IDs, including C5 header, IP, throttle, app permissions and JWT algorithm checks.
- JUnit artifact: `cybermarket-security-junit` (ID `12138276744`).
- JUnit XML SHA-256: `7f33df6c83b6c6d91aec27c3a340665fbcb2b5bd7dfd04ff950b5b40fcdc8a7d`.
- Sanitized summary JSON SHA-256: `25dc27f809568ef82d0303b8c3f2902b15ea5739c945c943c72b806cb8c894f6`.
- Artifact ZIP SHA-256: `536ca63008916b3fa463526da9d1ec7f4713d5b4a516337a8637083705d78a64`.
- Static artifact: `cybermarket-static-review` (ID `12138082357`).
- Bandit JSON SHA-256: `b166a288e515afc011419401807f9ae75872c904ee73716fc85dac3d8b0f4da3`. Bandit 1.8.6 examined 4,629 LOC and found **zero reported medium+ severity and confidence** matches under the specified filter; one low-severity signal was present in metrics but omitted by threshold.
- Bandit artifact ZIP SHA-256: `d5df677a083edecd0c5fc38106e34d913d321034e1996d1df9901c6873f43dd8`.

These are real execution results, not a statement that all 13 risks were fully eliminated. CM-T05/06/14/17/18 are characterization-only; staff/role details remain limited to fixture code paths.

## Results gate

Completed. JUnit, summary, SAST JSON and artifact checksums were inspected and recorded above. Subsequent C6 documentation/workflow changes need their own validation run, not inherited PASS claims from this checkpoint.

## Remaining external-environment evidence gaps

- R01/R02: header spoofability and rate limiting behind a **specific trusted-proxy deployment** remain untested.
- R04/R06: secure cookie transport, CSRF in an actual browser and deployment flags remain only locally characterized.
- R11: new-UUID order PII access policy is **UNRESOLVED**. CM-T05/T06 must never be classified as compliance.
- R13: app delegated permission consumers and external token audience enforcement beyond claims remain only partly covered.
- C5 does not execute a full browser/DAST scanner; deterministic GraphQL requests are in-process integration/dynamic tests.

## Next

Review all C2–C5 run artifacts and classify findings through EvidenceSynth MAP/GAP/AUDIT. Decide which gaps require a separately deployed, explicitly authorized laboratory. No academic article drafting and no PR merge at this stage.
