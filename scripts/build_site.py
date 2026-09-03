"""Write every generated artefact."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.site import build


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for written in build(args.root):
        print(written.relative_to(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
