# scripts/fetch_syllabi.py
"""Download the anchor bodies named in sources/syllabi.yaml into data/syllabi/.

A syllabus is revised annually and its URL carries an opaque media id, so
recording the SHA-256 is what makes "the CS2 syllabus" name one identifiable
document rather than whichever one is current. A hash mismatch is reported
rather than papered over: the body republished, and whether the corpus follows
is a decision rather than a download.

data/ is gitignored, so nothing this script writes is ever committed.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.request
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "sources" / "syllabi.yaml"
TARGET = REPO / "data" / "syllabi"


def load_manifest(path: Path = MANIFEST) -> list[dict]:
    return yaml.safe_load(path.read_text()) or []


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path, expected: str) -> bool:
    """False rather than an exception, because a missing file and a changed one
    are the same answer to the caller: this is not the document recorded."""
    if not path.is_file():
        return False
    return digest(path) == expected


def fetch(entry: dict, target: Path) -> tuple[str, str]:
    """Return (status, detail). Never raises on a hash mismatch: the caller
    decides, because a republished syllabus is a corpus question."""
    if not entry.get("url"):
        if not entry.get("filename"):
            return "local", f"{entry['id']}: no url, transcribed from {entry.get('local')}"
        # A local entry that names a filename has been copied into data/syllabi/
        # by hand, and its provenance is worth exactly as much as a downloaded
        # one. Hash it rather than waving it through, or the manifest records a
        # document nobody can identify later.
        destination = target / entry["filename"]
        if not destination.is_file():
            return "absent", f"{entry['id']}: expected {destination.name}, copy it in first"
        found = digest(destination)
        recorded = entry.get("sha256")
        if recorded is None:
            return "recorded", f"{entry['id']}: {found}"
        if found != recorded:
            return "mismatch", f"{entry['id']}: recorded {recorded}, found {found}"
        return "current", f"{entry['id']}: unchanged"
    destination = target / entry["filename"]
    recorded = entry.get("sha256")
    if recorded and verify(destination, recorded):
        return "current", f"{entry['id']}: unchanged"
    target.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(entry["url"]) as response:
        destination.write_bytes(response.read())
    found = digest(destination)
    if recorded is None:
        return "recorded", f"{entry['id']}: {found}"
    if found != recorded:
        return "mismatch", f"{entry['id']}: recorded {recorded}, found {found}"
    return "fetched", f"{entry['id']}: {found}"


def _leading_comment_block(path: Path) -> str:
    """Return the file's leading run of comment and blank lines, verbatim.

    yaml.safe_dump has no notion of comments, so writing entries back through
    it drops the manifest's header on every run unless something restores it.
    That happened for real on 4 September 2026: the first --write-hashes run
    silently ate the provenance note at the top of sources/syllabi.yaml.
    """
    header_lines: list[str] = []
    for line in path.read_text().splitlines(keepends=True):
        if line.strip() == "" or line.lstrip().startswith("#"):
            header_lines.append(line)
        else:
            break
    return "".join(header_lines)


def write_manifest(path: Path, entries: list[dict]) -> None:
    """Write entries back to path, keeping its leading comment block intact.

    Read the header before the dump rather than after, so the write always
    restores the comment that was on disk a moment ago rather than one carried
    in memory from an earlier, possibly stale, read.
    """
    header = _leading_comment_block(path)
    path.write_text(header + yaml.safe_dump(entries, sort_keys=False, width=88))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-hashes", action="store_true",
        help="record a newly computed digest back into the manifest",
    )
    args = parser.parse_args()

    entries = load_manifest()
    statuses: list[str] = []
    for entry in entries:
        status, detail = fetch(entry, TARGET)
        statuses.append(status)
        print(f"{status:9} {detail}")
        if status == "recorded" and args.write_hashes:
            entry["sha256"] = digest(TARGET / entry["filename"])
            entry["retrieved"] = date.today().isoformat()

    if args.write_hashes:
        write_manifest(MANIFEST, entries)
        print(f"\nmanifest updated: {MANIFEST.relative_to(REPO)}")

    mismatches = statuses.count("mismatch")
    print(f"\n{len(entries)} bodies, {mismatches} hash mismatches")
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
