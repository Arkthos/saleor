"""Build a conservative, machine-readable coverage map from JUnit evidence.

This tool does not certify OWASP ASVS or determine vulnerability status.
It fails if the current matrix and the executed test cases drift apart.
"""

import argparse
import csv
import json
import logging
from typing import TypedDict
from collections import Counter, defaultdict
from pathlib import Path


logger = logging.getLogger(__name__)


class CaseReport(TypedDict):
    """Normalized per-case row used to calculate risk coverage."""

    case_id: str
    risk_ids: list[str]
    observation_ids: list[str]
    asvs_ids: list[str]
    wstg_ids: list[str]
    evidence_type: str
    execution_count: int
    outcomes: dict[str, int]
    status: str


# Reviewed subset against pinned ASVS 5.0.0 corpus and WSTG v4.2.
# An ID match does not demonstrate compliance with a control.
ALLOWED_ASVS_IDS = {
    "v5.0.0-3.3.1",
    "v5.0.0-3.3.2",
    "v5.0.0-3.3.4",
    "v5.0.0-3.5.1",
    "v5.0.0-4.3.1",
    "v5.0.0-6.1.3",
    "v5.0.0-6.3.1",
    "v5.0.0-6.3.8",
    "v5.0.0-7.4.1",
    "v5.0.0-8.2.1",
    "v5.0.0-8.2.2",
    "v5.0.0-8.2.3",
    "v5.0.0-9.1.2",
    "v5.0.0-9.2.1",
    "v5.0.0-9.2.2",
    "v5.0.0-9.2.3",
}
ALLOWED_WSTG_IDS = {
    "WSTG-APIT-01",
    "WSTG-ATHN-03",
    "WSTG-ATHN-04",
    "WSTG-ATHZ-02",
    "WSTG-ATHZ-04",
    "WSTG-IDNT-04",
    "WSTG-SESS-02",
    "WSTG-SESS-05",
    "WSTG-SESS-06",
    "WSTG-SESS-07",
}


def produce_coverage(matrix_path: Path, summary_path: Path) -> dict:
    with matrix_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    executed = defaultdict(list)
    for row in summary["cases"]:
        executed[row["case_id"]].append(row)
    indexed = {row["case_id"]: row for row in rows}
    asvs_used = {item for row in rows for item in row["asvs_ids"].split(";") if item}
    wstg_used = {item for row in rows for item in row["wstg_ids"].split(";") if item}
    unknown_asvs = sorted(asvs_used - ALLOWED_ASVS_IDS)
    unknown_wstg = sorted(wstg_used - ALLOWED_WSTG_IDS)
    if unknown_asvs or unknown_wstg:
        raise ValueError(
            f"Unreviewed normative IDs: ASVS={unknown_asvs}; WSTG={unknown_wstg}"
        )
    if len(indexed) != len(rows):
        raise ValueError("Duplicate case ID in CyberMarket matrix")

    missing_execution = sorted(set(indexed) - set(executed))
    missing_traceability = sorted(set(executed) - set(indexed))
    if missing_execution or missing_traceability:
        raise ValueError(
            "Case mapping drift: not executed="
            f"{missing_execution}; not mapped={missing_traceability}"
        )

    case_reports: list[CaseReport] = []
    for case_id, metadata in sorted(indexed.items()):
        results = executed[case_id]
        declared_type = metadata["evidence_type"]
        if any(result["evidence_type"] != declared_type for result in results):
            raise ValueError(f"Evidence type drift: {case_id}")
        outcomes = dict(Counter(result["outcome"] for result in results))
        case_reports.append(
            {
                "case_id": case_id,
                "risk_ids": metadata["risk_ids"].split(";"),
                "observation_ids": metadata["observation_ids"].split(";"),
                "asvs_ids": metadata["asvs_ids"].split(";"),
                "wstg_ids": metadata["wstg_ids"].split(";"),
                "evidence_type": declared_type,
                "execution_count": len(results),
                "outcomes": outcomes,
                "status": (
                    "OBSERVED_NOT_CERTIFIED"
                    if declared_type == "characterization_only"
                    and outcomes == {"PASS": len(results)}
                    else "CONTRACT_PASSED_REVIEW_PENDING"
                    if outcomes == {"PASS": len(results)}
                    else "REQUIRES_INVESTIGATION"
                ),
            }
        )

    coverage = []
    for risk_num in range(1, 14):
        risk_id = f"R{risk_num:02}"
        linked = [c for c in case_reports if risk_id in c["risk_ids"]]
        contract_count = sum(
            c["evidence_type"] != "characterization_only" for c in linked
        )
        characterization_count = len(linked) - contract_count
        coverage.append(
            {
                "risk_id": risk_id,
                "cases": [c["case_id"] for c in linked],
                "contracts": contract_count,
                "characterizations": characterization_count,
                "classification": (
                    "UNTESTED"
                    if not linked
                    else "CHARACTERIZED_ONLY"
                    if not contract_count
                    else "MIXED_EVIDENCE_REVIEW_PENDING"
                    if characterization_count
                    else "CONTRACT_EVIDENCE_REVIEW_PENDING"
                ),
                "security_verdict": "NO_DETERMINADO",
            }
        )

    return {
        "schema": "cybermarket.coverage.v1",
        "tested_merge_commit": summary["source_commit"],
        "junit_sha256": summary["junit_sha256"],
        "executed_cases": len(case_reports),
        "executions": summary["test_count"],
        "outcomes": summary["counts"],
        "mapped_risks": sum(bool(item["cases"]) for item in coverage),
        "risk_count": len(coverage),
        "cases": case_reports,
        "risks": coverage,
        "warning": (
            "Presence of tests and PASS do not establish full control coverage, "
            "successful exploitation, ASVS conformance or residual risk."
        ),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    report = produce_coverage(args.matrix, args.summary)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    logger.info(
        "CyberMarket: %s executions, %s cases, %s/%s risks mapped",
        report["executions"],
        report["executed_cases"],
        report["mapped_risks"],
        report["risk_count"],
    )


if __name__ == "__main__":
    main()
