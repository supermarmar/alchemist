"""End-to-end over the real toolchain. Skipped where Quarto or Chrome is absent,
so the unit suite still runs on a machine that has neither.
"""

import os
import re
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


TEX_SOURCE = re.compile(r"\\(?:frac|int|exp|sum|prod|mathbf|mathrm|left|right)\b")
MONO_FACES = ("Menlo", "SFMono", "SF-Mono", "Courier", "Consolas", "LiberationMono")


def _prose_runs(pdf) -> tuple[str, set[str]]:
    """Extract the prose text of a PDF, dropping code listings.

    The lecture renders with `echo: true`, so Quarto prints every Python cell's
    source. One cell builds a matplotlib axis label, `"$\\mathrm{PD}_k$ (%)"`,
    whose mathtext shares a command name with the watchlist above. That is a code
    listing rather than a span KaTeX was ever asked to typeset, so it is filtered
    out by typeface: code sets in the mono face and prose in the sans.

    Filtering by face rather than by narrowing the regex is deliberate.
    `\\mathrm` appears four times in this lecture's genuine display
    mathematics, so it is one of the best sentinels available and dropping it
    from the watchlist would gut the check.
    """
    from pypdf import PdfReader

    prose: list[str] = []
    faces: set[str] = set()

    def visit(text, cm, tm, font_dict, font_size):
        face = str((font_dict or {}).get("/BaseFont", ""))
        faces.add(face)
        if not any(mono in face for mono in MONO_FACES):
            prose.append(text)

    for page in PdfReader(pdf).pages:
        page.extract_text(visitor_text=visit)
    return "".join(prose), faces


def test_the_exemplar_pdf_carries_typeset_mathematics():
    """A PDF whose maths snapshot fired early is complete, correctly trailed and
    A4 while showing raw TeX, so neither the size check nor the %%EOF check can
    see it. Extract the prose and look instead.

    No Quarto or Chrome guard, deliberately. This test renders nothing: it reads
    the committed PDF with pypdf, which is a dev dependency. Guarding it on the
    render toolchain meant it never ran in CI, which is where a regression in
    the committed artefact would actually be caught. The file guard below is the
    honest one.
    """
    pdf = REPO / "lectures" / "S1_credit-survival-bridge.pdf"
    if not pdf.is_file():
        pytest.skip("the exemplar lecture has not been printed yet")
    prose, faces = _prose_runs(pdf)
    # The stylesheet's mono stack is 'SF Mono', ui-monospace, Menlo, Consolas,
    # 'Liberation Mono', so which face wins depends on the machine. If none of
    # them appears, the filter has silently stopped filtering, and this assertion
    # turns that into a diagnosable failure rather than a mysterious red test.
    assert any(any(m in f for m in MONO_FACES) for f in faces), (
        f"no monospaced run found, so the code filter did nothing. "
        f"Faces seen: {sorted(faces)}"
    )
    assert "hazard" in prose.lower()          # extraction worked at all
    assert TEX_SOURCE.search(prose) is None   # and no command survived untypeset
