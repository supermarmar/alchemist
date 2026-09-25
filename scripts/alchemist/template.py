"""The tier-1 page template, as rules a machine can apply.

Three sections under fixed headings, one display block as the norm and two as
the ceiling, and a handful of house rules a page cannot carry. The Phase 0 plan
fixed the template at its Task 11 and the Phase 3 design restates it in section
4; this module is the one place the rules are code. Both `write_page.py` and
check 12 call it, so a page the tool accepts is a page the check passes, and a
hand edit that breaks the template fails the next commit.

It imports nothing from the package on purpose. `checks.py` imports it for
check 12 and `pages.py` imports check 1 from `checks.py`, and a validator that
imported either would close that into a cycle.
"""

from __future__ import annotations

import re

HEADINGS = ("## Definition", "## The expression", "## Why this node exists")
HEADING = re.compile(r"^#{1,6} .*$", re.M)
SECTION_BREAK = re.compile(r"^## .*$", re.M)
DISPLAY = re.compile(r"\$\$.+?\$\$", re.S)
DASH = re.compile(r"[–—]")
# An amount, never the bare sign: `$2m`, `$1.5 billion`, `$1,500`. Every `$`
# on a page is a maths delimiter, so `$1$` is the number one and passes. The
# one false positive is inline maths of the form `$2m$`, which the message
# tells the author to respace as `$2\,m$`.
CURRENCY = re.compile(
    r"\$\d[\d,]*(?:\.\d+)?\s?(?:m|bn|k|million|billion|thousand)\b"
    r"|\$\d{1,3}(?:,\d{3})+\b"
)
RATHER_THAN = re.compile(r"\brather than\b", re.I)
MAX_RATHER_THAN = 1  # G20: 200 of the 1,580 original stubs carried the phrase


def validate_body(body: str) -> list[str]:
    """Every breach of the template, one sentence each, worded for the author
    who has to fix it. An empty list means the body conforms."""
    problems: list[str] = []
    found = tuple(h.rstrip() for h in HEADING.findall(body))
    if found != HEADINGS:
        problems.append(
            f"headings are {list(found)!r}; the template wants exactly "
            f"{list(HEADINGS)!r} in that order and no other heading"
        )
    else:
        preamble, *sections = SECTION_BREAK.split(body)
        if preamble.strip():
            problems.append(
                f"text before the first heading: {preamble.strip()[:40]!r}; a "
                f"page opens on '## Definition'"
            )
        for heading, text in zip(HEADINGS, sections):
            if not text.strip():
                problems.append(f"{heading!r} has no text beneath it")
    blocks = len(DISPLAY.findall(body))
    if blocks == 0:
        problems.append(
            "no display block; 'The expression' carries the defining formula "
            "between $$ delimiters"
        )
    elif blocks > 2:
        problems.append(
            f"{blocks} display blocks; one is the norm and two the ceiling, so a "
            f"node wanting a third is a split candidate for the report"
        )
    for match in DASH.finditer(body):
        line = body.count("\n", 0, match.start()) + 1
        problems.append(
            f"em or en dash on line {line}; use a comma, full stop, colon or "
            f"parentheses"
        )
    for match in CURRENCY.finditer(body):
        problems.append(
            f"currency written with a dollar sign at {match.group()!r}; write the "
            f"unit word, since every $ on the page is a maths delimiter"
        )
    count = len(RATHER_THAN.findall(body))
    if count > MAX_RATHER_THAN:
        problems.append(
            f"'rather than' appears {count} times; the cap is {MAX_RATHER_THAN} "
            f"per page (G20)"
        )
    return problems
