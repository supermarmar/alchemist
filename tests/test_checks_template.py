from pathlib import Path

from conftest import PAGE_BODY
from scripts.alchemist.checks import check_template_conformance, run_all
from scripts.alchemist.model import Corpus, Node, load_corpus, load_objects

REPO = Path(__file__).resolve().parents[1]


def node(node_id: str, status: str, body: str) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("stats",), status=status, requires=(), spends=(),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body=body,
        path=Path(f"nodes/{node_id}.md"),
    )


def failures(*nodes: Node) -> list[str]:
    return check_template_conformance(Corpus({n.id: n for n in nodes}, {})).failures


def test_a_stub_is_exempt_whatever_its_body():
    assert failures(node("a", "stub", "One sentence of scope, no headings.")) == []


def test_a_conforming_drafted_page_passes():
    assert failures(node("a", "drafted", PAGE_BODY)) == []


def test_a_drafted_page_missing_a_heading_fails_and_names_the_node():
    result = failures(node("a", "drafted", PAGE_BODY.replace("## Why this node exists", "## Why")))
    assert len(result) == 1 and result[0].startswith("a: ") and "in that order" in result[0]


def test_a_reviewed_page_is_checked_too():
    result = failures(node("a", "reviewed", PAGE_BODY + "\n$$\nx\n$$\n\n$$\ny\n$$\n"))
    assert len(result) == 1 and result[0].startswith("a: 3 display blocks")


def test_run_all_reports_twelve_rules_with_the_template_last():
    """The rule number is the CLI's contract with every document that counts
    the checks, so pin it here rather than in prose alone."""
    results = run_all(load_corpus(REPO), load_objects(REPO), REPO, Path("/nonexistent"))
    assert len(results) == 12
    assert results[-1].rule == "12. written pages follow the template"
    assert results[-1].ok
