"""Shared fixtures for the vault index tests.

`ARTICLE` and `write_article` write a throwaway wiki article to a fixture
vault. Check 11 and the attach CLI's tests need the same shape article, and
`tests/` carries no convention for one test module importing another, so the
shared piece lives here rather than as a second copy that would drift from
the first.
"""

from pathlib import Path

ARTICLE = """---
title: {title}
slug: {slug}
type: method
topics: [{topics}]
sources: []
confidentiality: {confidentiality}
client_scope: []
last_updated: 2026-05-13
reviewed: false
---

A body.
"""


def write_article(vault, slug, *, title=None, topics="alpha, beta",
                  confidentiality="public-free"):
    path = vault / "wiki" / Path(slug + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ARTICLE.format(
        title=title or slug, slug=slug, topics=topics,
        confidentiality=confidentiality,
    ))
    return path
