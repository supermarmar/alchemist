import subprocess
import sys
from pathlib import Path

from conftest import write_node
from scripts.alchemist.model import parse_node

REPO = Path(__file__).resolve().parents[1]


def run(root, vault, *args):
    return subprocess.run(
        [sys.executable, "scripts/attach_articles.py",
         "--root", str(root), "--vault", str(vault), *args],
        capture_output=True, text=True, cwd=REPO,
    )


def test_it_sets_the_field_sorted(corpus_and_vault):
    """Sorted, so a rerun of the same batch is byte-identical."""
    root, vault = corpus_and_vault
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/paid", "methods/glm")
    assert result.returncode == 0
    assert parse_node(root / "nodes" / "a.md").vault_articles == ("methods/glm", "methods/paid")


def test_it_refuses_a_slug_that_does_not_resolve(corpus_and_vault):
    root, vault = corpus_and_vault
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/invented")
    assert result.returncode == 2
    assert "does not resolve" in result.stderr
    assert parse_node(root / "nodes" / "a.md").vault_articles == ()


def test_it_refuses_an_unclassified_article(corpus_and_vault):
    root, vault = corpus_and_vault
    (vault / "wiki" / "methods" / "bare.md").write_text(
        "---\ntitle: Bare\nslug: methods/bare\ntype: method\ntopics: []\n---\n\nBody.\n")
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/bare")
    assert result.returncode == 2
    assert "confidentiality" in result.stderr
    assert parse_node(root / "nodes" / "a.md").vault_articles == ()


def test_it_refuses_an_unknown_node(corpus_and_vault):
    root, vault = corpus_and_vault
    result = run(root, vault, "--node", "ghost", "--articles", "methods/glm")
    assert result.returncode == 2
    assert "no such node" in result.stderr


def test_no_articles_clears_the_field_and_touches_nothing_else(corpus_and_vault):
    """An uncovered node keeps an empty list, and the rest of the record has
    to survive the round trip through render untouched."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/glm")
    before = parse_node(root / "nodes" / "a.md")
    assert run(root, vault, "--node", "a", "--articles").returncode == 0
    after = parse_node(root / "nodes" / "a.md")
    assert after.vault_articles == ()
    assert (after.id, after.title, after.domains, after.status,
            after.requires, after.anchor, after.body) == (
        before.id, before.title, before.domains, before.status,
        before.requires, before.anchor, before.body)
