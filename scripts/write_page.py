r"""Write one tier-1 page, refusing a body or a spend the checks would refuse.

    .venv/bin/python scripts/write_page.py --node hazard-rate --body /tmp/hazard.md \
        --spends obj.hazard:credit obj.survival:credit

    .venv/bin/python scripts/write_page.py --check /tmp/hazard.md

The first form validates the body against the template and every spend against
check 1, sets `status: drafted`, replaces the body and re-renders the whole
record, so thirty-nine agents produce one shape of file. It touches no other
field, and it refuses to overwrite a `reviewed` node without `--force`, because
`reviewed` is Mario's verdict after a gate and a rerun batch must not undo it.

The second form runs the validator alone on a body file and exits 2 naming each
breach. The model measurement's two arms call it, since they write bodies into
staging rather than into `nodes/`.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_objects
from scripts.alchemist.pages import PageRefused, parse_spend, write_page
from scripts.alchemist.template import validate_body

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--check", type=Path, help="validate this body file and write nothing")
    parser.add_argument("--node")
    parser.add_argument("--body", type=Path)
    parser.add_argument("--spends", nargs="*", default=[], metavar="OBJECT:DOMAIN")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    if args.check is not None:
        problems = validate_body(args.check.read_text())
        for problem in problems:
            print(f"{args.check}: {problem}", file=sys.stderr)
        if not problems:
            print(f"{args.check}: conforms to the template")
        return 2 if problems else 0

    if args.node is None or args.body is None:
        parser.error("--node and --body are required unless --check is given")
    node_file = args.root / "nodes" / f"{args.node}.md"
    if not node_file.is_file():
        print(f"no such node {args.node!r} at {node_file}", file=sys.stderr)
        return 2
    try:
        spends = tuple(parse_spend(s) for s in args.spends)
        written = write_page(
            node_file, args.body.read_text(), spends, load_objects(args.root), force=args.force
        )
    except (ValueError, PageRefused) as exc:
        for line in str(exc).splitlines():
            print(f"{args.node}: {line}", file=sys.stderr)
        return 2
    print(f"{args.node}: drafted, {len(written.spends)} spends declared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
