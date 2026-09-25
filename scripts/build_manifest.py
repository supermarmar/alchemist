"""Write a phase's batch manifest.

    .venv/bin/python scripts/build_manifest.py                      # Phase 2, every node, by id
    .venv/bin/python scripts/build_manifest.py --phase 3 --order depth

Writes `.staging/phase-<n>/manifest.yaml`: one entry per batch, carrying its
wave and its explicit node ids. The directory is gitignored, and the manifest is
rebuilt from the corpus rather than kept. Phase 3 batches only the stubs and
orders them by depth in the `requires` graph, so prerequisites tend to land in
an earlier wave than the pages that cite them.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.batches import depth_key, manifest_payload, phase_node_ids
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--phase", type=int, choices=(2, 3), default=2)
    parser.add_argument("--order", choices=("id", "depth"), default="id")
    parser.add_argument("--out", type=Path, default=None,
                        help="defaults to .staging/phase-<phase>/manifest.yaml")
    args = parser.parse_args()
    out = args.out or REPO / ".staging" / f"phase-{args.phase}" / "manifest.yaml"

    corpus = load_corpus(args.root)
    ids = phase_node_ids(corpus.nodes, args.phase)
    key = depth_key(corpus.nodes) if args.order == "depth" else None
    payload = {
        "built": date.today().isoformat(),
        "phase": args.phase,
        "order": args.order,
        **manifest_payload(ids, key=key),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(payload, sort_keys=False))
    waves = max(batch["wave"] for batch in payload["batches"].values())
    print(f"{payload['nodes']} nodes -> {len(payload['batches'])} batches across {waves} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
