# tests/test_fetch_syllabi.py
"""The fetcher's hashing, tested without a network call.

Nothing in tests/ reaches the network, so the download itself is not under
test. What is under test is the part that would silently accept a wrong file.
"""

import hashlib
from pathlib import Path

import pytest
import yaml

from scripts.fetch_syllabi import TARGET, digest, load_manifest, verify, write_manifest

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


QUALIFICATION_LINES = {"Associateship Qualification", "Fellowship Qualification"}


def _self_title_or_none(txt_path: Path, max_name_lines: int = 3) -> str | None:
    """Read a document's own self-title off its extracted cover page.

    Every IFoA extraction shares one shape: an optional qualification line,
    then the subject name (occasionally wrapped across two lines, always
    ending in the parenthesised code), then a "Core Principles" or
    "Specialist Principles" line. Joining the name and that line gives a
    self-title that is a genuine substring of a correct manifest title and is
    not a substring of one copied from memory, which is what makes this a
    stronger check than a bare subject-code match: it fails on a title that
    keeps the right code but names the wrong subject, which is exactly what
    CM2's title did until 4 September 2026.

    Returns None where no parenthesised code turns up within the first
    `max_name_lines`, rather than guessing: the two ASSA covers are shaped
    differently ("Subject F107" / "Banking Principles" / ...) and the caller
    falls back to the weaker code-only check for those.
    """
    lines = [line.strip() for line in txt_path.read_text().splitlines() if line.strip()]
    if lines and lines[0] in QUALIFICATION_LINES:
        lines = lines[1:]
    name_parts: list[str] = []
    for line in lines[:max_name_lines]:
        name_parts.append(line)
        if "(" in line and ")" in line:
            type_line = lines[len(name_parts)] if len(lines) > len(name_parts) else ""
            return " ".join(name_parts + ([type_line] if type_line else []))
    return None


def test_every_extracted_syllabus_title_names_its_own_subject():
    """Guards the class of error rather than the thirteen instances found and
    fixed on 4 September 2026, CM2 worst of all: a manifest title written from
    memory named a different subject ("Financial Engineering and Loss
    Reserving") than the document itself carries ("Economic Modelling"), while
    still keeping the correct subject code, (CM2), in parentheses. A check for
    the code alone would not have caught that, so this checks the document's
    own name-plus-code span instead.

    A body whose anchor_prefix carries no subject segment (the University of
    Pretoria yearbooks, anchor_prefix "up", one document covering many
    modules) has no single subject to check and is skipped, as are the three
    vault- and Downloads-only entries that never reach data/syllabi/.

    Skips cleanly where data/syllabi/ is absent, exactly as
    tests/test_render_chain.py skips without Quarto: data/ is gitignored, so a
    fresh clone carries none of the text this test reads.
    """
    if not TARGET.is_dir():
        pytest.skip("data/syllabi/ is absent (data/ is gitignored)")

    checked = 0
    for entry in load_manifest():
        anchor_prefix = entry.get("anchor_prefix") or ""
        if "." not in anchor_prefix or not entry.get("filename"):
            continue
        txt_path = TARGET / f"{Path(entry['filename']).stem}.txt"
        if not txt_path.is_file():
            continue

        self_title = _self_title_or_none(txt_path)
        if self_title is not None:
            assert self_title in entry["title"], (
                f"{entry['id']}: document self-title {self_title!r} does not "
                f"appear in manifest title {entry['title']!r}"
            )
        else:
            # A cover shaped differently from the IFoA pattern: fall back to
            # the weaker code-only check rather than mis-parsing prose into a
            # bogus expected title.
            subject_code = anchor_prefix.rsplit(".", 1)[-1].upper()
            assert subject_code in entry["title"], (
                f"{entry['id']}: subject code {subject_code!r} does not appear "
                f"in title {entry['title']!r}"
            )
        checked += 1

    assert checked > 0, "no extracted syllabus found to check under data/syllabi/"
