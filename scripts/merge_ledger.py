"""Merge the ledger fragments into the two ledger files.

    .venv/bin/python scripts/merge_ledger.py

The only writer of `sources/wanted.yaml` and `sources/to-ingest.yaml`. It
refuses to write either while any fragment is malformed, because a partial
ledger reaching the gate wearing the appearance of a complete one is worse than
no ledger: acquisition is decided off it.

Both files are read, unioned together and then routed by status, so the split
between them maintains itself. An entry whose document turns out to be in the
vault already leaves the acquisition file on the next merge, and a fragment
proposing a document the ingest file holds extends that entry rather than
writing a second copy of it under acquisition.

Field disagreements are printed and do not block. The acquisition file's value
stands, since it is the file a human reads before buying anything, and the note
tells you where a fragment or the ingest file said otherwise.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.ledger import (
    ledger_paths,
    partition_by_status,
    read_fragments,
    union_entries,
)

REPO = Path(__file__).resolve().parents[1]

# A top-level list entry starts a line with "- id:"; a claim or note body is
# always indented under its own key, so this only matches the real header
# boundary rather than the same text appearing inside a block scalar.
HEADER_SPLIT = re.compile(r"^- id:", re.MULTILINE)

# Measured from sources/wanted.yaml's own folded claim and note bodies, whose
# longest wrapped line (four-space indent included) runs to 78 columns. A
# plain yaml.safe_dump call cannot reach that column at all: it drops folded
# style entirely, so LedgerDumper below restores it, and this is the target
# column that keeps the restored wrapping close to the hand-written original
# rather than PyYAML's own default of 80. It is a target, not a cap: PyYAML
# defers a line break until the next whitespace after the column is already
# past width, so an individual wrapped line can still run past 78.
LEDGER_WIDTH = 78

# The header written at the top of a ledger file this run has to create.
# Both committed files carry their own hand-written headers, which the merge
# preserves, so this is reached only where an entry routes into a file that is
# not there yet. It points at the other file rather than restating the field
# vocabulary, because a second copy of that vocabulary is a second thing to
# keep in step with `ledger.py`.
NEW_FILE_HEADER = (
    "# One entry per document. The field vocabulary is in sources/wanted.yaml.\n"
)


class LedgerDumper(yaml.SafeDumper):
    """Preserves the two styles PyYAML's plain SafeDumper discards.

    Loading a fragment or the seeded ledger throws away style information:
    a folded ``claim`` and a flow ``needed_by`` both come back as ordinary
    Python objects with no memory of how they were written. Re-dumped with
    the plain SafeDumper, a folded paragraph becomes a single-quoted flow
    scalar carrying a literal newline, and ``[a, b]`` becomes a block
    sequence. Both changes are cosmetic (the content survives) but
    permanent: every future merge repeats them, so genuine ledger changes
    end up buried in reformatting noise forever after. The two representers
    below restore the original styles instead, so a merge that changes
    nothing writes nothing different.
    """


def _represent_str(dumper: "LedgerDumper", data: str) -> yaml.Node:
    style = ">" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


# The largest all-scalar list still dumped in flow style; longer lists dump
# one item per line instead. Every needed_by seeded in sources/wanted.yaml
# today holds one to three ids, so six leaves headroom above anything
# already committed while staying well short of the sizes the corpus's own
# design bound predicts once acquisition entries start naming the nodes
# they would close: roughly 1,100 uncovered nodes across about 59 anchor
# documents, with assa.f107 alone anchoring 274 of them. A needed_by that
# size is exactly what block style protects, since flow style would
# re-wrap the whole entry on every single id inserted into it, which is
# the failure a 200-id review fixture demonstrated. Below the boundary, a
# short list still reads as one bounded group rather than a second table;
# above it, block style confines every future insertion to the one line it
# adds.
FLOW_LIST_MAX_ITEMS = 6


def _represent_list(dumper: "LedgerDumper", data: list) -> yaml.Node:
    flow = (
        all(not isinstance(item, (list, dict)) for item in data)
        and len(data) <= FLOW_LIST_MAX_ITEMS
    )
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=flow)


LedgerDumper.add_representer(str, _represent_str)
LedgerDumper.add_representer(list, _represent_list)


def _read(path: Path) -> tuple[str, list[dict]]:
    """A ledger file's header comment and its entries, tolerating an absent file."""
    if not path.is_file():
        return NEW_FILE_HEADER, []
    text = path.read_text()
    match = HEADER_SPLIT.search(text)
    header = text[: match.start()] if match else text
    return header, yaml.safe_load(text) or []


def _write(path: Path, header: str, entries: list[dict]) -> None:
    """Write one ledger file, and create nothing where there is nothing to say.

    A file that exists is always rewritten, header included, because the
    partition may have emptied it. One that does not exist is left alone until
    an entry actually routes into it, since an empty file beside the ledger is
    one more thing a reader has to work out the meaning of.
    """
    if not entries and not path.exists():
        return
    body = (
        yaml.dump(
            entries,
            Dumper=LedgerDumper,
            sort_keys=False,
            allow_unicode=True,
            width=LEDGER_WIDTH,
        )
        if entries
        else ""
    )
    path.write_text(header + body)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--staging", type=Path, default=REPO / ".staging" / "phase-2")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    acquisition_path, ingest_path = ledger_paths(args.root)
    acquisition_header, acquisition_seeded = _read(acquisition_path)
    ingest_header, ingest_seeded = _read(ingest_path)
    seeded = len(acquisition_seeded) + len(ingest_seeded)

    proposed, complaints = read_fragments(args.staging)
    if complaints:
        for complaint in complaints:
            print(f"malformed: {complaint}", file=sys.stderr)
        print(f"{len(complaints)} malformed fragments; nothing written", file=sys.stderr)
        return 2

    # The ingest file joins the fragments on the proposed side rather than the
    # seeded one, so that an id somehow held in both files resolves through the
    # rule already written for a disagreement: the acquisition copy's fields
    # stand, the needed_by lists union, and the difference is printed. Feeding
    # both files in as seeded would instead let one silently overwrite the other.
    merged, disagreements = union_entries(acquisition_seeded, ingest_seeded + proposed)
    for disagreement in disagreements:
        print(f"note: {disagreement}", file=sys.stderr)
    acquisition, ingest = partition_by_status(merged)
    split = (
        f"{len(acquisition)} to {acquisition_path.name}, "
        f"{len(ingest)} to {ingest_path.name}"
    )

    if args.dry_run:
        print(f"would write {len(merged)} entries ({seeded} seeded): {split}")
        return 0

    _write(acquisition_path, acquisition_header, acquisition)
    _write(ingest_path, ingest_header, ingest)
    print(
        f"{len(merged)} entries written ({seeded} seeded, "
        f"{len(merged) - seeded} new), {len(disagreements)} disagreements: {split}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
