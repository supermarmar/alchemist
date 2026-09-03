import subprocess
import sys
from pathlib import Path

from scripts.alchemist.model import (
    Alias, Corpus, MathObject, Node, Objects, Spend, TeachingPath,
)
from scripts.alchemist.site import (
    render_domain_dot, render_index, render_node_page, render_path_page,
)

REPO = Path(__file__).resolve().parents[1]


def node(node_id: str, requires=(), domains=("stats",), taught_in=None) -> Node:
    return Node(
        id=node_id, title=node_id.replace("-", " ").capitalize(), domains=domains,
        status="stub", requires=tuple(requires), spends=(), anchor=(),
        vault_articles=(), vault_sources=(), taught_in=taught_in, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def test_the_index_lists_every_path_and_counts_the_nodes():
    """The corpus holds three nodes while the path lists two, so the per-path count
    and the summary total are different strings. With them equal, deleting the
    per-path count entirely still passes, because the summary sentence supplies
    the same text. The third node also covers the "taught in full" figure, which
    otherwise has no test at all."""
    corpus = Corpus(
        {
            "a": node("a"),
            "b": node("b", ["a"]),
            "c": node("c", taught_in="S1_credit-survival-bridge"),
        },
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_index(corpus)
    assert "A path" in out
    assert "2 nodes" in out                      # the path's own count
    assert "3 nodes" in out                      # the corpus summary
    assert "1 of them taught in full" in out


def test_one_node_and_one_path_read_as_singular():
    corpus = Corpus(
        {"a": node("a")}, {"p": TeachingPath("p", "P", (), "", ("a",))}
    )
    out = render_index(corpus)
    assert "1 node," in out and "1 nodes" not in out
    assert "1 path." in out and "1 paths" not in out


def test_a_path_page_lists_its_nodes_in_order_and_marks_the_taught_ones():
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge"), "b": node("b", ["a"])},
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_path_page(corpus.paths["p"], corpus)
    assert out.index("../nodes/a.html") < out.index("../nodes/b.html")
    assert "S1_credit-survival-bridge" in out


def test_a_node_page_carries_the_body_the_aliases_and_what_it_unlocks():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("life", r"\mu_x", "force of mortality"),
                 Alias("credit", "h(t)", "default hazard")),
    )
    root = Node(
        id="survival-function", title="Survival function", domains=("life", "credit"),
        status="drafted", requires=(), spends=(Spend("obj.hazard", "life"),
                                              Spend("obj.hazard", "credit")),
        anchor=(), vault_articles=("methods/deep-learning-credit-scoring",),
        vault_sources=(), taught_in=None, body="## Definition\n\nThe probability of no event.\n",
        path=Path("nodes/survival-function.md"),
    )
    corpus = Corpus({"survival-function": root, "hazard-rate": node("hazard-rate", ["survival-function"])}, {})
    out = render_node_page(root, corpus, Objects({"obj.hazard": hazard}))
    assert "The probability of no event." in out
    assert "force of mortality" in out and "default hazard" in out
    assert "hazard-rate" in out
    assert "methods/deep-learning-credit-scoring" in out


def test_a_node_page_omits_the_alias_table_where_one_domain_is_spent():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("credit", "h(t)", "default hazard"),),
    )
    only = Node(
        id="a", title="A", domains=("credit",), status="stub", requires=(),
        spends=(Spend("obj.hazard", "credit"),), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="x\n", path=Path("nodes/a.md"),
    )
    out = render_node_page(only, Corpus({"a": only}, {}), Objects({"obj.hazard": hazard}))
    assert "Called in each domain" not in out


def test_the_dot_graph_carries_one_edge_per_prerequisite():
    corpus = Corpus({"a": node("a"), "b": node("b", ["a"])}, {})
    dot = render_domain_dot(corpus, "stats")
    assert '"a" -> "b"' in dot and dot.startswith("digraph")


def test_the_dot_graph_excludes_other_domains():
    corpus = Corpus(
        {"a": node("a", domains=("life",)), "b": node("b", ["a"], domains=("stats",))},
        {},
    )
    dot = render_domain_dot(corpus, "stats")
    assert '"b"' in dot and '"a" -> "b"' not in dot


def test_author_supplied_text_is_escaped():
    """"PD < 1%" is ordinary prose in this corpus and the repo is public, so an
    unescaped title corrupts the page the first time real content lands."""
    corpus = Corpus(
        {"a": node("a")},
        {"p": TeachingPath("p", "PD < 1% & rising", (), "See <b>this</b>.", ("a",))},
    )
    index = render_index(corpus)
    page = render_path_page(corpus.paths["p"], corpus)
    assert "PD &lt; 1% &amp; rising" in index
    assert "PD < 1% & rising" not in index
    assert "&lt;b&gt;this&lt;/b&gt;" in page
    assert "<b>this</b>" not in page


def test_a_quote_in_a_title_does_not_break_the_dot_label():
    """A DOT label is a quoted string, so an unescaped double quote ends the
    label early and `dot` fails on the rest of the line."""
    quoted = Node(
        id="a", title='The "ultimate" claim', domains=("stats",), status="stub",
        requires=(), spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="", path=Path("nodes/a.md"),
    )
    dot = render_domain_dot(Corpus({"a": quoted}, {}), "stats")
    assert '\\"ultimate\\"' in dot


def test_pages_below_site_reach_the_repo_root():
    """A page in site/paths/ is two levels below the root, so ../assets/ would
    resolve to site/assets/, which nothing ever creates."""
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge")},
        {"p": TeachingPath("p", "P", (), "", ("a",))},
    )
    page = render_path_page(corpus.paths["p"], corpus)
    assert "../../assets/lecture.css" in page
    assert "../../lectures/S1_credit-survival-bridge.html" in page


def test_check_py_exits_zero_on_the_real_repo():
    done = subprocess.run(
        [sys.executable, "scripts/check.py"], cwd=REPO, capture_output=True, text=True
    )
    assert done.returncode == 0, done.stdout + done.stderr


def test_check_py_exits_non_zero_when_a_rule_fails(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "paths").mkdir()
    (tmp_path / "notation").mkdir()
    (tmp_path / "nodes" / "b.md").write_text(
        "---\nid: b\ntitle: B\ndomains: [stats]\nstatus: stub\nrequires: [ghost]\n---\n\nx\n"
    )
    (tmp_path / "notation" / "objects.yaml").write_text("[]\n")
    (tmp_path / "notation" / "symbols.md").write_text("wrong\n")
    done = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "check.py"), "--root", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert done.returncode == 1 and "ghost" in done.stdout
