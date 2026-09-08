from pathlib import Path

from scripts.rename_anchor_prefix import rename_in_anchor_line, rename_manifest, rename_nodes

NODE = """---
id: {id}
title: A node
domains: [stats]
status: stub
requires: []
spends: []
anchor: [{anchors}]
vault_articles: []
vault_sources: []
taught_in: null
---

A body that mentions eth.dl-actuarial-2026.l01 in prose and must keep it.
"""


def write(nodes: Path, node_id: str, anchors: str) -> Path:
    path = nodes / f"{node_id}.md"
    path.write_text(NODE.format(id=node_id, anchors=anchors))
    return path


def test_the_anchor_line_is_renamed_and_the_body_is_not(tmp_path):
    nodes = tmp_path / "nodes"
    nodes.mkdir()
    path = write(nodes, "a", "eth.dl-actuarial-2026.l01, ifoa.cs2.4.6-2")
    touched = rename_nodes(nodes, "eth.dl-actuarial-2026", "ucsc.dl-actuarial-2026")
    text = path.read_text()
    assert touched == [path]
    assert "anchor: [ucsc.dl-actuarial-2026.l01, ifoa.cs2.4.6-2]" in text
    assert "mentions eth.dl-actuarial-2026.l01 in prose" in text


def test_a_longer_prefix_sharing_the_stem_is_left_alone(tmp_path):
    nodes = tmp_path / "nodes"
    nodes.mkdir()
    path = write(nodes, "b", "eth.dl-actuarial-2026-extra.l01")
    touched = rename_nodes(nodes, "eth.dl-actuarial-2026", "ucsc.dl-actuarial-2026")
    assert touched == []
    assert "eth.dl-actuarial-2026-extra.l01" in path.read_text()


def test_an_untouched_file_is_not_rewritten(tmp_path):
    nodes = tmp_path / "nodes"
    nodes.mkdir()
    path = write(nodes, "c", "ifoa.cs2.4.6-2")
    before = path.stat().st_mtime_ns
    assert rename_nodes(nodes, "eth.dl-actuarial-2026", "ucsc.dl-actuarial-2026") == []
    assert path.stat().st_mtime_ns == before


def test_the_manifest_prefix_and_its_dotted_uses_are_renamed(tmp_path):
    manifest = tmp_path / "syllabi.yaml"
    manifest.write_text(
        "- id: eth-dl-actuarial-2026\n  anchor_prefix: eth.dl-actuarial-2026\n"
        "  licence_note: 'Anchors run eth.dl-actuarial-2026.l01 through .l12.'\n"
    )
    assert rename_manifest(manifest, "eth.dl-actuarial-2026", "ucsc.dl-actuarial-2026")
    text = manifest.read_text()
    assert "anchor_prefix: ucsc.dl-actuarial-2026\n" in text
    assert "ucsc.dl-actuarial-2026.l01 through" in text
    assert "id: eth-dl-actuarial-2026" in text, "the manifest id is a staging key and stays"


def test_rename_in_anchor_line_is_a_pure_function():
    text = "anchor: [eth.dl-actuarial-2026.l04]\n"
    assert rename_in_anchor_line(text, "eth.dl-actuarial-2026", "ucsc.dl-actuarial-2026") == "anchor: [ucsc.dl-actuarial-2026.l04]\n"
