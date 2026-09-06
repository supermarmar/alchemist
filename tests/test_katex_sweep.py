import subprocess

import pytest

from scripts import katex_sweep
from scripts.katex_sweep import extract_spans, spans_in, sweep

QMD = """---
title: "T"
math: "$not maths, this is frontmatter$"
---

Inline $\\lambda(t)$ here.

$$
{}_tp_x = 1
$$

```python
cost = 5  # $ in a code fence is not maths
print("$x$")
```

And $\\mu_x$ after the fence.
"""


def test_frontmatter_is_not_scanned():
    assert all("frontmatter" not in tex for _, _, tex in extract_spans(QMD))


def test_fenced_code_is_not_scanned():
    assert all("code fence" not in tex for _, _, tex in extract_spans(QMD))
    assert all(tex.strip() != "x" for _, _, tex in extract_spans(QMD))


def test_display_and_inline_are_both_found_and_flagged():
    spans = extract_spans(QMD)
    assert (True, "{}_tp_x = 1") in [(d, t.strip()) for _, d, t in spans]
    assert r"\lambda(t)" in [t.strip() for _, d, t in spans if not d]
    assert r"\mu_x" in [t.strip() for _, d, t in spans if not d]


def test_line_numbers_are_reported_for_the_report():
    spans = extract_spans(QMD)
    assert all(line >= 1 for line, _, _ in spans)
    inline_lines = [line for line, d, t in spans if not d and "lambda" in t]
    assert inline_lines and inline_lines[0] == 6


def test_a_node_crash_surfaces_nodes_own_diagnostic(monkeypatch, tmp_path):
    """`CalledProcessError.__str__` omits stderr, so a bare `check=True` hands a
    Phase 4 user an exit status and no cause. The message must carry node's own
    text or the failure is undiagnosable.
    """
    qmd = tmp_path / "x.qmd"
    qmd.write_text("Inline $x$.\n")

    def boom(*args, **kwargs):
        raise subprocess.CalledProcessError(1, "node", stderr="Cannot find module")

    monkeypatch.setattr(katex_sweep.subprocess, "run", boom)
    with pytest.raises(RuntimeError, match="Cannot find module"):
        katex_sweep.sweep([qmd])


def test_extracts_spans_from_a_node_body(tmp_path):
    node = tmp_path / "hazard-rate.md"
    node.write_text(
        "---\nid: hazard-rate\ntitle: Hazard rate\n---\n\n"
        "The hazard is $h(t)$ and the survival function is $S(t)$.\n\n"
        "$$\nh(t) = -\\frac{d}{dt}\\log S(t)\n$$\n"
    )
    spans = spans_in(node)
    assert [tex.strip() for _, _, tex in spans] == [
        "h(t)", "S(t)", "h(t) = -\\frac{d}{dt}\\log S(t)",
    ]


def test_frontmatter_is_not_swept_as_mathematics(tmp_path):
    """A node's frontmatter is YAML, and a dollar in it is not a maths span."""
    node = tmp_path / "n.md"
    node.write_text("---\nid: n\ntitle: A $ sign and another $\n---\n\nBody.\n")
    assert spans_in(node) == []


def test_extracts_alias_symbols_from_objects_yaml(tmp_path):
    contract = tmp_path / "objects.yaml"
    contract.write_text(
        "- id: obj.hazard\n"
        "  name: Hazard\n"
        "  canonical: 'h(t)'\n"
        "  definition: The instantaneous rate.\n"
        "  aliases:\n"
        "    - {domain: life, symbol: '\\mu_x', name: force of mortality}\n"
        "    - {domain: gi, symbol: '\\lambda', name: claim intensity}\n"
    )
    assert sorted(tex for _, _, tex in spans_in(contract)) == [
        "\\lambda", "\\mu_x", "h(t)",
    ]


def test_an_unsupported_alias_is_reported(tmp_path):
    """The point of extending the sweep: a malformed alias publishes red error
    text on the symbol table, and every script still exits zero."""
    contract = tmp_path / "objects.yaml"
    contract.write_text(
        "- id: obj.broken\n"
        "  name: Broken\n"
        "  canonical: 'x'\n"
        "  definition: A rendering KaTeX cannot parse.\n"
        "  aliases:\n"
        "    - {domain: gi, symbol: '\\notacommand{x}', name: broken}\n"
    )
    assert sweep([contract]), "an unsupported alias must be reported"


def test_a_short_symbol_reports_its_own_line_not_an_earlier_collision(tmp_path):
    """A bare substring search for a short symbol matches the first line
    carrying it anywhere, including inside a longer symbol from an earlier
    entry. The reported line must be where the symbol itself is declared.
    """
    contract = tmp_path / "objects.yaml"
    contract.write_text(
        "- id: obj.hazard\n"
        "  name: Hazard\n"
        "  canonical: 'h(t)'\n"
        "  definition: The instantaneous rate.\n"
        "  aliases:\n"
        "    - {domain: life, symbol: '\\mu_x', name: force of mortality}\n"
        "- id: obj.response-mean\n"
        "  name: Expected response\n"
        "  canonical: '\\mu'\n"
        "  definition: The expectation of the response.\n"
        "  aliases: []\n"
    )
    lines = contract.read_text().splitlines()
    true_line = next(
        i for i, line in enumerate(lines, start=1) if line.strip() == "canonical: '\\mu'"
    )
    reported = {tex: line for line, _, tex in spans_in(contract)}
    assert reported["\\mu"] == true_line
