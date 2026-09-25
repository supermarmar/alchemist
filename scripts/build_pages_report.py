"""Print the numbers a Phase 3 gate note reads.

    .venv/bin/python scripts/build_pages_report.py

Pages per status and per domain, the display-block and word-count distributions
over written pages, the "rather than" total, and the written pages whose closing
section names none of their unlocks. It reports and never gates, following
`grain_audit.py`: these are the figures Mario reads at a wave's gate, beside the
grader's sample and his own spot-read.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_corpus
from scripts.alchemist.pages import page_statistics

REPO = Path(__file__).resolve().parents[1]


def _counts(counter: dict) -> str:
    return ", ".join(f"{key} {value}" for key, value in sorted(counter.items(), key=lambda kv: str(kv[0])))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    stats = page_statistics(load_corpus(args.root))
    words = stats["words"]
    print(f"Pages by status: {_counts(stats['by_status'])}")
    print(f"Written pages by domain: {_counts(stats['written_by_domain']) or 'none'}")
    print(f"Display blocks per written page: {_counts(stats['display_blocks']) or 'none'}")
    print(f"Words per written page: min {words['min']}, q1 {words['q1']}, "
          f"median {words['median']}, q3 {words['q3']}, max {words['max']}")
    print(f"'rather than' across written pages: {stats['rather_than']}")
    missing = stats["no_forward_reference"]
    print(f"Written pages naming none of their unlocks in the closing section: {len(missing)}")
    for node_id in missing:
        print(f"  {node_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
