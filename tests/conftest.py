"""Shared fixtures for the vault index tests.

`ARTICLE` and `write_article` write a throwaway wiki article to a fixture
vault. `NODE`, `write_node` and `corpus_and_vault` build a small node corpus
over such a vault. Check 11, the attach CLI and both their test modules need
the same shapes, and `tests/` carries no convention for one test module
importing another, so the shared pieces live here rather than as copies that
would drift from each other.
"""

from pathlib import Path

import pytest

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


NODE = """---
id: {id}
title: {title}
domains: [stats]
status: stub
requires: []
spends: []
anchor: [chosen]
vault_articles: [{articles}]
vault_sources: []
taught_in: null
---

A body.
"""


def write_node(root, node_id, articles=""):
    (root / "nodes" / f"{node_id}.md").write_text(
        NODE.format(id=node_id, title=node_id, articles=articles))


@pytest.fixture
def corpus_and_vault(tmp_path):
    root, vault = tmp_path / "repo", tmp_path / "vault"
    for sub in ("nodes", "paths", "notation", "sources"):
        (root / sub).mkdir(parents=True)
    (root / "notation" / "objects.yaml").write_text("[]\n")
    (root / "sources" / "wanted.yaml").write_text("[]\n")
    (vault / "wiki").mkdir(parents=True)
    write_article(vault, "methods/glm")
    write_article(vault, "methods/paid", confidentiality="public-paid")
    return root, vault
