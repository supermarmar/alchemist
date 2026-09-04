# tests/test_fetch_syllabi.py
"""The fetcher's hashing, tested without a network call.

Nothing in tests/ reaches the network, so the download itself is not under
test. What is under test is the part that would silently accept a wrong file.
"""

import hashlib
import re
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
SUBJECT_LINE = re.compile(r"Subject\s+\S+")


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
    falls back to `_descriptive_name_or_none` for those.
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


def _descriptive_name_or_none(txt_path: Path) -> str | None:
    """Read a cover's descriptive name off a "Subject <code>" opening line.

    The two ASSA covers open "Subject F107" then, on the very next line, the
    subject's plain name ("Banking Principles"), with no parenthesised code
    anywhere near the top for `_self_title_or_none` to find. Matching on that
    name line is stronger than falling back straight to the bare subject
    code, because the code alone would have passed on a title naming the
    wrong ASSA subject just as it passed on CM2's. Returns None where the
    cover does not open this way, so the caller can fall back further rather
    than mis-parsing prose into a bogus expected name.
    """
    lines = [line.strip() for line in txt_path.read_text().splitlines() if line.strip()]
    if len(lines) >= 2 and SUBJECT_LINE.fullmatch(lines[0]):
        return lines[1]
    return None


def _expected_title_fragment(entry: dict, target: Path) -> str | None:
    """Return the substring `entry["title"]` must contain, read off the
    entry's own extraction, or None where the entry is out of scope: no
    subject segment in `anchor_prefix` (the University of Pretoria yearbooks,
    one document covering many modules), no `filename`, or no extracted
    `.txt` yet.

    Tries the document's own self-title first, then a "Subject <code>" cover's
    descriptive name line, and only falls back to the bare subject code where
    neither shape matches, since the code alone is the weakest guard: it
    passes on a title that keeps the right code but names the wrong subject.
    """
    anchor_prefix = entry.get("anchor_prefix") or ""
    if "." not in anchor_prefix or not entry.get("filename"):
        return None
    txt_path = target / f"{Path(entry['filename']).stem}.txt"
    if not txt_path.is_file():
        return None

    self_title = _self_title_or_none(txt_path)
    if self_title is not None:
        return self_title

    descriptive_name = _descriptive_name_or_none(txt_path)
    if descriptive_name is not None:
        return descriptive_name

    return anchor_prefix.rsplit(".", 1)[-1].upper()


def _assert_every_extracted_title_names_its_own_subject(target: Path) -> None:
    """Check every manifest entry with an extraction under `target`, skipping
    rather than failing where nothing on disk is in scope.

    The skip matters on its own: `data/syllabi/` passes through a real
    intermediate state where it exists and holds PDFs but no `.txt` files, the
    gap between the brief's Step 6 (fetch) and Step 7 (`pdftotext`), and
    anyone without poppler installed sits there indefinitely. A trailing
    assert on the checked count turned that state into a suite-wide failure
    unconnected to the code under test; a skip reports it honestly instead.
    """
    checked = 0
    for entry in load_manifest():
        fragment = _expected_title_fragment(entry, target)
        if fragment is None:
            continue
        assert fragment in entry["title"], (
            f"{entry['id']}: expected {fragment!r} in title {entry['title']!r}"
        )
        checked += 1

    if checked == 0:
        pytest.skip(f"no extracted .txt files found under {target}")


def test_every_extracted_syllabus_title_names_its_own_subject():
    """Guards the class of error rather than the thirteen instances found and
    fixed on 4 September 2026, CM2 worst of all: a manifest title written from
    memory named a different subject ("Financial Engineering and Loss
    Reserving") than the document itself carries ("Economic Modelling"), while
    still keeping the correct subject code, (CM2), in parentheses. A check for
    the code alone would not have caught that, so this checks the document's
    own name-plus-code span instead, and the ASSA fallback matches on the
    cover's descriptive name rather than dropping straight to the code.

    Skips cleanly where data/syllabi/ is absent, exactly as
    tests/test_render_chain.py skips without Quarto: data/ is gitignored, so a
    fresh clone carries none of the text this test reads.
    """
    if not TARGET.is_dir():
        pytest.skip("data/syllabi/ is absent (data/ is gitignored)")
    _assert_every_extracted_title_names_its_own_subject(TARGET)


def test_the_subject_check_skips_rather_than_fails_with_pdfs_and_no_extractions(tmp_path):
    """data/syllabi/ can hold PDFs with no .txt files yet: the brief's Step 6
    fetches PDFs and Step 7 extracts them with pdftotext, and a machine
    without poppler installed sits in that gap indefinitely. That state must
    skip, not fail, since a run that checks nothing has nothing to say about
    whether any title is wrong.
    """
    target = tmp_path / "syllabi"
    target.mkdir()
    (target / "ifoa-cs1-2026.pdf").write_bytes(b"%PDF-1.7")
    with pytest.raises(pytest.skip.Exception):
        _assert_every_extracted_title_names_its_own_subject(target)
