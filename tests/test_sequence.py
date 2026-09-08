from pathlib import Path

from scripts.alchemist.model import Corpus, Node, TeachingPath
from scripts.alchemist.sequence import mechanical_order, rewrite_nodes


def node(node_id: str, requires=()) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("stats",), status="stub",
        requires=tuple(requires), spends=(), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="", path=Path(f"nodes/{node_id}.md"),
    )


def path(*nodes: str) -> TeachingPath:
    return TeachingPath(id="p", title="P", builds_on=(), preamble="", nodes=nodes)


def test_tier_first_then_id():
    """a and c are roots, b needs a. Id order alone would give a, b, c."""
    corpus = Corpus({n.id: n for n in (node("a"), node("b", ["a"]), node("c"))}, {})
    assert mechanical_order(path("c", "b", "a"), corpus) == ("a", "c", "b")


def test_a_prerequisite_outside_the_path_does_not_raise_the_tier():
    """a needs z, which is outside the path, so a stays at tier 0 and sorts
    before b on id. Counting the outside prerequisite would lift a to tier 1
    and put b first, which is the bug this test exists to catch."""
    corpus = Corpus({n.id: n for n in (node("a", ["z"]), node("b"), node("z"))}, {})
    assert mechanical_order(path("b", "a"), corpus) == ("a", "b")


def test_a_chain_climbs_one_tier_per_link():
    corpus = Corpus({n.id: n for n in (node("a"), node("b", ["a"]), node("c", ["b"]), node("d", ["a"]))}, {})
    assert mechanical_order(path("d", "c", "b", "a"), corpus) == ("a", "b", "d", "c")


def test_rewrite_nodes_touches_only_the_nodes_block():
    text = "id: p\ntitle: P\nbuilds_on: []\npreamble: >\n  Two lines\n  wrapped so.\nnodes:\n- b\n- a\n"
    out = rewrite_nodes(text, ["a", "b"])
    assert out == "id: p\ntitle: P\nbuilds_on: []\npreamble: >\n  Two lines\n  wrapped so.\nnodes:\n- a\n- b\n"


def test_rewrite_nodes_refuses_a_file_without_a_nodes_block():
    import pytest
    with pytest.raises(ValueError):
        rewrite_nodes("id: p\ntitle: P\n", ["a"])


def test_rewrite_nodes_refuses_a_comment_inside_the_block():
    import pytest
    with pytest.raises(ValueError):
        rewrite_nodes("id: p\nnodes:\n# a comment\n- a\n- b\n", ["b", "a"])


def test_rewrite_nodes_refuses_text_after_the_block():
    import pytest
    with pytest.raises(ValueError):
        rewrite_nodes("id: p\nnodes:\n- a\n- b\ntitle: P\n", ["b", "a"])
