import yaml

from scripts.alchemist.ledger import read_fragments, union_entries

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
