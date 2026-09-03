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
    c = corpus([node("a", ["b"]), node("b", ["a"])])
    result = check_requires_resolve_and_acyclic(c)
    assert result.failures and "cycle" in result.failures[0]


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
    c = corpus(
        [node("a"), node("b", ["a"]), node("c", ["b"])],
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


def test_a_path_naming_an_unknown_node_fails():
    c = corpus([node("a")], [TeachingPath("p", "P", (), "", ("a", "ghost"))])
    result = check_path_teachability(c)
    assert any("ghost" in f for f in result.failures)
