"""Verify conserved evidence, independently of Saleor and network services."""

from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "security/cybermarket/academic/avance2/evidencia/revalidacion_tecnica"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_sums(data):
    entries = {}
    for line in data.splitlines():
        if not line.strip():
            continue
        digest, name = line.split(maxsplit=1)
        name = name.removeprefix("*").removeprefix("./")
        require(len(digest) == 64 and all(c in "0123456789abcdef" for c in digest), "Invalid SHA-256")
        path = PurePosixPath(name)
        require(not path.is_absolute() and ".." not in path.parts, f"Unsafe checksum path: {name}")
        require(name not in entries, f"Duplicate checksum path: {name}")
        entries[name] = digest
    require(bool(entries), "Empty checksums")
    return entries


def counts(data):
    result = Counter()
    for case in ET.fromstring(data).iter("testcase"):
        result["total"] += 1
        if case.find("failure") is not None:
            result["failure"] += 1
        elif case.find("error") is not None:
            result["error"] += 1
        elif case.find("skipped") is not None:
            skipped = case.find("skipped")
            if skipped.get("type") == "pytest.xfail":
                result["xfail"] += 1
                # The name remains present in general JUnit without case properties.
                require("cm_t22" in case.get("name", "").lower(), "Unexpected XFAIL outside CM-T22")
            else:
                result["other_skipped"] += 1
        else:
            result["pass"] += 1
    return {key: result[key] for key in ["total", "pass", "failure", "error", "xfail", "other_skipped"]}


def main():
    sums = parse_sums((ROOT / "SHA256SUMS").read_text())
    listed = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", "--cached", "--others", "--exclude-standard", "-z"]
    ).decode().split("\0")
    actual = {p for p in listed if p and p != "SHA256SUMS" and (ROOT / p).is_file()}
    require(set(sums) == actual, "Delivery inventory differs from SHA256SUMS")
    for name, digest in sums.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, f"Changed delivery file: {name}")
    archives = 0
    inner = 0
    for path in sorted(ROOT.rglob("*.zip")):
        if ".git" in path.parts:
            continue
        with zipfile.ZipFile(path) as archive:
            require(archive.testzip() is None, f"Corrupt ZIP: {path.relative_to(ROOT)}")
            names = archive.namelist()
            require(len(names) == len(set(names)), f"Duplicate ZIP entries: {path}")
            for name in names:
                member = PurePosixPath(name)
                require(not member.is_absolute() and ".." not in member.parts, f"Unsafe ZIP member: {name}")
                if member.name == "SHA256SUMS":
                    prefix = str(member.parent)
                    for relative, digest in parse_sums(archive.read(name).decode()).items():
                        target = relative if prefix == "." else prefix + "/" + relative
                        require(target in names, f"Missing ZIP member: {target}")
                        require(hashlib.sha256(archive.read(target)).hexdigest() == digest, f"Changed ZIP member: {target}")
                        inner += 1
        archives += 1
    closure = json.loads((EVIDENCE / "CIERRE_TECNICO.json").read_text())
    raw = EVIDENCE / "raw"
    results = {}
    probes = {
        "general": ("final_general/public.zip", "test-results.xml"),
        "focal": ("final_focal/public.zip", "cybermarket-junit.xml"),
        "independent_units_validators": ("final_lab/original.zip", "units.xml"),
        "live": ("final_lab/original.zip", "live.xml"),
        "e2e": ("final_e2e/original.zip", "e2e.xml"),
    }
    for suite, (path, member) in probes.items():
        with zipfile.ZipFile(raw / path) as archive:
            result = counts(archive.read(member))
        require(result == closure["suites"][suite], f"JUnit/closure mismatch: {suite}: {result}")
        results[suite] = result
    with zipfile.ZipFile(raw / "final_lab/original.zip") as archive:
        require(counts(archive.read("focused.xml")) == results["focal"], "Lab/focal mismatch")
        environment = json.loads(archive.read("environment.json"))
        require(environment["checkout_sha"] == closure["tested_checkout_sha"], "Wrong Actions checkout")
    for label in ["general", "focal"]:
        public = closure[label + "_public_archive"]
        file = ROOT / public["path"]
        require(hashlib.sha256(file.read_bytes()).hexdigest() == public["sha256"], f"Public archive mismatch: {label}")
    for artifact in closure["artifact_verification"]:
        folder = raw / artifact["directory"]
        original = folder / "original.zip"
        if original.exists():
            require(hashlib.sha256(original.read_bytes()).hexdigest() == artifact["sha256"], f"Original archive mismatch: {folder.name}")
    for side in ["base", "head"]:
        with zipfile.ZipFile(raw / "licencias_final" / side / "public.zip") as archive:
            require(counts(archive.read("license-units.xml")) == {"total": 6, "pass": 6, "failure": 0, "error": 0, "xfail": 0, "other_skipped": 0}, f"License boundary mismatch: {side}")
    lock = json.loads((ROOT / "reproduction/source.lock.json").read_text())
    require(lock["test_source_sha"] == closure["source_sha"], "Reproduction source mismatch")
    require(hashlib.sha256((ROOT / "reproduction/reference/uv.lock").read_bytes()).hexdigest() == lock["uv_lock_sha256"], "Reference lock mismatch")
    print(json.dumps({"verified": True, "delivery_files": len(sums), "zip_archives": archives,
                      "inner_checksums": inner, "historical_suites": results,
                      "product_tests_rerun": False}, indent=2))


if __name__ == "__main__":
    main()
