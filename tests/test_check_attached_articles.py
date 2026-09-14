from pathlib import Path

import pytest

from conftest import write_node
from scripts.alchemist import checks as checks_module
from scripts.alchemist.checks import check_attached_articles
from scripts.alchemist.model import load_corpus
from scripts.alchemist.vault import AttachmentProblem


def test_a_resolving_public_free_slug_passes(corpus_and_vault):
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/glm")
    assert check_attached_articles(load_corpus(root), vault).failures == []


def test_a_resolving_public_paid_slug_passes(corpus_and_vault):
    """Check 5's rule, restated: purchased material informs a node through
    vault_articles because the article stays private and the prose is ours.
    Only vault_sources, which means the node quotes it, needs a waiver."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/paid")
    assert check_attached_articles(load_corpus(root), vault).failures == []


def test_a_slug_resolving_to_nothing_fails_and_names_the_path(corpus_and_vault):
    """A fabricated slug or a stale rename. This is the arm that makes an
    agent's claim mechanically checkable."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/invented")
    failures = check_attached_articles(load_corpus(root), vault).failures
    assert len(failures) == 1
    assert "does not resolve" in failures[0]
    assert "methods/invented.md" in failures[0]


def test_an_unclassified_article_fails_distinctly(corpus_and_vault):
    """Distinct from the resolution arm on purpose. This one fires when an
    article loses its classification in the vault after attachment, and a
    reclassification should not read as a rename."""
    root, vault = corpus_and_vault
    (vault / "wiki" / "methods" / "bare.md").write_text(
        "---\ntitle: Bare\nslug: methods/bare\ntype: method\ntopics: []\n---\n\nBody.\n")
    write_node(root, "a", "methods/bare")
    failures = check_attached_articles(load_corpus(root), vault).failures
    assert len(failures) == 1
    assert "carries no confidentiality field" in failures[0]
    assert "does not resolve" not in failures[0]


def test_an_unhandled_problem_kind_raises_rather_than_misreporting(corpus_and_vault, monkeypatch):
    """The three-way branch used to end in a bare `else`, which would have
    reported a fourth `AttachmentProblem` kind as `not-publishable` rather
    than failing loudly. Guard the fix: an unrecognised kind must raise,
    matching the attach tool's own exhaustive branch over the same type."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/glm")
    bogus = AttachmentProblem("bogus-kind", Path("nowhere"))
    monkeypatch.setattr(checks_module, "attachment_complaint", lambda vault, slug: bogus)
    with pytest.raises(NotImplementedError):
        check_attached_articles(load_corpus(root), vault)


def test_the_check_skips_where_no_vault_is_present(corpus_and_vault):
    """CI has no vault, so this arm is what stops the deploy failing. It also
    means CI does not gate a fabricated slug; the pre-commit hook does."""
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/invented")
    result = check_attached_articles(load_corpus(root), Path("/nonexistent"))
    assert result.skipped is not None
    assert result.failures == []
