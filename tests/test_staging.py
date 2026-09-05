"""The merge that turns twenty staging directories into one corpus.

**The corpus is a body too, and it wins.** Three drafted exemplars already sit in `nodes/` from Phase 0, one of them with a lecture attached through `taught_in`, and all three are anchored to CS1 and CS2 sections those two bodies stage. A merge that treated staging as the whole world would replace a written page with a two-sentence stub and orphan its lecture, and `check.py` would pass throughout, because a stub with `taught_in: null` breaks no rule. So `main()` reads the existing corpus, hands each existing record to `merge()`, and the existing record wins on everything a stub cannot supply while gaining the staged anchors, domains and prerequisites by union. Found during Task 8 Batch A, when the trunk agent noticed the three ids sitting immediately downstream of its own.

A shared node is the whole reason staging exists. CS2 and F107 both produce
survival-function, and the merged record has to carry both anchors: a dropped
anchor is silent, because the corpus still checks green without it.
"""

from pathlib import Path

import pytest

from scripts.alchemist.model import Node, parse_node
from scripts.alchemist.staging import collect, merge, near_misses, render, write_merged

STUB = """---
id: {id}
title: {title}
domains: [{domains}]
status: stub
requires: [{requires}]
spends: []
anchor: [{anchor}]
vault_articles: []
vault_sources: []
taught_in: null
---

{body}
"""


def stage(root: Path, body: str, **fields) -> Path:
    fields.setdefault("title", "Survival function")
    fields.setdefault("domains", "stats")
    fields.setdefault("requires", "")
    fields.setdefault("body", "A stub.")
    target = root / body / "nodes" / f"{fields['id']}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(STUB.format(**fields))
    return target


def test_merges_the_anchors_of_a_shared_node(tmp_path):
    stage(tmp_path, "ifoa-cs2-2026", id="survival-function", anchor="ifoa.cs2.4.1-1")
    stage(tmp_path, "assa-f107-2026", id="survival-function", anchor="assa.f107.1.12-4")
    merged, notes = merge(list(collect(tmp_path)["survival-function"]))
    assert set(merged.anchor) == {"ifoa.cs2.4.1-1", "assa.f107.1.12-4"}


def test_merges_the_domains_of_a_shared_node(tmp_path):
    stage(tmp_path, "a", id="hazard-rate", anchor="ifoa.cs2.4.1-1", domains="stats, life")
    stage(tmp_path, "b", id="hazard-rate", anchor="assa.f107.1.12-4", domains="credit, life")
    merged, _ = merge(list(collect(tmp_path)["hazard-rate"]))
    assert set(merged.domains) == {"stats", "life", "credit"}


def test_merges_the_prerequisites_of_a_shared_node(tmp_path):
    stage(tmp_path, "a", id="cox-model", anchor="ifoa.cs2.4.2-1", requires="hazard-rate")
    stage(tmp_path, "b", id="cox-model", anchor="ifoa.sp7.3.5-1", requires="survival-function")
    merged, _ = merge(list(collect(tmp_path)["cox-model"]))
    assert set(merged.requires) == {"hazard-rate", "survival-function"}


def test_a_title_disagreement_is_recorded_rather_than_guessed(tmp_path):
    stage(tmp_path, "a", id="chain-ladder", anchor="ifoa.cs2.4.3-1", title="Chain ladder")
    stage(tmp_path, "b", id="chain-ladder", anchor="ifoa.sp7.3.5-2", title="The chain ladder method")
    merged, notes = merge(list(collect(tmp_path)["chain-ladder"]))
    assert merged.title == "Chain ladder"
    assert any("The chain ladder method" in note for note in notes)


def test_a_single_body_node_passes_through_unchanged(tmp_path):
    stage(tmp_path, "a", id="ruin-theory", anchor="up.wst322.3")
    merged, notes = merge(list(collect(tmp_path)["ruin-theory"]))
    assert merged.anchor == ("up.wst322.3",)
    assert notes == []


def test_the_merged_fields_are_ordered_deterministically(tmp_path):
    """Two runs over the same staging must produce byte-identical files, or
    every re-run is a spurious diff across a thousand records."""
    stage(tmp_path, "b", id="n", anchor="ifoa.sp7.3.5-1", domains="credit, gi")
    stage(tmp_path, "a", id="n", anchor="ifoa.cs2.1.1-1", domains="gi, stats")
    first, _ = merge(list(collect(tmp_path)["n"]))
    second, _ = merge(list(collect(tmp_path)["n"]))
    assert first.anchor == second.anchor == ("ifoa.cs2.1.1-1", "ifoa.sp7.3.5-1")
    assert first.domains == second.domains == ("credit", "gi", "stats")


DRAFTED = """---
id: hazard-rate
title: Hazard rate
domains: [stats]
status: drafted
requires: [survival-function]
spends:
  - {object: obj.hazard, domain: stats}
anchor: [ifoa.cs2.2.1]
vault_articles: []
vault_sources: []
taught_in: S1_credit-survival-bridge
---

## Definition

A written page that took an afternoon.
"""


def test_a_drafted_corpus_record_is_protected(tmp_path):
    """Three Phase 0 exemplars sit in nodes/ as drafted, and CS1 and CS2 stage
    the same ids. The merge must union the new anchors onto them and keep every
    field a stub cannot supply, or a written page becomes two sentences."""
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "hazard-rate.md").write_text(DRAFTED)
    existing = parse_node(corpus / "hazard-rate.md")
    staging = tmp_path / "staging"
    stage(staging, "cs2", id="hazard-rate", anchor="ifoa.cs2.2.1-3", domains="life",
          requires="censoring", title="Hazard rate")
    merged, notes = merge(collect(staging)["hazard-rate"], existing)
    assert merged.status == "drafted"
    assert merged.taught_in == "S1_credit-survival-bridge"
    assert merged.spends == existing.spends
    assert "A written page" in merged.body
    assert merged.anchor == ("ifoa.cs2.2.1", "ifoa.cs2.2.1-3")
    assert merged.domains == ("life", "stats")
    assert merged.requires == ("censoring", "survival-function")
    assert any("protected drafted record" in note for note in notes)


def test_render_keeps_every_field_of_a_protected_record(tmp_path):
    """The renderer used to hardcode spends, the vault fields and taught_in as
    empty, which is correct for a stub and destroys a drafted record."""
    (tmp_path / "hazard-rate.md").write_text(DRAFTED)
    node = parse_node(tmp_path / "hazard-rate.md")
    (tmp_path / "hazard-rate.md").write_text(render(node))
    again = parse_node(tmp_path / "hazard-rate.md")
    assert again.spends == node.spends
    assert again.taught_in == node.taught_in
    assert again.status == "drafted"
    assert "{object: obj.hazard, domain: stats}" in render(node)


def test_a_title_containing_a_colon_still_renders_valid_yaml(tmp_path):
    """Found running the merge over the live staging: BCBS and F107 both stage
    "Pillar 1: minimum capital requirements", quoted in the source as YAML
    requires. The brief's render() wrote the colon straight onto the title line
    unquoted, which splits the line into two mapping keys and crashes parse_node
    on the file the merge itself produced. The staged file is written here with
    the same quoting the real transcription agents used, so this exercises
    render() rather than the stage() helper's own formatting."""
    staged = tmp_path / "a" / "nodes"
    staged.mkdir(parents=True)
    (staged / "pillar-1-minimum-capital-requirements.md").write_text(
        "---\n"
        "id: pillar-1-minimum-capital-requirements\n"
        "title: 'Pillar 1: minimum capital requirements'\n"
        "domains: [regulation]\n"
        "status: stub\n"
        "requires: []\n"
        "spends: []\n"
        "anchor: [bcbs.d424.pillar1.1]\n"
        "vault_articles: []\n"
        "vault_sources: []\n"
        "taught_in: null\n"
        "---\n\nA stub.\n"
    )
    merged, _ = merge(list(collect(tmp_path)["pillar-1-minimum-capital-requirements"]))
    target = tmp_path / "corpus"
    target.mkdir()
    written = write_merged({merged.id: merged}, target)
    reparsed = parse_node(written[0])
    assert reparsed.title == "Pillar 1: minimum capital requirements"


def test_near_misses_see_what_exact_match_cannot():
    """Both pairs Batch B found by accident, plus one negative that a looser
    test would report: market-risk and credit-risk differ by one token too."""
    ids = ["efficient-market-hypothesis", "efficient-markets-hypothesis",
           "reputation-risk", "reputational-risk", "chain-ladder", "chain-ladder-method",
           "market-risk", "credit-risk", "hazard-rate"]
    pairs = set(near_misses(ids))
    assert ("efficient-market-hypothesis", "efficient-markets-hypothesis") in pairs
    assert ("reputation-risk", "reputational-risk") in pairs
    assert ("chain-ladder", "chain-ladder-method") in pairs
    assert ("credit-risk", "market-risk") not in pairs
    assert not any("hazard-rate" in p for p in pairs)


def test_written_records_reparse(tmp_path):
    stage(tmp_path, "a", id="hazard-rate", anchor="ifoa.cs2.2.1-3", domains="stats, credit")
    stage(tmp_path, "b", id="hazard-rate", anchor="assa.f107.1.12-4", domains="credit")
    target = tmp_path / "corpus"
    target.mkdir()
    merged = {node_id: merge(records)[0] for node_id, records in collect(tmp_path).items()}
    written = write_merged(merged, target)
    reparsed = parse_node(written[0])
    assert set(reparsed.anchor) == {"ifoa.cs2.2.1-3", "assa.f107.1.12-4"}
    assert reparsed.status == "stub"
