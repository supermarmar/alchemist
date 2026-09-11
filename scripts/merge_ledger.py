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

    ledger.write_text(header + yaml.safe_dump(merged, sort_keys=False, allow_unicode=True))
    print(
        f"{len(merged)} entries written ({len(seeded)} seeded, "
        f"{len(merged) - len(seeded)} new), {len(disagreements)} disagreements"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
