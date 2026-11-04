"""Recover the pinned source without overwriting an existing laboratory."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--from-repository", dest="origin")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    lock = json.loads((root / "reproduction/source.lock.json").read_text())
    destination = args.destination.resolve()
    if destination.exists():
        parser.error("El destino ya existe; use una carpeta nueva.")
    origin = args.origin or lock["repository"]
    subprocess.run(["git", "init", str(destination)], check=True)
    def git(*arguments):
        return subprocess.check_output(
            ["git", "-C", str(destination), *arguments], text=True
        ).strip()
    git("remote", "add", "origin", origin)
    git("fetch", "--depth", "1", "origin", lock["test_source_sha"])
    git("checkout", "--detach", lock["test_source_sha"])
    if git("rev-parse", "HEAD^{tree}") != lock["test_source_tree"]:
        raise RuntimeError("El árbol recuperado no coincide con la fuente fijada.")
    digest = hashlib.sha256((destination / "uv.lock").read_bytes()).hexdigest()
    if digest != lock["uv_lock_sha256"]:
        raise RuntimeError("uv.lock no coincide con el hash registrado.")
    for relative in lock["retained_test_files"]:
        if (destination / relative).read_bytes() != (root / relative).read_bytes():
            raise RuntimeError(f"La prueba conservada difiere de la fuente: {relative}")
    print(json.dumps({"verified_source": git("rev-parse", "HEAD"),
                      "destination": str(destination),
                      "tests_verified": len(lock["retained_test_files"])}, indent=2))


if __name__ == "__main__":
    main()
