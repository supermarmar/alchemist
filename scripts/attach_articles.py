r"""Set one node's vault_articles, refusing a slug that will not survive check 11.

    .venv/bin/python scripts/attach_articles.py --node hazard-rate \
        --articles methods/survival-analysis concepts/default-intensity

    .venv/bin/python scripts/attach_articles.py --node hazard-rate --articles

The second form clears the field, which is what an uncovered node keeps.

Thirty-nine Phase 2 agents write these fields, and hand-edited YAML would give
thirty-nine styles and the occasional unparseable record. This tool re-renders
the whole record through the same `render` the staging merge uses, so every
write is identical in shape, and it validates each slug against the vault
first, so a fabrication is refused here rather than at the pre-commit hook.

`attachment_complaint` in `scripts.alchemist.vault` is the one place that
resolves and classifies a slug; check 11 calls it too, and a second copy of
that logic would drift from the first. This tool only decides how to word
each of the three outcomes it can return, and it reports against the slug it
was given rather than against a node, which is why its wording differs from
check 11's for the same problem.
"""

import argparse
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.checks import vault_root
from scripts.alchemist.model import parse_node
from scripts.alchemist.staging import render
from scripts.alchemist.vault import AttachmentProblem, attachment_complaint

REPO = Path(__file__).resolve().parents[1]


def _message(slug: str, problem: AttachmentProblem) -> str:
    """The one sentence this tool prints for `slug`, given why it failed."""
    if problem.kind == "missing":
        return f"{slug!r} does not resolve; looked for {problem.path}"
    elif problem.kind == "unclassified":
        return f"{slug!r} carries no confidentiality field at {problem.path}"
    elif problem.kind == "not-publishable":
        return (
            f"{slug!r} is {problem.confidentiality!r} rather than "
            f"public-free or public-paid"
        )
    raise NotImplementedError(f"unhandled attachment problem kind {problem.kind!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--node", required=True)
    parser.add_argument("--articles", nargs="*", default=[])
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--vault", type=Path, default=None)
    args = parser.parse_args()

    vault = args.vault or vault_root()
    node_file = args.root / "nodes" / f"{args.node}.md"
    if not node_file.is_file():
        print(f"no such node {args.node!r} at {node_file}", file=sys.stderr)
        return 2

    slugs = sorted(set(args.articles))
    complaints: list[str] = []
    for slug in slugs:
        problem = attachment_complaint(vault, slug)
        if problem is not None:
            complaints.append(_message(slug, problem))
    if complaints:
        for complaint in complaints:
            print(f"{args.node}: {complaint}", file=sys.stderr)
        return 2

    node = parse_node(node_file)
    node_file.write_text(render(replace(node, vault_articles=tuple(slugs))))
    print(f"{args.node}: {len(slugs)} articles attached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
