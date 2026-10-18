"""Regression tests for CyberMarket evidence integrity gates."""
import csv
import json
from pathlib import Path

import pytest

from security.cybermarket.validate_evidence import EXPECTED_VARIANTS, validate


def _fixture(tmp_path: Path):
    matrix = tmp_path / "matrix.csv"
    with matrix.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["case_id", "evidence_type"])
        writer.writeheader()
        for case_id in EXPECTED_VARIANTS:
            writer.writerow({
                "case_id": case_id,
                "evidence_type": (
                    "proposed_policy_expected_fail" if case_id == "CM-T22"
                    else "security_contract"
                ),
            })
    cases = [
        {
            "case_id": case_id,
            "test_function": f"test_{case_id.replace('-', '_').lower()}",
            "variant": f"test_{case_id.replace('-', '_').lower()}[{i}]"
            if count > 1 else "",
            "evidence_type": (
                "proposed_policy_expected_fail" if case_id == "CM-T22"
                else "security_contract"
            ),
            "outcome": "XFAIL" if case_id == "CM-T22" else "PASS",
        }
        for case_id, count in EXPECTED_VARIANTS.items()
        for i in range(count)
    ]
    summary = tmp_path / "summary.json"
    payload = {
        "test_count": len(cases),
        "counts": {"PASS": len(cases) - 2, "XFAIL": 2},
        "cases": cases,
    }
    summary.write_text(json.dumps(payload), encoding="utf-8")
    return matrix, summary, payload


def test_complete_manifest_passes(tmp_path):
    matrix, summary, _ = _fixture(tmp_path)
    assert validate(matrix, summary) == {
        "cases": 27, "executions": 61, "validated": True
    }


@pytest.mark.parametrize("defect", [
    "missing", "duplicate", "unsafe", "unexpected_xfail", "wrong_count"
])
def test_evidence_gate_rejects_invalid_results(tmp_path, defect):
    matrix, summary, payload = _fixture(tmp_path)
    if defect == "missing":
        payload["cases"].pop()
        payload["test_count"] -= 1
        payload["counts"]["PASS"] -= 1
    elif defect == "duplicate":
        payload["cases"][0] = payload["cases"][1].copy()
    elif defect == "unsafe":
        payload["cases"][0]["variant"] = "token=secret@host"
    elif defect == "unexpected_xfail":
        payload["cases"][0]["outcome"] = "XFAIL"
        payload["counts"]["PASS"] -= 1
        payload["counts"]["XFAIL"] += 1
    elif defect == "wrong_count":
        payload["test_count"] -= 1
    summary.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError):
        validate(matrix, summary)
