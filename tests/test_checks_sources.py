from pathlib import Path

from scripts.alchemist.checks import (
    check_gap_closure,
    check_ledger_references_resolve,
    check_publishable_citations,
    check_taught_in_resolves,
)
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


def taught(node_id: str, taught_in=None) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("credit",), status="stub",
        requires=(), spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=taught_in, body="", path=Path(f"nodes/{node_id}.md"),
    )


def lectures(tmp_path: Path, *stems: str) -> Path:
    (tmp_path / "lectures").mkdir()
    for stem in stems:
        (tmp_path / "lectures" / f"{stem}.qmd").write_text("---\ntitle: L\n---\n")
    return tmp_path


def test_a_taught_node_whose_lecture_exists_passes(tmp_path):
    root = lectures(tmp_path, "S1_credit-survival-bridge")
    c = Corpus({"n": taught("n", "S1_credit-survival-bridge")}, {})
    assert check_taught_in_resolves(c, root).failures == []


def test_a_taught_node_whose_lecture_is_missing_fails(tmp_path):
    """The Phase 4 failure: a node claims a lecture that has not been written,
    so its page and every path listing it publish a dead link. The lecture
    directory here holds a different lecture, so the rule has to compare the
    name rather than merely count files."""
    root = lectures(tmp_path, "S2_something-else")
    c = Corpus({"n": taught("n", "S1_credit-survival-bridge")}, {})
    result = check_taught_in_resolves(c, root)
    assert len(result.failures) == 1
    assert "S1_credit-survival-bridge" in result.failures[0]
    assert "n:" in result.failures[0]


def test_an_untaught_node_is_not_asked_for_a_lecture(tmp_path):
    """Most of the corpus is tier 1, so a null taught_in must not be read as
    naming a lecture called "None"."""
    root = lectures(tmp_path)
    c = Corpus({"n": taught("n")}, {})
    assert check_taught_in_resolves(c, root).failures == []


def test_an_absent_lecture_directory_skips_rather_than_fails(tmp_path):
    c = Corpus({"n": taught("n", "S1_credit-survival-bridge")}, {})
    result = check_taught_in_resolves(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None


def ledger(tmp_path: Path, text: str) -> Path:
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(text)
    return tmp_path


GHOST_LEDGER = "- id: g1\n  needed_by: [ghost]\n  status: wanted\n"


def test_a_ledger_naming_a_real_node_passes(tmp_path):
    root = ledger(tmp_path, "- id: g1\n  needed_by: [n]\n  status: wanted\n")
    c = Corpus({"n": node("n")}, {})
    assert check_ledger_references_resolve(c, root).failures == []


def test_a_ledger_naming_an_unknown_node_fails(tmp_path):
    """The hole this rule closes. Check 6 looks the id up with `.get` and moves
    on where it finds nothing, so a single typo disables gap enforcement for
    that node silently and permanently. Assert that check 6 stays quiet on the
    same ledger, which is what makes rule 9 the only thing that can see it."""
    root = ledger(tmp_path, GHOST_LEDGER)
    c = Corpus({"n": node("n", status="reviewed")}, {})
    assert check_gap_closure(c, root).failures == []
    result = check_ledger_references_resolve(c, root)
    assert len(result.failures) == 1
    assert "ghost" in result.failures[0] and "g1" in result.failures[0]


def test_an_ingested_gap_naming_an_unknown_node_still_fails(tmp_path):
    """Check 6 skips ingested entries, so a typo behind one would never surface
    there and would fire the day the entry is reopened."""
    root = ledger(tmp_path, "- id: g1\n  needed_by: [ghost]\n  status: ingested\n")
    c = Corpus({"n": node("n")}, {})
    assert len(check_ledger_references_resolve(c, root).failures) == 1


def test_an_absent_ledger_skips_rule_9_rather_than_failing(tmp_path):
    c = Corpus({"n": node("n")}, {})
    result = check_ledger_references_resolve(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None
