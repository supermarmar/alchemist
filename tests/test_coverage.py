from scripts.alchemist.coverage import (
    NO_INDEX, attachment_histogram, by_anchor_document, by_domain, render_report,
)
from scripts.alchemist.model import load_corpus
from scripts.build_coverage_report import _index_built

from conftest import write_node


def _set_domains(root, node_id, domains):
    path = root / "nodes" / f"{node_id}.md"
    path.write_text(path.read_text().replace("domains: [stats]", f"domains: [{domains}]"))


def _set_anchor(root, node_id, anchor):
    path = root / "nodes" / f"{node_id}.md"
    path.write_text(path.read_text().replace("anchor: [chosen]", f"anchor: [{anchor}]"))


def test_domain_counts_split_members_from_attached(corpus_and_vault):
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/glm")
    write_node(root, "b")
    assert by_domain(load_corpus(root)) == [("stats", 2, 1)]


def test_by_domain_sorts_by_member_count_descending_then_by_name(corpus_and_vault):
    """The sort order is a stated requirement, and a fixture with a single
    row, as above, cannot tell a broken tie break from a correct one. Credit
    leads on two members; ml and gi tie on one each, so a name-ascending
    break has to put gi before ml."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    write_node(root, "b")
    write_node(root, "c")
    write_node(root, "d")
    _set_domains(root, "a", "credit")
    _set_domains(root, "b", "credit")
    _set_domains(root, "c", "ml")
    _set_domains(root, "d", "gi")
    rows = by_domain(load_corpus(root))
    assert [row[0] for row in rows] == ["credit", "gi", "ml"]


def test_anchor_documents_group_on_body_and_subject(corpus_and_vault):
    """The ledger bound rests on this grouping: 59 documents across the whole
    corpus, so an uncovered node's entry names one of 59 rather than a new one."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    _set_anchor(root, "a", "ifoa.cs2.1.1-5")
    rows = by_anchor_document(load_corpus(root))
    assert ("ifoa.cs2", 1, 0) in rows


def test_anchor_documents_dedupe_two_anchors_under_one_document(corpus_and_vault):
    """A node citing two paragraphs of the same syllabus is one member of
    that document, not two: each anchor document's member count has to
    match the node count Mario reads it as."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    _set_anchor(root, "a", "ifoa.cp1.3.1-1, ifoa.cp1.3.1-2")
    rows = by_anchor_document(load_corpus(root))
    assert ("ifoa.cp1", 1, 0) in rows


def test_the_histogram_counts_nodes_per_attachment_count(corpus_and_vault):
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/glm")
    write_node(root, "b", "methods/glm, methods/paid")
    write_node(root, "c")
    assert attachment_histogram(load_corpus(root)) == {0: 1, 1: 1, 2: 1}


def test_the_report_names_the_index_build_date(corpus_and_vault):
    """A stale index is what makes an attachment wrong, so the report has to
    say which index produced it."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    report = render_report(load_corpus(root), "2026-09-10")
    assert "2026-09-10" in report
    assert "Coverage by domain" in report


def test_the_report_says_plainly_when_no_index_was_present(corpus_and_vault):
    """A missing index must not stop the report generating, since the
    coverage figures come from the corpus rather than the index."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    report = render_report(load_corpus(root), NO_INDEX)
    assert "No vault index was present" in report


def test_the_report_drops_the_hardest_claim_but_keeps_the_pretoria_grouping(corpus_and_vault):
    """The Pretoria course codes are a neutral grouping the report keeps,
    not a claim about where acquisition is hardest: that claim rested on a
    since-corrected count and must not appear."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    _set_anchor(root, "a", "up.wtw211.2.1")
    report = render_report(load_corpus(root), "2026-09-10")
    assert "hardest" not in report
    assert "University of Pretoria" in report
    assert "sources/syllabi.yaml" in report


def test_index_built_reports_no_index_when_the_file_is_absent(tmp_path):
    """`build_coverage_report.py` must not stop the report generating just
    because no index has ever been built."""
    assert _index_built(tmp_path / "vault-index.yaml") == NO_INDEX


def test_index_built_reports_no_index_when_the_built_key_is_absent(tmp_path):
    """An index file that exists but carries no `built` field is as
    unusable as no file at all, so it has to fall back the same way."""
    path = tmp_path / "vault-index.yaml"
    path.write_text("articles: []\n")
    assert _index_built(path) == NO_INDEX
