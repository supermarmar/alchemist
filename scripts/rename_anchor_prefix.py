"""Rename an anchor-body prefix on every node record and in the manifest.

An anchor prefix is a key, and a key that misattributes a licensed source is a
liability that grows with every phase, because Phase 2 attaches citations to the
records carrying it and Phase 3 writes their pages. The rename touches the `anchor:`
line of a node file and nothing else, so a drafted body is never rewritten, and it
reparses every touched file so a malformed result fails here with the path named.
The manifest id is left alone: the Phase 1 staging directory and its grain manifest
key on it, and it was never an attribution.

Usage:
    .venv/bin/python scripts/rename_anchor_prefix.py eth.dl-actuarial-2026 ucsc.dl-actuarial-2026
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import parse_node

REPO = Path(__file__).resolve().parents[1]
ANCHOR_LINE = re.compile(r"^anchor: \[.*\]$", re.M)


def rename_in_anchor_line(text: str, old: str, new: str) -> str:
    """Rewrite `old.` to `new.` inside the anchor line only. The trailing dot is
    what stops the prefix matching a longer prefix that starts the same way."""
    return ANCHOR_LINE.sub(lambda m: m.group(0).replace(f"{old}.", f"{new}."), text, count=1)


def rename_nodes(nodes_dir: Path, old: str, new: str) -> list[Path]:
    touched: list[Path] = []
    for path in sorted(nodes_dir.glob("*.md")):
        text = path.read_text()
        rewritten = rename_in_anchor_line(text, old, new)
        if rewritten != text:
            path.write_text(rewritten)
            parse_node(path)
            touched.append(path)
    return touched


def rename_manifest(manifest: Path, old: str, new: str) -> bool:
    text = manifest.read_text()
    rewritten = text.replace(f"anchor_prefix: {old}", f"anchor_prefix: {new}")
    rewritten = rewritten.replace(f"{old}.", f"{new}.")
    if rewritten == text:
        return False
    manifest.write_text(rewritten)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    touched = rename_nodes(args.root / "nodes", args.old, args.new)
    manifest_changed = rename_manifest(args.root / "sources" / "syllabi.yaml", args.old, args.new)
    left = [p for p in sorted((args.root / "nodes").glob("*.md")) if f"{args.old}." in p.read_text()]
    print(f"{len(touched)} node records renamed, manifest {'updated' if manifest_changed else 'unchanged'}")
    if left:
        print(f"{len(left)} node files still carry {args.old}. outside the anchor line:")
        for p in left:
            print(f"  {p.relative_to(args.root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
