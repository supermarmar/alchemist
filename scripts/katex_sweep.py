"""Test every mathematics span in a .qmd, a node body, or the notation
contract against KaTeX itself.

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

import yaml

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
    # Sort on line and kind only, never on the tex itself: two spans sharing a
    # line would otherwise fall back to alphabetical order on their content,
    # so "$h(t)$ ... $S(t)$" reports S before h. Timsort is stable, so this
    # keeps the finditer discovery order, which is document order, for spans
    # that tie on both keys.
    return sorted(spans, key=lambda span: (span[0], span[1]))


def extract_alias_spans(text: str) -> list[tuple[int, bool, str]]:
    """Every symbol in the notation contract, as an inline span.

    The contract's canonicals and aliases are raw TeX that reaches a reader
    only through the generated symbols.md, so a malformed one publishes red
    error text on the page every reader of the corpus opens first, while every
    script exits zero. Line numbers are recovered by searching the source text
    for the symbol, because yaml.safe_load discards them. Every canonical and
    alias in the contract is a single-quoted YAML scalar, so the search looks
    for the symbol between its quotes first: a bare substring search matches
    the first line carrying the symbol anywhere, including inside a longer
    symbol from an earlier entry or a word in a comment, which sent the
    expected response's canonical to the line for the hazard's force-of-
    mortality alias and the cohort index to the line for "objects" in this
    file's own header comment, before this fix.
    """
    entries = yaml.safe_load(text) or []
    lines = text.splitlines()
    spans: list[tuple[int, bool, str]] = []
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        symbols = [entry.get("canonical")]
        for alias in entry.get("aliases") or []:
            if isinstance(alias, dict):
                symbols.append(alias.get("symbol"))
        for symbol in symbols:
            if not symbol or symbol in seen:
                continue
            seen.add(symbol)
            quoted = f"'{symbol}'"
            line = next(
                (i for i, text_line in enumerate(lines, start=1) if quoted in text_line),
                None,
            )
            if line is None:
                line = next(
                    (i for i, text_line in enumerate(lines, start=1) if symbol in text_line),
                    1,
                )
            spans.append((line, False, symbol))
    return spans


def spans_in(path: Path) -> list[tuple[int, bool, str]]:
    """Dispatch on suffix, because a .yaml contract and a .md body carry their
    mathematics differently and neither is a .qmd."""
    text = path.read_text()
    if path.suffix in {".yaml", ".yml"}:
        return extract_alias_spans(text)
    return extract_spans(text)


def sweep(paths: list[Path]) -> list[str]:
    payload = []
    for path in paths:
        for line, display, tex in spans_in(path):
            payload.append(
                {"file": str(path), "line": line, "display": display, "tex": tex}
            )
    if not payload:
        return []
    try:
        done = subprocess.run(
            ["node", str(REPO / "scripts" / "katex_check.mjs")],
            input=json.dumps(payload), text=True, capture_output=True, check=True,
        )
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "node is not on PATH, so the sweep cannot run. Install it, for "
            "example with `brew install node`."
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            "the KaTeX harness failed rather than reporting spans. node exited "
            f"{exc.returncode}. Its own diagnostic follows:\n{exc.stderr}"
        ) from exc
    return [f for f in json.loads(done.stdout) if f]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", type=Path, nargs="+")
    args = parser.parse_args()
    failures = sweep(args.paths)
    for failure in failures:
        print(failure)
    total = sum(len(spans_in(p)) for p in args.paths)
    print(f"\n{total} spans across {len(args.paths)} files, {len(failures)} unsupported")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
