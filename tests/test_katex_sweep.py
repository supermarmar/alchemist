import subprocess

import pytest

from scripts import katex_sweep
from scripts.katex_sweep import extract_spans

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
