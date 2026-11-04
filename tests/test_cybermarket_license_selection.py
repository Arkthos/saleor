"""Ensure narrow declared-license selection cannot bypass unrelated GPL metadata."""

from copy import deepcopy

import pytest

from security.cybermarket.tools.normalize_license_selection import (
    SELECTED_LICENSE,
    WHEEL_SHA256,
    select_artistic_alternative,
)


@pytest.fixture
def license_document():
    return {
        "bomFormat": "CycloneDX",
        "components": [
            {
                "name": "text-unidecode",
                "version": "1.3",
                "hashes": [{"alg": "SHA-256", "content": WHEEL_SHA256}],
                "licenses": [
                    {"license": {"name": "Artistic License"}},
                    {"license": {"id": "GPL-1.0-only"}},
                    {"license": {"id": "GPL-2.0-or-later"}},
                ],
            },
            {
                "name": "other-gpl-package",
                "version": "1",
                "licenses": [{"license": {"id": "GPL-2.0-only"}}],
            },
        ],
    }


def test_verified_alternative_and_original_are_retained(license_document):
    before = deepcopy(license_document)
    result, trace = select_artistic_alternative(license_document)
    assert license_document == before
    assert result["components"][0]["licenses"] == [
        {"license": {"id": SELECTED_LICENSE}}
    ]
    assert trace[0]["original_licenses"] == before["components"][0]["licenses"]
    assert result["components"][1] == before["components"][1]


def test_other_gpl_component_is_never_changed(license_document):
    source = {"components": [license_document["components"][1]]}
    result, trace = select_artistic_alternative(source)
    assert result == source
    assert trace == []


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("version", "1.4", "version changed"),
        (
            "hashes",
            [{"alg": "SHA-256", "content": "0" * 64}],
            "wheel hash not confirmed",
        ),
        (
            "licenses",
            [{"license": {"id": "GPL-2.0-or-later"}}],
            "alternative not declared",
        ),
    ],
)
def test_unverified_metadata_cannot_be_relicensed(
    license_document, field, value, message
):
    license_document["components"][0][field] = value
    with pytest.raises(ValueError, match=message):
        select_artistic_alternative(license_document)


def test_repeated_selection_is_idempotent(license_document):
    first, _ = select_artistic_alternative(license_document)
    second, _ = select_artistic_alternative(first)
    assert first == second
