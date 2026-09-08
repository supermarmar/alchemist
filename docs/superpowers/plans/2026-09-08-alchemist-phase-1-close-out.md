# Alchemist Phase 1 Close-out Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the thirteen gate 2 decisions of 8 September 2026 to the Phase 1 skeleton, so that Phase 2 Attach starts from a corpus whose ids, titles, anchors, paths, and graphs are settled: one anchor prefix renamed on 90 records, twenty-one near-miss pairs merged, one node split, ten titles corrected under a stated casing rule with a check behind it, three new paths for the 427 unpathed nodes, per-domain graphs drawn for connected nodes only, and the credit trunk sequenced by hand.

**Architecture:** Eleven tasks in three groups, in dependency order. Sweeps first (Tasks 1 to 7), because every later step reads the ids, anchors, and titles they settle, and because a merge made after a citation is attached has to move the citation with it. Structure second (Tasks 8 and 9): the three path files, the two D12 domain edits and one edge, and the graph pruning. Trunk sequencing last (Task 10), over the final node set, so no placement is made twice. Three small tools are built with tests, since each is used more than once here and again in Phase 2: an anchor-prefix rename (Task 1), a path sequencer that reproduces Task 12's mechanical order (Task 3), and a node merge that unions fields, repoints every reference, and deletes the absorbed file (Task 4). Every task that touches `nodes/` or `paths/` regenerates `index.html`, which is a tracked artefact with no currency check, and commits it in the same commit.

**Tech Stack:** Python under the in-repo `.venv`; PyYAML and pytest; graphviz `dot` for `build_site.py`. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, sections 4.1 to 4.4 for the schemas and section 9 for the phases. **Decisions:** `notes/gate-2-decisions-2026-09-08.md`, which is the binding record for every ruling this plan applies; where this plan and that note disagree, the note wins and this plan is drift.

**Branch:** `feat/phase-1-close-out`, cut from `main` once PR #3 (`docs/gate-2-review`) has merged, since the decisions note and this plan live on that branch. Merging PR #3 is Mario's call; if it is still open when execution starts, cut from `docs/gate-2-review` instead and say so in the PR body.

**Model routing:** Tasks 1 to 9 and 11 are Sonnet implementation work with exact code below. Task 10 is pedagogical judgement over 277 nodes and runs on the most capable available model (Opus, or Fable 5.1), with Mario reading the result as the gate. Set the model explicitly on every dispatch.

## Global Constraints

- Python is always `.venv/bin/python`. Never a system `python3`.
- The repo is public. Assume anything committed is published on landing. Nothing from a Gini engagement, no client parameters or figures.
- Node ids are stable slugs matching `^[a-z0-9]+(-[a-z0-9]+)*$` and are never renamed. A merge (Task 4) removes an id and repoints every reference to it; that is the one edit this plan makes to the id set, and D6 (c) ratified every committed id, so no task renames one.
- `domains` draws on the closed vocabulary in `scripts/alchemist/model.py`'s `DOMAINS`: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`, `regulation`, `eco`, `fin-man`. No task adds a domain.
- `anchor` follows `<body>.<subject>.<section>[.<item>]`, lowercase and dot-separated, three or four segments, or the literal `chosen`, enforced by `model.py`'s `ANCHOR` pattern.
- Writing rules apply to every file this plan touches, this plan included: British English; no em or en dashes as punctuation; no negated counterpart clauses ("X, not Y", "not only ... but also"); currency written with the unit word.
- Conventional Commits, one concern per commit, **explicit paths on every `git add`**; `-A` and `--no-verify` are both forbidden. The Co-Authored-By trailer on every commit.
- `check.py` runs on every commit through `.githooks/pre-commit` and validates the working tree. Where a task says "check.py passes", it means all rules report `ok` or `SKIP` and the summary line ends `0 failures`.
- A node file is written only through `scripts.alchemist.staging.render` or by editing one frontmatter line in place. Nothing in this plan rewrites a node body.
- The braids (`survival-braid`, `markov-transition-braid`, `claims-reserving-braid`) are hand-sequenced and no task runs the sequencer over them.

## The standing instruction, carried in every dispatch

Phase 1's costliest failures were specifications the coordinator wrote that turned out wrong, and tests that passed for a reason other than the one they named. Two rules follow. First, **for every test you write, inject the bug the test names and confirm the test goes red before you make it green**, and say in your report which injection you ran. Second, after `check.py` passes, **report what it did not verify** about your change: the nine rules test integrity, acyclicity, path order, and symbol resolution, and nothing about whether a merge chose the right survivor, a title reads well, or a path preamble describes its nodes.

Read `notes/gate-2-decisions-2026-09-08.md` before starting any task. It is short.

---

## File structure

Created:

- `scripts/rename_anchor_prefix.py`, the D3 sweep over node anchor lines and the manifest.
- `scripts/alchemist/sequence.py`, the mechanical path order and a nodes-block rewriter.
- `scripts/sequence_path.py`, its command line, with `--check`.
- `scripts/alchemist/merges.py`, one node merge: union, repoint, delete.
- `scripts/merge_nodes.py`, its command line, taking a pairs file.
- `nodes/age-period-cohort-mortality-model.md`, the D9 split.
- `paths/enterprise-risk-and-regulation.yaml`, `paths/banking-and-financial-management.yaml`, `paths/economics.yaml`, the D2 paths.
- `notes/credit-trunk-sequence-2026-09.md`, the D1 stages and rationale.
- `notes/phase-1-close-out-report-2026-09.md`, the measured outcome.
- Tests: `tests/test_rename_anchor_prefix.py`, `tests/test_sequence.py`, `tests/test_merges.py`, `tests/test_checks_titles.py`.

Modified:

- `nodes/*.md`: 90 anchor lines (Task 1), 22 survivors and their referrers (Task 4), one split (Task 5), ten title lines (Task 6), two domain lines and one requires line (Task 8), one requires line (Task 4, N106).
- `paths/*.yaml`: repointed lines (Task 4), `life.yaml` and `claims-reserving-braid.yaml` (Task 5), the seven mechanical paths re-sequenced after each corpus change (Tasks 4, 5, 8), `credit-trunk.yaml` by hand (Task 10).
- `sources/syllabi.yaml`, `notes/transcription-brief.md`, `CLAUDE.md`, `README.md`, the spec, and the Phase 1 plan: the prefix rename (Task 1), the abbreviation list (Task 2), the casing rule and the tenth check (Task 7).
- `scripts/alchemist/checks.py`: rule 10 (Task 7). `scripts/alchemist/site.py`: `render_domain_dot` (Task 9). `tests/test_cli.py`: the two dot-graph tests (Task 9).
- `index.html`: regenerated whenever `nodes/` or `paths/` change.

---

### Task 1: Rename the anchor prefix (D3, G14)

**Files:**
- Create: `scripts/rename_anchor_prefix.py`
- Test: `tests/test_rename_anchor_prefix.py`
- Modify: 90 files under `nodes/` (by the script), `sources/syllabi.yaml:176-193`, `notes/transcription-brief.md:131`, `CLAUDE.md:30`, `CLAUDE.md:68`, `CLAUDE.md:134-137`, `README.md:99`, `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md:131`, `docs/superpowers/plans/2026-09-04-alchemist-phase-1.md:255,265,612,1355,1545`

**Interfaces:**
- Produces: `rename_in_anchor_line(text: str, old: str, new: str) -> str`, `rename_nodes(nodes_dir: Path, old: str, new: str) -> list[Path]`, `rename_manifest(manifest: Path, old: str, new: str) -> bool`.

The lecture set is attributed to Università Cattolica del Sacro Cuore in `sources/syllabi.yaml` and the README, and the prefix `eth.dl-actuarial-2026` still encodes the earlier ETH Zurich attribution on 90 node records carrying 96 anchors. The rename touches the `anchor:` line of a node file and nothing else, so no body is rewritten. The manifest `id: eth-dl-actuarial-2026` stays as it is, because the Phase 1 staging directory `.superpowers/phase-1/eth-dl-actuarial-2026/` and its grain manifest key on it; the note text in the manifest says so.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_rename_anchor_prefix.py
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_rename_anchor_prefix.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.rename_anchor_prefix'`.

- [ ] **Step 3: Write the script**

```python
# scripts/rename_anchor_prefix.py
"""Rename an anchor-body prefix on every node record and in the manifest.

An anchor prefix is a key, and a key that misattributes a licensed source is a
liability that grows with every phase, because Phase 2 attaches citations to the
records carrying it and Phase 3 writes their pages. The rename touches the `anchor:`
line of a node file and nothing else, so a drafted body is never rewritten, and it
reparses every touched file so a malformed result fails here with the path named.
The manifest id is left alone: the Phase 1 staging directory and its grain manifest
key on it, and it was never an attribution.

Usage:
    .venv/bin/python scripts/rename_anchor_prefix.py eth.dl-actuarial-2026 ucsc.dl-actuarial-2026
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import parse_node

REPO = Path(__file__).resolve().parents[1]
ANCHOR_LINE = re.compile(r"^anchor: \[.*\]$", re.M)


def rename_in_anchor_line(text: str, old: str, new: str) -> str:
    """Rewrite `old.` to `new.` inside the anchor line only. The trailing dot is
    what stops the prefix matching a longer prefix that starts the same way."""
    return ANCHOR_LINE.sub(lambda m: m.group(0).replace(f"{old}.", f"{new}."), text, count=1)


def rename_nodes(nodes_dir: Path, old: str, new: str) -> list[Path]:
    touched: list[Path] = []
    for path in sorted(nodes_dir.glob("*.md")):
        text = path.read_text()
        rewritten = rename_in_anchor_line(text, old, new)
        if rewritten != text:
            path.write_text(rewritten)
            parse_node(path)
            touched.append(path)
    return touched


def rename_manifest(manifest: Path, old: str, new: str) -> bool:
    text = manifest.read_text()
    rewritten = text.replace(f"anchor_prefix: {old}", f"anchor_prefix: {new}")
    rewritten = rewritten.replace(f"{old}.", f"{new}.")
    if rewritten == text:
        return False
    manifest.write_text(rewritten)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("old")
    parser.add_argument("new")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    touched = rename_nodes(args.root / "nodes", args.old, args.new)
    manifest_changed = rename_manifest(args.root / "sources" / "syllabi.yaml", args.old, args.new)
    left = [p for p in sorted((args.root / "nodes").glob("*.md")) if f"{args.old}." in p.read_text()]
    print(f"{len(touched)} node records renamed, manifest {'updated' if manifest_changed else 'unchanged'}")
    if left:
        print(f"{len(left)} node files still carry {args.old}. outside the anchor line:")
        for p in left:
            print(f"  {p.relative_to(args.root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_rename_anchor_prefix.py -v`
Expected: 5 passed. Injection to run first: change `f"{old}."` to `old` in `rename_in_anchor_line` and confirm `test_a_longer_prefix_sharing_the_stem_is_left_alone` goes red; change the `ANCHOR_LINE.sub` to a whole-text `replace` and confirm `test_the_anchor_line_is_renamed_and_the_body_is_not` goes red.

- [ ] **Step 5: Run the rename on the corpus**

Run: `.venv/bin/python scripts/rename_anchor_prefix.py eth.dl-actuarial-2026 ucsc.dl-actuarial-2026`
Expected: `90 node records renamed, manifest updated` and no "still carry" lines.

- [ ] **Step 6: Edit the manifest note by hand**

In `sources/syllabi.yaml`, the `note:` of the `eth-dl-actuarial-2026` entry (lines 182 to 189) currently ends:

```
    Richman on lectures 10 to 12, per the title slide. The anchor prefix
    eth.dl-actuarial-2026 traces to an earlier, mistaken attribution to ETH Zurich and is
    retained this phase as a stable key rather than as an attribution: renaming it touches
    all ninety anchored node records plus the brief, CLAUDE.md, the spec and the plan, and
    the rename itself is a Phase 2 decision.
```

Replace those five lines with:

```
    Richman on lectures 10 to 12, per the title slide. The anchor prefix carried an
    earlier, mistaken ETH Zurich attribution until gate 2 renamed it on 8 September 2026
    (D3) to match the issuer. The manifest id is unchanged, because the Phase 1 staging
    directory and its grain manifest key on it and it was never an attribution.
```

- [ ] **Step 7: Edit the brief, CLAUDE.md, README, spec, and plan**

`notes/transcription-brief.md:131`, replace the row:

```
| ETH summer school | `eth.dl-actuarial-2026` | twelve lectures | `eth.dl-actuarial-2026.l02`, where `l04` covers the combined lecture 04-05 and `l10` the combined 10-11 |
```
with
```
| UCSC summer school | `ucsc.dl-actuarial-2026` | twelve lectures | `ucsc.dl-actuarial-2026.l02`, where `l04` covers the combined lecture 04-05 and `l10` the combined 10-11 |
```

`CLAUDE.md:68`: replace `` `eth.dl-actuarial-2026.l02` `` with `` `ucsc.dl-actuarial-2026.l02` ``.

`CLAUDE.md:134`: replace `- **The ETH summer-school material this corpus derives from is licensed CC BY-NC 4.0.**` with `- **The Università Cattolica summer-school material this corpus derives from is licensed CC BY-NC 4.0.**`

`CLAUDE.md:137`: replace `stays non-commercial; should it ever become fee-earning, the ETH-derived nodes need` with `stays non-commercial; should it ever become fee-earning, the summer-school-derived nodes need`.

`CLAUDE.md:30` (G14, the stale corpus size): replace `A uniform full-lecture standard for all 1,100 to 1,400 nodes the corpus holds would take` with `A uniform full-lecture standard for the 1,500-odd nodes the corpus holds would take`.

`README.md:99`: replace `eth.dl-actuarial-2026.l01` with `ucsc.dl-actuarial-2026.l01`.

Spec line 131 and plan lines 255, 265, 612, 1355, 1545: replace every literal `eth.dl-actuarial-2026` with `ucsc.dl-actuarial-2026`. Leave the plan's prose about ETH as it stands; the plan is a dated record and only the key is renamed.

Run: `grep -rn "eth\.dl-actuarial-2026" --exclude-dir=.git --exclude-dir=.superpowers --exclude-dir=.venv --exclude-dir=site . | grep -v "notes/gate-2-\|notes/phase-1-report.md\|notes/merge-report\|notes/prerequisite-report\|docs/superpowers/plans/2026-09-08"`
Expected: no output. The excluded files are dated records of Phase 1 and keep the prefix they measured.

- [ ] **Step 8: Verify and commit**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python -m pytest -q`
Expected: `1580 nodes, 10 paths, 0 failures` and the suite green.

```bash
git add scripts/rename_anchor_prefix.py tests/test_rename_anchor_prefix.py nodes sources/syllabi.yaml notes/transcription-brief.md CLAUDE.md README.md docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md docs/superpowers/plans/2026-09-04-alchemist-phase-1.md
git commit -m "feat(anchors): rename eth.dl-actuarial-2026 to ucsc.dl-actuarial-2026 (D3)

90 node records, 96 anchors, the manifest prefix and note, the brief,
CLAUDE.md, README, spec and plan. The manifest id stays as the staging key.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

`git add nodes` is acceptable here because every changed file under `nodes/` is the script's output; confirm with `git status --short nodes | wc -l` reading `90` before adding.

---

### Task 2: Ratify the abbreviation list (D6 c)

**Files:**
- Modify: `notes/transcription-brief.md:65-70`

- [ ] **Step 1: Replace rule 3**

Lines 65 to 70 read:

```
3. **Spell out an abbreviation unless it is on this list: `glm`, `gam`, `arima`, `garch`,
   `gev`, `gpd`, `mcmc`, `pca`, `svd`.** Those nine are what practitioners actually say, and
   nobody says "generalised linear model" twice in a sentence. Everything else is spelled out,
   so `probability-of-default` rather than `pd`. The list is closed. Report a case you believe
   belongs on it rather than adding it yourself, because a list twenty agents can each extend
   independently is the same failure as no list.
```

Replace with:

```
3. **Spell out an abbreviation unless it is on this list.** Statistics and machine learning:
   `glm`, `gam`, `arima`, `arma`, `garch`, `gev`, `gpd`, `mcmc`, `pca`, `svd`, `lasso`, `cls`,
   `sql`. Regulation and banking: `pd`, `lgd`, `ead`, `ecl`, `irb`, `cva`, `dcf`, `lcr`,
   `nsfr`, `tlac`, `sme`, `crr`, `ftp`, `roe`, `gdp`, `ilaap`, `icaap`, `sa`, `eu`, `otc`,
   `cds`, `isda`, `sicr`, `eir`, `fvoci`, `fvpl`, `poci`. Those forty are what practitioners
   actually say, and nobody says "generalised linear model" twice in a sentence. Everything
   else is spelled out. The list closed at nine for Phase 1 and was ratified at forty at gate 2
   on 8 September 2026 (D6), when 63 committed ids already carried the banking set; ids are
   never renamed, so `probability-of-default` stands beside any future `pd-` id. Report a case
   you believe belongs on the list and do not add it yourself, because a list twenty agents
   can each extend independently is the same failure as no list.
```

- [ ] **Step 2: Verify the count and commit**

Run: `sed -n 65,75p notes/transcription-brief.md | grep -o '`[a-z]*`' | sort -u | wc -l`
Expected: `40`.

```bash
git add notes/transcription-brief.md
git commit -m "docs(brief): ratify the forty-token abbreviation list (D6)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: The path sequencer

**Files:**
- Create: `scripts/alchemist/sequence.py`, `scripts/sequence_path.py`
- Test: `tests/test_sequence.py`

**Interfaces:**
- Produces: `mechanical_order(path: TeachingPath, corpus: Corpus) -> tuple[str, ...]` and `rewrite_nodes(text: str, order: Iterable[str]) -> str` in `scripts.alchemist.sequence`; the command `scripts/sequence_path.py [--check] [--root ROOT] PATH_ID [PATH_ID ...]`, exit 1 under `--check` when any named path is out of mechanical order.
- Consumed by: Tasks 4, 5, 8 (re-sequencing after corpus edits) and Task 10 (the inverse check).

Task 12 sequenced the seven mechanical paths by topological tier with alphabetical ties, and measured on 8 September 2026 every one of them still satisfies `nodes == sorted(nodes, key=(in-path depth, id))`. The tool reproduces that rule so a corpus edit can re-sequence them without a hand pass, and rewrites only the `nodes:` block so a preamble's wrapping survives.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_sequence.py
from pathlib import Path

from scripts.alchemist.model import Corpus, Node, TeachingPath
from scripts.alchemist.sequence import mechanical_order, rewrite_nodes


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
    corpus = Corpus({n.id: n for n in (node("a"), node("b", ["z"]), node("z"))}, {})
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
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_sequence.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.sequence'`.

- [ ] **Step 3: Write the module**

```python
# scripts/alchemist/sequence.py
"""The mechanical order of a path: topological tier, then id.

Task 12 sequenced the domain paths this way and the braids by hand. A node's tier
is the longest chain of prerequisites behind it inside the same path, so tier 0
holds what the path can open with, and inside a tier the ids sort alphabetically,
which is deterministic and says nothing about pedagogy. D1 (a) replaces this order
on the credit trunk by hand and leaves it on every other path until its pages
exist, so anything that edits `requires` re-runs this over the mechanical paths.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from .model import Corpus, TeachingPath

NODES_BLOCK = re.compile(r"^nodes:\n(?:- .*\n?)*", re.M)


def mechanical_order(path: TeachingPath, corpus: Corpus) -> tuple[str, ...]:
    members = set(path.nodes)
    depth: dict[str, int] = {}

    def tier(node_id: str) -> int:
        if node_id in depth:
            return depth[node_id]
        inside = [r for r in corpus.nodes[node_id].requires if r in members]
        depth[node_id] = 0 if not inside else 1 + max(tier(r) for r in inside)
        return depth[node_id]

    for node_id in path.nodes:
        tier(node_id)
    return tuple(sorted(path.nodes, key=lambda n: (depth[n], n)))


def rewrite_nodes(text: str, order: Iterable[str]) -> str:
    """Replace the nodes block and nothing else, so a preamble's wrapping survives."""
    if NODES_BLOCK.search(text) is None:
        raise ValueError("no nodes block to rewrite")
    block = "nodes:\n" + "".join(f"- {n}\n" for n in order)
    return NODES_BLOCK.sub(lambda _: block, text, count=1)
```

```python
# scripts/sequence_path.py
"""Write a path's nodes block in mechanical order, or check that it already is.

    .venv/bin/python scripts/sequence_path.py life general-insurance
    .venv/bin/python scripts/sequence_path.py --check credit-trunk

Never run this over a braid: the braids are ordered by hand as their preambles
narrate, and the credit trunk joins them once D1 is applied.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_corpus
from scripts.alchemist.sequence import mechanical_order, rewrite_nodes

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path_ids", nargs="+")
    parser.add_argument("--check", action="store_true", help="exit 1 if any path is out of order; write nothing")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    out_of_order = 0
    for path_id in args.path_ids:
        path = corpus.paths[path_id]
        file = args.root / "paths" / f"{path_id}.yaml"
        text = file.read_text()
        rewritten = rewrite_nodes(text, mechanical_order(path, corpus))
        if rewritten == text:
            print(f"{path_id}: in order")
            continue
        out_of_order += 1
        if args.check:
            print(f"{path_id}: out of mechanical order")
        else:
            file.write_text(rewritten)
            print(f"{path_id}: rewritten")
    return 1 if (args.check and out_of_order) else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_sequence.py -v`
Expected: 5 passed. Injection: sort by id alone and confirm `test_tier_first_then_id` goes red; count an out-of-path prerequisite and confirm `test_a_prerequisite_outside_the_path_does_not_raise_the_tier` goes red.

- [ ] **Step 5: Confirm the tool reproduces Task 12 on the corpus**

Run: `.venv/bin/python scripts/sequence_path.py --check credit-trunk life general-insurance financial-engineering machine-learning data-engineering maths-stats-prerequisites`
Expected: seven lines ending `in order` and exit 0. If any path reads `out of mechanical order`, stop and report: the rule is misstated and Tasks 4, 5, and 8 must not run until it is right.

- [ ] **Step 6: Commit**

```bash
git add scripts/alchemist/sequence.py scripts/sequence_path.py tests/test_sequence.py
git commit -m "feat(paths): add the mechanical sequencer Task 12 ordered the domain paths by

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Merge the twenty-one near-miss pairs (D7)

**Files:**
- Create: `scripts/alchemist/merges.py`, `scripts/merge_nodes.py`
- Test: `tests/test_merges.py`
- Modify: 22 survivor files and their referrers under `nodes/`, path files that list an absorbed id, `nodes/revised-standardised-approach-credit-risk.md` (N106 edge), the seven mechanical paths (re-sequenced), `index.html`

**Interfaces:**
- Consumes: `scripts.alchemist.staging.render(node: Node) -> str`, `scripts.alchemist.model.parse_node`, `parse_path`; Task 3's `sequence_path.py`.
- Produces: `merged_record(survivor: Node, absorbed: Node) -> Node`, `repoint_requires(text, absorbed, survivor, node_id) -> str`, `repoint_path(text, absorbed, survivor) -> str`, `ledger_names(ledger: Path, node_id: str) -> bool`, `merge_pair(root: Path, absorbed_id: str, survivor_id: str) -> list[Path]`.

The survivor keeps its id, title, status, body, spends, `taught_in`, and vault fields, and gains the absorbed record's domains, anchors, and prerequisites by union, with the edge between the pair dropped (four pairs carry one). Every `requires` entry naming the absorbed id is repointed to the survivor and deduplicated, every path line naming it is repointed or, where the survivor is already in that path, removed, and the absorbed file is deleted. A gap-ledger `needed_by` naming an absorbed id stops the merge, since a mistyped ledger id disables check 6 silently; none does today, measured.

**Ruling during execution, 8 September 2026.** The pair `linear-model linear-regression` was withdrawn. Merging it closed the cycle `least-squares-estimation -> linear-regression -> least-squares-estimation`, because `linear-model` (up.wst311.6) is the full-rank general linear model, fitted by least squares and tested by nested models, and requires `least-squares-estimation`, while `linear-regression-model` and `linear-regression` are the introductory model that estimation is derived for. The review page's N75 read the three as one node; the edges say otherwise. Twenty-one pairs apply and `linear-model` stands, which Mario confirms or reverses on reading.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_merges.py
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


def write_node(nodes: Path, node_id: str, *, title=None, domains="stats", requires="", anchor="chosen", body="A body.") -> Path:
    path = nodes / f"{node_id}.md"
    path.write_text(NODE.format(id=node_id, title=title or node_id, domains=domains, requires=requires, anchor=anchor, body=body))
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


def test_ledger_names_reads_needed_by_only(tmp_path):
    ledger = tmp_path / "wanted.yaml"
    ledger.write_text("- id: b-paper\n  needed_by: [c]\n  claim: mentions b in prose\n")
    assert ledger_names(ledger, "b") is False
    assert ledger_names(ledger, "c") is True
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_merges.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.merges'`.

- [ ] **Step 3: Write the module and the command**

```python
# scripts/alchemist/merges.py
"""Merge one node id into another.

The survivor keeps its identity and gains the absorbed record's anchors, domains,
and prerequisites; every reference to the absorbed id is repointed; the absorbed
file is deleted. Ids are never renamed, and a merge is the one edit that removes
one, so it does every part of the job or none: a survivor written without the
repointing leaves dangling `requires` entries that check 3 catches and dangling
path lines that check 4 catches, and a repointing without the deletion leaves a
duplicate. Task 11 did six of these by hand in Phase 1; gate 2 ruled twenty-two
more (D7), which is what made a tool worth its tests.

Only the `requires:` line of a referring node is rewritten, as a flow sequence,
which is how every record written by `staging.render` carries it. A record whose
requires is a block sequence is left alone and check 3 reports the dangling id.
"""

from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path

import yaml

from .model import Node, parse_node, parse_path
from .staging import render

REQUIRES_LINE = re.compile(r"^requires: \[(.*)\]$", re.M)


def merged_record(survivor: Node, absorbed: Node) -> Node:
    both = {survivor.id, absorbed.id}

    def union(field: str) -> tuple[str, ...]:
        return tuple(sorted(set(getattr(survivor, field)) | set(getattr(absorbed, field))))

    return replace(
        survivor,
        domains=union("domains"),
        requires=tuple(r for r in union("requires") if r not in both),
        anchor=union("anchor"),
        vault_articles=union("vault_articles"),
        vault_sources=union("vault_sources"),
    )


def repoint_requires(text: str, absorbed: str, survivor: str, node_id: str) -> str:
    """Rewrite one node's requires line: absorbed becomes survivor, deduplicated, no self-edge."""
    match = REQUIRES_LINE.search(text)
    if match is None:
        return text
    items = [i.strip() for i in match.group(1).split(",") if i.strip()]
    if absorbed not in items:
        return text
    kept: list[str] = []
    for item in items:
        target = survivor if item == absorbed else item
        if target != node_id and target not in kept:
            kept.append(target)
    return text[: match.start()] + f"requires: [{', '.join(kept)}]" + text[match.end():]


def repoint_path(text: str, absorbed: str, survivor: str) -> str:
    lines = text.split("\n")
    if f"- {absorbed}" not in lines:
        return text
    if f"- {survivor}" in lines:
        lines = [line for line in lines if line != f"- {absorbed}"]
    else:
        lines = [f"- {survivor}" if line == f"- {absorbed}" else line for line in lines]
    return "\n".join(lines)


def ledger_names(ledger: Path, node_id: str) -> bool:
    entries = yaml.safe_load(ledger.read_text()) or []
    return any(node_id in (entry.get("needed_by") or []) for entry in entries)


def merge_pair(root: Path, absorbed_id: str, survivor_id: str) -> list[Path]:
    nodes_dir = root / "nodes"
    ledger = root / "sources" / "wanted.yaml"
    if ledger.exists() and ledger_names(ledger, absorbed_id):
        raise ValueError(f"{absorbed_id} is named in {ledger}; repoint the ledger first")
    absorbed = parse_node(nodes_dir / f"{absorbed_id}.md")
    survivor = parse_node(nodes_dir / f"{survivor_id}.md")

    touched: list[Path] = []
    survivor_file = nodes_dir / f"{survivor_id}.md"
    survivor_file.write_text(render(merged_record(survivor, absorbed)))
    touched.append(survivor_file)
    absorbed.path.unlink()
    touched.append(absorbed.path)

    for path in sorted(nodes_dir.glob("*.md")):
        text = path.read_text()
        rewritten = repoint_requires(text, absorbed_id, survivor_id, path.stem)
        if rewritten != text:
            path.write_text(rewritten)
            parse_node(path)
            touched.append(path)
    for path in sorted((root / "paths").glob("*.yaml")):
        text = path.read_text()
        rewritten = repoint_path(text, absorbed_id, survivor_id)
        if rewritten != text:
            path.write_text(rewritten)
            parse_path(path)
            touched.append(path)
    return touched
```

```python
# scripts/merge_nodes.py
"""Apply a list of node merges, one `absorbed survivor` pair per line.

    .venv/bin/python scripts/merge_nodes.py --pairs .superpowers/close-out/merges.txt

Lines starting with # are comments. Pairs apply in file order, so a triple is two
lines naming the same survivor. Run check.py afterwards: a union can close a cycle
that no single record carried, and check 3 is what reports it.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.merges import merge_pair

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pairs", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    merged = 0
    for line in args.pairs.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        absorbed, survivor = line.split()
        touched = merge_pair(args.root, absorbed, survivor)
        merged += 1
        print(f"{absorbed} -> {survivor}: {len(touched)} files")
    print(f"{merged} merges applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_merges.py -v`
Expected: 11 passed. Injections: drop the `if target != node_id` clause and confirm `test_the_edge_between_the_pair_is_dropped_and_the_rest_kept` stays green but `test_a_referrer_is_repointed_and_deduplicated` still passes, then drop the `target not in kept` clause and confirm that test goes red; make `repoint_path` always substitute and confirm `test_a_path_holding_both_drops_the_absorbed_line` goes red; remove the ledger guard and confirm `test_a_ledger_naming_the_absorbed_id_stops_the_merge` goes red.

- [ ] **Step 5: Write the pairs file and apply the merges**

```bash
mkdir -p .superpowers/close-out
cat > .superpowers/close-out/merges.txt <<'EOF'
# gate 2, D7: the proposed merges, less N75's linear-model which the corpus places above least-squares estimation (absorbed survivor)
central-bank-activities central-bank
counterparty-risk counterparty-credit-risk
credit-risk-mitigation-overview credit-risk-mitigation
f-statistic-distribution f-distribution
general-insurance-product-overview general-insurance-product
hypothesis-test hypothesis-testing
linear-regression-model linear-regression
loan-schedule loan-repayment-schedule
profit-testing profit-test
random-sampling random-sample
risk-based-loan-pricing risk-based-pricing
risk-modelling risk-model
sampling-distribution-of-mean-and-variance sampling-distribution-of-normal-mean-and-variance
stochastic-process-classification stochastic-process
t-statistic-distribution t-distribution
# the six ruled on 8 September, shorter id surviving
credit-scoring-model credit-scoring
level-annuity-certain level-annuity
markov-jump-process markov-process
named-probability-distribution probability-distribution
risk-identification-techniques risk-identification
risk-measurement-methods risk-measurement
EOF
.venv/bin/python scripts/merge_nodes.py --pairs .superpowers/close-out/merges.txt
```
Expected: 21 lines and `21 merges applied`. `.superpowers/` is gitignored, so the pairs file is a working note; the record is the decisions note.

- [ ] **Step 6: Add the N106 edge**

In `nodes/revised-standardised-approach-credit-risk.md`, the line `requires: [basel-i-credit-risk-quantification]` becomes `requires: [basel-i-credit-risk-quantification, standardised-approach-credit-risk]`. Measured on 8 September, `standardised-approach-credit-risk` requires `pillar-1-minimum-capital-requirements`, `risk-weighted-assets`, and `securitisation`, none of which is the revised node, so no cycle closes; check 3 confirms.

- [ ] **Step 7: Re-sequence the mechanical paths, verify, regenerate the index**

Merges change `requires`, so tiers move, and two of them expose a prerequisite a path's closure does not supply. Pull those in first: append `- risk-measurement` to `paths/general-insurance.yaml` (the survivor `risk-model` gains it from `risk-modelling`, and its own prerequisite `risk-classification` is already a member) and `- credit-risk` to `paths/life.yaml` (the repointed `counterparty-credit-risk` requires it, and it is a root). The sequencer places both.

Run: `.venv/bin/python scripts/sequence_path.py credit-trunk life general-insurance financial-engineering machine-learning data-engineering maths-stats-prerequisites`
Run: `.venv/bin/python scripts/check.py`
Expected: `1559 nodes, 10 paths, 0 failures`. A failure under rule 3 names a cycle a union closed; report it with the pair and stop. Do not edit an edge to break it.
Run: `.venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -q`
Expected: suite green; `index.html` modified.

- [ ] **Step 8: Commit**

```bash
git add scripts/alchemist/merges.py scripts/merge_nodes.py tests/test_merges.py nodes paths index.html
git commit -m "feat(nodes): merge the twenty-one near-miss pairs ruled at gate 2 (D7)

Fifteen proposed on the review page and six ruled on 8 September with the
shorter id surviving. N75's linear-model stays: it is the full-rank general
linear model, taught after least-squares estimation, and merging it closed
a cycle through that node. Fields unioned, every requires entry and path
line repointed, absorbed files deleted, N106's edge added, mechanical paths
re-sequenced. Two paths gain a prerequisite the merges exposed: general
insurance takes risk-measurement and life takes credit-risk, both placed by
the sequencer. 1,580 nodes become 1,559.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Report what check.py did not verify: whether each survivor's title still describes the union (Task 6 retitles `credit-scoring`), and whether any absorbed body carried a sentence the survivor's body lacks. List the 22 absorbed bodies' first sentences in the report for Mario's read.

---

### Task 5: Split age-period-cohort (D9)

**Files:**
- Create: `nodes/age-period-cohort-mortality-model.md`
- Modify: `nodes/age-period-cohort.md`, `paths/life.yaml`, `paths/claims-reserving-braid.yaml`, `index.html`

The merged node carries the lecture set's identification problem in its body and CS2's mortality projection model in its frontmatter. The split gives each anchor the node it names. `vintage-analysis` keeps requiring `age-period-cohort`, and the claims-reserving braid drops `mortality-projection-approaches`, which was in the braid only as that node's prerequisite.

- [ ] **Step 1: Write the new node**

```markdown
---
id: age-period-cohort-mortality-model
title: Age-period-cohort mortality model
domains: [life]
status: stub
requires: [age-period-cohort, mortality-projection-approaches]
spends: []
anchor: [ifoa.cs2.4.6-2, ifoa.cs2.4.6-3]
vault_articles: []
vault_sources: []
taught_in: null
---

A projection model that writes the log of a mortality rate as the sum of an age effect, a calendar-period effect, and a cohort effect for the year of birth, fits the three effects to a table of observed rates, and extrapolates the period and cohort effects to project future mortality. Because the three axes are linked, the fit needs an identifiability constraint before the effects can be estimated, which is the problem the parent node states.
```

- [ ] **Step 2: Narrow the parent**

In `nodes/age-period-cohort.md`, three frontmatter lines change and the body stays:

```
domains: [life, stats]
requires: [mortality-projection-approaches]
anchor: [ucsc.dl-actuarial-2026.l01, ifoa.cs2.4.6-2, ifoa.cs2.4.6-3]
```
become
```
domains: [stats]
requires: []
anchor: [ucsc.dl-actuarial-2026.l01]
```

- [ ] **Step 3: Paths**

Append `- age-period-cohort-mortality-model` to the `nodes:` block of `paths/life.yaml`, then re-sequence: `.venv/bin/python scripts/sequence_path.py life`. Both prerequisites are in the life path, measured on 8 September, so check 4 holds.

In `paths/claims-reserving-braid.yaml`, delete the line `- mortality-projection-approaches`. The braid's preamble names the age-period-cohort framework and never the mortality projection node, so no prose changes.

- [ ] **Step 4: Verify and commit**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -q`
Expected: `1560 nodes, 10 paths, 0 failures`, suite green.

```bash
git add nodes/age-period-cohort.md nodes/age-period-cohort-mortality-model.md paths/life.yaml paths/claims-reserving-braid.yaml index.html
git commit -m "feat(nodes): split age-period-cohort into the problem and CS2's model (D9)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Retitle under the casing rule and the T rows (D4, D5, N42)

**Files:**
- Modify: ten title lines under `nodes/`, `index.html`

Ten `title:` lines change and nothing else in each file. Nine follow D4 (a) and the D5 rows; the tenth is the N42 survivor, whose title today names only F207's half of the merged node. Three titles stay capitalised under D4's defined-term exemption and are listed so Mario can confirm on reading: `business-indicator-component` (Business Indicator Component), `internal-loss-multiplier` (Internal Loss Multiplier), and `crr-eu` (Capital Requirements Regulation), each a body's own defined term where the term is the node.

- [ ] **Step 1: Edit the ten lines**

| File | Before | After | Why |
|---|---|---|---|
| `nodes/credit-risk-mitigation.md` | `title: Other credit risk mitigation techniques` | `title: Credit risk mitigation` | T3 |
| `nodes/risk-concentration.md` | `title: Concentration` | `title: Risk concentration` | T4 |
| `nodes/esg-risk.md` | `title: Environmental, Sustainability and Governance risk` | `title: Environmental, sustainability and governance risk` | T6 |
| `nodes/f-distribution.md` | `title: F distribution` | `title: F-distribution` | T7 |
| `nodes/liability-categorisation-for-asset-liability-management.md` | `title: Liability categorisation for asset liability management` | `title: Liability categorisation for asset-liability management` | T8 |
| `nodes/tail-value-at-risk.md` | `title: Tail Value at Risk` | `title: Tail value at risk` | T12 |
| `nodes/value-at-risk.md` | `title: Value at Risk` | `title: Value at risk` | T14 |
| `nodes/value-at-risk-weaknesses.md` | `title: Weaknesses of Value at Risk` | `title: Weaknesses of value at risk` | D4 |
| `nodes/binomial-representation-theorem.md` | `title: Binomial Representation Theorem` | `title: Binomial representation theorem` | D4 |
| `nodes/credit-scoring.md` | `title: Credit scoring and bureau data` | `title: Credit scoring` | N42 |

For each: `sed -i '' 's/^title: <before>$/title: <after>/' <file>` with the exact strings above, then `grep -c "^title: <after>$" <file>` reads `1`.

- [ ] **Step 2: Verify and commit**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -q`
Expected: `1560 nodes, 10 paths, 0 failures`.

```bash
git add nodes/credit-risk-mitigation.md nodes/risk-concentration.md nodes/esg-risk.md nodes/f-distribution.md nodes/liability-categorisation-for-asset-liability-management.md nodes/tail-value-at-risk.md nodes/value-at-risk.md nodes/value-at-risk-weaknesses.md nodes/binomial-representation-theorem.md nodes/credit-scoring.md index.html
git commit -m "fix(nodes): retitle ten records under the sentence-case rule and the T rows (D4, D5)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Check 10, titles are sentence case (D4, G5)

**Files:**
- Modify: `scripts/alchemist/checks.py:1,381-392`, `notes/transcription-brief.md` (insert after line 73), `CLAUDE.md:77-99,109,171` (insert a section before line 77), `README.md:40-52`
- Test: `tests/test_checks_titles.py`

**Interfaces:**
- Produces: `check_titles_sentence_case(corpus: Corpus) -> Result`, appended to `run_all`; `PROPER_NAMES: frozenset[str]` in `checks.py`.

A title in the source's own casing reads as a different concept from the same title in sentence case, and twenty transcribers produced fourteen such disagreements. The rule: the first word may carry any case; every later word is lowercase unless it is a proper name on the list, an acronym (two or more capitals), a Roman numeral, a single letter, or a possessive of a name. Hyphenated compounds are checked part by part.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_checks_titles.py
from pathlib import Path

from scripts.alchemist.checks import check_titles_sentence_case
from scripts.alchemist.model import Corpus, Node


def node(node_id: str, title: str) -> Node:
    return Node(
        id=node_id, title=title, domains=("stats",), status="stub", requires=(), spends=(),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def failures(*titles: str) -> list[str]:
    corpus = Corpus({f"n{i}": node(f"n{i}", t) for i, t in enumerate(titles)}, {})
    return check_titles_sentence_case(corpus).failures


def test_a_capitalised_common_noun_fails_and_is_named():
    result = failures("Tail Value at Risk")
    assert len(result) == 1 and "Value" in result[0] and "Risk" in result[0]


def test_sentence_case_passes():
    assert failures("Tail value at risk", "t-distribution", "Weaknesses of value at risk") == []


def test_a_proper_name_on_the_list_passes():
    assert failures("Compound Poisson process", "Shortcomings of the Basel Accord") == []


def test_an_acronym_a_roman_numeral_and_a_single_letter_pass():
    assert failures("Addressing NSFR compliance", "Tier II capital", "Capital buffer versus CCoB plus CCyB", "Distribution of the F-statistic") == []


def test_a_possessive_name_and_a_hyphenated_pair_of_names_pass():
    assert failures("Assumptions underlying Black's model", "Bolzano-Weierstrass and Heine-Borel theorems", "Wave equation and Laplace's equation") == []


def test_a_bracketed_acronym_passes():
    assert failures("Bond stripping (STRIPS)") == []


def test_a_name_off_the_list_fails_so_the_list_is_the_only_exemption():
    assert len(failures("The Keynesian cross")) == 1


def test_the_first_word_is_free():
    assert failures("Keynesian multiplier", "ILAAP") == []
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_checks_titles.py -v`
Expected: FAIL, `ImportError: cannot import name 'check_titles_sentence_case'`.

- [ ] **Step 3: Write the check**

In `scripts/alchemist/checks.py`, change line 1 from `"""The nine rules. Each returns a Result, so the runner reports every failure in` to `"""The ten rules. Each returns a Result, so the runner reports every failure in`. Add `import re` beside `import os`. Insert before `def run_all`:

```python
PROPER_NAMES = frozenset({
    "Accord", "American", "Basel", "Bayes", "Black", "Bolzano", "Borel", "Brace",
    "Brownian", "Business", "Capital", "Carlo", "Component", "Depression", "Euclidean",
    "Gatarek", "Great", "Greeks", "Heine", "Indicator", "Internal", "Laplace", "Lloyd",
    "Loss", "Markov", "Monte", "Multiplier", "Musiela", "Organization", "Pareto",
    "Poisson", "Regulation", "Requirements", "Scholes", "Tier", "Trade", "Weierstrass",
    "World",
})
ROMAN = re.compile(r"^(?:I|II|III|IV|V|VI|VII|VIII|IX|X)$")


def _capitalised_off_list(title: str) -> list[str]:
    """Words after the first that carry a capital the rule does not allow."""
    offenders: list[str] = []
    for word in title.split()[1:]:
        for part in word.split("-"):
            core = part.strip("(),:;\"'").removesuffix("'s")
            if not core or not core[0].isupper():
                continue
            if len(core) == 1 or sum(ch.isupper() for ch in core) >= 2:
                continue
            if ROMAN.match(core) or core in PROPER_NAMES:
                continue
            offenders.append(part)
    return offenders


def check_titles_sentence_case(corpus: Corpus) -> Result:
    """Sentence case, ruled at gate 2 (D4, 8 September 2026). A title in the source's
    own casing reads as a different concept from the same title in sentence case,
    and twenty transcribers produced fourteen such disagreements. Proper names,
    acronyms, Roman numerals, single letters and possessives of names pass; a
    body's defined term that is itself the node is on the list by name, which is
    why Business Indicator Component and Capital Requirements Regulation pass.
    """
    result = Result("10. titles are sentence case")
    for node in sorted(corpus.nodes.values(), key=lambda n: n.id):
        offenders = _capitalised_off_list(node.title)
        if offenders:
            result.failures.append(
                f"{node.id}: title {node.title!r} capitalises {', '.join(offenders)}, "
                f"which is off the proper-name list"
            )
    return result
```

Append `check_titles_sentence_case(corpus),` as the last entry of the list `run_all` returns.

- [ ] **Step 4: Run the tests to verify they pass, then the check on the corpus**

Run: `.venv/bin/python -m pytest tests/test_checks_titles.py -v`
Expected: 8 passed. Injections: remove `.removesuffix("'s")` and confirm `test_a_possessive_name_and_a_hyphenated_pair_of_names_pass` goes red; remove the `word.split("-")` loop (check the whole word) and confirm the same test goes red on Bolzano-Weierstrass; drop `[1:]` and confirm `test_the_first_word_is_free` goes red.

Run: `.venv/bin/python scripts/check.py`
Expected: `ok    10. titles are sentence case` and `0 failures`. Where rule 10 fails on the corpus, each failure is one of two things: a genuine name the list lacks, which you add to `PROPER_NAMES` and report by name, or a source-cased title Task 6 missed, which you retitle in sentence case and report. Do neither silently.

- [ ] **Step 5: State the rule and the count in the brief, CLAUDE.md, and README**

`notes/transcription-brief.md`: insert after line 73 (the end of id rule 4):

```

### Titles

Sentence case throughout: a capital on the first word, on proper names (Black-Scholes,
Poisson, Basel III, Lloyd's), and on a body's own defined term where that term is the node,
as in Capital Requirements Regulation or Internal Loss Multiplier. Everything else is
lowercase, so Value at risk and Tail value at risk. Check 10 flags a title that capitalises
a word off the proper-name list in `scripts/alchemist/checks.py`; where a genuine name trips
it, report the name for the list. Ruled at gate 2 on 8 September 2026 (D4).
```

`CLAUDE.md`: insert before line 77 (`## The nine checks`):

```
## Title casing

Titles are sentence case: a capital on the first word, on proper names, and on a body's own
defined term where the term is the node (Capital Requirements Regulation). Check 10 enforces
it against the `PROPER_NAMES` list in `checks.py`, so a genuine name the list lacks is added
there by name, and a source's title case is corrected in the record. Ruled at gate 2 (D4).

```

Then: line 77 `## The nine checks` becomes `## The ten checks`; line 79 `enforces nine rules` becomes `enforces ten rules`; in the rule list at lines 84 to 88, after `and every `needed_by` id in the gap ledger resolving to a node.` append ` Rule 10, added at gate 2, is that every title is sentence case.`; line 98 `still gets eight of the nine` becomes `still gets nine of the ten`; line 109 `# the nine checks` becomes `# the ten checks`; line 171 `` `checks.py` for the nine rules `` becomes `` `checks.py` for the ten rules ``.

`README.md`: line 40 `enforces nine rules` becomes `enforces ten rules`; in the list ending at line 45, after `and that every node id in the gap ledger resolves` insert `, and that every title is sentence case`; line 48 `One of the nine` becomes `One of the ten`; line 50 `eight of the nine checks` becomes `nine of the ten checks`; the following sentence's `the other eight` becomes `the other nine`.

Run: `grep -n -i "nine" CLAUDE.md README.md scripts/alchemist/checks.py`
Expected: no line still counts the checks as nine.

- [ ] **Step 6: Verify and commit**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python -m pytest -q`
Expected: ten `ok` or `SKIP` lines, `0 failures`, suite green. `tests/test_cli.py::test_check_py_exits_zero_on_the_real_repo` is the one that would catch a corpus failure.

```bash
git add scripts/alchemist/checks.py tests/test_checks_titles.py notes/transcription-brief.md CLAUDE.md README.md
git commit -m "feat(checks): add rule 10, titles are sentence case (D4)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 8: Three paths for the unpathed nodes, and the three D12 records (D2, D12)

**Files:**
- Create: `paths/enterprise-risk-and-regulation.yaml`, `paths/banking-and-financial-management.yaml`, `paths/economics.yaml`
- Modify: `nodes/actuarial-professionalism-in-banking.md`, `nodes/actuarial-techniques-in-banking.md`, `nodes/stochastic-modelling-for-risk.md`, `index.html`

**Interfaces:**
- Consumes: Task 3's `mechanical_order` and `sequence_path.py`.

Membership is by domain set, regulation first, then economics, then banking, which is the grouping the decisions note records. Where a member's prerequisite is in no path the new path can build on, the prerequisite joins the path, so `model-fitting` joins enterprise risk and regulation and the three banking nodes that regulation nodes need (`why-banks-hold-capital`, `fair-value-accounting`, `enterprise-risk-management-concept`) sit in both. The dependency runs regulation, then banking, then economics, measured on 8 September: 16 banking nodes need a regulation node, 3 regulation nodes need a banking node, 1 economics node needs a banking node, and nothing runs the other way. The three D12 records: two banking-material nodes carrying only `actuarial` gain `fin-man` and so join the banking path, and the third gains an edge.

- [ ] **Step 1: The D12 records**

`nodes/actuarial-professionalism-in-banking.md` and `nodes/actuarial-techniques-in-banking.md`: `domains: [actuarial]` becomes `domains: [actuarial, fin-man]`.

`nodes/stochastic-modelling-for-risk.md`: `requires: []` becomes `requires: [probability-distribution]`. Its body defines the node as representing an uncertain outcome as a probability distribution, which is the prerequisite.

- [ ] **Step 2: Build the three path files**

Write this to `.superpowers/close-out/draw_paths.py` and run it with `.venv/bin/python .superpowers/close-out/draw_paths.py` from the repo root. It is a one-off and is not committed; the path files it writes are the artefact, and the rule is recorded in the decisions note and each preamble.

```python
"""Draw the three gate 2 paths (D2) from the nodes in no path, by domain set."""
import sys
import textwrap
from collections import Counter
from pathlib import Path

sys.path.insert(0, ".")
from scripts.alchemist.model import TeachingPath, load_corpus
from scripts.alchemist.sequence import mechanical_order

REG, BANK, ECO = "enterprise-risk-and-regulation", "banking-and-financial-management", "economics"
ORDER = [REG, BANK, ECO]
SPEC = {
    REG: (
        "Enterprise risk and regulation",
        ["credit-trunk", "financial-engineering", "life", "general-insurance", "data-engineering"],
        "How a regulated financial firm identifies, measures, and governs risk, and what its "
        "regulators require of it: the risk management function and its committees, risk appetite, "
        "the three lines of defence, model risk management, and the Basel capital and liquidity "
        "framework from Basel I through the 2017 finalisation, with the leverage ratio, the output "
        "floor, the liquidity coverage and net stable funding ratios, the capital buffers, and the "
        "internal capital and liquidity adequacy assessment processes. Hedge accounting, conduct "
        "risk, insurance regulation, and recovery and resolution sit alongside. It builds on the "
        "credit trunk because the internal ratings-based rules regulate the parameters the trunk "
        "estimates, and on the life and general insurance paths, which supply the prerequisites "
        "its CP1 principles nodes draw on.",
    ),
    BANK: (
        "Banking and financial management",
        [REG, "credit-trunk", "financial-engineering", "life", "general-insurance"],
        "What a bank is and how it is run as a business: the balance sheet and income statement, "
        "deposit taking and wholesale funding, the funds transfer pricing regimes that price "
        "liquidity between businesses, and the capital, return, and liquidity metrics a treasury "
        "and an asset-liability committee manage. The path carries the ASSA banking papers' "
        "material on operational risk data and loss modelling, pension obligation risk, and the "
        "enterprise risk management vocabulary of appetite, culture, and reporting, together with "
        "the strategy and case-study material the papers end on. It builds on the enterprise risk "
        "and regulation path because the ratios and buffers it manages are the ones that path "
        "defines, and on the credit trunk because the loan book is the asset being funded.",
    ),
    ECO: (
        "Economics",
        [BANK, "financial-engineering", "general-insurance", "life", "credit-trunk"],
        "The macroeconomics and microeconomics the banking material assumes: the circular flow, "
        "aggregate demand and supply, growth, unemployment and inflation, money and monetary "
        "policy, fiscal policy, interest and exchange rates, trade, and the market structures from "
        "perfect competition to monopoly. The path also holds the economic history since the Great "
        "Depression and the strategic material on how a bank fares through the cycle, because net "
        "interest income, expected credit losses, and the outlook for a loan book are all "
        "conditional on the economy. It builds on the banking path for the balance-sheet "
        "vocabulary and on financial engineering for the instruments the economy moves.",
    ),
}

corpus = load_corpus()
nodes, paths = corpus.nodes, corpus.paths
member = Counter(k for p in paths.values() for k in p.nodes)
orphans = [k for k in nodes if member[k] == 0]


def bucket(node_id):
    d = set(nodes[node_id].domains)
    if "regulation" in d:
        return REG
    if "eco" in d:
        return ECO
    if "fin-man" in d:
        return BANK
    return None


members = {pid: set() for pid in ORDER}
for k in orphans:
    b = bucket(k)
    if b:
        members[b].add(k)


def supplied(pid):
    seen, frontier = set(), list(SPEC[pid][1])
    while frontier:
        nxt = frontier.pop()
        if nxt in seen:
            continue
        seen.add(nxt)
        frontier.extend(paths[nxt].builds_on if nxt in paths else SPEC[nxt][1])
    out = set()
    for p in seen:
        out |= set(paths[p].nodes) if p in paths else members[p]
    return out


for pid in ORDER:
    have = supplied(pid)
    pulled, changed = [], True
    while changed:
        changed = False
        for k in sorted(members[pid]):
            for r in nodes[k].requires:
                if r not in members[pid] and r not in have:
                    members[pid].add(r)
                    pulled.append(r)
                    changed = True
    title, builds_on, preamble = SPEC[pid]
    draft = TeachingPath(pid, title, tuple(builds_on), preamble, tuple(sorted(members[pid])))
    order = mechanical_order(draft, corpus)
    text = (
        f"id: {pid}\ntitle: {title}\nbuilds_on: [{', '.join(builds_on)}]\npreamble: >\n"
        + textwrap.fill(preamble, width=86, initial_indent="  ", subsequent_indent="  ")
        + "\nnodes:\n" + "".join(f"- {n}\n" for n in order)
    )
    Path("paths", f"{pid}.yaml").write_text(text)
    print(f"{pid}: {len(order)} nodes, pulled in {sorted(pulled)}")
```

Expected, from a dry run on the 8 September tree before Task 4's merges: enterprise risk and regulation 153 nodes, pulling in `model-fitting`, `why-banks-hold-capital`, `fair-value-accounting`, `enterprise-risk-management-concept`, and the two prerequisites those bring, `bank-business-model` and `risk-modelling` (which Task 4 merges into `risk-model`, so expect that id instead); banking and financial management 163 with nothing pulled in; economics 100 with nothing pulled in. The merges may move the first figure by one or two. Report the measured three figures and the pulled-in list. A pulled-in node you did not expect is a prerequisite living in no path; report it and leave it in.

- [ ] **Step 3: Verify**

Run: `.venv/bin/python scripts/check.py`
Expected: `1560 nodes, 13 paths, 0 failures`, with rule 4 `ok`. A rule 4 failure names a node and its missing prerequisite; the fix is to add the missing path to that path's `builds_on` in `SPEC` and re-run. Deleting the edge is not a fix.

Run this measurement and put the two numbers in the report:

```bash
.venv/bin/python - <<'EOF'
import sys; sys.path.insert(0, ".")
from collections import Counter
from scripts.alchemist.model import load_corpus
c = load_corpus(); member = Counter(k for p in c.paths.values() for k in p.nodes)
rb = Counter(r for n in c.nodes.values() for r in n.requires)
orphans = [k for k in c.nodes if member[k] == 0]
print("in no path:", len(orphans), sorted(orphans))
print("no edge and no path:", [k for k in orphans if not c.nodes[k].requires and rb[k] == 0])
EOF
```
Expected: `in no path: 16` and `no edge and no path: []` (measured during execution; the plan first said 17, before `model-fitting` was counted as pulled into the regulation path).

Run: `.venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -q`

- [ ] **Step 4: Commit**

```bash
git add paths/enterprise-risk-and-regulation.yaml paths/banking-and-financial-management.yaml paths/economics.yaml nodes/actuarial-professionalism-in-banking.md nodes/actuarial-techniques-in-banking.md nodes/stochastic-modelling-for-risk.md index.html
git commit -m "feat(paths): draw the three gate 2 paths for the unpathed nodes (D2, D12)

Enterprise risk and regulation, banking and financial management, and
economics, by domain set, in mechanical order. Two banking nodes gain
fin-man and one CP1 node gains an edge, so no node is left with neither.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Report what check.py did not verify: that each preamble describes its members. Read the three node lists against their preambles and name any topic a preamble claims that the list lacks, and cut the claim.

---

### Task 9: Draw domain graphs for connected nodes only (D10 b)

**Files:**
- Modify: `scripts/alchemist/site.py:379-397`, `tests/test_cli.py:189-195`
- Test: `tests/test_cli.py` (one test rewritten, one added)

A member with no edge inside its domain is a lone box that says nothing a node page does not, and at 450 members the lone boxes were a third of the drawing. Measured on 8 September, fin-man falls from 450 drawn nodes to 301, stats from 384 to 307, regulation from 327 to 270.

- [ ] **Step 1: Rewrite the existing test and add one**

`tests/test_cli.py:189-195` currently asserts `'"b"' in dot` for a node whose only prerequisite is in another domain. Under (b) that node is not drawn. Replace the test:

```python
def test_a_node_whose_only_prerequisite_sits_in_another_domain_is_not_drawn():
    corpus = Corpus(
        {"a": node("a", domains=("life",)), "b": node("b", ["a"], domains=("stats",))},
        {},
    )
    dot = render_domain_dot(corpus, "stats")
    assert '"b"' not in dot and '"a" -> "b"' not in dot


def test_a_member_with_an_in_domain_edge_is_drawn_and_a_lone_member_is_not():
    corpus = Corpus({"a": node("a"), "b": node("b", ["a"]), "c": node("c")}, {})
    dot = render_domain_dot(corpus, "stats")
    assert '"a"' in dot and '"b"' in dot and '"a" -> "b"' in dot
    assert '"c"' not in dot
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_cli.py -k "dot" -v`
Expected: the two new tests FAIL (`"b"` is drawn; `"c"` is drawn), the edge-count test passes.

- [ ] **Step 3: Change the renderer**

Replace `render_domain_dot` in `scripts/alchemist/site.py` with:

```python
def render_domain_dot(corpus: Corpus, domain: str) -> str:
    """One graph per domain, drawn for the nodes with an edge inside it. An edge is
    drawn only where both ends sit in the domain, so a domain view stays readable
    and does not drag in every root; a member with no such edge is a lone box that
    says nothing a node page does not, and at 450 members the lone boxes were a
    third of the drawing (D10, gate 2, 8 September 2026).
    """
    members = {n.id for n in corpus.nodes.values() if domain in n.domains}
    edges = [
        (required, node_id)
        for node_id in sorted(members)
        for required in sorted(corpus.nodes[node_id].requires)
        if required in members
    ]
    drawn = sorted({end for edge in edges for end in edge})
    lines = [
        "digraph alchemist {",
        '  rankdir=LR; node [shape=box, fontname="Helvetica", fontsize=10];',
    ]
    for node_id in drawn:
        label = _dot_label(corpus.nodes[node_id].title)
        lines.append(f'  "{node_id}" [label="{label}"];')
    for required, node_id in edges:
        lines.append(f'  "{required}" -> "{node_id}";')
    lines.append("}")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_cli.py tests/test_site.py -v`
Expected: all pass. Injection: set `drawn = sorted(members)` and confirm `test_a_member_with_an_in_domain_edge_is_drawn_and_a_lone_member_is_not` goes red.

- [ ] **Step 5: Regenerate and measure**

Run: `.venv/bin/python scripts/build_site.py && for d in fin-man stats regulation; do echo "$d $(grep -c 'label=' site/graphs/$d.svg 2>/dev/null || grep -c '<title>' site/graphs/$d.svg)"; done`
Expected: about 301, 307, 270 drawn nodes. `site/` is gitignored, so the SVGs are not committed; the figures go in the report.

- [ ] **Step 6: Commit**

```bash
git add scripts/alchemist/site.py tests/test_cli.py
git commit -m "feat(site): draw domain graphs for nodes with an in-domain edge only (D10)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 10: Hand-sequence the credit trunk (D1 a)

**Files:**
- Create: `notes/credit-trunk-sequence-2026-09.md`
- Modify: `paths/credit-trunk.yaml` (the `nodes:` block only), `index.html`

**Model:** the most capable available, Opus or Fable 5.1. This is the one task in the plan that calls for judgement; every other task is transcription with tests.

The trunk's 273 nodes (277 before Task 4's merges) sit in tier-then-alphabetical order, so it opens with Accounting for impairments, Actual versus predicted plot, and Automated decision-making safeguards. Its preamble states the arc: credit risk from the definitions a portfolio manager states without a model, through internal ratings-based parameter estimation, to capital requirements and the governance a regulator expects around them. The nineteen lectures the trunk material was copied from give the arc's middle in teaching order: `01_credit-use-case`, `02_credit-edf-glm`, `03_credit-deep-learning-overview`, `04-05_credit-fnn`, `06_credit-covariate-engineering`, `07_credit-calibration`, `08_credit-icenet-regularisation`, `09_credit-localglmnet`, `10-11_credit-transformer`, `12_credit-foundation-models`, then `C1` interaction and causation, `D1` default definition, `F1` classing and characteristic analysis, `R1` IFRS 9 point-in-time PD, `R2` IRB capital, `R3` sampling and representativeness, and `S1` to `S3` survival. Their titles are the guide; the files themselves are outside this repo at `~/Documents/Repos/actuarial_deep_learning/credit_lectures/` and need not be read.

- [ ] **Step 1: Write the stages first**

Create `notes/credit-trunk-sequence-2026-09.md` with a heading, one paragraph stating the arc in your own words, and then between five and eight named stages, each with one sentence saying what a reader can do at its end. Write this before touching the path file, so the placements are made against a stated arc and a reader can check them against it.

- [ ] **Step 2: Place every node**

Read the 277 node records (`nodes/<id>.md` for each id in `paths/credit-trunk.yaml`), assign each to a stage, and order within a stage for teaching: definitions before methods, methods before their regulatory treatment, an estimator before its validation. Every node's prerequisites inside the trunk must come before it; check 4 enforces that and nothing else. Do not add or remove a node; membership is not this task's question.

Write the new order into the `nodes:` block of `paths/credit-trunk.yaml`. Use `rewrite_nodes` so nothing above the block changes:

```bash
.venv/bin/python - <<'EOF'
import sys; sys.path.insert(0, ".")
from pathlib import Path
from scripts.alchemist.sequence import rewrite_nodes
order = [line.strip() for line in Path(".superpowers/close-out/trunk-order.txt").read_text().splitlines() if line.strip()]
file = Path("paths/credit-trunk.yaml")
file.write_text(rewrite_nodes(file.read_text(), order))
EOF
```
where `.superpowers/close-out/trunk-order.txt` holds the 277 ids, one per line, in the new order.

- [ ] **Step 3: Verify three ways**

```bash
.venv/bin/python - <<'EOF'
import sys; sys.path.insert(0, ".")
import subprocess
from scripts.alchemist.model import parse_path
from pathlib import Path
new = parse_path(Path("paths/credit-trunk.yaml")).nodes
old = subprocess.run(["git", "show", "HEAD:paths/credit-trunk.yaml"], capture_output=True, text=True, check=True).stdout
old_ids = [l[2:] for l in old.splitlines() if l.startswith("- ")]
assert sorted(new) == sorted(old_ids), "the node set changed"
assert len(new) == len(set(new)), "a node is listed twice"
print("same 277 nodes, no duplicates")
EOF
.venv/bin/python scripts/check.py
.venv/bin/python scripts/sequence_path.py --check credit-trunk; echo "exit $?"
```
Expected: `same 277 nodes, no duplicates`; `0 failures`; and `credit-trunk: out of mechanical order` with `exit 1`, which proves the order is now a chosen one. If `--check` exits 0 the order is still mechanical and the task is not done.

- [ ] **Step 4: Finish the note**

Append to `notes/credit-trunk-sequence-2026-09.md`: a table of the stages with each stage's node count and its first three ids; a list of the placements you were least sure of, with the alternative you rejected and why, no fewer than three and no more than ten; and the line `Ordered by hand on <date>; the nine other mechanical paths stay in tier-then-alphabetical order until their pages exist (D1 a).`

- [ ] **Step 5: Commit**

Run: `.venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -q`

```bash
git add paths/credit-trunk.yaml notes/credit-trunk-sequence-2026-09.md index.html
git commit -m "feat(paths): sequence the credit trunk by hand against its preamble's arc (D1)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

The gate is Mario reading `notes/credit-trunk-sequence-2026-09.md` and the path diff. Say so in the report and stop.

---

### Task 11: Close-out report

**Files:**
- Create: `notes/phase-1-close-out-report-2026-09.md`

- [ ] **Step 1: Measure**

```bash
.venv/bin/python scripts/check.py
.venv/bin/python -m pytest -q
.venv/bin/python - <<'EOF'
import sys; sys.path.insert(0, ".")
from collections import Counter
from scripts.alchemist.model import load_corpus
c = load_corpus(); n, p = c.nodes, c.paths
member = Counter(k for q in p.values() for k in q.nodes)
rb = Counter(r for x in n.values() for r in x.requires)
print("nodes", len(n), "paths", len(p), "edges", sum(len(x.requires) for x in n.values()))
print("in no path", sum(1 for k in n if member[k] == 0), "no edge", sum(1 for k, x in n.items() if not x.requires and rb[k] == 0),
      "no edge and no path", sum(1 for k, x in n.items() if not x.requires and rb[k] == 0 and member[k] == 0))
print("per path", {q.id: len(q.nodes) for q in p.values()})
print("domains", dict(Counter(d for x in n.values() for d in x.domains)))
EOF
```

- [ ] **Step 2: Write the report**

`notes/phase-1-close-out-report-2026-09.md`: a heading; one paragraph saying what closed and where the decisions record is; a table with one row per decision (D1 to D13), the option applied, the commit hash, and the measured effect, with D8, D11, and D13 marked as applied by leaving the corpus unchanged; the measurements from Step 1 as a short table against the 8 September baseline (1,580 nodes, 10 paths, 1,424 edges, 427 in no path, 257 with no edge, 109 with neither); the three D10 graph figures from Task 9; and a closing paragraph naming what Phase 2 Attach inherits: the sixteen stats and actuarial nodes still in no path, listed by id, and the gate 2 backlog items this plan did not take (G1, G2, G3, G4, G6, G7, G8, G9, G10, G11, G12, G13, G17, G18, G19, G20, G21, G22), one line each with the id and title from the review page. British English, no dashes, no negated counterparts.

- [ ] **Step 3: Commit**

```bash
git add notes/phase-1-close-out-report-2026-09.md
git commit -m "docs(notes): report the Phase 1 close-out against the gate 2 decisions

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

Then use the finishing-a-development-branch skill: push `feat/phase-1-close-out` and open a PR against `main` whose body links the decisions note, the close-out report, and the trunk sequence note, and names the one gate Mario reads (Task 10). Never self-merge.

---

## Self-review

**Decision coverage.** D1 Task 10; D2 Task 8; D3 Task 1; D4 Tasks 6 and 7; D5 Task 6; D6 Task 2; D7 Task 4; D8 no change, recorded in Task 11; D9 Task 5; D10 Task 9; D11 no change, recorded in Task 11; D12 Task 8; D13 no change, recorded in Task 11. The seven near-miss rulings and the six survivors are in Task 4's pairs file, matching the decisions note's table.

**Dependency order.** Task 3 precedes 4, 5, 8, and 10, which call the sequencer. Task 1 precedes 5, whose new anchor literal is the renamed prefix. Task 4 precedes 6 (the `credit-scoring` title) and 8 (orphan counts after merges). Task 6 precedes 7, whose check must pass on the corpus. Task 10 is last so no placement is made twice.

**Type consistency.** `mechanical_order(path: TeachingPath, corpus: Corpus)` and `rewrite_nodes(text, order)` are named the same in Tasks 3, 8, and 10. `merge_pair(root, absorbed_id, survivor_id)` returns the touched paths in Task 4's module and its tests. `check_titles_sentence_case(corpus)` returns a `Result` whose `rule` string is `10. titles are sentence case`, matching the CLAUDE.md and README wording.

**Figures.** 1,580 nodes less 21 plus 1 is 1,560; Task 4's expected count is 1,559 because Task 5's split follows it, and the twenty-second merge (N75's `linear-model`) was withdrawn during execution. The 16 nodes left in no path are the 19 stats and actuarial nodes of the decisions note less the two the D12 domain edit moves and `model-fitting`, which the regulation path pulls in as a prerequisite. Path counts in Task 8 are stated as approximate because Task 4 absorbs some orphans; the task reports the measured figures.
