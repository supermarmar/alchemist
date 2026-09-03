"""Rewrite vendor/katex/katex.min.css so its font URLs are base64 data URIs.

Run once after vendoring a new KaTeX. A single-file lecture needs the fonts
inside the CSS, because inlining a stylesheet that points at fonts/ by relative
URL yields a page whose mathematics renders in a fallback face.

Only the woff2 faces are embedded. KaTeX also ships woff and ttf for older
browsers, and carrying all three would treble the payload for no reader we have.
"""

import base64
import re
from pathlib import Path

VENDOR = Path(__file__).resolve().parents[1] / "vendor" / "katex"
URL = re.compile(r"url\((fonts/[^)]+\.woff2)\)")


def main() -> int:
    css = VENDOR / "katex.min.css"
    text = css.read_text()

    def embed(match: re.Match[str]) -> str:
        data = (VENDOR / match.group(1)).read_bytes()
        encoded = base64.b64encode(data).decode("ascii")
        return f"url(data:font/woff2;base64,{encoded})"

    rewritten, count = URL.subn(embed, text)
    # Drop the woff and ttf sources, which now sit after a data URI that always wins.
    rewritten = re.sub(r",\s*url\(fonts/[^)]+\.(?:woff|ttf)\)\s*format\([^)]+\)", "", rewritten)
    css.write_text(rewritten)
    print(f"embedded {count} woff2 faces into {css.name}, now {len(rewritten):,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
