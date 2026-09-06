"""Report grain across every body, for gate 2."""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.grain import audit, fused_titles, requires_distribution
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=REPO / ".superpowers" / "phase-1")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    manifests = [
        yaml.safe_load(p.read_text())
        for p in sorted(args.staging.glob("*/manifest.yaml"))
    ]
    report = audit(manifests)
    corpus = load_corpus(args.root)

    print(f"{'body':28} {'items':>6} {'nodes':>6} {'ratio':>6}")
    for body in sorted(report.per_body):
        grain = report.per_body[body]
        ratio = "n/a" if grain.ratio is None else f"{grain.ratio:.2f}"
        flag = "  <-- outside 0.5 to 1.5" if body in report.outliers else ""
        print(f"{body:28} {grain.items:6} {grain.nodes:6} {ratio:>6}{flag}")

    distribution = requires_distribution([n.requires for n in corpus.nodes.values()])
    print("\nprerequisites per node:")
    for length, count in distribution.items():
        print(f"  {length:2} prerequisites: {count:5} nodes")

    fused = fused_titles([n.title for n in corpus.nodes.values()])
    print(f"\n{len(fused)} titles carry 'and' or a comma, of {len(corpus.nodes)} nodes:")
    for title in fused[:40]:
        print(f"  {title}")
    if len(fused) > 40:
        print(f"  ... and {len(fused) - 40} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
