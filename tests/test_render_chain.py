"""End-to-end over the real toolchain. Skipped where Quarto or Chrome is absent,
so the unit suite still runs on a machine that has neither.
"""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
QUARTO = Path(os.environ.get("QUARTO", Path.home() / ".local" / "bin" / "quarto"))
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

PROBE = """---
title: "Render probe"
format:
  html:
    css: ../assets/lecture.css
    embed-resources: false
    html-math-method:
      method: katex
      url: "../vendor/katex/"
---

Inline $\\lambda(t)$ and a display:

$$
{}_tp_x = \\exp\\left(-\\int_0^t \\mu_{x+s}\\,ds\\right)
$$
"""


@pytest.fixture
def probe():
    target = REPO / "lectures" / "_probe.qmd"
    target.write_text(PROBE)
    yield target
    for suffix in (".qmd", ".html", ".pdf"):
        target.with_suffix(suffix).unlink(missing_ok=True)
    shutil.rmtree(REPO / "lectures" / "_probe_files", ignore_errors=True)


@pytest.mark.skipif(not QUARTO.is_file(), reason="quarto not installed")
def test_a_rendered_lecture_carries_no_external_reference(probe):
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    html = probe.with_suffix(".html").read_text()
    # Assert the specific paths are no longer referenced, rather than the bare
    # substrings `href=` and `src=`. The real inlined katex.min.js contains `src=`
    # in its own image-rendering code, so a substring assertion fails spuriously
    # the moment a genuine asset is inlined, which is what Task 8 found.
    assert "vendor/katex/katex.min.css" not in html
    assert "vendor/katex/katex.min.js" not in html
    assert "assets/lecture.css" not in html
    assert "katex.render" in html   # Quarto's own render loop survived
    assert ".katex" in html         # the stylesheet's rules were inlined


@pytest.mark.skipif(not QUARTO.is_file(), reason="quarto not installed")
def test_the_katex_path_is_not_concatenated_without_a_separator(probe):
    """Quarto joins its katex url to the filename with no separator, so a url
    missing its trailing slash yields vendor/katexkatex.min.js and silently
    fails to typeset. Verified against Quarto 1.10.18 on 3 September 2026."""
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    assert "katexkatex" not in probe.with_suffix(".html").read_text()


@pytest.mark.skipif(
    not (QUARTO.is_file() and CHROME.is_file()), reason="quarto or chrome absent"
)
def test_the_pdf_is_complete(probe):
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    subprocess.run(
        ["bash", "scripts/html_to_pdf.sh", str(probe.with_suffix(".html").relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    pdf = probe.with_suffix(".pdf")
    assert pdf.stat().st_size > 10_000
    assert b"%%EOF" in pdf.read_bytes()[-64:]
