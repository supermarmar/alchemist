"""Run every rule over the corpus. Exit 1 on any failure."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.checks import run_all, vault_root
from scripts.alchemist.model import load_corpus, load_objects


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    objects = load_objects(args.root)
    results = run_all(corpus, objects, args.root, vault_root())

    failed = 0
    for result in results:
        if result.skipped:
            print(f"SKIP  {result.rule}: {result.skipped}")
        elif result.ok:
            print(f"ok    {result.rule}")
        else:
            failed += len(result.failures)
            print(f"FAIL  {result.rule}")
            for failure in result.failures:
                print(f"        {failure}")
    print(f"\n{len(corpus.nodes)} nodes, {len(corpus.paths)} paths, {failed} failures")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
