from pathlib import Path

import pytest

from scripts.alchemist.merges import (
    ledger_names,
    merge_pair,
    merged_record,
    repoint_path,
    repoint_requires,
)
from scripts.alchemist.model import parse_node, parse_path

NODE = """---
id: {id}
title: {title}
domains: [{domains}]
status: {status}
requires: [{requires}]
spends: {spends}
anchor: [{anchor}]
vault_articles: []
vault_sources: []
taught_in: {taught_in}
---

{body}
"""


def write_node(
    nodes: Path, node_id: str, *, title=None, domains="stats", requires="",
    anchor="chosen", body="A body.", status="stub", spends="[]", taught_in="null",
) -> Path:
    path = nodes / f"{node_id}.md"
    path.write_text(NODE.format(
        id=node_id, title=title or node_id, domains=domains, requires=requires,
        anchor=anchor, body=body, status=status, spends=spends, taught_in=taught_in,
    ))
    return path


def write_path(paths: Path, path_id: str, nodes: list[str]) -> Path:
    path = paths / f"{path_id}.yaml"
    path.write_text(f"id: {path_id}\ntitle: {path_id}\nbuilds_on: []\npreamble: >\n  A path.\nnodes:\n" + "".join(f"- {n}\n" for n in nodes))
    return path


@pytest.fixture
def repo(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "paths").mkdir()
    (tmp_path / "sources").mkdir()
    nodes, paths = tmp_path / "nodes", tmp_path / "paths"
    write_node(nodes, "a", title="A survives", domains="stats", requires="", anchor="ifoa.cs1.1.1", body="The survivor's body.")
    write_node(nodes, "b", title="B is absorbed", domains="credit", requires="a, z", anchor="assa.f107.2.2", body="The absorbed body.")
    write_node(nodes, "c", requires="b, a")
    write_node(nodes, "z")
    write_path(paths, "both", ["a", "b", "c"])
    write_path(paths, "only-b", ["z", "b", "c"])
    (tmp_path / "sources" / "wanted.yaml").write_text("- id: src\n  needed_by: [c]\n  status: wanted\n")
    return tmp_path


def test_the_survivor_keeps_its_identity_and_gains_the_union(repo):
    merge_pair(repo, "b", "a")
    a = parse_node(repo / "nodes" / "a.md")
    assert a.title == "A survives" and a.body.strip() == "The survivor's body."
    assert a.domains == ("credit", "stats")
    assert a.anchor == ("assa.f107.2.2", "ifoa.cs1.1.1")


def test_the_edge_between_the_pair_is_dropped_and_the_rest_kept(repo):
    merge_pair(repo, "b", "a")
    assert parse_node(repo / "nodes" / "a.md").requires == ("z",)


def test_the_absorbed_file_is_deleted(repo):
    merge_pair(repo, "b", "a")
    assert not (repo / "nodes" / "b.md").exists()


def test_a_referrer_is_repointed_and_deduplicated(repo):
    merge_pair(repo, "b", "a")
    assert parse_node(repo / "nodes" / "c.md").requires == ("a",)


def test_a_path_holding_both_drops_the_absorbed_line(repo):
    merge_pair(repo, "b", "a")
    assert parse_path(repo / "paths" / "both.yaml").nodes == ("a", "c")


def test_a_path_holding_only_the_absorbed_id_gets_the_survivor_in_place(repo):
    merge_pair(repo, "b", "a")
    assert parse_path(repo / "paths" / "only-b.yaml").nodes == ("z", "a", "c")


def test_a_ledger_naming_the_absorbed_id_stops_the_merge(repo):
    (repo / "sources" / "wanted.yaml").write_text("- id: src\n  needed_by: [b]\n  status: wanted\n")
    with pytest.raises(ValueError, match="wanted.yaml"):
        merge_pair(repo, "b", "a")
    assert (repo / "nodes" / "b.md").exists(), "a refused merge changes nothing"


def test_merged_record_is_pure(repo):
    a = parse_node(repo / "nodes" / "a.md")
    b = parse_node(repo / "nodes" / "b.md")
    merged = merged_record(a, b)
    assert merged.id == "a" and merged.requires == ("z",) and merged.status == "stub"


def test_repoint_requires_leaves_an_unrelated_line_untouched():
    text = "requires: [x, y]\n"
    assert repoint_requires(text, "b", "a", "c") == text


def test_repoint_path_leaves_an_unrelated_file_untouched():
    text = "nodes:\n- x\n- y\n"
    assert repoint_path(text, "b", "a") == text


def test_a_path_listing_the_absorbed_id_twice_gets_one_survivor_line():
    text = "nodes:\n- z\n- b\n- c\n- b\n"
    assert repoint_path(text, "b", "a") == "nodes:\n- z\n- a\n- c\n"


def test_ledger_names_reads_needed_by_only(tmp_path):
    ledger = tmp_path / "wanted.yaml"
    ledger.write_text("- id: b-paper\n  needed_by: [c]\n  claim: mentions b in prose\n")
    assert ledger_names(ledger, "b") is False
    assert ledger_names(ledger, "c") is True


def test_a_node_cannot_absorb_itself(repo):
    with pytest.raises(ValueError, match="cannot absorb itself"):
        merge_pair(repo, "a", "a")
    assert (repo / "nodes" / "a.md").exists()


def test_a_missing_survivor_names_the_pair(repo):
    with pytest.raises(ValueError) as excinfo:
        merge_pair(repo, "b", "ghost")
    assert "b" in str(excinfo.value) and "ghost" in str(excinfo.value)


def test_a_taught_record_is_not_absorbed(repo):
    write_node(repo / "nodes", "d", taught_in="S1_some-lecture")
    with pytest.raises(ValueError, match="taught_in"):
        merge_pair(repo, "d", "a")
    assert (repo / "nodes" / "d.md").exists()
    assert (repo / "nodes" / "a.md").exists()


def test_a_record_with_spends_is_not_absorbed(repo):
    write_node(repo / "nodes", "e", spends="[{object: obj.hazard, domain: credit}]")
    with pytest.raises(ValueError, match="spends"):
        merge_pair(repo, "e", "a")
    assert (repo / "nodes" / "e.md").exists()
    assert (repo / "nodes" / "a.md").exists()


def test_a_longer_absorbed_body_prints_a_note(repo, capsys):
    write_node(repo / "nodes", "f", body="word " * 50)
    merge_pair(repo, "f", "a")
    assert "note:" in capsys.readouterr().err


def test_a_drafted_record_is_not_absorbed(repo):
    """The status arm on its own. The taught_in and spends arms have their own
    tests, so this one carries no taught_in and no spends and still refuses."""
    write_node(repo / "nodes", "d", status="drafted")
    with pytest.raises(ValueError, match="carries status"):
        merge_pair(repo, "d", "a")
    assert (repo / "nodes" / "d.md").exists()


def test_a_missing_absorbed_file_names_the_pair(repo):
    """The loop checks the absorbed file first, so its arm is reached only by an
    absorbed id with no file. test_a_missing_survivor_names_the_pair covers the
    other half of the same loop."""
    with pytest.raises(ValueError, match="no such node ghost"):
        merge_pair(repo, "ghost", "a")
