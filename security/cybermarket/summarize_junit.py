"""Sanitized, deterministic CyberMarket JUnit report and integrity manifest.

Only predefined test metadata and outcomes are exported. No assertion
tracebacks, requests, JWTs, cookie values, account email or response bodies.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
from xml.etree import ElementTree as ET


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def summarize(junit: Path, commit: str) -> dict:
    root = ET.parse(junit).getroot()
    suites = [root] if root.tag == "testsuite" else root.findall(".//testsuite")
    cases = []
    for suite in suites:
        for test in suite.findall("testcase"):
            props = {
                p.get("name"): p.get("value")
                for p in test.findall("./properties/property")
            }
            verdict = (
                "ERROR"
                if test.find("error") is not None
                else "FAIL"
                if test.find("failure") is not None
                else "SKIP"
                if test.find("skipped") is not None
                else "PASS"
            )
            name = (test.get("name") or "").split("[", 1)[0]
            cases.append(
                {
                    "case_id": props.get("cybermarket_case_id", "UNMAPPED"),
                    "variant": test.get("name", "")
                    if "[" in test.get("name", "")
                    else "",
                    "test_function": name,
                    "risk_ids": props.get("risk_id", ""),
                    "observation_ids": props.get("observation_id", ""),
                    "evidence_type": props.get("evidence_type", "unclassified"),
                    "outcome": verdict,
                }
            )
    counts = {
        kind: sum(case["outcome"] == kind for case in cases)
        for kind in ("PASS", "FAIL", "ERROR", "SKIP")
    }
    return {
        "schema": "cybermarket.junit.summary.v1",
        "source_commit": commit,
        "junit_sha256": sha256(junit),
        "test_count": len(cases),
        "counts": counts,
        "cases": sorted(cases, key=lambda x: (x["case_id"], x["variant"])),
        "note": "Runtime outcomes only; PASS is not ASVS security conformance.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--junit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--commit", default=os.environ.get("GITHUB_SHA", "local"))
    args = parser.parse_args()
    summary = summarize(args.junit, args.commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"CyberMarket: {summary['test_count']} cases, {summary['counts']}")


if __name__ == "__main__":
    main()
