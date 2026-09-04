# tests/test_fetch_syllabi.py
"""The fetcher's hashing, tested without a network call.

Nothing in tests/ reaches the network, so the download itself is not under
test. What is under test is the part that would silently accept a wrong file.
"""

import hashlib

import yaml

from scripts.fetch_syllabi import digest, load_manifest, verify, write_manifest

REPO_MANIFEST = "sources/syllabi.yaml"


def test_digest_matches_hashlib(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"%PDF-1.7 not really a pdf")
    assert digest(target) == hashlib.sha256(target.read_bytes()).hexdigest()


def test_verify_accepts_a_matching_digest(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"contents")
    assert verify(target, digest(target)) is True


def test_verify_rejects_a_changed_file(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"contents")
    recorded = digest(target)
    target.write_bytes(b"the body republished")
    assert verify(target, recorded) is False


def test_verify_rejects_a_missing_file(tmp_path):
    assert verify(tmp_path / "absent.pdf", "0" * 64) is False


def test_the_manifest_names_twenty_bodies():
    entries = load_manifest()
    assert len(entries) == 20


def test_every_manifest_entry_carries_an_anchor_prefix():
    for entry in load_manifest():
        assert entry["anchor_prefix"], f"{entry['id']} has no anchor_prefix"


def test_every_downloadable_entry_carries_a_filename():
    for entry in load_manifest():
        if entry.get("url"):
            assert entry.get("filename"), f"{entry['id']} has a url and no filename"


def test_write_manifest_preserves_the_header_comment(tmp_path):
    """yaml.safe_dump has no notion of comments, and this is the regression
    that ate the manifest's header once already, on 4 September 2026."""
    manifest = tmp_path / "syllabi.yaml"
    manifest.write_text(
        "# A header comment.\n"
        "# A second header line.\n"
        "\n"
        "- id: a\n"
        "  sha256: null\n"
    )
    entries = load_manifest(manifest)
    entries[0]["sha256"] = "a" * 64

    write_manifest(manifest, entries)

    written = manifest.read_text()
    assert written.startswith("# A header comment.\n# A second header line.\n\n")
    assert yaml.safe_load(written)[0]["sha256"] == "a" * 64
