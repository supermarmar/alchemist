"""Apply a list of node merges, one `absorbed survivor` pair per line.

    .venv/bin/python scripts/merge_nodes.py --pairs .superpowers/close-out/merges.txt

Lines starting with # are comments. Pairs apply in file order, so a triple is two
lines naming the same survivor. Run check.py afterwards: a union can close a cycle
that no single record carried, and check 3 is what reports it.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.merges import merge_pair

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pairs", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    merged = 0
    for line in args.pairs.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        absorbed, survivor = line.split()
        touched = merge_pair(args.root, absorbed, survivor)
        merged += 1
        print(f"{absorbed} -> {survivor}: {len(touched)} files")
    print(f"{merged} merges applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
