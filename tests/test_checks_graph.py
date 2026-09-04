# tests/test_checks_graph.py
from pathlib import Path

from scripts.alchemist.checks import (
    check_path_teachability,
    check_requires_resolve_and_acyclic,
)
from scripts.alchemist.model import Corpus, Node, TeachingPath


def node(node_id: str, requires=()) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("stats",), status="stub",
        requires=tuple(requires), spends=(), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="", path=Path(f"nodes/{node_id}.md"),
    )


def corpus(nodes, paths=()) -> Corpus:
    return Corpus({n.id: n for n in nodes}, {p.id: p for p in paths})


def test_a_resolvable_acyclic_graph_passes():
    c = corpus([node("a"), node("b", ["a"])])
    assert check_requires_resolve_and_acyclic(c).failures == []


def test_a_dangling_prerequisite_fails():
    result = check_requires_resolve_and_acyclic(corpus([node("b", ["ghost"])]))
    assert len(result.failures) == 1 and "ghost" in result.failures[0]


def test_a_cycle_fails_and_names_its_members():
    """Asserts the trail rather than the word "cycle". A message reading only
    "cycle" is useless in a 600-node graph, and the old assertion passed against
    exactly that. The DFS enters from the sorted ids, so `a` is the entry point
    and the trail closes back on it.
    """
    c = corpus([node("a", ["b"]), node("b", ["a"])])
    result = check_requires_resolve_and_acyclic(c)
    assert result.failures == ["cycle: a -> b -> a"]


def test_a_self_loop_fails():
    result = check_requires_resolve_and_acyclic(corpus([node("a", ["a"])]))
    assert result.failures and "cycle" in result.failures[0]


def test_a_path_with_prerequisites_in_order_passes():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [TeachingPath("p", "P", (), "", ("a", "b"))],
    )
    assert check_path_teachability(c).failures == []


def test_a_path_with_a_prerequisite_later_fails():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [TeachingPath("p", "P", (), "", ("b", "a"))],
    )
    result = check_path_teachability(c)
    assert len(result.failures) == 1 and "before" in result.failures[0]


def test_builds_on_supplies_the_prerequisite():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [
            TeachingPath("base", "Base", (), "", ("a",)),
            TeachingPath("p", "P", ("base",), "", ("b",)),
        ],
    )
    assert check_path_teachability(c).failures == []


def test_builds_on_is_transitive():
    """`c` requires the grandparent's node as well as the parent's, so this passes
    only if the closure walks the whole chain. A one-level implementation supplies
    {"b"} alone and fails on "a"."""
    c = corpus(
        [node("a"), node("b", ["a"]), node("c", ["a", "b"])],
        [
            TeachingPath("one", "One", (), "", ("a",)),
            TeachingPath("two", "Two", ("one",), "", ("b",)),
            TeachingPath("three", "Three", ("two",), "", ("c",)),
        ],
    )
    assert check_path_teachability(c).failures == []


def test_a_builds_on_cycle_is_reported_rather_than_hanging():
    c = corpus(
        [node("a")],
        [
            TeachingPath("one", "One", ("two",), "", ("a",)),
            TeachingPath("two", "Two", ("one",), "", ()),
        ],
    )
    result = check_path_teachability(c)
    assert result.failures and "builds_on cycle" in result.failures[0]


def test_a_builds_on_cycle_between_other_paths_terminates():
    """Covers the `seen` guard, which the two-path cycle test above never reaches:
    there the cycle returns early on `nxt == path_id`. Here `x` sits outside the
    cycle, so only `seen` stops the frontier revisiting `two` forever. Dropping the
    guard makes this test hang rather than fail, which is the honest cost of
    testing termination without adding a timeout dependency."""
    c = corpus(
        [node("a")],
        [
            TeachingPath("x", "X", ("two",), "", ("a",)),
            TeachingPath("two", "Two", ("three",), "", ()),
            TeachingPath("three", "Three", ("two",), "", ()),
        ],
    )
    result = check_path_teachability(c)
    cycles = [f for f in result.failures if "builds_on cycle" in f]
    assert len(cycles) == 2
    assert not any(f.startswith("x:") for f in cycles)


def test_a_path_naming_an_unknown_node_fails():
    c = corpus([node("a")], [TeachingPath("p", "P", (), "", ("a", "ghost"))])
    result = check_path_teachability(c)
    assert any("ghost" in f for f in result.failures)
