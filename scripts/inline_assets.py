"""Inline our own three assets into a rendered lecture, so the file is
self-contained and opens from a bare disk with no network.

Quarto's own embed-resources: true is not used, because it inlines Quarto's
theme assets too, and render_lecture.sh removes those by matching link and
script tags that point into _files/libs/. Inlining defeats that strip. Doing it
ourselves afterwards reaches the same single file and leaves the strip working.

Raises rather than skips on a missing asset: a lecture that quietly lost its
stylesheet still renders, just wrongly, which is the failure mode this whole
pipeline exists to avoid.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r'[ \t]*<link[^>]*href="([^"]+\.css)"[^>]*>\n?')
SCRIPT = re.compile(r'[ \t]*<script[^>]*src="([^"]+\.js)"[^>]*>\s*</script>\n?')


def _resolve(reference: str, html_path: Path, root: Path) -> Path:
    candidate = (html_path.parent / reference).resolve()
    if not candidate.is_file():
        raise FileNotFoundError(f"{html_path}: cannot find {reference}")
    if root.resolve() not in candidate.parents:
        raise ValueError(f"{html_path}: {reference} escapes the repo")
    return candidate


def inline(html_path: Path, root: Path) -> int:
    text = html_path.read_text()
    count = 0

    def css(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _resolve(match.group(1), html_path, root).read_text()
        return f"<style>\n{body}\n</style>\n"

    def js(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _resolve(match.group(1), html_path, root).read_text()
        return f"<script>\n{body}\n</script>\n"

    text = LINK.sub(css, text)
    text = SCRIPT.sub(js, text)
    if count:
        html_path.write_text(text)
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, nargs="+")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for html in args.html:
        print(f"inlined {inline(html, args.root)} assets into {html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
