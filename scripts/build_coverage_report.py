"""Render the Phase 2 coverage report, one of the gate's two artefacts.

    .venv/bin/python scripts/build_coverage_report.py

Reads `data/vault-index.yaml` only for its `built` field, so a stale or
absent index reports plainly rather than stopping the run: the coverage
figures come from the corpus itself, never from the index. All of the
figuring lives in `scripts/alchemist/coverage.py`; this stays a thin
argument parser over it, matching how `check.py` sits over `checks.py`.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.coverage import NO_INDEX, render_report
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def _index_built(path: Path) -> str:
    """The index's `built` field, or `NO_INDEX` where the index is absent or
    carries no such field.
    """
    if not path.is_file():
        return NO_INDEX
    built = (yaml.safe_load(path.read_text()) or {}).get("built")
    return str(built) if built else NO_INDEX


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--index", type=Path, default=REPO / "data" / "vault-index.yaml")
    parser.add_argument("--out", type=Path, default=REPO / "notes" / "phase-2-coverage-2026-09.md")
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    report = render_report(corpus, _index_built(args.index))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report)

    attached = sum(1 for node in corpus.nodes.values() if node.vault_articles)
    uncovered = len(corpus.nodes) - attached
    print(f"{len(corpus.nodes)} nodes, {attached} attached, {uncovered} uncovered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
