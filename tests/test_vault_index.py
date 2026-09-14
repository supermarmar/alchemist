from pathlib import Path

import pytest
import yaml

from conftest import ARTICLE, write_article
from scripts.alchemist.vault import (
    Article,
    AttachmentProblem,
    article_path,
    attachment_complaint,
    read_wiki,
)


@pytest.fixture
def vault(tmp_path):
    (tmp_path / "wiki").mkdir()
    write_article(tmp_path, "methods/glm", title="Generalised linear models")
    write_article(tmp_path, "regulation/crr", title="Capital Requirements Regulation",
                  confidentiality="public-paid")
    return tmp_path


def test_an_article_reads_into_a_record(vault):
    articles, skipped = read_wiki(vault)
    assert skipped == []
    assert articles == [
        Article("methods/glm", "Generalised linear models", "method",
                ("alpha", "beta"), "public-free"),
        Article("regulation/crr", "Capital Requirements Regulation", "method",
                ("alpha", "beta"), "public-paid"),
    ]


def test_articles_come_back_sorted_by_slug(vault):
    write_article(vault, "concepts/aaa")
    articles, _ = read_wiki(vault)
    assert [a.slug for a in articles] == ["concepts/aaa", "methods/glm", "regulation/crr"]


def test_an_unclassified_article_is_skipped_and_named(vault):
    """The 34 real ones are the AI and engineering material. Excluding them is
    what stops an agent attaching a slug whose publishability is unknown."""
    path = vault / "wiki" / "methods" / "unclassified.md"
    path.write_text(ARTICLE.format(
        title="Unclassified", slug="methods/unclassified", topics="x",
        confidentiality="public-free",
    ).replace("confidentiality: public-free\n", ""))
    articles, skipped = read_wiki(vault)
    assert "methods/unclassified" not in [a.slug for a in articles]
    assert any("methods/unclassified" in s and "confidentiality" in s for s in skipped)


def test_unparseable_frontmatter_is_skipped_and_named(vault):
    (vault / "wiki" / "methods" / "broken.md").write_text("---\n: : :\n---\n\nBody.\n")
    articles, skipped = read_wiki(vault)
    assert "methods/broken" not in [a.slug for a in articles]
    assert any("methods/broken" in s for s in skipped)


def test_the_readme_and_meta_are_not_articles(vault):
    (vault / "wiki" / "README.md").write_text("# The wiki\n")
    (vault / "wiki" / "_meta" / "sources").mkdir(parents=True)
    (vault / "wiki" / "_meta" / "health.md").write_text("# Health\n")
    articles, skipped = read_wiki(vault)
    assert [a.slug for a in articles] == ["methods/glm", "regulation/crr"]
    assert skipped == []


def test_article_path_round_trips_a_slug(vault):
    assert article_path(vault, "methods/glm") == vault / "wiki" / "methods" / "glm.md"
    assert article_path(vault, "methods/glm").is_file()


def test_attachment_complaint_is_none_for_a_publishable_slug(vault):
    assert attachment_complaint(vault, "methods/glm") is None


def test_attachment_complaint_names_the_path_for_a_missing_slug(vault):
    complaint = attachment_complaint(vault, "methods/missing")
    assert complaint == AttachmentProblem(
        "missing", vault / "wiki" / "methods" / "missing.md")


def test_attachment_complaint_names_the_missing_confidentiality_field(vault):
    path = vault / "wiki" / "methods" / "unclassified.md"
    path.write_text(ARTICLE.format(
        title="Unclassified", slug="methods/unclassified", topics="x",
        confidentiality="public-free",
    ).replace("confidentiality: public-free\n", ""))
    complaint = attachment_complaint(vault, "methods/unclassified")
    assert complaint == AttachmentProblem("unclassified", path)


def test_attachment_complaint_names_the_unpublishable_value(vault):
    path = write_article(vault, "methods/internal-only", confidentiality="internal")
    complaint = attachment_complaint(vault, "methods/internal-only")
    assert complaint == AttachmentProblem("not-publishable", path, "internal")


def test_attachment_complaint_treats_unparseable_frontmatter_as_unclassified(vault):
    path = vault / "wiki" / "methods" / "broken.md"
    path.write_text("---\n: : :\n---\n\nBody.\n")
    complaint = attachment_complaint(vault, "methods/broken")
    assert complaint == AttachmentProblem("unclassified", path)


def test_attachment_complaint_treats_non_mapping_frontmatter_as_unclassified(vault):
    path = vault / "wiki" / "methods" / "listlike.md"
    path.write_text("---\n- a\n- b\n---\n\nBody.\n")
    complaint = attachment_complaint(vault, "methods/listlike")
    assert complaint == AttachmentProblem("unclassified", path)
