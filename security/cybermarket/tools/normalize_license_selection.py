"""Record the declared Artistic alternative for the exact locked text-unidecode wheel."""

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path

PACKAGE = "text-unidecode"
VERSION = "1.3"
WHEEL_SHA256 = "1311f10e8b895935241623731c2ba64f4c455287888b18189350b67134a822e8"
LICENSE_SOURCE = "https://github.com/kmike/text-unidecode/blob/1.3/README.rst"
SELECTED_LICENSE = "Artistic-1.0-Perl"


def select_artistic_alternative(sbom):
    """Change only the verified dual-license component; fail on unexpected metadata."""
    result = deepcopy(sbom)
    selections = []
    for component in result.get("components", []):
        if component.get("name") != PACKAGE:
            continue
        if component.get("version") != VERSION:
            raise ValueError("Review required: text-unidecode version changed")
        hashes = component.get("hashes", [])
        if {"alg": "SHA-256", "content": WHEEL_SHA256} not in hashes:
            raise ValueError("Review required: locked wheel hash not confirmed")
        licenses = component.get("licenses", [])
        has_artistic = any(
            item.get("license", {}).get("name") == "Artistic License"
            or item.get("license", {}).get("id") == SELECTED_LICENSE
            for item in licenses
        )
        if not has_artistic:
            raise ValueError("Review required: Artistic alternative not declared")
        selections.append(
            {
                "package": PACKAGE,
                "version": VERSION,
                "wheel_sha256": WHEEL_SHA256,
                "source": LICENSE_SOURCE,
                "original_licenses": deepcopy(licenses),
                "selected_license": SELECTED_LICENSE,
                "reason": "Author permits either Artistic or GPL; select Artistic under existing rules",
            }
        )
        component["licenses"] = [{"license": {"id": SELECTED_LICENSE}}]
    return result, selections


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("record", type=Path)
    arguments = parser.parse_args()
    original = arguments.source.read_bytes()
    result, selections = select_artistic_alternative(json.loads(original))
    output = (json.dumps(result, indent=2) + "\n").encode()
    record = {
        "schema": "cybermarket.license.selection.v1",
        "source_sha256": hashlib.sha256(original).hexdigest(),
        "output_sha256": hashlib.sha256(output).hexdigest(),
        "selections": selections,
        "policy_rules_changed": False,
    }
    arguments.output.write_bytes(output)
    arguments.record.write_text(json.dumps(record, indent=2) + "\n")


if __name__ == "__main__":
    main()
