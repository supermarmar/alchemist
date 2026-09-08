import subprocess
import sys
from pathlib import Path

import pytest

from scripts.alchemist.model import Corpus, Node, TeachingPath
from scripts.alchemist.sequence import mechanical_order, rewrite_nodes

REPO = Path(__file__).resolve().parents[1]

# Frontmatter shape copied from tests/test_merges.py's NODE template, trimmed to
# the fields sequence_path.py's fixture needs: a slug id, a domain, a status and
# an optional requires list.
NODE = """---
id: {id}
title: {title}
domains: [stats]
status: stub
requires: [{requires}]
spends: []
anchor: [chosen]
vault_articles: []
vault_sources: []
taught_in: null
---

A body.
"""


def write_node(nodes_dir: Path, node_id: str, requires: str = "") -> None:
    (nodes_dir / f"{node_id}.md").write_text(NODE.format(id=node_id, title=node_id, requires=requires))


def write_path_file(paths_dir: Path, path_id: str, nodes: list[str]) -> None:
    text = (
        f"id: {path_id}\ntitle: {path_id}\nbuilds_on: []\npreamble: >\n  A path.\nnodes:\n"
        + "".join(f"- {n}\n" for n in nodes)
    )
    (paths_dir / f"{path_id}.yaml").write_text(text)


@pytest.fixture
def sequenced_root(tmp_path):
    """A tmp corpus for the CLI subprocess tests, so a regressed guard rewrites a
    throwaway file rather than the real `paths/credit-trunk.yaml`."""
    nodes_dir, paths_dir = tmp_path / "nodes", tmp_path / "paths"
    nodes_dir.mkdir()
    paths_dir.mkdir()
    write_node(nodes_dir, "a")
    write_node(nodes_dir, "b", requires="a")
    write_path_file(paths_dir, "credit-trunk", ["b", "a"])  # out of mechanical order
    write_path_file(paths_dir, "life", ["a", "b"])          # already in mechanical order
    return tmp_path


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


def test_a_cycle_inside_the_path_is_named():
    """a requires b and b requires a, so no tier can settle for either."""
    import pytest
    corpus = Corpus({n.id: n for n in (node("a", ["b"]), node("b", ["a"]))}, {})
    with pytest.raises(ValueError, match="cycle inside") as excinfo:
        mechanical_order(path("a", "b"), corpus)
    assert "a" in str(excinfo.value) and "b" in str(excinfo.value)


def test_sequence_path_refuses_a_hand_ordered_path_without_force(sequenced_root):
    target = sequenced_root / "paths" / "credit-trunk.yaml"
    before = target.read_bytes()
    done = subprocess.run(
        [sys.executable, "scripts/sequence_path.py", "--root", str(sequenced_root), "credit-trunk"],
        cwd=REPO, capture_output=True, text=True,
    )
    assert done.returncode == 2
    assert "ordered by hand" in done.stderr
    assert target.read_bytes() == before


def test_sequence_path_force_rewrites_a_hand_ordered_path(sequenced_root):
    target = sequenced_root / "paths" / "credit-trunk.yaml"
    done = subprocess.run(
        [sys.executable, "scripts/sequence_path.py", "--root", str(sequenced_root), "--force", "credit-trunk"],
        cwd=REPO, capture_output=True, text=True,
    )
    assert done.returncode == 0
    assert "credit-trunk: rewritten" in done.stdout
    assert target.read_text().endswith("nodes:\n- a\n- b\n")


def test_sequence_path_check_is_allowed_on_a_hand_ordered_path(sequenced_root):
    target = sequenced_root / "paths" / "credit-trunk.yaml"
    before = target.read_bytes()
    done = subprocess.run(
        [sys.executable, "scripts/sequence_path.py", "--root", str(sequenced_root), "--check", "credit-trunk"],
        cwd=REPO, capture_output=True, text=True,
    )
    assert done.returncode == 1
    assert "out of mechanical order" in done.stdout
    assert done.stderr == ""
    assert target.read_bytes() == before


def test_sequence_path_names_an_unknown_path(sequenced_root):
    credit_before = (sequenced_root / "paths" / "credit-trunk.yaml").read_bytes()
    life_before = (sequenced_root / "paths" / "life.yaml").read_bytes()
    done = subprocess.run(
        [sys.executable, "scripts/sequence_path.py", "--root", str(sequenced_root), "no-such-path"],
        cwd=REPO, capture_output=True, text=True,
    )
    assert done.returncode == 2
    assert "no such path" in done.stderr
    assert (sequenced_root / "paths" / "credit-trunk.yaml").read_bytes() == credit_before
    assert (sequenced_root / "paths" / "life.yaml").read_bytes() == life_before
