"""Capture allowlisted environment metadata without reading secret values."""

import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
from pathlib import Path

root = Path.cwd()
output = root / "technical-results"
output.mkdir(exist_ok=True)
metadata = {
    "schema": "cybermarket.technical.environment.v1",
    "checkout_sha": subprocess.check_output(
        ["git", "rev-parse", "HEAD"], text=True
    ).strip(),
    "event_sha": os.environ.get("GITHUB_SHA"),
    "run_id": os.environ.get("GITHUB_RUN_ID"),
    "python": platform.python_version(),
    "lock_sha256": hashlib.sha256((root / "uv.lock").read_bytes()).hexdigest(),
    "packages": {
        name: importlib.metadata.version(name)
        for name in [
            "Django",
            "graphene",
            "graphql-core",
            "PyJWT",
            "pytest",
            "uvicorn",
            "cryptography",
        ]
    },
    "lab": {
        "bind": "127.0.0.1",
        "data": "synthetic",
        "smtp": "locmem",
        "plugins": [],
        "usage_telemetry": False,
        "browser_network": "loopback-only",
        "tls_verification": "enabled with disposable CA",
        "product_code_modified": False,
    },
}
(output / "environment.json").write_text(json.dumps(metadata, indent=2) + "\n")
