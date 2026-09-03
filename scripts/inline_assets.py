"""Inline our own three assets into a rendered lecture, so the file is
self-contained and opens from a bare disk with no network.

Quarto's own embed-resources: true is not used, because it inlines Quarto's
theme assets too, and render_lecture.sh removes those by matching link and
script tags that point into _files/libs/. Inlining defeats that strip. Doing it
ourselves afterwards reaches the same single file and leaves the strip working.

Raises rather than skips on a missing asset, and on an asset carrying the tag
that would close the element it is spliced into: a lecture that quietly lost its
stylesheet, or that spilled half a script onto the page, still renders, just
wrongly, which is the failure mode this whole pipeline exists to avoid.
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


def _asset_body(reference: str, html_path: Path, root: Path, closing: str) -> str:
    """The asset's text, refused where it carries the tag that would end its own
    element.

    Splicing a stylesheet between `<style>` and `</style>` is only safe while
    the stylesheet contains no `</style>` of its own, and the same holds for a
    script. Where it does, the browser terminates the element at that point and
    renders the remainder as page text, silently, with every script in the chain
    exiting zero. That is the failure class this pipeline exists to remove, so
    it raises instead. Dormant across all three current assets, and a base64
    woff2 payload cannot contain `<` at all, but a KaTeX bump or a stylesheet
    edit is all it would take.
    """
    body = _resolve(reference, html_path, root).read_text()
    if closing in body:
        raise ValueError(
            f"{html_path}: {reference} contains {closing!r}, which would end the "
            f"element it is being inlined into and spill the rest onto the page"
        )
    return body


def inline(html_path: Path, root: Path) -> int:
    text = html_path.read_text()
    count = 0

    def css(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _asset_body(match.group(1), html_path, root, "</style>")
        return f"<style>\n{body}\n</style>\n"

    def js(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _asset_body(match.group(1), html_path, root, "</script>")
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
