import yaml

from scripts.alchemist.batches import manifest_payload, slice_batches, stray_writes, wave_of


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
