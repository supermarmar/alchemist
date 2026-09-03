from pathlib import Path

from scripts.alchemist.checks import check_gap_closure, check_publishable_citations
from scripts.alchemist.model import Corpus, Node

REGISTER = """---
id: {id}
confidentiality: {confidentiality}
publication_waiver: {waiver}
---
body
"""


def node(node_id: str, status="stub", sources=(), articles=()) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("credit",), status=status,
        requires=(), spends=(), anchor=(), vault_articles=tuple(articles),
        vault_sources=tuple(sources), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def fake_vault(tmp_path: Path, entries: dict[str, tuple[str, str]]) -> Path:
    registry = tmp_path / "wiki" / "_meta" / "sources"
    registry.mkdir(parents=True)
    for source_id, (confidentiality, waiver) in entries.items():
        (registry / f"{source_id}.md").write_text(
            REGISTER.format(id=source_id, confidentiality=confidentiality, waiver=waiver)
        )
    return tmp_path


def test_a_public_free_source_passes(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-free", "null")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_a_public_paid_source_without_a_waiver_fails(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-paid", "null")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    result = check_publishable_citations(c, vault)
    assert len(result.failures) == 1 and "public-paid" in result.failures[0]


def test_a_public_paid_source_with_a_waiver_passes(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-paid", "'granted 2026-09-01'")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_a_source_missing_from_the_register_fails(tmp_path):
    vault = fake_vault(tmp_path, {})
    c = Corpus({"n": node("n", sources=["ghost"])}, {})
    result = check_publishable_citations(c, vault)
    assert len(result.failures) == 1 and "not in the vault register" in result.failures[0]


def test_an_absent_vault_skips_rather_than_fails(tmp_path):
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    result = check_publishable_citations(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None


def test_a_paid_source_may_inform_through_vault_articles(tmp_path):
    """Check 5 walks `vault_sources` only. A paid source with no waiver can still
    inform a node through `vault_articles`, because the article lives in the
    private vault and the node's own prose is original. Mutating the loop to walk
    `vault_articles` as well would block purchased material from informing at all,
    which is the opposite of the intended rule. The value here is register-id
    shaped rather than slug shaped precisely so that such a mutant would resolve
    it and fail."""
    vault = fake_vault(tmp_path, {"paid": ("public-paid", "null")})
    c = Corpus({"n": node("n", articles=["paid"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_an_absent_ledger_skips_rather_than_fails(tmp_path):
    c = Corpus({"n": node("n", status="reviewed")}, {})
    result = check_gap_closure(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None


def test_a_reviewed_node_with_an_open_gap_fails(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: wanted\n"
    )
    c = Corpus({"n": node("n", status="reviewed")}, {})
    result = check_gap_closure(c, tmp_path)
    assert len(result.failures) == 1 and "g1" in result.failures[0]


def test_a_reviewed_node_whose_gap_is_ingested_passes(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: ingested\n"
    )
    c = Corpus({"n": node("n", status="reviewed")}, {})
    assert check_gap_closure(c, tmp_path).failures == []


def test_a_stub_node_with_an_open_gap_passes(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: wanted\n"
    )
    c = Corpus({"n": node("n", status="stub")}, {})
    assert check_gap_closure(c, tmp_path).failures == []
