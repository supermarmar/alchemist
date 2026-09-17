import difflib

import yaml

from scripts.alchemist.ledger import (
    ledger_paths,
    partition_by_status,
    read_fragments,
    union_entries,
)
from scripts.merge_ledger import FLOW_LIST_MAX_ITEMS, LedgerDumper

ENTRY = {
    "id": "ifoa-cs2-core-reading-2026",
    "needed_by": ["hazard-rate"],
    "claim": "The standard treatment of the hazard function.",
    "document": "IFoA CS2 Core Reading, 2026",
    "expected_tier": "T4",
    "acquisition": "purchased-personal",
    "status": "wanted",
}


def fragment(staging, number, entries):
    staging.mkdir(parents=True, exist_ok=True)
    path = staging / f"ledger-{number:02d}.yaml"
    path.write_text(yaml.safe_dump(entries, sort_keys=False))
    return path


def test_two_fragments_naming_one_document_union_their_needed_by(tmp_path):
    a = dict(ENTRY, needed_by=["hazard-rate"])
    b = dict(ENTRY, needed_by=["survival-function", "hazard-rate"])
    merged, complaints = union_entries([], [a, b])
    assert complaints == []
    assert len(merged) == 1
    assert merged[0]["needed_by"] == ["hazard-rate", "survival-function"]


def test_a_seeded_entry_is_preserved_and_only_extended(tmp_path):
    """The four Phase 1 entries keep every field. A fragment naming one of
    them adds node ids and changes nothing else."""
    seeded = dict(ENTRY, claim="The seeded claim.", note="Keep me.")
    proposed = dict(ENTRY, needed_by=["new-node"], claim="A different claim.")
    merged, complaints = union_entries([seeded], [proposed])
    assert merged[0]["claim"] == "The seeded claim."
    assert merged[0]["note"] == "Keep me."
    assert merged[0]["needed_by"] == ["hazard-rate", "new-node"]
    assert any("claim" in c for c in complaints)


def test_notes_on_one_id_accumulate_rather_than_dropping(tmp_path):
    """Each batch's note says which chapters of a shared document its own
    nodes need, and acquisition is decided off the merged ledger, so keeping
    the first note and dropping the rest would lose the reasoning where it is
    read."""
    seeded = dict(ENTRY, note="The survival-analysis chapters.\n")
    first = dict(ENTRY, needed_by=["arima"], note="The time series chapters.\n")
    second = dict(ENTRY, needed_by=["f1-score"], note="The classifier metrics.\n")
    merged, complaints = union_entries([seeded], [first, second])
    assert merged[0]["note"] == (
        "The survival-analysis chapters.\n\n"
        "The time series chapters.\n\n"
        "The classifier metrics.\n"
    )
    assert not any("note" in c for c in complaints)


def test_an_identical_note_is_not_repeated(tmp_path):
    repeated = "The same reasoning, reached twice.\n"
    merged, _ = union_entries(
        [], [dict(ENTRY, note=repeated), dict(ENTRY, needed_by=["other"], note=repeated)]
    )
    assert merged[0]["note"] == repeated


def test_distinct_documents_stay_distinct_and_sort_by_id(tmp_path):
    other = dict(ENTRY, id="assa-f107-notes", needed_by=["binning"])
    merged, _ = union_entries([], [ENTRY, other])
    assert [e["id"] for e in merged] == ["assa-f107-notes", "ifoa-cs2-core-reading-2026"]


def test_read_fragments_collects_every_file_in_order(tmp_path):
    staging = tmp_path / "phase-2"
    fragment(staging, 2, [dict(ENTRY, needed_by=["b"])])
    fragment(staging, 1, [dict(ENTRY, needed_by=["a"])])
    entries, complaints = read_fragments(staging)
    assert complaints == []
    assert [e["needed_by"] for e in entries] == [["a"], ["b"]]


def test_a_malformed_fragment_is_a_complaint_rather_than_a_trace(tmp_path):
    """Following _ledger_entries' precedent in checks.py, whose docstring
    records the three shapes that used to crash: a bare string in the list,
    a mapping where a list belongs, and a missing id."""
    staging = tmp_path / "phase-2"
    fragment(staging, 1, [ENTRY])
    (staging / "ledger-02.yaml").write_text("- just a string\n")
    (staging / "ledger-03.yaml").write_text(yaml.safe_dump([{"needed_by": ["a"]}]))
    (staging / "ledger-04.yaml").write_text("id: not a list\n")
    entries, complaints = read_fragments(staging)
    assert len(complaints) == 3
    assert any("ledger-02" in c for c in complaints)
    assert any("ledger-03" in c and "id" in c for c in complaints)
    assert any("ledger-04" in c for c in complaints)


def test_a_missing_needed_by_becomes_an_empty_list(tmp_path):
    """checks.py's rule 9 reads needed_by on every entry, so an entry that
    reaches the ledger without one would disable check 6 silently."""
    merged, _ = union_entries([], [{k: v for k, v in ENTRY.items() if k != "needed_by"}])
    assert merged[0]["needed_by"] == []


def test_union_with_nothing_proposed_returns_seeded_sorted_by_id(tmp_path):
    """The dry-run's whole promise: with no fragments, the union is the
    identity. This is the unit-level half of that guarantee; the CLI's own
    dry-run against the real four-entry ledger is the end-to-end half."""
    seeded = [dict(ENTRY, id="zzz-last"), dict(ENTRY, id="aaa-first", needed_by=[])]
    merged, complaints = union_entries(seeded, [])
    assert complaints == []
    assert [e["id"] for e in merged] == ["aaa-first", "zzz-last"]
    assert merged[1]["claim"] == ENTRY["claim"]


def test_a_fragment_entry_may_omit_needed_by_without_complaint(tmp_path):
    """needed_by defaults away at the union stage, so its absence from a
    fragment is under-specified rather than malformed, unlike a genuinely
    missing claim or acquisition."""
    staging = tmp_path / "phase-2"
    entry = {k: v for k, v in ENTRY.items() if k != "needed_by"}
    fragment(staging, 1, [entry])
    entries, complaints = read_fragments(staging)
    assert complaints == []
    assert entries[0]["id"] == ENTRY["id"]
    assert "needed_by" not in entries[0]


def test_a_fragment_missing_required_fields_names_every_one(tmp_path):
    """A complaint naming only 'malformed' would send an agent back to
    re-read the spec it already left; naming the missing keys lets it fix
    the file directly."""
    staging = tmp_path / "phase-2"
    fragment(staging, 1, [{"id": "thin-entry", "needed_by": ["some-node"]}])
    entries, complaints = read_fragments(staging)
    assert entries == []
    assert len(complaints) == 1
    complaint = complaints[0]
    assert "ledger-01" in complaint
    assert "thin-entry" in complaint
    for field in ("claim", "document", "expected_tier", "acquisition", "status"):
        assert field in complaint


def test_a_fragment_with_an_unlisted_acquisition_or_status_is_a_complaint(tmp_path):
    staging = tmp_path / "phase-2"
    fragment(staging, 1, [dict(ENTRY, id="bad-acquisition", acquisition="stolen")])
    fragment(staging, 2, [dict(ENTRY, id="bad-status", status="lost")])
    entries, complaints = read_fragments(staging)
    assert entries == []
    assert len(complaints) == 2
    assert any("bad-acquisition" in c and "acquisition" in c and "stolen" in c for c in complaints)
    assert any("bad-status" in c and "status" in c and "lost" in c for c in complaints)


def test_a_needed_by_that_is_not_a_list_is_a_complaint(tmp_path):
    """Following _ledger_entries' own asymmetry: absent is under-specified,
    present-but-wrong-shaped is the thing that used to crash a caller
    iterating it."""
    staging = tmp_path / "phase-2"
    fragment(staging, 1, [dict(ENTRY, needed_by="hazard-rate")])
    entries, complaints = read_fragments(staging)
    assert entries == []
    assert len(complaints) == 1
    assert "needed_by" in complaints[0]


def _dump_needed_by(ids):
    return yaml.dump(
        [dict(ENTRY, needed_by=ids)], Dumper=LedgerDumper, sort_keys=False,
        allow_unicode=True,
    )


def test_a_needed_by_list_at_the_threshold_stays_flow():
    """A two-node entry, and anything up to the threshold, is short enough
    to stay a single bounded group rather than switch to block style."""
    dumped = _dump_needed_by([f"node-{i}" for i in range(FLOW_LIST_MAX_ITEMS)])
    assert "needed_by: [" in dumped
    assert "needed_by:\n" not in dumped


def test_a_needed_by_list_past_the_threshold_goes_block():
    """One id past the threshold and the list drops to one id per line,
    verbose but stable."""
    dumped = _dump_needed_by([f"node-{i}" for i in range(FLOW_LIST_MAX_ITEMS + 1)])
    assert "needed_by:\n" in dumped
    assert "needed_by: [" not in dumped


def test_inserting_one_id_into_a_long_needed_by_touches_only_that_line():
    """The property the block-style switch exists for. A 200-id fragment
    is well inside the corpus's own design bound (roughly 1,100 uncovered
    nodes across about 59 anchor documents, with assa.f107 alone anchoring
    274 of them), so entries this size are the expected outcome rather
    than a stress case. Flow style would re-wrap that whole entry on every
    single id inserted into it; block style must not. Inserted mid-list,
    not appended, since an append could pass by only ever touching the
    last line."""
    ids = [f"node-{i:03d}" for i in range(200)]
    before = _dump_needed_by(ids)
    after = _dump_needed_by(ids[:100] + ["node-inserted"] + ids[100:])

    opcodes = difflib.SequenceMatcher(
        None, before.splitlines(), after.splitlines()
    ).get_opcodes()
    changes = [op for op in opcodes if op[0] != "equal"]

    assert len(changes) == 1
    tag, i1, i2, j1, j2 = changes[0]
    assert tag == "insert"
    assert i1 == i2
    assert after.splitlines()[j1:j2] == ["  - node-inserted"]


def test_a_reference_file_in_staging_is_not_read_as_a_fragment(tmp_path):
    """A digest of the ids proposed so far is a reading aid, not a proposal.

    Wave 2 was dispatched with one written to `ledger-ids.yaml`, which the old
    `ledger-*.yaml` glob matched. It parsed as a well-formed fragment, because
    every required field was present and a missing needed_by normalises to an
    empty list, so the merge read its own reference file back as a fourteenth
    fragment and nothing said so.
    """
    staging = tmp_path / "phase-2"
    fragment(staging, 3, [dict(ENTRY, needed_by=["hazard-rate"])])
    digest = {k: v for k, v in ENTRY.items() if k != "needed_by"}
    (staging / "ledger-ids.yaml").write_text(yaml.safe_dump([digest], sort_keys=False))
    entries, complaints = read_fragments(staging)
    assert complaints == []
    assert [e["needed_by"] for e in entries] == [["hazard-rate"]]


def test_ledger_paths_names_both_files_under_sources(tmp_path):
    assert ledger_paths(tmp_path) == (
        tmp_path / "sources" / "wanted.yaml",
        tmp_path / "sources" / "to-ingest.yaml",
    )


def test_status_routes_an_entry_to_one_file_or_the_other():
    """The whole split rule. An entry whose document nobody holds stays in the
    acquisition file; one already in the vault, whether extracted to raw or
    written up as an article, moves to the ingest file."""
    acquisition, ingest = partition_by_status([
        dict(ENTRY, id="a", status="wanted"),
        dict(ENTRY, id="b", status="located"),
        dict(ENTRY, id="c", status="in-raw"),
        dict(ENTRY, id="d", status="ingested"),
    ])
    assert [e["id"] for e in acquisition] == ["a", "b"]
    assert [e["id"] for e in ingest] == ["c", "d"]


def test_a_status_outside_the_vocabulary_stays_in_the_acquisition_file():
    """`read_fragments` rejects a status outside STATUS_VALUES, but a hand-typed
    ledger entry reaches the partition without passing it. Routing the oddity to
    the acquisition file keeps it in front of whoever reads that file, and check
    6 blocks on it because it is not `ingested`. Dropping it would lose the
    entry from both files on the next merge."""
    acquisition, ingest = partition_by_status([dict(ENTRY, id="a", status="nonsense")])
    assert [e["id"] for e in acquisition] == ["a"]
    assert ingest == []
