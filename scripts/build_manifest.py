"""Write the Phase 2 batch manifest.

    .venv/bin/python scripts/build_manifest.py

Writes `.staging/phase-2/manifest.yaml`: one entry per batch, carrying its wave
and its explicit node ids. The directory is gitignored, and the manifest is
rebuilt from the corpus rather than kept.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.batches import manifest_payload
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--out", type=Path, default=REPO / ".staging" / "phase-2" / "manifest.yaml")
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    payload = {"built": date.today().isoformat(), **manifest_payload(list(corpus.nodes))}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(payload, sort_keys=False))
    waves = max(batch["wave"] for batch in payload["batches"].values())
    print(f"{payload['nodes']} nodes -> {len(payload['batches'])} batches across {waves} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
