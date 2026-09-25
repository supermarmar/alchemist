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




# ---------------------------------------------------------------------------
# Page fixtures. `test_pages.py` and `test_write_page.py` both need a node whose
# domains and status they choose, an objects file with two hazard aliases, and
# one conforming body; they live here for the reason the header states.
# ---------------------------------------------------------------------------

PAGE_OBJECTS = """- id: obj.hazard
  name: Hazard rate
  canonical: 'h(t)'
  definition: The instantaneous rate at which the event occurs, given survival to t.
  aliases:
    - {domain: credit, symbol: 'h(t)', name: default hazard}
    - {domain: stats, symbol: '\\lambda(t)', name: hazard function}
"""

PAGE_NODE = """---
id: {id}
title: {title}
domains: [{domains}]
status: {status}
requires: []
spends: []
anchor: [chosen]
vault_articles: []
vault_sources: []
taught_in: null
---

A stub body awaiting its page.
"""

PAGE_BODY = """## Definition

The hazard rate at a time is the instantaneous rate at which the event occurs,
given that it has not occurred by then.

## The expression

$$
h(t) = \\lim_{\\Delta t \\to 0} \\frac{P(t \\le T \\lt t + \\Delta t \\mid T \\ge t)}{\\Delta t}
$$

Here $h(t)$ is the hazard, $T$ the event time and $\\Delta t$ a short interval.

## Why this node exists

A model of whether cannot say when, and the hazard supplies the timing. The
discrete-time hazard needs it next.
"""


def write_stub(root, node_id, *, domains="credit, stats", status="stub"):
    path = root / "nodes" / f"{node_id}.md"
    path.write_text(PAGE_NODE.format(
        id=node_id, title=node_id.capitalize(), domains=domains, status=status))
    return path


@pytest.fixture
def page_repo(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "objects.yaml").write_text(PAGE_OBJECTS)
    return tmp_path
