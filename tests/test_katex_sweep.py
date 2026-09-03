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
