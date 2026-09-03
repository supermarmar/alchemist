"""Test every mathematics span in a .qmd against KaTeX itself.

KaTeX supports a strict subset of MathJax, and the seventeen credit lectures
carried across from actuarial_deep_learning were authored against MathJax. A
construct KaTeX cannot parse renders as red error text rather than failing the
build, so it has to be found deliberately.

This runs the real parser rather than grepping for a list of suspects, so it
stays correct as lectures are added in Phase 4.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
FENCE = re.compile(r"^[ \t]*```.*?^[ \t]*```[ \t]*$", re.S | re.M)
DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
INLINE = re.compile(r"(?<![\$\w])\$([^\$\n]+?)\$(?![\$\w])")


def _blank(match: re.Match[str]) -> str:
    """Replace a span with the same number of newlines, so line numbers hold."""
    return "\n" * match.group(0).count("\n")


def extract_spans(text: str) -> list[tuple[int, bool, str]]:
    text = FRONTMATTER.sub(_blank, text)
    text = FENCE.sub(_blank, text)

    spans: list[tuple[int, bool, str]] = []
    for match in DISPLAY.finditer(text):
        spans.append((text[: match.start()].count("\n") + 1, True, match.group(1)))
    text = DISPLAY.sub(_blank, text)
    for match in INLINE.finditer(text):
        spans.append((text[: match.start()].count("\n") + 1, False, match.group(1)))
    return sorted(spans)


def sweep(paths: list[Path]) -> list[str]:
    payload = []
    for path in paths:
        for line, display, tex in extract_spans(path.read_text()):
            payload.append(
                {"file": str(path), "line": line, "display": display, "tex": tex}
            )
    if not payload:
        return []
    done = subprocess.run(
        ["node", str(REPO / "scripts" / "katex_check.mjs")],
        input=json.dumps(payload), text=True, capture_output=True, check=True,
    )
    return [f for f in json.loads(done.stdout) if f]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("qmd", type=Path, nargs="+")
    args = parser.parse_args()
    failures = sweep(args.qmd)
    for failure in failures:
        print(failure)
    total = sum(len(extract_spans(p.read_text())) for p in args.qmd)
    print(f"\n{total} spans across {len(args.qmd)} files, {len(failures)} unsupported")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
