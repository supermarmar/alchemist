"""Merge the Phase 2 ledger fragments into sources/wanted.yaml.

    .venv/bin/python scripts/merge_ledger.py

The only writer of that file during Phase 2. It refuses to write at all where
any fragment is malformed, because a partial ledger reaching the gate wearing
the appearance of a complete one is worse than no ledger: acquisition is
decided off it.

Field disagreements are printed and do not block. The seeded entry's value
stands, and the note tells you where an agent thought otherwise.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.ledger import read_fragments, union_entries

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


def _represent_list(dumper: "LedgerDumper", data: list) -> yaml.Node:
    flow = all(not isinstance(item, (list, dict)) for item in data)
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=flow)


LedgerDumper.add_representer(str, _represent_str)
LedgerDumper.add_representer(list, _represent_list)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--staging", type=Path, default=REPO / ".staging" / "phase-2")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ledger = args.root / "sources" / "wanted.yaml"
    text = ledger.read_text()
    match = HEADER_SPLIT.search(text)
    header = text[: match.start()] if match else text
    seeded = yaml.safe_load(text) or []

    proposed, complaints = read_fragments(args.staging)
    if complaints:
        for complaint in complaints:
            print(f"malformed: {complaint}", file=sys.stderr)
        print(f"{len(complaints)} malformed fragments; nothing written", file=sys.stderr)
        return 2

    merged, disagreements = union_entries(seeded, proposed)
    for disagreement in disagreements:
        print(f"note: {disagreement}", file=sys.stderr)

    if args.dry_run:
        print(f"would write {len(merged)} entries ({len(seeded)} seeded)")
        return 0

    ledger.write_text(
        header
        + yaml.dump(
            merged,
            Dumper=LedgerDumper,
            sort_keys=False,
            allow_unicode=True,
            width=LEDGER_WIDTH,
        )
    )
    print(
        f"{len(merged)} entries written ({len(seeded)} seeded, "
        f"{len(merged) - len(seeded)} new), {len(disagreements)} disagreements"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
