"""Write a path's nodes block in mechanical order, or check that it already is.

    .venv/bin/python scripts/sequence_path.py life general-insurance
    .venv/bin/python scripts/sequence_path.py --check credit-trunk

Never run this over a braid: the braids are ordered by hand as their preambles
narrate, and the credit trunk joined them at gate 2. The tool refuses all four
without --force.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_corpus
from scripts.alchemist.sequence import mechanical_order, rewrite_nodes

REPO = Path(__file__).resolve().parents[1]

HAND_ORDERED = frozenset({"credit-trunk", "survival-braid", "markov-transition-braid", "claims-reserving-braid"})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path_ids", nargs="+")
    parser.add_argument("--check", action="store_true", help="exit 1 if any path is out of order; write nothing")
    parser.add_argument("--force", action="store_true", help="rewrite a hand-ordered path anyway")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    corpus = load_corpus(args.root)

    for path_id in args.path_ids:
        if path_id not in corpus.paths:
            print(f"{path_id}: no such path", file=sys.stderr)
            return 2
        if path_id in HAND_ORDERED and not args.check and not args.force:
            print(f"{path_id}: ordered by hand; pass --force to overwrite it", file=sys.stderr)
            return 2

    out_of_order = 0
    for path_id in args.path_ids:
        path = corpus.paths[path_id]
        file = args.root / "paths" / f"{path_id}.yaml"
        text = file.read_text()
        rewritten = rewrite_nodes(text, mechanical_order(path, corpus))
        if rewritten == text:
            print(f"{path_id}: in order")
            continue
        out_of_order += 1
        if args.check:
            print(f"{path_id}: out of mechanical order")
        else:
            file.write_text(rewritten)
            print(f"{path_id}: rewritten")
    return 1 if (args.check and out_of_order) else 0


if __name__ == "__main__":
    raise SystemExit(main())
