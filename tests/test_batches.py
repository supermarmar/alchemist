from pathlib import Path

import pytest
import yaml

from scripts.alchemist.batches import depth_key, manifest_payload, phase_node_ids, requires_depth, slice_batches, stray_writes, wave_of
from scripts.alchemist.model import Node


def test_the_corpus_slices_into_thirty_nine_batches_of_forty():
    ids = [f"n{i:04d}" for i in range(1560)]
    batches = slice_batches(ids)
    assert len(batches) == 39
    assert all(len(b) == 40 for b in batches)
    assert batches[0][0] == "n0000"
    assert batches[38][-1] == "n1559"
    assert [i for b in batches for i in b] == ids


def test_a_short_final_batch_is_kept_rather_than_padded():
    assert [len(b) for b in slice_batches([f"n{i}" for i in range(85)])] == [40, 40, 5]


def test_batches_map_to_three_waves_of_thirteen():
    """Thirty-nine agents exceed the fifteen-agent guideline, so the batches
    run in waves. Spec section 10 said forty per agent fits inside the cap,
    which it does not; three waves of thirteen is what does."""
    assert wave_of(1) == 1
    assert wave_of(13) == 1
    assert wave_of(14) == 2
    assert wave_of(26) == 2
    assert wave_of(27) == 3
    assert wave_of(39) == 3


# stray_writes reads a batch as {"wave": ..., "nodes": [...]}, the shape
# manifest_payload actually produces, not a bare list of ids.
MANIFEST = {"batches": {1: {"wave": 1, "nodes": ["a", "b"]}, 2: {"wave": 1, "nodes": ["c"]}}}


def test_stray_writes_reports_nothing_for_a_clean_batch():
    assert stray_writes(MANIFEST, 1, ["a", "b"]) == []


def test_stray_writes_reports_a_node_from_another_batch():
    assert stray_writes(MANIFEST, 1, ["a", "c"]) == ["c"]


def test_stray_writes_reports_a_node_owned_by_no_batch():
    """A changed id absent from every batch, not merely from this one, must
    still surface: stray_writes checks disjointness against the whole
    manifest, not just against the batch under test."""
    assert stray_writes(MANIFEST, 1, ["a", "zz"]) == ["zz"]


def test_stray_writes_names_the_unknown_batch_and_the_range_it_holds():
    """Thirty-nine agents are about to run on this. An operator who mistypes a
    batch number needs to be told what went wrong, not handed a bare
    KeyError with no way to tell a typo from a real defect."""
    with pytest.raises(KeyError, match=r"batch 5 is not in the manifest, which holds batches 1 to 2"):
        stray_writes(MANIFEST, 5, ["a"])


def test_stray_writes_reads_the_shape_manifest_payload_writes():
    """A round trip through yaml.safe_dump/safe_load, on manifest_payload's
    own output, because stray_writes and the manifest writer must agree on
    the manifest's shape or the verifier reads every honest write as a stray
    one. This is the test that would have caught batches nested one level
    too shallow."""
    payload = manifest_payload([f"n{i:02d}" for i in range(45)])
    manifest = yaml.safe_load(yaml.safe_dump(payload))
    assert stray_writes(manifest, 1, ["n00"]) == []
    assert stray_writes(manifest, 1, ["n40"]) == ["n40"]  # owned by batch 2


def node(node_id, requires=(), status="stub"):
    return Node(
        id=node_id, title=node_id, domains=("stats",), status=status, requires=tuple(requires),
        spends=(), anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def test_requires_depth_is_the_longest_chain_beneath_a_node():
    nodes = {"a": node("a"), "b": node("b", ["a"]), "c": node("c", ["a", "b"]), "d": node("d")}
    assert requires_depth(nodes) == {"a": 0, "b": 1, "c": 2, "d": 0}


def test_the_depth_key_orders_by_depth_then_id():
    """Roots first, alphabetical within a depth, so a prerequisite lands in an
    earlier wave than its dependents more often than the alphabetical order
    Phase 2 used: 456 against 232 of the 1,107 non-root nodes, measured on
    19 September 2026."""
    nodes = {"z": node("z"), "a": node("a", ["z"]), "m": node("m"), "b": node("b", ["a"])}
    assert slice_batches(list(nodes), key=depth_key(nodes)) == [["m", "z", "a", "b"]]


def test_slice_batches_still_sorts_alphabetically_without_a_key():
    assert slice_batches(["b", "a"], size=1) == [["a"], ["b"]]


def test_manifest_payload_passes_the_key_through():
    nodes = {"z": node("z"), "a": node("a", ["z"])}
    payload = manifest_payload(list(nodes), size=1, key=depth_key(nodes))
    assert payload["batches"][1]["nodes"] == ["z"]
    assert payload["batches"][2]["nodes"] == ["a"]


def test_phase_3_batches_only_the_stubs_and_phase_2_batches_everything():
    nodes = {"a": node("a"), "b": node("b", status="drafted"), "c": node("c", status="reviewed")}
    assert phase_node_ids(nodes, 3) == ["a"]
    assert phase_node_ids(nodes, 2) == ["a", "b", "c"]
