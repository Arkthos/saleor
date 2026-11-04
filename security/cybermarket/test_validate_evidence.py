"""Legacy CI entrypoint for evidence-validator regression tests."""

from pathlib import Path
from runpy import run_path

_module = run_path(
    str(
        Path(__file__).resolve().parents[2]
        / "tests/test_cybermarket_evidence_validator.py"
    )
)
test_complete_manifest_passes = _module["test_complete_manifest_passes"]
test_evidence_gate_rejects_invalid_results = _module[
    "test_evidence_gate_rejects_invalid_results"
]
