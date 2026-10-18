# C9-R1 CI checkpoint

Status: OPEN. Focused run 39151402065 passed (59 PASS, 2 expected XFAIL). Linters 39151402041 failed (Ruff, mypy and deptry). General run 39151402037 was cancelled. New verification is pending. No Saleor product code changed. No merge or final closure.

Evidence: JUnit artifact 12144759037 contains 61 invocations across 27 cases; all three SHA256SUMS entries were verified. SAST artifact 12145496896 contains one Bandit B105 LOW/MEDIUM finding at saleor/core/jwt.py:23, previously triaged as a scanner false positive. E2E 39151402043 succeeded. The latest branch revision is under revalidation; do not reuse results from a previous SHA.

## CI closure verification — 2026-10-18

All required workflows on PR-head `ca2e7d2d39f75308e5bdcd12735f73ca06302dc1` completed SUCCESS: Linters 39158960622, focused GraphQL and SAST 39158960620, general Tests 39158960695, E2E 39158960630 and Changelog 39158960627. Focused: 59 PASS, 2 expected XFAIL, 0 FAIL/ERROR/SKIP (61 variants/27 cases); six evidence-validator regressions PASS. General: 17,613 PASS, 2 expected XFAIL, 0 FAIL/ERROR (17,615 JUnit entries, 34 warnings). E2E: 211 PASS, 3 warnings.

Artifact SHA-256 ZIPs verified independently: focused 12147854253 `9ecda9c48df4a5cce6dbf498a922cf08a641363874b1f90f44ee8ea441c891bd`; general JUnit 12148706646 `01407bd2c364116c4b946a4ed0ac0eb3af1fabfb249360b953f10beaf2186733`; SAST 12148162080 `eec36fc2420af784c9f09944ecc841148c07cb10d520a82ce2c276c15fb6cc74`; query counts 12148885974 `740a802c16de81655dee005f81412dc1f31870375770b97cb285c9a547d48a49`. Embedded SHA256SUMS entries for focused and SAST all matched. General XML independently parsed: 17,615 cases, no failures/errors, two expected pytest.xfail; focused summary matches its 61 cases. All 13 mapped risk verdicts remain NO_DETERMINADO. One Bandit B105 LOW finding (cookie-name false positive) persists. C10 live validation not executed; no vulnerability or approved-policy breach established. CI-scope C2–C9 can close; academic writing, deployment, product code changes and PR merge remain excluded.
