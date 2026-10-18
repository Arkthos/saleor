"""Fail closed when CyberMarket JUnit evidence is incomplete or ambiguous."""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

EXPECTED_VARIANTS = {
    "CM-T01": 1, "CM-T02": 1, "CM-T03": 4, "CM-T04": 1,
    "CM-T05": 1, "CM-T06": 1, "CM-T07": 1, "CM-T08": 1,
    "CM-T09": 2, "CM-T10": 1, "CM-T11": 1, "CM-T12": 1,
    "CM-T13": 1, "CM-T14": 2, "CM-T15": 1, "CM-T16": 1,
    "CM-T17": 3, "CM-T18": 3, "CM-T19": 6, "CM-T20": 2,
    "CM-T21": 1, "CM-T22": 2, "CM-T23": 6, "CM-T24": 3,
    "CM-T25": 6, "CM-T26": 2, "CM-T27": 6,
}
ALLOWED_TYPES = {
    "security_contract", "characterization_only", "proposed_policy_expected_fail"
}
SAFE_NAME = re.compile(r"^[A-Za-z0-9_.,:\[\] /-]{1,200}$")


def validate(matrix: Path, summary: Path) -> dict:
    with matrix.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    data = json.loads(summary.read_text(encoding="utf-8"))
    matrix_ids = [r["case_id"] for r in rows]
    if len(matrix_ids) != len(set(matrix_ids)) or set(matrix_ids) != set(EXPECTED_VARIANTS):
        raise ValueError("Matrix case IDs do not match reviewed expected set")
    cases = data["cases"]
    counts = Counter()
    variants = set()
    for case in cases:
        case_id = case["case_id"]
        if case_id not in EXPECTED_VARIANTS:
            raise ValueError(f"Unknown or missing case ID: {case_id!r}")
        if case["evidence_type"] not in ALLOWED_TYPES:
            raise ValueError(f"Invalid evidence type: {case_id}")
        if case["outcome"] not in {"PASS", "XFAIL"}:
            raise ValueError(f"Unexpected outcome: {case_id}: {case['outcome']}")
        name = case["variant"] or case["test_function"]
        if not SAFE_NAME.fullmatch(name):
            raise ValueError(f"Unsafe or malformed test identifier: {case_id}")
        key = (case_id, name)
        if key in variants:
            raise ValueError(f"Duplicate variant: {case_id}: {name}")
        variants.add(key)
        counts[case_id] += 1
    if dict(counts) != EXPECTED_VARIANTS:
        raise ValueError(f"Unexpected variant cardinality: {dict(counts)}")
    if data["test_count"] != len(cases):
        raise ValueError("Summary test_count differs from cases length")
    if sum(data["counts"].values()) != len(cases):
        raise ValueError("Summary outcome counts differ from cases length")
    for row in rows:
        if any(c["evidence_type"] != row["evidence_type"] for c in cases if c["case_id"] == row["case_id"]):
            raise ValueError(f"Evidence type drift: {row['case_id']}")
    if any(c["outcome"] != "XFAIL" for c in cases if c["case_id"] == "CM-T22"):
        raise ValueError("Provisional policy outcomes must be strict XFAIL")
    if any(c["outcome"] != "PASS" for c in cases if c["case_id"] != "CM-T22"):
        raise ValueError("Unexpected non-PASS outside provisional policy")
    return {"cases": len(counts), "executions": len(cases), "validated": True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(args.matrix, args.summary), sort_keys=True))


if __name__ == "__main__":
    main()
