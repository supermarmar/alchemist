from pathlib import Path

import pytest

from conftest import PAGE_BODY, write_stub
from scripts.alchemist.model import Corpus, Node, Spend, load_objects, parse_node
from scripts.alchemist.pages import PageRefused, page_statistics, parse_spend, write_page


def test_it_writes_the_body_the_spends_and_drafted(page_repo):
    path = write_stub(page_repo, "hazard")
    write_page(path, PAGE_BODY, (Spend("obj.hazard", "credit"),), load_objects(page_repo))
    node = parse_node(path)
    assert node.status == "drafted"
    assert node.spends == (Spend("obj.hazard", "credit"),)
    assert node.body.strip() == PAGE_BODY.strip()
    assert node.domains == ("credit", "stats") and node.anchor == ("chosen",)  # untouched


def test_a_rerun_is_byte_identical_whatever_the_spend_order(page_repo):
    path = write_stub(page_repo, "hazard")
    spends = (Spend("obj.hazard", "stats"), Spend("obj.hazard", "credit"))
    write_page(path, PAGE_BODY, spends, load_objects(page_repo))
    first = path.read_bytes()
    write_page(path, PAGE_BODY, tuple(reversed(spends)), load_objects(page_repo))
    assert path.read_bytes() == first


def test_spends_are_sorted_and_deduplicated(page_repo):
    path = write_stub(page_repo, "hazard")
    spends = (Spend("obj.hazard", "stats"), Spend("obj.hazard", "credit"), Spend("obj.hazard", "stats"))
    written = write_page(path, PAGE_BODY, spends, load_objects(page_repo))
    assert written.spends == (Spend("obj.hazard", "credit"), Spend("obj.hazard", "stats"))


def test_a_body_breaking_the_template_is_refused_and_the_file_untouched(page_repo):
    path = write_stub(page_repo, "hazard")
    before = path.read_bytes()
    with pytest.raises(PageRefused, match="in that order"):
        write_page(path, PAGE_BODY.replace("## Why this node exists", "## Why"), (), load_objects(page_repo))
    assert path.read_bytes() == before


def test_a_spend_check_1_would_refuse_is_refused_here(page_repo):
    """The three arms of check 1, so the pre-commit hook never sees what the
    tool could have caught with the author present."""
    path = write_stub(page_repo, "hazard", domains="credit")
    objects = load_objects(page_repo)
    with pytest.raises(PageRefused, match="unknown object"):
        write_page(path, PAGE_BODY, (Spend("obj.ghost", "credit"),), objects)
    with pytest.raises(PageRefused, match="not among its own domains"):
        write_page(path, PAGE_BODY, (Spend("obj.hazard", "stats"),), objects)
    life = write_stub(page_repo, "life", domains="life")
    with pytest.raises(PageRefused, match="no alias for domain"):
        write_page(life, PAGE_BODY, (Spend("obj.hazard", "life"),), objects)
    assert parse_node(path).status == "stub" and parse_node(life).status == "stub"


def test_a_reviewed_page_is_refused_without_force_and_downgraded_with_it(page_repo):
    path = write_stub(page_repo, "hazard", status="reviewed")
    with pytest.raises(PageRefused, match="reviewed"):
        write_page(path, PAGE_BODY, (), load_objects(page_repo))
    assert write_page(path, PAGE_BODY, (), load_objects(page_repo), force=True).status == "drafted"


def test_parse_spend_reads_the_colon_form_and_refuses_anything_else():
    assert parse_spend("obj.hazard:credit") == Spend("obj.hazard", "credit")
    for bad in ("obj.hazard", "obj.hazard:", ":credit"):
        with pytest.raises(ValueError, match="object:domain"):
            parse_spend(bad)


def node(node_id, *, status="drafted", requires=(), domains=("stats",), body="", title=None):
    return Node(
        id=node_id, title=title or node_id.replace("-", " ").capitalize(), domains=domains,
        status=status, requires=tuple(requires), spends=(), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body=body, path=Path(f"nodes/{node_id}.md"),
    )


def test_statistics_count_status_domain_blocks_words_and_the_capped_phrase():
    corpus = Corpus({
        "a": node("a", status="stub", body="A stub."),
        "b": node("b", domains=("life", "stats"), body=PAGE_BODY),
        "c": node("c", body=PAGE_BODY + "\n$$\nx\n$$\n", requires=["b"]),
    }, {})
    stats = page_statistics(corpus)
    assert stats["by_status"] == {"stub": 1, "drafted": 2}
    assert stats["written_by_domain"] == {"life": 1, "stats": 2}
    assert stats["display_blocks"] == {1: 1, 2: 1}
    assert stats["words"]["min"] <= stats["words"]["median"] <= stats["words"]["max"]
    assert stats["rather_than"] == 0


def test_a_written_page_naming_none_of_its_unlocks_is_listed():
    """`hazard-rate` unlocks `cox-model` and its closing section never names
    that title, so it is listed; `cox-model` unlocks nothing and is exempt. The
    match is title or id in the closing section, lowercased, which is
    approximate and says so."""
    def corpus(hazard_body):
        return Corpus({
            "hazard-rate": node("hazard-rate", body=hazard_body, title="Hazard rate"),
            "cox-model": node("cox-model", body=PAGE_BODY, requires=["hazard-rate"], title="Cox model"),
        }, {})
    assert page_statistics(corpus(PAGE_BODY))["no_forward_reference"] == ["hazard-rate"]
    named = PAGE_BODY.replace("discrete-time hazard needs it next", "Cox model needs it next")
    assert page_statistics(corpus(named))["no_forward_reference"] == []


def test_an_unlock_title_wrapped_across_a_line_break_still_counts_as_named():
    """A page body is hard-wrapped, so a two-word title often straddles a line
    break. Three of the first ten landed pages did exactly that and were listed
    as misses, which would have filled every wave's gate with false alarms."""
    corpus = Corpus({
        "hazard-rate": node("hazard-rate", title="Hazard rate",
                            body=PAGE_BODY.replace("discrete-time hazard needs it next", "Cox\nmodel needs it next")),
        "cox-model": node("cox-model", body=PAGE_BODY, requires=["hazard-rate"], title="Cox model"),
    }, {})
    assert page_statistics(corpus)["no_forward_reference"] == []
