# C9-R1 CI checkpoint

Status: OPEN. Focused run 39151402065 passed (59 PASS, 2 expected XFAIL). Linters 39151402041 failed (Ruff, mypy and deptry). General run 39151402037 was cancelled. New verification is pending. No Saleor product code changed. No merge or final closure.

Evidence: JUnit artifact 12144759037 contains 61 invocations across 27 cases; all three SHA256SUMS entries were verified. SAST artifact 12145496896 contains one Bandit B105 LOW/MEDIUM finding at saleor/core/jwt.py:23, previously triaged as a scanner false positive. E2E 39151402043 succeeded. The latest branch revision is under revalidation; do not reuse results from a previous SHA.
