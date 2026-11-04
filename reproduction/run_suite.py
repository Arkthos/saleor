"""Run one selected suite in a separately prepared, pinned Saleor checkout."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("suite", choices=["focal", "units", "licenses", "live", "e2e", "general"])
    args = parser.parse_args()
    source = args.source.resolve()
    root = Path(__file__).resolve().parents[1]
    lock = json.loads((root / "reproduction/source.lock.json").read_text())
    actual = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    if actual != lock["test_source_sha"]:
        parser.error("La fuente no coincide con el SHA fijado; use prepare_source.py.")
    changes = subprocess.check_output(["git", "-C", str(source), "status", "--porcelain", "--untracked-files=no"], text=True)
    if changes:
        parser.error("Hay archivos versionados modificados en la fuente de pruebas.")
    groups = {
        "focal": [str(p.relative_to(source)) for p in sorted((source / "saleor/graphql/tests").glob("test_cybermarket_security_*.py"))],
        "units": ["tests/test_cybermarket_security_units.py", "tests/test_cybermarket_evidence_validator.py", "security/cybermarket/test_validate_evidence.py", "--noconftest"],
        "licenses": ["tests/test_cybermarket_license_selection.py", "--noconftest"],
        "live": ["security/cybermarket/live/tests/test_http_security.py", "security/cybermarket/live/tests/test_browser_transport.py", "--allow-hosts=127.0.0.1,localhost,::1"],
        "e2e": ["-m", "e2e"],
        "general": ["-m", "not e2e"],
    }
    if args.suite == "focal" and len(groups["focal"]) != 4:
        parser.error("No se encontraron los cuatro archivos focales.")
    parent = source / "technical-results"
    parent.mkdir(exist_ok=True)
    run_directory = Path(tempfile.mkdtemp(prefix=args.suite + "-", dir=parent))
    output = run_directory / "technical-results"
    output.mkdir()
    command = ["uv", "run"]
    if args.suite == "live":
        command += ["--with", "playwright==1.56.0"]
    command += ["pytest", *groups[args.suite], "-q", "-n", "0", "--junitxml=" + str(output / "results.xml"), "-o", "junit_family=legacy", "--tb=short"]
    if args.suite in {"focal", "live", "e2e", "general"}:
        command.append("--reuse-db")
    environment = dict(os.environ)
    environment.setdefault("DJANGO_SETTINGS_MODULE", "saleor.tests.settings")
    environment.setdefault("PYTHONPATH", str(source))
    environment.setdefault("SECRET_KEY", "cybermarket-disposable-local-lab-only-key")
    environment.setdefault("SEND_USAGE_TELEMETRY", "False")
    environment["CYBERMARKET_SOURCE_SHA"] = actual
    manifest = {"source_sha": actual, "suite": args.suite,
                "started_at": datetime.now(timezone.utc).isoformat(),
                "launcher_python": sys.version.split()[0], "command": command}
    # Never serialize the environment: it can contain credentials.
    result = subprocess.run(command, cwd=source, env=environment, check=False)
    manifest["pytest_exit_code"] = result.returncode
    (output / "run.json").write_text(json.dumps(manifest, indent=2) + "\n")
    sanitize = subprocess.run(["uv", "run", "--project", str(source), "python", str(source / "security/cybermarket/live/tests/sanitize_evidence.py")], cwd=run_directory, env=environment, check=False)
    print(f"Nueva evidencia: {output}")
    return result.returncode or sanitize.returncode


if __name__ == "__main__":
    raise SystemExit(main())
