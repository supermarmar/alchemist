# Alchemist Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transcribe 20 published anchor bodies into 1,100 to 1,400 stub node records with `requires` and `anchor` populated, plus ten path files, four further notation objects, a seeded gap ledger, and one generated review document that gate 2 can actually be read from.

**Architecture:** Phase 1 is content rather than software, so it inverts Phase 0's shape. Four waves run in order. Wave 0 prepares the machinery and the brief, serially, because 20 parallel agents hitting an unsettled domain vocabulary or an unstated anchor convention is a reconcile job that costs more than the commits that avoid it. Wave 1 dispatches one agent per anchor body, each writing into a private staging directory rather than into `nodes/`. Wave 2 merges staging into the corpus, unioning the fields that a shared node accumulates across bodies, then resolves cross-body prerequisites and builds the paths. Wave 3 generates the review document. The small amount of new software (a merge, a grain audit, a review renderer, two check hardenings and a sweep extension) is written test-first; the transcription is not, because there is nothing to assert about a judgement call.

**Tech Stack:** Python 3.14.7 under `uv` in the in-repo `.venv`; PyYAML and pytest for the tooling; `pdftotext` from poppler for syllabus extraction; node and the vendored KaTeX for the sweep; graphviz `dot` for the domain graphs.

**Spec:** `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, as amended at gate 1 by commit `11e97d7`. Sections 4.1 to 4.4 hold every schema, section 5 the nine checks, and section 9's Phase 1 row the deliverable.

**Branch:** `feat/phase-1-skeleton`, cut from `feat/phase-0-machinery`. PR #1 is open and unmerged and merging it is Mario's call, so Phase 1 builds on the branch rather than waiting. The risk if review changes `model.py`'s validation is a sweep over records, which is cheap while they are stubs.

## Global Constraints

- Python is always `.venv/bin/python`. Never a system `python3`: this machine carries 3.14.3 under `/Library/Frameworks` and 3.14.7 under `/opt/homebrew`, and neither has the packages.
- The repo is public. Assume anything committed is published on landing. Nothing from a Gini engagement, no client parameters or figures, and no example borrowing either.
- `data/` is gitignored. Public downloads only. The 20 source documents live at `data/syllabi/` and never enter a commit; `sources/syllabi.yaml` records their provenance and is committed.
- ETH-derived material is licensed **CC BY-NC 4.0**, so the corpus stays non-commercial, with attribution and a statement of changes.
- Node ids are stable slugs matching `^[a-z0-9]+(-[a-z0-9]+)*$` and are never renamed.
- `domains` draws on a closed vocabulary. Task 2 widens it from ten to twelve: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`, `regulation`, `eco`, `fin-man`. **No task before Task 2 may use `eco` or `fin-man`, and every task after it may.**
- `anchor` follows `<body>.<subject>.<section>[.<item>]`, lowercase and dot-separated, three or four segments, or the literal `chosen`. A three-level syllabus hyphenates its third level into the item segment: CS2 item 1.1.5 is `ifoa.cs2.1.1-5`. Task 7's mapping table is binding and no transcriber invents its own.
- Writing rules apply to every file, this plan included: British English, and no em or en dashes as punctuation. Write currency with the unit word rather than a bare dollar sign, because every `$` on a page is a maths delimiter.
- Conventional Commits, one concern per commit. **Commit with explicit paths rather than `git add -A`:** the coordinator commits plan corrections to this branch while implementers work, and a `-A` in that window sweeps them in. It happened once in Phase 0.
- `check.py` runs on every commit through `.githooks/pre-commit`, and it validates the **working tree** rather than the index.

## The standing instruction, carried in every dispatch

Phase 0's biggest process lesson was that twelve tests across nine of fourteen tasks shipped green under the exact bug they named. The fix was a standing instruction to check whether each test would actually fail under the bug it names, and to report rather than silently patch. Seven were caught that way.

Phase 1 has almost no tests, so the lesson translates rather than transfers. **`check.py` passing is not evidence that a batch of nodes is right.** It verifies referential integrity, acyclicity, path teachability and symbol resolution. It verifies nothing about whether an anchor points at a section that exists in the document it names, whether grain is consistent with the rest of the corpus, or whether `requires` is pedagogically ordered rather than merely acyclic. Every dispatch in Waves 1 and 2 therefore ends with:

> After `check.py` passes, report what it did **not** verify about your batch. Specifically: name three anchors you emitted and quote the heading each one points at from the source document, so the mapping is demonstrated rather than asserted. Report your node count against your document's item count and explain any ratio below 0.5 or above 1.5. Report any `requires` edge you were unsure about. **Measure rather than read**, and report rather than silently patch.

---

## File Structure

| Path | Responsibility |
|---|---|
| `sources/syllabi.yaml` | The 20 anchor bodies: id, title, issuer, URL, SHA-256, retrieval date, anchor prefix. Committed; the PDFs it points at are not. |
| `scripts/fetch_syllabi.py` | Downloads the manifest's documents into gitignored `data/syllabi/` and verifies each SHA-256. Records hashes on a first run, verifies on every later one. |
| `scripts/alchemist/model.py:18-21` | `DOMAINS` widens from ten to twelve. |
| `scripts/alchemist/checks.py` | `check_gap_closure` and `check_ledger_references_resolve` harden against a malformed ledger entry. |
| `scripts/alchemist/staging.py` | New. Merges the per-body staging directories into `nodes/`, unioning `anchor`, `domains`, `requires`, `spends`, and reports every merge. Pure functions over dictionaries; the I/O sits in `merge_staging.py`. |
| `scripts/alchemist/grain.py` | New. The grain audit. Emits numbers rather than judgements. |
| `scripts/alchemist/site.py` | Gains `render_review(corpus)`, the gate-2 document, wired into `build()`. |
| `scripts/merge_staging.py` | CLI entry point for the merge. |
| `scripts/grain_audit.py` | CLI entry point for the grain audit. |
| `scripts/katex_sweep.py` | Gains `.md` and `.yaml` handling so node bodies, `objects.yaml` aliases and `symbols.md` are swept alongside `.qmd`. |
| `notation/objects.yaml` | Gains an `ml` alias on `obj.hazard` and four reserving objects, taking the contract from twelve objects to sixteen. |
| `notes/transcription-brief.md` | The document every Wave 1 agent reads. Anchor mapping table, granularity rule with worked examples, slug conventions, domain assignment, the staging contract. |
| `.gitignore` | Gains `.superpowers/` so the staging directory is ignored. **It is not ignored today:** `git check-ignore .superpowers/` exits 1, and the only thing keeping Phase 0's workspace out of git is a nested `.superpowers/sdd/.gitignore` that a `phase-1/` sibling does not inherit. |
| `.superpowers/phase-1/<body>/` | Per-body staging, ignored once Task 1 widens `.gitignore`. |
| `nodes/<id>.md` | The deliverable, after the merge. |
| `paths/<id>.yaml` | Ten path files, two of which already exist. |
| `sources/wanted.yaml` | The gap ledger, seeded. |
| `site/review.md` | Generated. What gate 2 reads. |
| `tests/test_staging.py`, `tests/test_grain.py` | New test modules, one per new concern, following `tests/`'s existing flat layout. |

---

# Wave 0: preparation

Seven tasks, run in order, before any transcription agent is dispatched. Tasks 2 to 6 each change something a Wave 1 agent depends on, and changing any of them mid-flight invalidates work already staged.

---

### Task 1: The syllabus manifest and the fetcher

**Files:**
- Create: `sources/syllabi.yaml`
- Create: `scripts/fetch_syllabi.py`
- Test: `tests/test_fetch_syllabi.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `sources/syllabi.yaml` with one entry per body carrying `id`, `title`, `issuer`, `anchor_prefix`, `url`, `filename`, `sha256`, `retrieved`, `licence_note`. `scripts/fetch_syllabi.py` exposing `load_manifest(path: Path = MANIFEST) -> list[dict]`, `digest(path: Path) -> str`, `verify(path: Path, expected: str) -> bool` and `fetch(entry: dict, target: Path) -> tuple[str, str]`.

The manifest is the reason this task exists. A syllabus is revised annually and the URLs carry opaque media ids (`/media/lbujcuwo/cs2_syllabus-2026-_final-proof.pdf`), so a node anchored at `ifoa.cs2.1.1-5` is anchored against a specific document that has to be identifiable in two years. Recording the SHA-256 makes "the CS2 syllabus" mean one file rather than whichever one is current.

**Two things the fetcher must not do.** It must not run in a test: `tests/` makes no network call anywhere in this repo, and `tests/test_render_chain.py` sets the precedent of skipping cleanly rather than reaching out. So the test covers `digest` and `verify` against a local temporary file only. And it must not overwrite a file whose hash already matches, because re-downloading 15 PDFs to prove they are unchanged wastes the manifest's whole point.

- [ ] **Step 1: Write the manifest**

The 20 bodies, of which 15 carry URLs verified as free public downloads on 4 September 2026. Leave every `sha256` as `null`; Step 5 fills them.

```yaml
# The 20 anchor bodies Phase 1 transcribes. Every entry is a free public
# download: no login, no payment, no click-through licence.
#
# The PDFs land in data/syllabi/, which is gitignored, so this file is the
# only committed record that a node anchored at ifoa.cs2.1.1-5 is anchored
# against one identifiable document rather than against "the CS2 syllabus",
# which is revised annually and served from an opaque media id.
#
# sha256 is recorded on the first fetch and verified on every later one.
# A mismatch means the body republished, which is a decision for you rather
# than something the fetcher should paper over.
- id: ifoa-cs1-2026
  title: "Actuarial Statistics (CS1) Core Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cs1
  url: "https://actuaries.org.uk/media/5xzbwoyf/cs1_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cs1-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-cs2-2026
  title: "Risk Modelling and Survival Analysis (CS2) Core Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cs2
  url: "https://actuaries.org.uk/media/lbujcuwo/cs2_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cs2-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-cm1-2026
  title: "Actuarial Mathematics for Modelling (CM1) Core Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cm1
  url: "https://actuaries.org.uk/media/yfnkmkbq/cm1_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cm1-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-cm2-2026
  title: "Economic Modelling (CM2) Core Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cm2
  url: "https://actuaries.org.uk/media/vlino2en/cm2_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cm2-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-cb2-2026
  title: "Business Economics (CB2) Core Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cb2
  url: "https://actuaries.org.uk/media/c5sfq0cz/cb2_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cb2-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-cp1-2026
  title: "Actuarial Practice (CP1) Core Principals, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.cp1
  url: "https://actuaries.org.uk/media/or2gteyh/cp1_syllabus-2026-_final-proof.pdf"
  filename: ifoa-cp1-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp1-2026
  title: "Health and Care (SP1) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp1
  url: "https://actuaries.org.uk/media/xznnhvy3/sp1_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp1-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp2-2026
  title: "Life Insurance (SP2) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp2
  url: "https://actuaries.org.uk/media/0tzb1l3z/sp2_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp2-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp5-2026
  title: "Investment and Finance (SP5) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp5
  url: "https://actuaries.org.uk/media/i5mhdpbr/sp5_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp5-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp6-2026
  title: "Financial Derivatives (SP6) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp6
  url: "https://actuaries.org.uk/media/rnaebhef/sp6_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp6-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp7-2026
  title: "General Insurance Reserving and Capital Modelling (SP7) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp7
  url: "https://actuaries.org.uk/media/2dinpmq4/sp7_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp7-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp8-2026
  title: "General Insurance Pricing (SP8) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp8
  url: "https://actuaries.org.uk/media/wd5dljtc/sp8_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp8-2026.pdf
  sha256: null
  retrieved: null
- id: ifoa-sp9-2026
  title: "Enterprise Risk Management (SP9) Specialist Principles, syllabus for the 2026 examinations"
  issuer: "Institute and Faculty of Actuaries"
  anchor_prefix: ifoa.sp9
  url: "https://actuaries.org.uk/media/ui2fyvbf/sp9_syllabus-2026-_final-proof.pdf"
  filename: ifoa-sp9-2026.pdf
  sha256: null
  retrieved: null
- id: assa-f107-2026
  title: "Banking Principles (F107 / B100), Fellowship Principles syllabus for the 2026 examinations"
  issuer: "Actuarial Society of South Africa"
  anchor_prefix: assa.f107
  url: "https://www.actuarialsociety.org.za/wp-content/uploads/2025/12/Subject-F107_B100-Banking-Principles-_2026_Clean.pdf"
  filename: assa-f107-2026.pdf
  sha256: null
  retrieved: null
- id: assa-f207-2026
  title: "Banking Applications (F207 / B200), Fellowship Applications syllabus for the 2026 examinations"
  issuer: "Actuarial Society of South Africa"
  anchor_prefix: assa.f207
  url: "https://www.actuarialsociety.org.za/wp-content/uploads/2025/12/Subject-F207_B200-Banking-Applciations-2026_Clean.pdf"
  filename: assa-f207-2026.pdf
  sha256: null
  retrieved: null
```

Five entries have no download URL and are transcribed from documents already on disk. Record them in the same file so the manifest is the single list of bodies, with `url: null` and a `local` key naming where the source sits.

```yaml
- id: bcbs-d424
  title: "Basel III: finalising post-crisis reforms (d424)"
  issuer: "Basel Committee on Banking Supervision"
  anchor_prefix: bcbs.d424
  url: null
  local: "${ALCHEMIST_VAULT}/markdown/bcbs/d424.md"
  filename: null
  sha256: null
  retrieved: null
  note: >
    Held in the vault rather than downloaded. The vault is a separate private
    repo, so this entry names a path rather than carrying the text. Anchors
    are paragraph references, spelled bcbs.d424.irb.para-220.
- id: iasb-ifrs9
  title: "IFRS 9 Financial Instruments"
  issuer: "International Accounting Standards Board"
  anchor_prefix: iasb.ifrs9
  url: null
  local: "${ALCHEMIST_VAULT}/markdown/ifrs/ifrs9_standard.md"
  filename: null
  sha256: null
  retrieved: null
  note: >
    Anchors are clause references with the final level hyphenated, so clause
    5.5.1 is iasb.ifrs9.5.5-1. Chapter 5.5 on impairment is the section the
    credit trunk actually needs.
- id: eth-dl-actuarial-2026
  title: "Deep Learning for Actuarial Modelling, ETH summer school, twelve lectures"
  issuer: "ETH Zurich"
  anchor_prefix: eth.dl-actuarial-2026
  url: null
  local: "~/Documents/Repos/actuarial_deep_learning/lectures/"
  filename: null
  sha256: null
  retrieved: null
  licence_note: >
    CC BY-NC 4.0. Reuse, remix and adaptation are permitted for
    non-commercial purposes only, with attribution and a statement of
    changes, both carried in README.md. Anchors are lecture numbers,
    eth.dl-actuarial-2026.l01 through .l12, where l04 covers the combined
    04-05 lecture and l10 the combined 10-11.
- id: up-02133413
  title: "BSc (Actuarial and Financial Mathematics), University of Pretoria Yearbook 2026"
  issuer: "University of Pretoria"
  anchor_prefix: up
  url: null
  local: "~/Downloads/Programme-02133413.pdf"
  filename: up-02133413.pdf
  sha256: null
  retrieved: null
  note: >
    Anchors take the module code as the subject segment: up.wst311.4 for
    WST 311 section 4. Copy the PDF into data/syllabi/ rather than reading
    it from Downloads, so the manifest's hash means something.
- id: up-02240278
  title: "BScHons (Actuarial Science), University of Pretoria Yearbook 2023"
  issuer: "University of Pretoria"
  anchor_prefix: up
  url: null
  local: "~/Downloads/Programme-02240278.pdf"
  filename: up-02240278.pdf
  sha256: null
  retrieved: null
  note: >
    Honours modules take up.iashons<number>.<section>, so IAS 712 section 2
    is up.iashons712.2.
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_fetch_syllabi.py
"""The fetcher's hashing, tested without a network call.

Nothing in tests/ reaches the network, so the download itself is not under
test. What is under test is the part that would silently accept a wrong file.
"""

import hashlib

import pytest
import yaml

from scripts.fetch_syllabi import digest, load_manifest, verify

REPO_MANIFEST = "sources/syllabi.yaml"


def test_digest_matches_hashlib(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"%PDF-1.7 not really a pdf")
    assert digest(target) == hashlib.sha256(target.read_bytes()).hexdigest()


def test_verify_accepts_a_matching_digest(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"contents")
    assert verify(target, digest(target)) is True


def test_verify_rejects_a_changed_file(tmp_path):
    target = tmp_path / "doc.pdf"
    target.write_bytes(b"contents")
    recorded = digest(target)
    target.write_bytes(b"the body republished")
    assert verify(target, recorded) is False


def test_verify_rejects_a_missing_file(tmp_path):
    assert verify(tmp_path / "absent.pdf", "0" * 64) is False


def test_the_manifest_names_twenty_bodies():
    entries = load_manifest()
    assert len(entries) == 20


def test_every_manifest_entry_carries_an_anchor_prefix():
    for entry in load_manifest():
        assert entry["anchor_prefix"], f"{entry['id']} has no anchor_prefix"


def test_every_downloadable_entry_carries_a_filename():
    for entry in load_manifest():
        if entry.get("url"):
            assert entry.get("filename"), f"{entry['id']} has a url and no filename"
```

- [ ] **Step 3: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_fetch_syllabi.py -v`
Expected: FAIL, collection error, `ModuleNotFoundError: No module named 'scripts.fetch_syllabi'`.

- [ ] **Step 4: Write the fetcher**

```python
# scripts/fetch_syllabi.py
"""Download the anchor bodies named in sources/syllabi.yaml into data/syllabi/.

A syllabus is revised annually and its URL carries an opaque media id, so
recording the SHA-256 is what makes "the CS2 syllabus" name one identifiable
document rather than whichever one is current. A hash mismatch is reported
rather than papered over: the body republished, and whether the corpus follows
is a decision rather than a download.

data/ is gitignored, so nothing this script writes is ever committed.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import urllib.request
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "sources" / "syllabi.yaml"
TARGET = REPO / "data" / "syllabi"


def load_manifest(path: Path = MANIFEST) -> list[dict]:
    return yaml.safe_load(path.read_text()) or []


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path, expected: str) -> bool:
    """False rather than an exception, because a missing file and a changed one
    are the same answer to the caller: this is not the document recorded."""
    if not path.is_file():
        return False
    return digest(path) == expected


def fetch(entry: dict, target: Path) -> tuple[str, str]:
    """Return (status, detail). Never raises on a hash mismatch: the caller
    decides, because a republished syllabus is a corpus question."""
    if not entry.get("url"):
        if not entry.get("filename"):
            return "local", f"{entry['id']}: no url, transcribed from {entry.get('local')}"
        # A local entry that names a filename has been copied into data/syllabi/
        # by hand, and its provenance is worth exactly as much as a downloaded
        # one. Hash it rather than waving it through, or the manifest records a
        # document nobody can identify later.
        destination = target / entry["filename"]
        if not destination.is_file():
            return "absent", f"{entry['id']}: expected {destination.name}, copy it in first"
        found = digest(destination)
        recorded = entry.get("sha256")
        if recorded is None:
            return "recorded", f"{entry['id']}: {found}"
        if found != recorded:
            return "mismatch", f"{entry['id']}: recorded {recorded}, found {found}"
        return "current", f"{entry['id']}: unchanged"
    destination = target / entry["filename"]
    recorded = entry.get("sha256")
    if recorded and verify(destination, recorded):
        return "current", f"{entry['id']}: unchanged"
    target.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(entry["url"]) as response:
        destination.write_bytes(response.read())
    found = digest(destination)
    if recorded is None:
        return "recorded", f"{entry['id']}: {found}"
    if found != recorded:
        return "mismatch", f"{entry['id']}: recorded {recorded}, found {found}"
    return "fetched", f"{entry['id']}: {found}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-hashes", action="store_true",
        help="record a newly computed digest back into the manifest",
    )
    args = parser.parse_args()

    entries = load_manifest()
    statuses: list[str] = []
    for entry in entries:
        status, detail = fetch(entry, TARGET)
        statuses.append(status)
        print(f"{status:9} {detail}")
        if status == "recorded" and args.write_hashes:
            entry["sha256"] = digest(TARGET / entry["filename"])
            entry["retrieved"] = date.today().isoformat()

    if args.write_hashes:
        MANIFEST.write_text(yaml.safe_dump(entries, sort_keys=False, width=88))
        print(f"\nmanifest updated: {MANIFEST.relative_to(REPO)}")

    mismatches = statuses.count("mismatch")
    print(f"\n{len(entries)} bodies, {mismatches} hash mismatches")
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_fetch_syllabi.py -v`
Expected: PASS, seven tests.

- [ ] **Step 6: Fetch the documents and record the hashes**

```bash
cd ~/Documents/Repos/alchemist
cp ~/Downloads/Programme-02133413.pdf data/syllabi/up-02133413.pdf
cp ~/Downloads/Programme-02240278.pdf data/syllabi/up-02240278.pdf
.venv/bin/python scripts/fetch_syllabi.py --write-hashes
```

Expected: **seventeen** lines reading `recorded`, being the fifteen downloads plus the two copied UP programmes, and **three** reading `local`, being BCBS d424, IFRS 9 and the ETH course, none of which is a file in `data/syllabi/`. Then `0 hash mismatches`.

Re-run without `--write-hashes` and all seventeen should read `current`, which is the proof that the recorded hashes are the ones on disk. A line reading `absent` means a UP programme was not copied in at Step 6's first two commands, and the manifest would otherwise carry a null hash for a document the corpus anchors against.

- [ ] **Step 7: Extract the text every transcriber will read**

```bash
cd ~/Documents/Repos/alchemist/data/syllabi
for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done
ls -la *.txt | wc -l
```

Expected: seventeen text files. `pdftotext -layout` preserves the indentation that carries the syllabus hierarchy, and without `-layout` the numbering runs together and the level of an item becomes a guess. Install poppler with `brew install poppler` if it is absent.

- [ ] **Step 8: Verify the extraction is readable**

Run: `head -60 data/syllabi/ifoa-cs2-2026.txt`
Expected: the topic weightings table and the opening of objective 1, with `1.1` and `1.1.1` visibly indented at different depths. If a document extracts as a single unindented run, record it in the task report rather than working around it: that body needs a different extraction and the transcriber must be told.

- [ ] **Step 9: Ignore the staging directory before anything writes to it**

Wave 1 writes roughly 1,400 stub files into `.superpowers/phase-1/`, and **that path is not
ignored today.** Measured on 4 September 2026: `git check-ignore -v .superpowers/` exits 1, and
what keeps Phase 0's workspace out of git is a nested `.superpowers/sdd/.gitignore` carrying a
single `*`, which a `phase-1/` sibling does not inherit. Left alone, `git status` becomes
unreadable at exactly the point the coordinator most needs to read it.

```bash
cd ~/Documents/Repos/alchemist
printf '.superpowers/\n' >> .gitignore
git check-ignore -v .superpowers/phase-1/ && echo "staging is ignored"
```

Expected: the `check-ignore` line naming `.gitignore` as the source, then `staging is ignored`.
Phase 0's workspace stays exactly where it is; its own nested file becomes redundant rather
than wrong, and removing it is not this plan's business.

- [ ] **Step 10: Commit**

```bash
git add sources/syllabi.yaml scripts/fetch_syllabi.py tests/test_fetch_syllabi.py .gitignore
git commit -m "feat(sources): record the 20 anchor bodies and fetch them reproducibly"
```

---

### Task 2: Widen the domain vocabulary to twelve

**Files:**
- Modify: `scripts/alchemist/model.py:18-21`
- Modify: `CLAUDE.md`, the "Closed domain vocabulary" section
- Modify: `docs/superpowers/plans/2026-09-03-alchemist-phase-0.md`, the Global Constraints line
- Test: `tests/test_model.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `DOMAINS` containing twelve entries. Every later task may use `eco` and `fin-man`.

Gate 1 fixed the body list at 20 documents, and CB2 is business economics while CP1 is actuarial practice. Neither has anywhere to sit in a ten-domain vocabulary, and routing them into `actuarial` would make check 2, which is scoped to a domain, weaker for no gain. Spec section 4.1 has listed twelve since design time and the code enforced ten, so this closes a known divergence rather than opening a new one.

**All three files change in one commit.** `CLAUDE.md` states outright that adding a domain means updating `DOMAINS` and its own list together, and the Phase 0 plan's Global Constraints carries a third copy.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_model.py`:

```python
def test_the_vocabulary_carries_twelve_domains():
    """CB2 economics and CP1 actuarial practice entered the corpus at gate 1,
    and neither has anywhere to sit in the ten-domain vocabulary."""
    assert DOMAINS == frozenset({
        "maths", "stats", "ml", "data-eng", "fin-eng", "actuarial",
        "life", "gi", "credit", "regulation", "eco", "fin-man",
    })


def test_accepts_a_node_in_the_two_new_domains(tmp_path):
    widened = VALID.replace("[stats, credit]", "[eco, fin-man]")
    node = parse_node(write(tmp_path, "hazard-rate.md", widened))
    assert node.domains == ("eco", "fin-man")
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_model.py -k "twelve or two_new" -v`
Expected: FAIL. The first on the set comparison, the second with `ValueError: unknown domains`.

- [ ] **Step 3: Widen the constant**

`scripts/alchemist/model.py`, replacing lines 18 to 21:

```python
DOMAINS = frozenset({
    "maths", "stats", "ml", "data-eng", "fin-eng",
    "actuarial", "life", "gi", "credit", "regulation",
    "eco", "fin-man",
})
```

- [ ] **Step 4: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_model.py -v`
Expected: PASS, every test in the module.

- [ ] **Step 5: Update the two prose copies**

In `CLAUDE.md`, replace the "Closed domain vocabulary" body with:

```markdown
`domains` draws on a closed vocabulary, because check 2 is scoped to a single domain and an
open vocabulary would make that check meaningless. The list enforced by
`scripts/alchemist/model.py`'s `DOMAINS` constant is:

`maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`,
`regulation`, `eco`, `fin-man`.

It carried ten until Phase 1 Task 2, which added `eco` and `fin-man` and so closed the
divergence from spec section 4.1, which has listed twelve since design time. Adding a domain
means updating `DOMAINS` and this list together, in the same commit.
```

Two further passages in `CLAUDE.md` were settled at gate 1 and are stale. Replace the body of
its "Anchor grammar" section from "lowercase and dot-separated" onwards with:

```markdown
lowercase and dot-separated, three or four segments: `ifoa.cs2.3.2`, `assa.f107.4.1`,
`bcbs.d424.irb.para-220`, `eth.dl-actuarial-2026.l02`. Phase 1 populates this field across 20
anchor bodies in parallel, so the grammar is stated here rather than left to each transcriber
to invent.

A body numbering three levels deep hyphenates its third level into the item segment, because
the grammar allows four segments at most: CS2 item 1.1.5 is `ifoa.cs2.1.1-5`, following the
precedent `bcbs.d424.irb.para-220` sets for a composite final segment. Each body maps into the
grammar differently, and the per-body table is in `notes/transcription-brief.md`.
```

And in its "The two tiers" section, replace "for all 400 to 600 expected nodes" with "for all
1,100 to 1,400 nodes the corpus holds".

In `docs/superpowers/plans/2026-09-03-alchemist-phase-0.md`, replace the Global Constraints line:

```markdown
- `domains` draws on a closed vocabulary: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`, `regulation`. Widened to twelve by Phase 1 Task 2, which added `eco` and `fin-man`.
```

- [ ] **Step 6: Run the full suite and the checks**

Run: `.venv/bin/python -m pytest && .venv/bin/python scripts/check.py`
Expected: every test passes, nine checks report `ok`.

- [ ] **Step 7: Commit**

```bash
git add scripts/alchemist/model.py tests/test_model.py CLAUDE.md docs/superpowers/plans/2026-09-03-alchemist-phase-0.md
git commit -m "feat(model): widen the domain vocabulary to twelve"
```

---

### Task 3: Harden the two ledger checks against a malformed entry

**Files:**
- Modify: `scripts/alchemist/checks.py`, `check_gap_closure` and `check_ledger_references_resolve`
- Test: `tests/test_checks_sources.py`

**Interfaces:**
- Consumes: nothing.
- Produces: both checks returning failures rather than raising, on every malformed shape.

This is one of the three findings Phase 0 parked with a ruling, and Phase 1 seeds the ledger it guards, so it is fixed before the seeding rather than after. **The crash modes were measured on 4 September 2026 rather than read off the source**, and there are two:

| Ledger shape | `check_gap_closure` | `check_ledger_references_resolve` |
|---|---|---|
| An entry that is a bare string, not a mapping | `AttributeError: 'str' object has no attribute 'get'` | same |
| The whole file is a mapping, not a list | `AttributeError: 'str' object has no attribute 'get'`, because iterating a dict yields its keys | same |
| An entry with no `id`, whose `needed_by` names an unknown node | 0 failures, correctly | `KeyError: 'id'` |

Note the third row, because it is the one reading the code does not give you. `check_gap_closure` never touches `entry['id']` unless it has already found a reviewed node, so a missing `id` is harmless there and fatal in rule 9. A test written from the source alone would likely have asserted both crash, and would have shipped green against the wrong behaviour.

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_checks_sources.py`:

```python
MALFORMED = {
    "an entry that is a bare string": "- just-a-string\n",
    "a ledger that is a mapping": "id: not-a-list\nneeded_by: [x]\n",
    "an entry with no id": "- needed_by: [no-such-node]\n  status: wanted\n",
    "an entry whose needed_by is a string": "- id: e\n  needed_by: oops\n  status: wanted\n",
}


def _ledger(tmp_path, body):
    (tmp_path / "sources").mkdir(exist_ok=True)
    (tmp_path / "sources" / "wanted.yaml").write_text(body)
    return tmp_path


@pytest.mark.parametrize("shape", sorted(MALFORMED))
def test_gap_closure_reports_rather_than_crashes(tmp_path, shape):
    result = check_gap_closure(one_node_corpus(), root=_ledger(tmp_path, MALFORMED[shape]))
    assert result.failures, f"{shape}: expected a recorded failure"
    assert "malformed" in " ".join(result.failures).lower()


@pytest.mark.parametrize("shape", sorted(MALFORMED))
def test_ledger_references_report_rather_than_crash(tmp_path, shape):
    result = check_ledger_references_resolve(
        one_node_corpus(), root=_ledger(tmp_path, MALFORMED[shape])
    )
    assert result.failures, f"{shape}: expected a recorded failure"


def test_a_well_formed_ledger_still_passes(tmp_path):
    body = (
        "- id: some-source\n"
        "  needed_by: [conditional-probability]\n"
        "  status: wanted\n"
    )
    root = _ledger(tmp_path, body)
    assert check_gap_closure(one_node_corpus(), root=root).failures == []
    assert check_ledger_references_resolve(one_node_corpus(), root=root).failures == []
```

**Two things about this module, checked by reading it rather than assumed.** It does **not**
import `pytest`, so add `import pytest` at the top or every `@pytest.mark.parametrize` above is a
`NameError`. And it has no `one_node_corpus()`: what it has is `node(node_id, status=...)`, which
returns a single `Node`. Build the corpus from that rather than inventing a second fixture beside
a working one:

```python
def one_node_corpus() -> Corpus:
    """A corpus of one stub node, so the ledger checks have something to resolve against.

    Built on this module's existing `node()` helper rather than beside it, because a second
    fixture returning the same shape is how two fixtures drift apart.
    """
    return Corpus(nodes={"conditional-probability": node("conditional-probability")}, paths={})
```

- [ ] **Step 2: Run the tests and verify they fail, and verify they fail for the right reason**

Run: `.venv/bin/python -m pytest tests/test_checks_sources.py -k "malformed or rather_than" -v`
Expected: FAIL, and **each failure must be the `AttributeError` or `KeyError` from the table above rather than an assertion failure**. A test that fails on `assert result.failures` has not exercised the crash. Run with `-x --tb=short` and read the exception type on each parametrised case. Report the eight exception types you actually saw.

- [ ] **Step 3: Harden both checks**

Replace both functions in `scripts/alchemist/checks.py`:

```python
def _ledger_entries(ledger: Path) -> tuple[list[dict], list[str]]:
    """Read the ledger defensively and return (usable entries, complaints).

    A malformed entry has to become a recorded failure rather than a stack
    trace, because Phase 1 seeds this ledger and a trace mid-run costs more to
    diagnose than the guard costs to write. The shapes that used to crash were
    measured rather than guessed: a bare string in the list, a mapping where a
    list belongs, and a missing `id` reached only through rule 9's failure path.
    """
    raw = yaml.safe_load(ledger.read_text())
    if raw is None:
        return [], []
    if not isinstance(raw, list):
        return [], [
            f"{ledger.name}: malformed, the file is a "
            f"{type(raw).__name__} where a list of entries belongs"
        ]
    entries, complaints = [], []
    for position, entry in enumerate(raw, start=1):
        if not isinstance(entry, dict):
            complaints.append(
                f"{ledger.name}: malformed entry {position}, a "
                f"{type(entry).__name__} where a mapping belongs"
            )
            continue
        if "id" not in entry:
            complaints.append(f"{ledger.name}: malformed entry {position}, no id")
            continue
        needed = entry.get("needed_by") or []
        if not isinstance(needed, list):
            complaints.append(
                f"{entry['id']}: malformed needed_by, a "
                f"{type(needed).__name__} where a list of node ids belongs"
            )
            continue
        entries.append(entry)
    return entries, complaints


def check_gap_closure(corpus: Corpus, root: Path = REPO) -> Result:
    result = Result("6. no reviewed node carries an open source gap")
    ledger = root / "sources" / "wanted.yaml"
    if not ledger.is_file():
        result.skipped = f"no ledger at {ledger}"
        return result
    entries, complaints = _ledger_entries(ledger)
    result.failures.extend(complaints)
    for entry in entries:
        if entry.get("status") == "ingested":
            continue
        for node_id in entry["needed_by"] or []:
            node = corpus.nodes.get(node_id)
            if node is not None and node.status == "reviewed":
                result.failures.append(
                    f"{node_id}: reviewed, but gap {entry['id']!r} is still "
                    f"{entry.get('status')!r}"
                )
    return result


def check_ledger_references_resolve(corpus: Corpus, root: Path = REPO) -> Result:
    """A mistyped id in `needed_by` disables check 6 for that node, silently.

    Check 6 looks each id up with `corpus.nodes.get` and moves on where it finds
    nothing, which is correct for its own rule and useless as a guard. So the
    only thing standing between one typo and a permanently unenforced gap is
    this rule.
    """
    result = Result("9. every ledger reference resolves")
    ledger = root / "sources" / "wanted.yaml"
    if not ledger.is_file():
        result.skipped = f"no ledger at {ledger}"
        return result
    entries, complaints = _ledger_entries(ledger)
    result.failures.extend(complaints)
    for entry in entries:
        for node_id in entry["needed_by"] or []:
            if node_id not in corpus.nodes:
                result.failures.append(
                    f"{entry['id']}: needed_by names unknown node {node_id!r}, "
                    f"so check 6 can never enforce this gap"
                )
    return result
```

- [ ] **Step 4: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_checks_sources.py -v`
Expected: PASS, every test in the module including the pre-existing ones.

- [ ] **Step 5: Verify the tests would fail under the bug they name**

Revert `_ledger_entries` to a one-line `return yaml.safe_load(ledger.read_text()) or [], []` and re-run. Every parametrised malformed case must fail. Restore the hardened version. **Report what you observed**, not what you expected: this is the check that catches a test asserting something the bug never touched.

- [ ] **Step 6: Update the ruling and commit**

Add to `docs/superpowers/rulings-phase-0.md`, under the parked findings:

```markdown
**Closed by Phase 1 Task 3.** The two ledger checks crashed rather than recording a failure
on a malformed entry. Three shapes were measured on 4 September 2026: a bare string in the
list and a mapping where the list belongs both raised `AttributeError` in either check, and an
entry with no `id` whose `needed_by` named an unknown node raised `KeyError` in rule 9 alone,
because check 6 never reaches `entry['id']` unless it has already found a reviewed node. Both
now share `_ledger_entries`, which reports each shape as a failure naming the entry's position.
```

```bash
git add scripts/alchemist/checks.py tests/test_checks_sources.py docs/superpowers/rulings-phase-0.md
git commit -m "fix(checks): report a malformed ledger entry rather than crashing"
```

---

### Task 4: Give the hazard an ml alias and settle the regularisation note

**Files:**
- Modify: `notation/objects.yaml`
- Modify: `notation/symbols.md`, by regeneration only
- Test: `tests/test_notation.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `obj.hazard` carrying five aliases including `ml`. `obj.regularisation` carrying a complete note.

Deep survival models are machine learning, so the trunk's `S3_deep-survival-credit` lecture will produce `ml` nodes that spend the hazard. Check 1 has no fallback to the canonical rendering, so a node spending `obj.hazard` in `ml` fails today with `obj.hazard has no alias for domain 'ml'`. Adding the alias costs one line and is the review moment the strict rule exists to force.

The alias is `h(t)`, matching credit and the canonical, because the deep survival literature writes the hazard that way and inventing an `ml` spelling would make the corpus look wrong to the field the node is written for.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_notation.py`:

```python
def test_the_hazard_carries_an_ml_alias():
    """Deep survival models are machine learning, and check 1 has no fallback
    to the canonical rendering, so an ml node spending the hazard fails without
    this alias."""
    objects = load_objects(REPO)
    assert objects.rendering(Spend("obj.hazard", "ml")) == "h(t)"


def test_the_regularisation_note_survived_its_commas():
    """Three notes were truncated at their first comma before load_objects
    started rejecting unknown alias keys. This one lost the reason it existed."""
    objects = load_objects(REPO)
    alias = objects.by_id["obj.regularisation"].for_domain("ml")
    assert "hazard" in alias.note
    assert len(alias.note) > 60
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_notation.py -k "ml_alias or commas" -v`
Expected: FAIL. The first with `LookupError: obj.hazard has no alias for domain 'ml'`.

- [ ] **Step 3: Edit the contract**

In `notation/objects.yaml`, add one alias line under `obj.hazard`:

```yaml
    - {domain: ml, symbol: 'h(t)', name: hazard, note: "deep survival models write the hazard as the credit and canonical spelling do, so no ml spelling is invented"}
```

And replace `obj.regularisation`'s `ml` alias line with a note that carries its reason:

```yaml
    - {domain: ml, symbol: '\lambda_{\mathrm{reg}}', name: regularisation weight, note: "subscripted deliberately: bare lambda is the claim intensity in gi and the hazard function in stats, and once obj.hazard carries an ml alias a node spending both objects in ml would fail check 1 with no remedy"}
```

**Quote every note.** An alias is a YAML flow mapping, so an unquoted note ends at its first comma and the remainder parses as a bare key with a null value. That is exactly what happened to this note.

- [ ] **Step 4: Regenerate the symbol table**

Run: `.venv/bin/python scripts/build_site.py`
`notation/symbols.md` is generated and never hand-edited, and check 7 compares it against what `objects.yaml` would produce.

- [ ] **Step 5: Run the tests and the checks**

Run: `.venv/bin/python -m pytest tests/test_notation.py -v && .venv/bin/python scripts/check.py`
Expected: PASS, and nine checks `ok`. Check 2 in particular must stay green: `h(t)` in `ml` collides with nothing, because no other object claims that rendering in that domain.

- [ ] **Step 6: Commit**

```bash
git add notation/objects.yaml notation/symbols.md tests/test_notation.py
git commit -m "feat(notation): give the hazard an ml alias and restore the regularisation note"
```

---

### Task 5: Seed the reserving vocabulary and sweep for others the trunk omits

**Files:**
- Modify: `notation/objects.yaml`
- Modify: `notation/symbols.md`, by regeneration only
- Create: `notes/vocabulary-sweep-2026-09-04.md`
- Test: `tests/test_notation.py`

**Interfaces:**
- Consumes: Task 4's edits to the same file.
- Produces: sixteen objects in `objects.yaml`, up from twelve.

The twelve seeded objects were derived from credit, life and general insurance **as the ETH course frames them**, which is a modelling frame rather than a reserving one. The general-insurance reserving vocabulary is therefore absent by construction rather than by oversight. `notes/uni-programme-anchors.md` requires four objects, and it also requires a sweep for other whole vocabularies the same framing omits, because one such gap implies others.

**Why the collisions are real.** A run-off triangle is an accident-period by development-period array, and its credit twin is the origination-cohort by months-on-book array that IFRS 9 and IRB use daily. The objects collide the way the hazard does.

| Object | General insurance | Credit |
|---|---|---|
| Cohort index | accident period | origination vintage |
| Development index | development period | months on book, or months since default |
| Development factor | chain ladder link ratio | roll rate |
| Ultimate | ultimate claims | lifetime loss, or ultimate recovery |

- [ ] **Step 1: Write the failing test**

Add to `tests/test_notation.py`:

```python
RESERVING = {
    "obj.cohort-index": ("gi", "credit"),
    "obj.development-index": ("gi", "credit"),
    "obj.development-factor": ("gi", "credit"),
    "obj.ultimate": ("gi", "credit"),
}


@pytest.mark.parametrize("object_id,domains", sorted(RESERVING.items()))
def test_the_reserving_vocabulary_is_seeded(object_id, domains):
    """The twelve seeded objects came from the ETH course's modelling frame,
    which is not a reserving frame, so this vocabulary was missing entirely."""
    objects = load_objects(REPO)
    assert object_id in objects.by_id
    for domain in domains:
        assert objects.by_id[object_id].for_domain(domain) is not None


def test_the_contract_carries_at_least_sixteen_objects():
    """At least, and deliberately so. Step 4 tells the implementer to seed whatever the
    vocabulary sweep justifies, so an exact count would turn a correct judgement
    into a red test. The four that must be there are pinned by name above."""
    assert len(load_objects(REPO).by_id) >= 16
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_notation.py -k "reserving or seventeen" -v`
Add `import pytest` if the module lacks it; it does not, so no change is expected here.
Expected: FAIL, `KeyError` or an assertion on the count.

- [ ] **Step 3: Append the four objects**

```yaml
- id: obj.cohort-index
  name: Cohort index
  canonical: 'i'
  definition: The index of the period in which the exposure originated.
  aliases:
    - {domain: gi, symbol: 'i', name: accident period, note: "the row of a run-off triangle"}
    - {domain: credit, symbol: 'i', name: origination vintage, note: "the row of a vintage curve or a roll-rate matrix"}
- id: obj.development-index
  name: Development index
  canonical: 'j'
  definition: The index of elapsed time since the cohort originated.
  aliases:
    - {domain: gi, symbol: 'j', name: development period, note: "the column of a run-off triangle"}
    - {domain: credit, symbol: 'j', name: months on book, note: "months since origination, or months since default for a recovery profile"}
- id: obj.development-factor
  name: Development factor
  canonical: 'f_j'
  definition: The ratio carrying a cohort from one development index to the next.
  aliases:
    - {domain: gi, symbol: 'f_j', name: link ratio, note: "the chain ladder age-to-age factor"}
    - {domain: credit, symbol: 'r_j', name: roll rate, note: "the transition rate between delinquency buckets at development index j"}
- id: obj.ultimate
  name: Ultimate
  canonical: 'U_i'
  definition: The total the cohort reaches once development is complete.
  aliases:
    - {domain: gi, symbol: 'U_i', name: ultimate claims}
    - {domain: credit, symbol: 'U_i', name: lifetime loss, note: "or ultimate recovery where the array is a recovery profile"}
```

- [ ] **Step 4: Run the sweep for other omitted vocabularies and record it**

This is judgement rather than code, so it is a written note rather than an assertion. Work through the 20 bodies' topic headings and ask of each: does this vocabulary appear anywhere in `objects.yaml`, and would a practitioner in that field recognise the spelling the corpus would give it? Write `notes/vocabulary-sweep-2026-09-04.md` with a row per candidate, its verdict, and the reason. Candidates the body list makes likely, each of which must be checked rather than assumed:

- Multi-state and Markov notation, from CS2 topic 3 and UP WST 312. A transition intensity is `\mu_{ij}` in life and a rating transition matrix entry in credit, and neither is in the contract.
- Time-series notation, from CS2 topic 2 and UP WST 321. The backward shift operator and the ARIMA orders have no entry.
- Credibility notation, from UP WST 322 and SP8. The credibility factor `Z` is the direct ancestor of the trunk's Credibility Transformer.
- Ruin-theory notation, from UP WST 322. The adjustment coefficient and the surplus process.
- Interest and discount notation, from CM1. `v` is already in the contract as the life discount factor, so check what CM1 adds beyond it.
- Capital notation, from F107 and BCBS d424. Risk-weighted assets, the capital ratio and the correlation `R` already partly present.

**Seed only what a node will actually spend.** An object nothing spends is noise in the bridge table, and the contract's value is that every entry earns a reader's attention. Record the ones you rejected and why, because Phase 3 will meet them again.

- [ ] **Step 5: Regenerate, test and check**

Run: `.venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest tests/test_notation.py -v && .venv/bin/python scripts/check.py`
Expected: PASS, nine checks `ok`. Check 2 must stay green: `i` and `j` are claimed once each per domain, and `f_j` against `r_j` is exactly why the credit alias differs.

- [ ] **Step 6: Commit**

```bash
git add notation/objects.yaml notation/symbols.md tests/test_notation.py notes/vocabulary-sweep-2026-09-04.md
git commit -m "feat(notation): seed the reserving vocabulary and record the sweep"
```

---

### Task 6: Extend the KaTeX sweep beyond .qmd

**Files:**
- Modify: `scripts/katex_sweep.py`
- Test: `tests/test_katex_sweep.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `sweep(paths)` accepting `.md` and `.yaml` alongside `.qmd`; `spans_in(path) -> list[tuple[int, bool, str]]` dispatching on suffix.

`scripts/katex_sweep.py` takes `.qmd` only, and every node body's `$...$` goes through dollarmath into KaTeX's auto-render on a published page. An unsupported construct renders as red error text while every script exits zero, which is the failure this sweep exists to prevent and currently cannot see.

**The bigger exposure in Phase 1 is not node bodies.** Phase 1 produces stubs, whose bodies are nearly empty. What it does produce is four new notation objects whose aliases are raw TeX (`f_j`, `U_i`, `\mu_{ij}`), feeding a generated and committed `symbols.md`. A malformed alias there publishes red error text on the symbol table every reader of the corpus opens first.

- [ ] **Step 1: Write the failing test**

First widen the module's import line, which today reads
`from scripts.katex_sweep import extract_spans` and must become:

```python
from scripts.katex_sweep import extract_spans, spans_in, sweep
```

Then add to `tests/test_katex_sweep.py`:

```python
def test_extracts_spans_from_a_node_body(tmp_path):
    node = tmp_path / "hazard-rate.md"
    node.write_text(
        "---\nid: hazard-rate\ntitle: Hazard rate\n---\n\n"
        "The hazard is $h(t)$ and the survival function is $S(t)$.\n\n"
        "$$\nh(t) = -\\frac{d}{dt}\\log S(t)\n$$\n"
    )
    spans = spans_in(node)
    assert [tex.strip() for _, _, tex in spans] == [
        "h(t)", "S(t)", "h(t) = -\\frac{d}{dt}\\log S(t)",
    ]


def test_frontmatter_is_not_swept_as_mathematics(tmp_path):
    """A node's frontmatter is YAML, and a dollar in it is not a maths span."""
    node = tmp_path / "n.md"
    node.write_text("---\nid: n\ntitle: A $ sign and another $\n---\n\nBody.\n")
    assert spans_in(node) == []


def test_extracts_alias_symbols_from_objects_yaml(tmp_path):
    contract = tmp_path / "objects.yaml"
    contract.write_text(
        "- id: obj.hazard\n"
        "  name: Hazard\n"
        "  canonical: 'h(t)'\n"
        "  definition: The instantaneous rate.\n"
        "  aliases:\n"
        "    - {domain: life, symbol: '\\mu_x', name: force of mortality}\n"
        "    - {domain: gi, symbol: '\\lambda', name: claim intensity}\n"
    )
    assert sorted(tex for _, _, tex in spans_in(contract)) == [
        "\\lambda", "\\mu_x", "h(t)",
    ]


def test_an_unsupported_alias_is_reported(tmp_path):
    """The point of extending the sweep: a malformed alias publishes red error
    text on the symbol table, and every script still exits zero."""
    contract = tmp_path / "objects.yaml"
    contract.write_text(
        "- id: obj.broken\n"
        "  name: Broken\n"
        "  canonical: 'x'\n"
        "  definition: A rendering KaTeX cannot parse.\n"
        "  aliases:\n"
        "    - {domain: gi, symbol: '\\notacommand{x}', name: broken}\n"
    )
    assert sweep([contract]), "an unsupported alias must be reported"
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_katex_sweep.py -k "node_body or frontmatter or alias" -v`
Expected: FAIL, `ImportError: cannot import name 'spans_in'`.

- [ ] **Step 3: Extend the sweep**

Replace `extract_spans`'s single use with a suffix dispatch, keeping `extract_spans` itself as the markdown-and-qmd path so nothing that calls it breaks:

```python
def extract_alias_spans(text: str) -> list[tuple[int, bool, str]]:
    """Every symbol in the notation contract, as an inline span.

    The contract's canonicals and aliases are raw TeX that reaches a reader
    only through the generated symbols.md, so a malformed one publishes red
    error text on the page every reader of the corpus opens first, while every
    script exits zero. Line numbers are recovered by searching the source text
    for the symbol, because yaml.safe_load discards them.
    """
    entries = yaml.safe_load(text) or []
    lines = text.splitlines()
    spans: list[tuple[int, bool, str]] = []
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        symbols = [entry.get("canonical")]
        for alias in entry.get("aliases") or []:
            if isinstance(alias, dict):
                symbols.append(alias.get("symbol"))
        for symbol in symbols:
            if not symbol or symbol in seen:
                continue
            seen.add(symbol)
            line = next(
                (i for i, text_line in enumerate(lines, start=1) if symbol in text_line),
                1,
            )
            spans.append((line, False, symbol))
    return spans


def spans_in(path: Path) -> list[tuple[int, bool, str]]:
    """Dispatch on suffix, because a .yaml contract and a .md body carry their
    mathematics differently and neither is a .qmd."""
    text = path.read_text()
    if path.suffix in {".yaml", ".yml"}:
        return extract_alias_spans(text)
    return extract_spans(text)
```

Then replace `extract_spans(path.read_text())` with `spans_in(path)` in both `sweep` and `main`, and widen the CLI argument's name from `qmd` to `paths` so the help text stops lying:

```python
    parser.add_argument("paths", type=Path, nargs="+")
    args = parser.parse_args()
    failures = sweep(args.paths)
    for failure in failures:
        print(failure)
    total = sum(len(spans_in(p)) for p in args.paths)
    print(f"\n{total} spans across {len(args.paths)} files, {len(failures)} unsupported")
```

Add `import yaml` at the top.

- [ ] **Step 4: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_katex_sweep.py -v`
Expected: PASS, including the pre-existing `.qmd` tests, which must not regress.

- [ ] **Step 5: Sweep the corpus as it stands**

```bash
.venv/bin/python scripts/katex_sweep.py \
  notation/objects.yaml notation/symbols.md nodes/*.md lectures/*.qmd
```

Expected: `0 unsupported`. Tasks 4 and 5 have just added five renderings to the contract, so this is the first time any of them meets the parser. If a rendering fails, fix it in `objects.yaml`, regenerate `symbols.md`, and note it.

- [ ] **Step 6: Commit**

```bash
git add scripts/katex_sweep.py tests/test_katex_sweep.py
git commit -m "feat(katex): sweep node bodies and the notation contract alongside .qmd"
```

---

### Task 7: The transcription brief

**Files:**
- Create: `notes/transcription-brief.md`

**Interfaces:**
- Consumes: Tasks 1 to 6, all of which it describes as settled.
- Produces: the single document every Wave 1 agent reads. Nothing in Wave 1 may contradict it.

Twenty agents will each invent a convention unless one is written down. Phase 0's spec already says the anchor grammar is stated centrally "rather than left to each transcriber to invent", and this is where that promise is kept for everything else too: the slug, the grain, the domains, and what a stub's body may contain.

- [ ] **Step 1: Write the brief**

The full text follows. Write it verbatim; it is the contract twenty dispatches depend on.

````markdown
# Transcription brief, Phase 1

Read this in full before transcribing. It is binding, and where it disagrees with your own
judgement, follow it and record the disagreement in your report rather than departing quietly.
Inconsistent conventions are invisible in a node list read once and expensive in Phase 3.

## What you produce

Stub node records, one markdown file per node, written into **your own staging directory**:

```
.superpowers/phase-1/<body-id>/nodes/<node-id>.md
.superpowers/phase-1/<body-id>/manifest.yaml
```

You do **not** write into `nodes/`. Twenty agents share that namespace and several of
you will produce `survival-function`; writing direct means the second clobbers the first and
drops its anchor silently. Task 9 merges your staging into the corpus and unions the fields a
shared node accumulates.

## The node record

```yaml
---
id: hazard-rate
title: Hazard rate
domains: [stats, life, gi, credit]
status: stub
requires: [survival-function]
spends: []
anchor: [ifoa.cs2.2.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

One or two sentences saying what this node covers, in your own words, so a
reader of the review document can tell it apart from its neighbours.
```

Six fields are fixed for every stub you write. `status` is always `stub`. `spends` is always
empty, because a stub declares no symbols and Phase 3 fills it when it writes the page.
`vault_articles` and `vault_sources` are always empty, because attaching sources is Phase 2.
`taught_in` is always `null`, because check 8 fails on a lecture that does not exist yet.

The body is **one or two sentences and no mathematics**. Keep it under a paragraph, leave the
citable definition to Phase 3, and use no `$...$` at all: Phase 3 writes the page against a locked template, and prose
written now is prose Phase 3 has to read and discard. The body exists so that gate 2 can tell
`hazard-rate` from `force-of-mortality` in a list, and that is its whole job.

## Node ids

Lowercase, hyphen-separated, matching `^[a-z0-9]+(-[a-z0-9]+)*$`, and **never renamed** once
merged. Four rules that stop twenty agents diverging:

1. **Name the concept rather than the syllabus.** `chain-ladder` rather than `cs2-topic-4-2`. Two
   bodies teaching one concept must collide on the id, because the collision is what makes the
   node shared rather than duplicated.
2. **Singular, and no article.** `loss-distribution` rather than `the-loss-distributions`. A
   fixed named term keeps its conventional form even where that reads as plural, so
   `efficient-markets-hypothesis`, `option-greeks` and `term-structure-of-interest-rates` stand,
   because forcing the singular misnames the term practitioners use.
3. **Spell out an abbreviation unless it is on this list: `glm`, `gam`, `arima`, `garch`,
   `gev`, `gpd`, `mcmc`, `pca`, `svd`.** Those nine are what practitioners actually say, and
   nobody says "generalised linear model" twice in a sentence. Everything else is spelled out,
   so `probability-of-default` rather than `pd`. The list is closed. Report a case you believe
   belongs on it rather than adding it yourself, because a list twenty agents can each extend
   independently is the same failure as no list.
4. **British English in the id as everywhere else.** `generalised-linear-model`,
   `discretisation`, `modelling`.

Where you suspect another body covers the same concept under a different name, still emit your
node and record the suspicion in your manifest's `duplicate_of` field. Guessing at another
agent's slug is worse than declaring the overlap.

## Granularity

A node is **one thing a reader can be examined on separately and that carries its own
prerequisites**, targeting one node per twenty to forty minutes of teaching.

Gate 1 tied this to the **syllabus item**, meaning CS2 1.1.5 rather than CS2 1.1. That is a
default rather than an identity, and two departures from it are expected:

- **Fold** an item that restates its neighbour. CS2 1.2.5 reads "loss distributions for both
  the insurer and the reinsurer after the operation of simple forms of proportional and excess
  of loss reinsurance where underlying losses take the forms given in 1.2.4". It applies 1.2.4
  and is not separately examinable, so it folds into the node 1.2.4 produced and adds its
  anchor to that node's list.
- **Split** an item naming several things examined separately. CS2 1.4.1 reads "recognise
  extreme value distributions, suitable for modelling the distribution of severity of loss and
  their relationships". The generalised extreme value and the generalised Pareto are separate
  nodes with separate prerequisites, and both take the anchor `ifoa.cs2.1.4-1`.

- **Hunt for restatements before you write.** A broad principles paper states one concept
  under several headings: a risk taxonomy and then a "main risks" list, PD, LGD and EAD defined
  once and again under model development, the Basel pillars introduced generically and re-named
  under a specific risk. Each restatement is a fold onto the node the first statement produced,
  and a transcriber who does not look for them first writes the same node three times.

Where your source numbers its items, an item is the finest numbered entry, and that holds where a
numbered item continues in unnumbered bullets: the bullets decide anchoring and splitting and add
nothing to the item count. Batch B split on exactly this, SP1 and SP9 counting bullets while SP5
and SP8 did not, and the ratios stopped comparing. Where a numbered source carries an unnumbered
glossary or defined-terms appendix (IFRS 9's Appendix A), leave it out of the count, fold its content
onto clause-anchored nodes, and state the exclusion in your report, because it can move the ratio
across the band on its own. Where the source does not number at all (a yearbook module description, a
regulation's running paragraphs), count with one rule so ratios compare across bodies: a full-stop-terminated sentence is one item, and a colon-introduced
list counts each listed member as an item. The two Pretoria agents each invented a rule and the two
disagreed, so their ratios were never comparable; state the rule you used in your report.

Your ratio of nodes to items should land between 0.5 and 1.5. Task 10 measures it across every
body and a ratio outside that band is reported to Mario, so explain yours in your report rather
than being surprised by it.

## The anchor mapping table

`anchor` is a **list**, because a node put in the corpus by three bodies carries three anchors.
Every anchor is lowercase, dot-separated, and three or four segments, or the literal `chosen`.
The grammar allows four segments at most, so a body numbering three levels deep hyphenates its
third level into the item segment.

| Body | Prefix | Source numbering | Anchor spelling |
|---|---|---|---|
| IFoA CS1, CS2, CM1, CM2, CB2, CP1 | `ifoa.<subject>` | topic, section, item: `1`, `1.1`, `1.1.5` | `ifoa.cs2.1.1-5` |
| IFoA SP1, SP2, SP5, SP6, SP7, SP8, SP9 | `ifoa.<subject>` | same three levels where present, decided per section rather than per subject, since one paper can carry both | `ifoa.sp7.3.5-1` for item 3.5.1 under 3.5 Reserving result analyses, or `ifoa.sp7.2.1` where section 2.1 has no third level |
| ASSA F107, F207 | `assa.<subject>` | outer section, then an objective list that **restarts at 1 inside each section**, then sub-items | section 1, objective 12, item 12.4 becomes `assa.f107.1.12-4` |
| BCBS d424 | `bcbs.d424` | numbered paragraphs, restarting from 1 inside each chapter, so the chapter is the section segment: `intro`, `sa`, `irb`, `cva`, `oprisk`, `floor`, `lr` | `bcbs.d424.irb.para-220` |
| IASB IFRS 9 | `iasb.ifrs9` | clauses: `5.5.1`; Appendix B paragraphs `B5.5.37` restart with a letter prefix and no chapter digit | `iasb.ifrs9.5.5-1`, and `iasb.ifrs9.b5.5-37` for the appendix, the prefix lowercased into the section segment |
| ETH summer school | `eth.dl-actuarial-2026` | twelve lectures | `eth.dl-actuarial-2026.l02`, where `l04` covers the combined lecture 04-05 and `l10` the combined 10-11 |
| UP undergraduate and honours | `up.<module-code>` | module code lowercased with no insertion, then section within the module description | `up.wst311.4`, `up.ias712.2`, `up.fni700.1` |

**Read the F107 row twice.** Its objective numbering restarts inside each outer section, so
"objective 12" is ambiguous without the section and `assa.f107.12.4` would name two different
things. The section segment is what disambiguates it.

**Where the source stops numbering and continues in bullets**, a bullet under a numbered item
takes its position in document order as the hyphenated final segment, so the second bullet under
SP8's item 3.5 is `ifoa.sp8.3.5-2`, and your report says you did this, because a reader verifying
that anchor has to count bullets rather than read a number. Bullets become separate nodes where
each names a separately teachable technique or object (SP8's burning cost, frequency-severity and
original loss curve approaches under 3.5), and fold into the parent item's single node where they
list considerations, factors or examples of one topic (SP8's 1.3, 2.2 and 3.4).

Where one numbered item carries both unnumbered bullets and numbered sub-items (SP6's 2.9 has a
bullet list and then 2.9.1 and 2.9.2), the bullets share the bare item anchor and only the numbered
sub-items take a hyphenated suffix, so a bullet position can never collide with a sub-item number.
Where PDF extraction has joined two bullets on one line ("Convertibles property derivatives"), read
them as two and say so in your report.

**`chosen` is the anchor for a prerequisite your paper assumes and never states.** A specialist
paper takes core technique for granted: SP7 discusses stochastic reserving throughout and never
names the deterministic chain ladder it builds on. Write the node, anchor it `chosen`, and say so
in your report, rather than stretching a real heading to cover something it does not say.

An anchor must point at something that exists. Before you finish, pick three of your anchors,
find the heading each one names in your source text, and quote it in your report. That
demonstrates the mapping rather than asserting it, and it is the only check anyone will make
on this.

## Domains

The closed vocabulary is twelve: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`,
`life`, `gi`, `credit`, `regulation`, `eco`, `fin-man`. Nothing outside it parses.

Assign the domains a node **belongs to** rather than the domains that might one day cite it. A node
in four domains is making a claim that four fields teach this object, and that claim generates
the bridge table. Two guides:

- `maths` and `stats` are for the roots, meaning material with no insurance or banking content
  at all. A survival function is `stats`; an exposed-to-risk calculation is `life`.
- `regulation` is for material whose content is what a rule requires rather than for material a rule
  happens to use. The IRB risk-weight formula is `credit` and `regulation`; the Vasicek
  single-factor model underneath it is `credit` and `stats`.

## Prerequisites

`requires` names nodes, and you can only name nodes you know about, which is your own body's.
**Emit within-body prerequisites only.** Task 11 resolves the cross-body edges once every
staging directory exists, and a guess at a node another agent may or may not have produced is
a broken reference that check 3 will reject.

Two rules. `requires` is what a reader must already hold to follow this node rather than everything
related to it, so a list beyond five entries is usually a grain problem rather than a rich
node. And the graph must stay acyclic, so where two nodes seem mutually prerequisite, one of
them is really two nodes and you should split it.

## Before you invent an id

Rule 1 says two bodies teaching one concept must collide on the id, and a merged id is never
renamed afterwards, so a collision missed here is a collision missed permanently. Make it a
procedure rather than a hope:

```bash
cd ~/Documents/Repos/alchemist
{ find .superpowers/phase-1 -path '*/nodes/*.md' 2>/dev/null; find nodes -maxdepth 1 -name '*.md'; } | sed 's#.*/##; s/\.md$//' | sort -u
```

That prints every id staged so far, by any body, together with every id already in the corpus at
`nodes/`, which holds drafted records from Phase 0 that the merge protects and that you must reuse
rather than reinvent. Before you write a node, look for one naming
your concept and reuse it exactly, character for character. Where a staged id means what you
mean but spells it differently, take the staged spelling over your own and say so in that
node's `duplicate_of`.

Agents run in parallel, so this list holds whatever landed before you started and it will be
incomplete. Run it again immediately before you write your files, because bodies land while you
read: SP2's first scan found nothing to reuse and its second, minutes later, found fourteen. It is still what separates a merge that unions two records from one that carries
`hazard-rate` and `hazard-function` as two nodes forever. For a concept you expect another body
to teach and cannot find staged, write your own id and name the expectation in `duplicate_of`,
which is what Task 9 and Task 11 read to catch the near misses this check could not.

Reusing a staged id also donates your node's `requires` and `domains` into the shared record when
Task 9 unions the fields. Where your reading of the concept differs materially from the body that
staged it, say so in `duplicate_of`: CS2's `age-period-cohort` is a mortality projection model and
the trunk's is a vintage-curve decomposition of loss rates, and the merged node needs a human to
look at that union rather than assume it resolves.

## Your manifest

```yaml
body: ifoa-cs2-2026
source: data/syllabi/ifoa-cs2-2026.txt
items_in_document: 87
nodes_emitted: 94
nodes:
  - id: hazard-rate
    title: Hazard rate
    anchor: [ifoa.cs2.2.1-3]
    domains: [stats, life, gi, credit]
    requires: [survival-function]
    duplicate_of: null
  - id: loss-distribution
    title: Loss distribution
    anchor: [ifoa.cs2.1.1-1]
    domains: [gi, stats]
    requires: []
    duplicate_of: "likely the same concept SP8 will call severity-distribution"
    needs: [claim-frequency-model]
```

`duplicate_of` names a concept you believe another body teaches under a different id. `needs`
lists prerequisites this node has that live in another body rather than yours, which your batch
check would reject in `requires` because it resolves ids within your own batch only. Keep the two
apart: Task 11 reads `needs` as edges to draw once every body is merged, and `duplicate_of` as
records to consider merging, and prose in one slot made it do both by hand. Omit `needs` where
there is nothing to list.

## Before you report

Run `.venv/bin/python scripts/check.py` and expect it to pass. It confirms the corpus you have
not touched is still whole, which is what "write nothing into `nodes/`" is standing on. It reads
`nodes/` and `paths/` at the repository root, so it cannot see your staging directory, and
checking your own batch takes a second command:

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
from pathlib import Path
from scripts.alchemist.model import parse_node, Corpus
from scripts.alchemist.checks import check_requires_resolve_and_acyclic

records = sorted(Path(".superpowers/phase-1/<body-id>/nodes").glob("*.md"))
nodes, failures = {}, []
for record in records:
    try:
        node = parse_node(record)
        nodes[node.id] = node
    except Exception as exc:
        failures.append(f"{record}: {type(exc).__name__}: {exc}")

result = check_requires_resolve_and_acyclic(Corpus(nodes=nodes, paths={}))
failures.extend(result.failures)

print(f"{len(records)} staged records, {len(failures)} problems")
for failure in failures:
    print(f"  {failure}")
EOF
```

Then round-trip your own manifest, because neither command above reads it and hand-rolled YAML
goes invalid the moment a long `duplicate_of` string wraps mid-sentence:

```bash
.venv/bin/python -c "
import yaml, sys
m = yaml.safe_load(open('.superpowers/phase-1/<body-id>/manifest.yaml'))
assert len(m['nodes']) == m['nodes_emitted'], (len(m['nodes']), m['nodes_emitted'])
print(f\"manifest parses, {m['nodes_emitted']} entries\")"
```

Replace `<body-id>` with your own and expect `0 problems`. This is `parse_node` plus the
acyclicity half of check 3, run against only the nodes you wrote: it rejects a malformed
anchor, an unknown domain, an id that fails the slug pattern, a filename that disagrees with
its id, and a `requires` edge that does not resolve within your own batch or that closes a
cycle. Then report what neither command verified about your batch. Neither checks that an
anchor points at a section that exists, that your grain matches the corpus, or that `requires`
is pedagogically ordered rather than merely acyclic, and neither can check symbol resolution,
path teachability or a cross-body edge, because those need every body's nodes sharing one
namespace, which is what Task 9 and Task 11 build once every staging directory exists. Report:

1. Three anchors, each with the heading it names quoted from your source.
2. Your node count against your document's item count, with any ratio outside 0.5 to 1.5
   explained.
3. Every `requires` edge you were unsure about.
4. Every cross-body overlap you suspect, which is what your `duplicate_of` fields carry.

**Measure rather than read, and report rather than silently patch.**
````

- [ ] **Step 2: Verify the brief against the machinery it describes**

Every claim in the brief must be true of the code as it now stands. Check each by running it rather than by reading:

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python -c "
from scripts.alchemist.model import ANCHOR, DOMAINS, SLUG, STATUSES
for a in ['ifoa.cs2.1.1-5', 'ifoa.sp7.3.5-1', 'assa.f107.1.12-4', 'bcbs.d424.irb.para-220',
          'iasb.ifrs9.5.5-1', 'eth.dl-actuarial-2026.l02', 'up.wst311.4', 'up.iashons712.2']:
    assert ANCHOR.match(a), a
for s in ['hazard-rate', 'generalised-linear-model', 'glm', 'arima']:
    assert SLUG.match(s), s
assert len(DOMAINS) == 12 and {'eco', 'fin-man'} <= DOMAINS
assert 'stub' in STATUSES
print('every anchor, slug and vocabulary claim in the brief holds')
"
```

Expected: the single success line. **If any assertion fails, the brief is wrong and the brief changes** rather than the assertion.

- [ ] **Step 3: Commit**

```bash
git add notes/transcription-brief.md
git commit -m "docs(phase-1): write the transcription brief every body agent reads"
```

---

# Wave 1: transcription

### Task 8: Transcribe the 20 bodies into staging

**Files:**
- Create: `.superpowers/phase-1/<body-id>/nodes/*.md` and `manifest.yaml`, for each of 20 bodies
- Modify: nothing in the corpus

**Interfaces:**
- Consumes: `notes/transcription-brief.md`, `sources/syllabi.yaml`, `data/syllabi/*.txt`, `notation/objects.yaml`.
- Produces: 20 staging directories, each with a `manifest.yaml` matching the brief's schema. Task 9 consumes them.

**This task is 20 dispatches rather than one.** Run them in two batches so a convention problem found in the first batch is fixed before the second inherits it, and so the review between batches is a real gate rather than a formality.

**Batch A, twelve bodies, chosen so the trunk and both braids land first:**
`ifoa-cs2-2026`, `ifoa-cs1-2026`, `ifoa-cm1-2026`, `ifoa-cm2-2026`, `assa-f107-2026`, `assa-f207-2026`, `ifoa-sp7-2026`, `ifoa-sp8-2026`, `ifoa-sp2-2026`, `eth-dl-actuarial-2026`, `up-02133413`, `up-02240278`.

`eth-dl-actuarial-2026` is in Batch A and reads twelve `.qmd` lectures rather than a syllabus. Its nodes are the concepts each lecture teaches, its anchors are lecture numbers, and it is the body most likely to produce nodes every other body also produces, because it is the trunk. Dispatch it first within the batch, so its ids are on disk before the eleven bodies that will collide with them.

**Batch B, eight bodies:**
`ifoa-cb2-2026`, `ifoa-cp1-2026`, `ifoa-sp1-2026`, `ifoa-sp5-2026`, `ifoa-sp6-2026`, `ifoa-sp9-2026`, `bcbs-d424`, `iasb-ifrs9`.

Twelve and eight make the twenty. A ninth and tenth dispatch may be added to Batch B where Batch A's two University of Pretoria agents report that one agent per programme produced too coarse a grain, splitting a programme into its module groups. That is a decision taken at the Step 2 gate with their reports in hand, so it changes the dispatch count rather than the body count: the corpus still has twenty anchor bodies either way.

- [ ] **Step 1: Dispatch Batch A**

One agent per body, `model: "sonnet"` explicitly, per the spec's routing table and `~/.claude/CLAUDE.md`. The dispatch prompt, with `<BODY-ID>` substituted:

```
Transcribe one published syllabus into stub node records for the Alchemist corpus.

Read these three, in this order, before writing anything:
1. ~/Documents/Repos/alchemist/notes/transcription-brief.md  (binding; follow it exactly)
2. ~/Documents/Repos/alchemist/notation/objects.yaml         (the notation contract)
3. Your source document, named by the `<BODY-ID>` entry in
   ~/Documents/Repos/alchemist/sources/syllabi.yaml

Your body is <BODY-ID>. Write every node into
.superpowers/phase-1/<BODY-ID>/nodes/ and your manifest to
.superpowers/phase-1/<BODY-ID>/manifest.yaml, both per the brief's schema.

Write NOTHING into nodes/, paths/, notation/ or sources/. Commit nothing.
Python is always .venv/bin/python.

Run BOTH commands under "Before you report" in the brief. `check.py` alone
cannot see your staging directory, so it verifies nothing about what you
wrote; the second command is the one that checks your own batch. Then report
what neither verified:
three anchors with the heading each one names quoted from your source; your
node count against your document's item count, explaining any ratio below 0.5
or above 1.5; every `requires` edge you were unsure about; and every
cross-body overlap you suspect. Measure rather than read, and report rather
than silently patch.
```

- [ ] **Step 2: Review Batch A before dispatching Batch B**

Read the twelve reports rather than the 700 files. Four things decide whether Batch B goes out unchanged:

1. **Do the quoted headings match the anchors?** Spot-check three agents by opening their source text and finding the heading yourself. This is the only verification the anchor mapping gets, so it is worth doing rather than trusting.
2. **Are the node-to-item ratios inside 0.5 to 1.5?** An agent outside the band with a good explanation is fine; two agents outside it in opposite directions means the grain rule is not landing and the brief needs a worked example from the body that misread it.
3. **Do the ids look like concepts?** A manifest full of `cs2-topic-4-2` means rule 1 did not land, and every id has to be rewritten before it is merged, which is cheap now and impossible after Phase 3.
4. **Do the `duplicate_of` notes cluster?** Three agents flagging the same overlap is a signal that Task 9's merge will be doing real work rather than trivial unions.

Fix the brief where it failed, and record what changed and why in the task report. **A brief correction is committed to this branch with an explicit path** rather than with `git add -A`, because Batch A's staging is untracked and a sweep would commit 700 stub files.

- [ ] **Step 3: Dispatch Batch B**

Same prompt, the eight remaining bodies, plus any UP module split the Step 2 gate called for. Note the two that read something other than a syllabus:

- `bcbs-d424` and `iasb-ifrs9` read regulation from the vault, and their nodes are what the rule requires rather than the machinery it uses. Both agents need `ALCHEMIST_VAULT` set, and the vault is private, so nothing they quote may enter a node body. The brief already forbids a body beyond two sentences, which is what keeps that safe.

- [ ] **Step 4: Verify the staging is complete and well-formed**

Three things are verified here, and the second and third are the ones that matter.

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
from pathlib import Path
import yaml

staging = Path(".superpowers/phase-1")
bodies = sorted(p for p in staging.iterdir() if p.is_dir())
print(f"{'body':28} {'files':>6} {'claimed':>8}  manifest")
problems = []
for body in bodies:
    files = len(list((body / "nodes").glob("*.md")))
    manifest_path = body / "manifest.yaml"
    if not manifest_path.is_file():
        problems.append(f"{body.name}: no manifest")
        print(f"{body.name:28} {files:6} {'-':>8}  MISSING")
        continue
    try:
        manifest = yaml.safe_load(manifest_path.read_text()) or {}
    except yaml.YAMLError as exc:
        problems.append(f"{body.name}: manifest will not parse: {str(exc).splitlines()[0]}")
        print(f"{body.name:28} {files:6} {'-':>8}  <-- MALFORMED MANIFEST")
        continue
    claimed = manifest.get("nodes_emitted")
    flag = ""
    if claimed != files:
        problems.append(f"{body.name}: claims {claimed} nodes, wrote {files}")
        flag = "<-- DISAGREES"
    if files == 0:
        problems.append(f"{body.name}: wrote no nodes")
        flag = "<-- WROTE NOTHING"
    print(f"{body.name:28} {files:6} {str(claimed):>8}  {flag or 'ok'}")

print(f"\n{len(bodies)} bodies")
for problem in problems:
    print(f"  PROBLEM {problem}")
EOF
```

Expected: 20 rows, every `files` equal to every `claimed`, and no problem lines.

**A manifest that will not parse is reported rather than fatal.** F107's agent found that hand-rolled manifest YAML goes invalid when PyYAML wraps a long `duplicate_of` string mid-sentence, and caught it only by a round-trip parse that neither of the brief's two required commands performs. Left unguarded, one such manifest would raise out of this loop and take the other nineteen rows with it.

**The count reconciliation is the point.** `scripts/grain_audit.py` reads `nodes_emitted` straight from the manifest, so an agent that claims 94 and wrote 40 produces a grain ratio that is fiction, and the grain table is the main thing gate 2 reads. The standing instruction says measure rather than read, and this is the one place the pipeline would otherwise read. `items_in_document` stays self-reported because counting syllabus items needs judgement; the node count does not.

A body that disagrees, has no manifest or wrote nothing is a **failed dispatch to re-run** rather than something for Task 9 to cope with.

- [ ] **Step 5: Parse every staged record before the merge touches it**

`collect()` calls `parse_node` on every staged file, and `parse_node` raises on a malformed anchor, an unknown domain, or a filename that disagrees with its id. Across 1,400 files from 20 agents at least one will be malformed, and the merge would die partway through on a single `ValueError` with the rest unexamined. One pass produces the whole fix list instead.

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
from pathlib import Path
from scripts.alchemist.model import parse_node

records = sorted(Path(".superpowers/phase-1").glob("*/nodes/*.md"))
failures = []
for record in records:
    try:
        parse_node(record)
    except Exception as exc:
        failures.append(f"{record}: {type(exc).__name__}: {exc}")

print(f"{len(records)} staged records, {len(failures)} that will not parse")
for failure in failures:
    print(f"  {failure}")
EOF
```

Expected: `0 that will not parse`. Every failure names its own path and its own reason, so fix them in staging and re-run this until it is clean. **Do not fix them after the merge:** a record that will not parse never reaches `nodes/`, so the corpus would silently be missing it and check 3 would report the gap as a broken prerequisite somewhere else entirely.

- [ ] **Step 6: Record the wave**

Write `.superpowers/phase-1/wave-1-report.md` carrying the per-body counts, the four review findings from Step 2, every brief correction, and the full list of suspected overlaps. Task 9 reads the overlap list, and Task 10 compares its own measurements against the counts here. This file is gitignored along with the rest of `.superpowers/`, which is deliberate: it is working state, and what survives into the repo is the merge report Task 9 commits.

---

# Wave 2: reconcile

### Task 9: Merge the staging directories into the corpus

**Files:**
- Create: `scripts/alchemist/staging.py`
- Create: `scripts/merge_staging.py`
- Create: `tests/test_staging.py`
- Create: `nodes/*.md`, one per distinct staged id. Batch A alone staged 1,225 records over roughly 950 distinct ids, so expect the merged corpus to pass the spec's 1,100 to 1,400 estimate once Batch B lands; the Step 4 table is the authority on the count, this line is a forecast.
- Create: `notes/merge-report-2026-09-04.md`

**Interfaces:**
- Consumes: `.superpowers/phase-1/<body>/nodes/*.md`.
- Produces: `merge(records: list[Node]) -> tuple[Node, list[str]]` merging every record sharing an id; `collect(staging: Path) -> dict[str, list[Node]]`; `write_merged(merged, target) -> list[Path]`.

The merge is where a shared node becomes shared rather than duplicated. CS2 and F107 both produce `survival-function`, and the merged record must carry both anchors, the union of both domain sets and the union of both `requires` lists. Getting this wrong is silent: the corpus still checks green with one anchor missing, and nobody finds out until Phase 3 writes a page that cannot say why the node exists.

**Conflicts that are not unions.** Two agents can give one id two different titles. That is not resolvable automatically and must not be guessed: the merge takes the first title in body order, records the alternative in the report, and Mario reads it at gate 2.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_staging.py
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
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_staging.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.staging'`.

- [ ] **Step 3: Write the merge**

```python
# scripts/alchemist/staging.py
"""Merge the per-body staging directories into one corpus.

Twenty agents transcribe in parallel and several of them produce the same
node: survival-function comes out of CS2, F107 and the ETH lectures alike. Each
writes into its own directory, and this is where a shared node becomes shared
rather than duplicated.

The union is the point. A merged record carries every body's anchor, the union
of their domain sets and the union of their prerequisites, because a dropped
anchor is silent: the corpus still checks green without it and the loss surfaces
only in Phase 3, when a page cannot say why its node exists.

A title disagreement is not a union and is never guessed. The first title in
body order wins and the alternative is reported, because which of "Chain ladder"
and "The chain ladder method" the corpus uses is a decision rather than a merge.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import yaml

from .model import Node, parse_node


def collect(staging: Path) -> dict[str, list[Node]]:
    """Every staged record, grouped by id, in body-directory order.

    The order is sorted rather than filesystem order, so a merge run twice over
    the same staging produces byte-identical output. A thousand records that
    re-order on every run make every diff unreadable.
    """
    grouped: dict[str, list[Node]] = {}
    for body in sorted(p for p in staging.iterdir() if p.is_dir()):
        for record in sorted((body / "nodes").glob("*.md")):
            node = parse_node(record)
            grouped.setdefault(node.id, []).append(node)
    return grouped


def merge(records: list[Node], existing: Node | None = None) -> tuple[Node, list[str]]:
    """One merged record and the notes a reader has to adjudicate.

    `existing` is the record already in nodes/ under this id, where there is one.
    Three drafted exemplars sit there from Phase 0, one with a lecture attached,
    and CS1 and CS2 stage the same ids because they teach the same concepts. A
    corpus record wins on everything a stub cannot supply, meaning title, status,
    body, spends, the vault fields and taught_in, and gains the staged anchors,
    domains and prerequisites by union. Without this the merge replaces a written
    page with two sentences and orphans its lecture.
    """
    first = existing or records[0]
    everyone = ([existing] if existing is not None else []) + records
    notes: list[str] = []

    def body_of(node: Node) -> str:
        return "nodes" if node is existing else node.path.parts[-3]

    for other in records:
        if other is first:
            continue
        if other.title != first.title:
            notes.append(
                f"{first.id}: titled {first.title!r} in {body_of(first)} and "
                f"{other.title!r} in {body_of(other)}, keeping the first"
            )

    def union(field: str) -> tuple[str, ...]:
        return tuple(sorted({value for r in everyone for value in getattr(r, field)}))

    bodies = sorted({body_of(r) for r in records})
    if len(bodies) > 1:
        notes.append(f"{first.id}: merged from {len(bodies)} bodies, {', '.join(bodies)}")
    if existing is not None:
        notes.append(
            f"{first.id}: protected {existing.status} record already in nodes/, "
            f"gained anchors from {', '.join(bodies)}"
        )

    protected = existing is not None
    merged = Node(
        id=first.id,
        title=first.title,
        domains=union("domains"),
        status=first.status if protected else "stub",
        requires=union("requires"),
        spends=first.spends if protected else (),
        anchor=union("anchor"),
        vault_articles=first.vault_articles if protected else (),
        vault_sources=first.vault_sources if protected else (),
        taught_in=first.taught_in if protected else None,
        body=first.body,
        path=first.path,
    )
    return merged, notes


def _tokens_close(x: str, y: str) -> bool:
    """Two hyphen-separated tokens that read as one word spelled two ways."""
    return x != y and len(x) >= 4 and len(y) >= 4 and x[:4] == y[:4]


def near_misses(ids: Iterable[str]) -> list[tuple[str, str]]:
    """Pairs of distinct ids the exact-match reuse check is blind to by construction.

    Batch A and B agents reused an id only on a character-for-character match, so
    CM2 staged efficient-markets-hypothesis beside the undergraduate's
    efficient-market-hypothesis, and SP9 staged reputational-risk beside SP1's
    reputation-risk, with no collision and no warning. Two ids are near misses
    where they have the same token count and exactly one token differs while
    sharing its first four letters, or where one is the other with a single
    token inserted. Roughly 120 pairs over 1,600 ids; a list a human reads once
    in Task 11 rather than a rule the merge acts on.
    """
    ordered = sorted(set(ids))
    split = {i: i.split("-") for i in ordered}
    out: list[tuple[str, str]] = []
    for a_i, a in enumerate(ordered):
        ta = split[a]
        for b in ordered[a_i + 1:]:
            tb = split[b]
            if abs(len(ta) - len(tb)) > 1:
                continue
            if len(ta) == len(tb):
                diff = [(x, y) for x, y in zip(ta, tb) if x != y]
                if len(diff) == 1 and _tokens_close(*diff[0]):
                    out.append((a, b))
            else:
                longer, shorter = (ta, tb) if len(ta) > len(tb) else (tb, ta)
                if any(longer[:k] + longer[k + 1:] == shorter for k in range(len(longer))):
                    out.append((a, b))
    return out


def render(node: Node) -> str:
    """Frontmatter written by hand rather than by yaml.safe_dump, so the file
    reads the way the exemplar nodes do: flow sequences on one line, and the
    field order the spec's example uses rather than alphabetical. Every field
    renders from the record, because a protected drafted node carries spends, a
    lecture and vault entries that a stub-only renderer would drop in silence."""
    if node.spends:
        spends = "spends:\n" + "\n".join(
            f"  - {{object: {s.object}, domain: {s.domain}}}" for s in node.spends
        )
    else:
        spends = "spends: []"
    meta = [
        f"id: {node.id}",
        f"title: {node.title}",
        f"domains: [{', '.join(node.domains)}]",
        f"status: {node.status}",
        f"requires: [{', '.join(node.requires)}]",
        spends,
        f"anchor: [{', '.join(node.anchor)}]",
        f"vault_articles: [{', '.join(node.vault_articles)}]",
        f"vault_sources: [{', '.join(node.vault_sources)}]",
        f"taught_in: {node.taught_in or 'null'}",
    ]
    return "---\n" + "\n".join(meta) + "\n---\n\n" + node.body.strip() + "\n"


def write_merged(merged: dict[str, Node], target: Path) -> list[Path]:
    target.mkdir(parents=True, exist_ok=True)
    written = []
    for node_id in sorted(merged):
        destination = target / f"{node_id}.md"
        destination.write_text(render(merged[node_id]))
        written.append(destination)
    return written
```

```python
# scripts/merge_staging.py
"""Merge Phase 1's staging directories into nodes/ and report every merge."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import parse_node
from scripts.alchemist.staging import collect, merge, near_misses, write_merged

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=REPO / ".superpowers" / "phase-1")
    parser.add_argument("--target", type=Path, default=REPO / "nodes")
    parser.add_argument("--report", type=Path, default=REPO / "notes" / "merge-report-2026-09-04.md")
    args = parser.parse_args()

    grouped = collect(args.staging)
    existing = {n.id: n for n in (parse_node(p) for p in sorted(args.target.glob("*.md")))}
    merged, notes = {}, []
    for node_id, records in grouped.items():
        merged[node_id], node_notes = merge(records, existing.get(node_id))
        notes.extend(node_notes)

    written = write_merged(merged, args.target)
    shared = sum(1 for records in grouped.values() if len(records) > 1)
    protected = sum(1 for node_id in merged if node_id in existing)

    lines = [
        "# Merge report, Phase 1",
        "",
        f"- Staged records: {sum(len(r) for r in grouped.values())}",
        f"- Distinct nodes: {len(merged)}",
        f"- Nodes produced by more than one body: {shared}",
        f"- Records already in `{args.target.name}/` and protected: {protected}",
        f"- Written to `{args.target.name}/`: {len(written)}",
        "",
        "## Notes to adjudicate",
        "",
    ]
    lines.extend(f"- {note}" for note in sorted(notes))
    pairs = near_misses(merged)
    lines += ["", "## Near-miss ids for Task 11", "",
              "Distinct ids one token apart, which the exact-match reuse check could not see. "
              "Each is a merge, a parent-child pair, or a coincidence, and a human decides which.", ""]
    lines.extend(f"- `{a}` and `{b}`" for a, b in pairs)
    args.report.write_text("\n".join(lines) + "\n")

    print(f"{len(merged)} nodes written, {shared} shared across bodies, {len(pairs)} near-miss pairs")
    print(f"report: {args.report.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_staging.py -v`
Expected: PASS, ten tests.

- [ ] **Step 5: Verify the tests would fail under the bug they name**

Change `union` to `return tuple(getattr(first, field))`, meaning take the first record's value rather than the union, and re-run. `test_merges_the_anchors_of_a_shared_node`, `test_merges_the_domains_of_a_shared_node` and `test_merges_the_prerequisites_of_a_shared_node` must all fail. Restore the union. **Report which three failed and which passed anyway**, because a test that still passes was not testing the union.

Then break the protection two ways in turn and restore after each. First, change `protected = existing is not None` to `protected = False`: `test_a_drafted_corpus_record_is_protected` must fail on `status`. Second, in `render`, put the literal `"spends: []"` back in place of the `spends` variable: `test_render_keeps_every_field_of_a_protected_record` must fail on `spends`. A test that survives either injection is testing nothing about the record it names.

Then loosen `_tokens_close` to `return x != y` and re-run: `test_near_misses_see_what_exact_match_cannot` must fail on the `credit-risk`, `market-risk` negative, because a detector that pairs every one-token difference reports several hundred pairs and buries the real ones. Restore it.

- [ ] **Step 6: Run the merge**

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python scripts/merge_staging.py
ls nodes/*.md | wc -l
```

Expected: a node count equal to the number of distinct ids across the staging directories, which the Step 4 table of Task 8 already tells you, and a shared count in the tens to low hundreds. Batch A measured 46 shared ids among roughly 950 distinct before Batch B ran, so a shared count near zero means the agents did not collide on ids and Task 11 has more to do; a count in the hundreds would be higher than anything measured so far and is worth a look rather than a celebration.

- [ ] **Step 7: Run the checks and expect check 3 to fail**

Run: `.venv/bin/python scripts/check.py`
Expected: checks 1, 2, 5, 6, 7, 8 and 9 `ok`; **check 3 fails on unresolved prerequisites and check 4 fails on path teachability**. Both are expected here and both are Tasks 11 and 12's work. Record the failure counts, because Task 11 measures its own progress against them.

- [ ] **Step 8: Commit**

The pre-commit hook runs `check.py` and will reject this commit while check 3 fails. Commit the code and the report now and the nodes at the end of Task 11, when the graph resolves.

```bash
git add scripts/alchemist/staging.py scripts/merge_staging.py tests/test_staging.py
git commit -m "feat(staging): merge the per-body directories, unioning what a shared node carries"
```

---

### Task 10: The grain audit

**Files:**
- Create: `scripts/alchemist/grain.py`
- Create: `scripts/grain_audit.py`
- Create: `tests/test_grain.py`

**Interfaces:**
- Consumes: `.superpowers/phase-1/<body>/manifest.yaml`, and the merged `Corpus`.
- Produces: `audit(manifests: list[dict]) -> GrainReport`, `requires_distribution(requires: list[tuple[str, ...]]) -> dict[int, int]` and `fused_titles(titles: list[str]) -> list[str]`. `audit` takes the manifests alone and never the corpus: the corpus is loaded by `scripts/grain_audit.py` for the prerequisite distribution, and passing it into `audit` would hand the function an argument it ignores.

The spec says outright that inconsistent grain is invisible in a node list read once and surfaces only in Phase 3. So this emits **numbers rather than judgements**: an agent that produced six nodes where another produced one for a comparable section shows up as a figure Mario can read, and nothing here decides whether that is wrong.

**The fused-title flag is the cheapest signal available.** A title carrying "and" or a comma is the reliable tell for two examinable things in one node, because a syllabus item reading "estimation and forecasting" is two nodes and an agent under time pressure emits one.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_grain.py
"""The grain audit emits numbers rather than judgements.

Inconsistent grain is invisible in a node list read once and expensive in
Phase 3. What makes it visible is a figure: this body produced 1.9 nodes per
syllabus item and that one produced 0.3.
"""

import pytest

from scripts.alchemist.grain import audit, fused_titles, requires_distribution


def test_counts_nodes_per_body_from_the_manifests():
    manifests = [
        {"body": "ifoa-cs2-2026", "items_in_document": 87, "nodes_emitted": 94},
        {"body": "ifoa-sp7-2026", "items_in_document": 24, "nodes_emitted": 8},
    ]
    report = audit(manifests)
    assert report.per_body["ifoa-cs2-2026"].ratio == pytest.approx(94 / 87)
    assert report.per_body["ifoa-sp7-2026"].ratio == pytest.approx(8 / 24)


def test_flags_a_body_outside_the_band():
    manifests = [
        {"body": "inside", "items_in_document": 100, "nodes_emitted": 120},
        {"body": "too-coarse", "items_in_document": 100, "nodes_emitted": 30},
        {"body": "too-fine", "items_in_document": 100, "nodes_emitted": 210},
    ]
    report = audit(manifests)
    assert set(report.outliers) == {"too-coarse", "too-fine"}


def test_a_body_with_no_items_recorded_is_reported_rather_than_divided():
    """A zero denominator is a manifest problem rather than a ratio of infinity."""
    report = audit([{"body": "b", "items_in_document": 0, "nodes_emitted": 40}])
    assert report.per_body["b"].ratio is None
    assert "b" in report.unmeasurable


def test_band_boundaries_are_inclusive():
    manifests = [
        {"body": "at-low", "items_in_document": 100, "nodes_emitted": 50},
        {"body": "at-high", "items_in_document": 100, "nodes_emitted": 150},
        {"body": "below-low", "items_in_document": 100, "nodes_emitted": 49},
        {"body": "above-high", "items_in_document": 100, "nodes_emitted": 151},
    ]
    report = audit(manifests)
    assert "at-low" not in report.outliers and "at-low" not in report.unmeasurable
    assert "at-high" not in report.outliers and "at-high" not in report.unmeasurable
    assert "below-low" in report.outliers
    assert "above-high" in report.outliers


def test_the_requires_distribution_counts_each_length():
    assert requires_distribution([(), ("a",), ("a", "b"), ("a", "b")]) == {0: 1, 1: 1, 2: 2}


@pytest.mark.parametrize("title,flagged", [
    ("Hazard rate", False),
    ("Estimation and forecasting", True),
    ("Copulas, dependence and tail behaviour", True),
    ("Bornhuetter-Ferguson", False),
    ("Profit and loss attribution", True),
])
def test_flags_a_title_carrying_and_or_a_comma(title, flagged):
    assert bool(fused_titles([title])) is flagged


def test_fused_titles_are_sorted_and_deduplicated():
    titles = [
        "Profit and loss attribution",
        "Estimation and forecasting",
        "Copulas, dependence and tail behaviour",
        "Estimation and forecasting",
    ]
    assert fused_titles(titles) == [
        "Copulas, dependence and tail behaviour",
        "Estimation and forecasting",
        "Profit and loss attribution",
    ]
```

- [ ] **Step 2: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_grain.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.grain'`.

- [ ] **Step 3: Write the audit**

```python
# scripts/alchemist/grain.py
"""Measure grain across the bodies. Emit numbers rather than judgements.

Spec section 4.1a states that inconsistent grain is invisible in a node list
read once and surfaces only in Phase 3, when some pages come out at two
paragraphs and others are lectures in disguise. So nothing here decides whether
a body is wrong. It reports that CS2 produced 1.08 nodes per syllabus item and
SP7 produced 0.33, and a reader draws the conclusion.

The band is 0.5 to 1.5, which is the brief's own instruction to the agents, so
a body outside it is a body that departed from what it was told and owes an
explanation rather than a correction.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

BAND = (0.5, 1.5)
FUSED = re.compile(r"\band\b|,")


@dataclass(frozen=True)
class BodyGrain:
    body: str
    items: int
    nodes: int
    ratio: float | None


@dataclass
class GrainReport:
    per_body: dict[str, BodyGrain] = field(default_factory=dict)
    outliers: list[str] = field(default_factory=list)
    unmeasurable: list[str] = field(default_factory=list)


def audit(manifests: list[dict]) -> GrainReport:
    report = GrainReport()
    for manifest in manifests:
        body = manifest["body"]
        items = int(manifest.get("items_in_document") or 0)
        nodes = int(manifest.get("nodes_emitted") or 0)
        if items == 0:
            report.per_body[body] = BodyGrain(body, items, nodes, None)
            report.unmeasurable.append(body)
            continue
        ratio = nodes / items
        report.per_body[body] = BodyGrain(body, items, nodes, ratio)
        if not BAND[0] <= ratio <= BAND[1]:
            report.outliers.append(body)
    return report


def requires_distribution(requires: list[tuple[str, ...]]) -> dict[int, int]:
    """How many nodes carry zero prerequisites, how many carry one, and so on.

    A long tail is the second grain signal after the ratio: a node needing eight
    prerequisites is usually three nodes rather than one rich one.
    """
    counts: dict[int, int] = {}
    for entry in requires:
        counts[len(entry)] = counts.get(len(entry), 0) + 1
    return dict(sorted(counts.items()))


def fused_titles(titles: list[str]) -> list[str]:
    """Every distinct title carrying "and" or a comma, sorted.

    The cheapest available tell for two examinable things fused into one node,
    because a syllabus item reading "estimation and forecasting" is two nodes and
    an agent under time pressure emits one. Many flags are false positives:
    "Profit and loss attribution" is one thing. It is a list to read rather than a list
    to act on. Two nodes sharing the exact same title text collapse to one entry here,
    since the report flags the title itself rather than a count of the nodes that carry it.
    """
    return sorted({t for t in titles if FUSED.search(t)})
```

```python
# scripts/grain_audit.py
"""Report grain across every body, for gate 2."""

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.grain import audit, fused_titles, requires_distribution
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=REPO / ".superpowers" / "phase-1")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    manifests = [
        yaml.safe_load(p.read_text())
        for p in sorted(args.staging.glob("*/manifest.yaml"))
    ]
    report = audit(manifests)
    corpus = load_corpus(args.root)

    print(f"{'body':28} {'items':>6} {'nodes':>6} {'ratio':>6}")
    for body in sorted(report.per_body):
        grain = report.per_body[body]
        ratio = "n/a" if grain.ratio is None else f"{grain.ratio:.2f}"
        flag = "  <-- outside 0.5 to 1.5" if body in report.outliers else ""
        print(f"{body:28} {grain.items:6} {grain.nodes:6} {ratio:>6}{flag}")

    distribution = requires_distribution([n.requires for n in corpus.nodes.values()])
    print("\nprerequisites per node:")
    for length, count in distribution.items():
        print(f"  {length:2} prerequisites: {count:5} nodes")

    fused = fused_titles([n.title for n in corpus.nodes.values()])
    print(f"\n{len(fused)} titles carry 'and' or a comma, of {len(corpus.nodes)} nodes:")
    for title in fused[:40]:
        print(f"  {title}")
    if len(fused) > 40:
        print(f"  ... and {len(fused) - 40} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_grain.py -v`
Expected: PASS, eleven tests including the five parametrised title cases.

- [ ] **Step 5: Run the audit over the merged corpus**

Run: `.venv/bin/python scripts/grain_audit.py`
Expected: a table of 20 rows, a prerequisite distribution, and a fused-title list. Read the outliers and decide, per body, whether to re-dispatch that agent with a corrected instruction or to accept the ratio with a reason. **Re-dispatch is cheap now and impossible after Phase 3**, so err towards re-dispatching.

- [ ] **Step 6: Leave the files in the working tree; there is no commit at the end of this task**

The pre-commit hook runs `check.py` over the working tree, and the merged `nodes/` from Task 9 fails
check 3 (five cycles) and check 4 (two path failures) until Tasks 11 and 12 land. Task 9's
implementer got its code-only commit through by restoring `nodes/` to pristine, committing, and
copying the merged tree back; that worked once and is a hazard with 1,583 files, so it is done no
more. `grain.py`, `grain_audit.py` and `test_grain.py` stay in the working tree and are added, with
explicit paths, to the commit that closes Task 12. Never `--no-verify`.

---

### Task 11: Resolve cross-body prerequisites and break every cycle

**Files:**
- Modify: `nodes/*.md`, the `requires` field, plus, where the merge report's near-miss section shows two records for one concept, merging them: `anchor`, `domains` and `requires` unioned onto the survivor whose id follows the brief's rules, the other file deleted, and every `requires` naming it repointed. A node over the five-prerequisite ceiling may be split into new records. (Widened at execution from `requires` only, after the merge surfaced 122 near-miss pairs; the records are uncommitted, so this is the last cheap moment to merge.)
- Create: `notes/prerequisite-report-2026-09-04.md`

**Interfaces:**
- Consumes: the merged corpus, Task 10's report, Wave 1's suspected-overlap list.
- Produces: a corpus where check 3 passes.

Each Wave 1 agent emitted within-body prerequisites only, because an agent cannot name a node another agent may not have produced. So the corpus now has a real graph inside each body and almost no edges between them, and check 3 fails on every `requires` naming a node that no body actually emitted. This is where the graph becomes one graph.

**A `chosen` anchor comes off once another body supplies a real one.** SP7 staged `chain-ladder` as `chosen` because its specialist paper assumes the deterministic method without naming it, and F107, SP8 or CS2 may anchor the same node to a real item. After the merge the union carries both. `chosen` records that the depth was the transcriber's own call, so where a real anchor now sits beside it that record is false, and this task removes it. Found in Batch A.

**Three ways an edge is missing, and they need different fixes.** A prerequisite naming a node nobody wrote is either a node that should exist and does not, in which case write it; or a node another body wrote under a different slug, in which case repoint the edge; or a concept below the corpus's floor, in which case delete the edge and let the node's `anchor` carry the stopping rule.

- [ ] **Step 1: List every unresolved prerequisite**

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python -c "
from pathlib import Path
from scripts.alchemist.model import load_corpus
corpus = load_corpus(Path.cwd())
missing = {}
for node in corpus.nodes.values():
    for required in node.requires:
        if required not in corpus.nodes:
            missing.setdefault(required, []).append(node.id)
for required in sorted(missing, key=lambda r: -len(missing[r])):
    print(f'{len(missing[required]):4}  {required}')
print(f'\n{len(missing)} unresolved ids across {sum(len(v) for v in missing.values())} edges')
"
```

The ids most edges point at are the ones to fix first: one missing root node can account for forty edges, and writing it resolves all forty at once.

- [ ] **Step 2: Resolve them, in that order**

Work down the list. For each, decide between the three fixes above and record the decision. A node you write here is a stub like any other, with `anchor: [chosen]` where no body put it in the corpus, which is exactly what the literal `chosen` is for: it marks a node whose depth you selected, and it is honest about where the stopping rule is yours rather than external.

Re-run Step 1 after each batch of ten and watch the count fall. Stop when it reaches zero.

- [ ] **Step 3: Add the cross-body edges the braids need**

Three edges are not merely missing but load-bearing, and they are the reason the corpus is a graph rather than three separate syllabi:

- **The claims-reserving braid.** The chain ladder node requires the exponential dispersion family node, because the chain ladder reserve estimates are identical to those of an over-dispersed Poisson generalised linear model with a log link and additive origin and development effects. **This was verified by direct read on 4 September 2026** against the vault's copy of England and Verrall (2002), sections 2.2.1, 2.3.4 and 7.2.14, and is recorded in `notes/uni-programme-anchors.md`. Renshaw and Verrall (1998) is the attribution; Mack (1991) is not and must not be cited.
- **The survival braid.** The force of mortality, the claim intensity and the default hazard all require the hazard rate node, which is what makes them one object under four names rather than three unrelated definitions.
- **The Markov transition braid.** The rating transition matrix node requires the Markov jump process node, which the life multiple-state models node also requires. `notes/uni-programme-anchors.md` calls this the second braid and a strong one, and this edge is what makes it exist.

- [ ] **Step 4: Break every cycle**

Run: `.venv/bin/python scripts/check.py`
Check 3 reports a cycle by naming the nodes in it. A cycle means two nodes were each written as needing the other, and the resolution is almost always that one of them is two nodes: the part the other needs, and the part that needs the other. Split it, and re-run.

- [ ] **Step 5: Verify check 3 passes and record the work**

Run: `.venv/bin/python scripts/check.py`
Expected: check 3 `ok`. Check 4 still fails, because the paths do not exist yet.

Write `notes/prerequisite-report-2026-09-04.md` carrying: the unresolved count at the start and at each pass, every node written to close a gap and why, every edge repointed and to what, every edge deleted and the floor that justified it, and every cycle broken with the split that broke it. Gate 2 reads this alongside the merge report.

- [ ] **Step 6: Do not commit yet**

There is no commit at the end of this task, deliberately. The hook runs `check.py` against the working tree and check 4 still fails, because the paths do not exist until Task 12. A commit here would be rejected, and the only ways past a rejection are `--no-verify`, which is forbidden, or a commit that leaves the corpus broken on the branch.

So Tasks 11 and 12 land in one commit, at Task 12's Step 6. Leave `nodes/` and the two reports uncommitted in the working tree and move straight on. **The one thing to do before moving on:** `git status --porcelain nodes/ | wc -l` should report roughly the node count, confirming nothing was staged by accident. Staging is ignored from Task 1, so nothing else should appear.

---

### Task 12: The ten path files

**Files:**
- Create: `paths/credit-trunk.yaml`, `paths/life.yaml`, `paths/general-insurance.yaml`, `paths/machine-learning.yaml`, `paths/financial-engineering.yaml`, `paths/data-engineering.yaml`, `paths/claims-reserving-braid.yaml`, `paths/markov-transition-braid.yaml`
- Modify: `paths/maths-stats-prerequisites.yaml`, `paths/survival-braid.yaml`

**Interfaces:**
- Consumes: the resolved corpus.
- Produces: ten paths where check 4 passes.

Ordering lives in path files and never on the node, so this is where the corpus becomes teachable rather than merely acyclic. Check 4 is the rule that makes a path teachable: every node's prerequisites appear earlier in the same path, or anywhere in a path reachable through `builds_on`.

**`builds_on` is what keeps a domain path from restating its own roots.** The life path assumes the mathematics and statistics path, and without a way to say so every path in the corpus would fail check 4.

**The membership rule, stated because otherwise it is invented at execution time across roughly 1,600 nodes.** A node belongs in a domain path when it carries that domain in `domains`, minus the nodes already reachable through that path's `builds_on`. So the life path holds every node carrying `life`, less everything in `maths-stats-prerequisites`, because `builds_on` is exactly the mechanism for not restating a path's own roots. Three consequences follow and each is intended:

- **A node in four domains sits in four paths**, and spec section 4.3 says outright that a node sits in as many paths as it earns. The hazard rate is in the life, general-insurance, credit and survival-braid paths, which is what a braided corpus looks like.
- **A braid path is chosen rather than derived.** The three braids are arguments rather than domains, so their membership is the sequence that makes the argument: the claims-reserving braid runs from the exponential dispersion family to the recovery profile whether or not every node on the way carries `gi`.
- **`maths` and `stats` nodes are in the prerequisite path only**, unless a domain path genuinely re-teaches one, which should be rare enough to be worth a note when it happens.

The rule is mechanical, so apply it mechanically:

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
from pathlib import Path
from scripts.alchemist.model import load_corpus

corpus = load_corpus(Path.cwd())
for domain in ["credit", "life", "gi", "ml", "fin-eng", "data-eng"]:
    members = sorted(n.id for n in corpus.nodes.values() if domain in n.domains)
    print(f"{domain:10} {len(members):5} nodes")
EOF
```

- [ ] **Step 1: Extend the two existing paths**

`paths/maths-stats-prerequisites.yaml` currently holds one node and must hold every root: everything with no insurance or banking content, which is the `maths` and `stats` material the domain paths take as given. `paths/survival-braid.yaml` currently holds two and must run from the survival function through the hazard rate, the force of mortality, the claim intensity and the default hazard into the discrete-time hazard.

- [ ] **Step 2: Write the eight new paths**

Each takes the shape spec section 4.3 fixes:

```yaml
id: claims-reserving-braid
title: Claims reserving, from the exponential dispersion family to the recovery profile
builds_on: [maths-stats-prerequisites]
preamble: >
  A run-off triangle is an accident-period by development-period array, and its
  credit twin is the origination-cohort by months-on-book array that IFRS 9 and
  IRB use daily. The braid runs from the exponential dispersion family through
  the chain ladder and Bornhuetter-Ferguson into vintage curves, roll rates and
  the recovery profile. It is a branch of the trunk rather than an appendix,
  because the chain ladder reserve estimates are identical to those of an
  over-dispersed Poisson model with a log link and additive origin and
  development effects.
nodes: [exponential-dispersion-family, ..., lgd-recovery-profile]
```

The `builds_on` for each: every domain path builds on `maths-stats-prerequisites`; `claims-reserving-braid` and `markov-transition-braid` build on it too; `survival-braid` already does. `credit-trunk` additionally builds on `machine-learning`, because the trunk runs through deep survival modelling and restating the machine-learning roots inside it would duplicate a hundred nodes.

- [ ] **Step 3: Order each path by topological sort, then adjust for pedagogy**

`requires` is acyclic after Task 11, so every path has exactly one family of correct orderings and a topological sort over each path's induced subgraph finds one in a single pass. Running check 4 and moving one node at a time would take hours across hundreds of edges and would introduce its own mistakes, so the sort is the method and check 4 is the verification.

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
# Order each path so every prerequisite precedes its dependant.
#
# Ties break alphabetically rather than arbitrarily, so re-running produces the
# same order and a re-sorted path is not a spurious diff. A prerequisite
# satisfied through builds_on is ignored here, because it is already earlier by
# definition and pulling it in would duplicate another path's nodes.
#
# Only the value of `nodes:` is rewritten, by text substitution. Round-tripping
# the whole file through yaml.safe_dump turned a block-scalar preamble into a
# quoted string with a changed trailing value on a fixture, which is prose the
# path's author wrote and this script has no business touching.
import re
from graphlib import TopologicalSorter
from pathlib import Path

from scripts.alchemist.model import load_corpus

# The value runs to the next top-level key. A block-list item starts with "- ",
# so the lookahead excludes it rather than stopping at any non-space character;
# without that exclusion a block-style path had its old list left in place under
# the new one.
NODES_KEY = re.compile(r"^nodes:.*?(?=^(?!- )\S|\Z)", re.S | re.M)

corpus = load_corpus(Path.cwd())

for path_id, path in corpus.paths.items():
    members = set(path.nodes)
    graph = {
        node_id: {r for r in corpus.nodes[node_id].requires if r in members}
        for node_id in members
    }
    sorter = TopologicalSorter(graph)
    sorter.prepare()
    ordered = []
    while sorter.is_active():
        ready = sorted(sorter.get_ready())
        ordered.extend(ready)
        for node_id in ready:
            sorter.done(node_id)

    # A path whose existing order already satisfies every prerequisite is left as it
    # is, whatever the sort would have produced. The braids are hand-sequenced to
    # argue something, and any valid hand order is one of many valid topological
    # orders; the sort's alphabetical ties would flatten it into a different one.
    # Task 12's first run did exactly that to two braids, and the review caught it.
    seen: set[str] = set()
    already_valid = True
    for node_id in path.nodes:
        if any(r in members and r not in seen for r in corpus.nodes[node_id].requires):
            already_valid = False
            break
        seen.add(node_id)
    if already_valid:
        print(f"{path_id:30} already ordered, {len(path.nodes)} nodes")
        continue
    target = Path("paths") / f"{path_id}.yaml"
    block = "nodes:\n" + "".join(f"- {node_id}\n" for node_id in ordered)
    text, count = NODES_KEY.subn(block, target.read_text())
    assert count == 1, f"{path_id}: the nodes key matched {count} times"
    target.write_text(text)
    print(f"{path_id:30} reordered, {len(ordered)} nodes")
EOF
```

Then verify, and adjust by hand only where the sort is correct but reads badly:

Run: `.venv/bin/python scripts/check.py`
Expected: check 4 `ok`. A remaining failure names a node and a prerequisite the sort could not place, which means the prerequisite is in **neither** this path nor anything its `builds_on` reaches. **`builds_on` is the right fix where the prerequisite belongs to another domain, and adding the node to this path is the right fix where it belongs to this one.** Reaching for `builds_on` to silence a within-domain failure hides a membership mistake rather than fixing it.

A topological sort is correct and frequently unpedagogical: it will happily put every zero-prerequisite node first, so a path opens with forty definitions before it teaches anything. Move nodes by hand where that happens, re-run check 4 after each move, and stop when the path reads like a course rather than like a build order.

- [ ] **Step 4: Verify every node sits in at least one path**

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python -c "
from pathlib import Path
from scripts.alchemist.model import load_corpus
corpus = load_corpus(Path.cwd())
placed = {n for p in corpus.paths.values() for n in p.nodes}
orphans = sorted(set(corpus.nodes) - placed)
print(f'{len(orphans)} nodes sit in no path, of {len(corpus.nodes)}')
for node_id in orphans[:40]:
    print(f'  {node_id}  {corpus.nodes[node_id].domains}')
"
```

An orphan is not a failure and no check rejects one, so this is a judgement for gate 2 rather than a gate here. A node in no path is either a path that is missing or a node that should not have been written, and Task 14's review document lists them so Mario decides.

- [ ] **Step 5: Run the full checks and the suite**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python -m pytest`
Expected: nine checks `ok` over roughly 1,600 nodes (Task 8 staged 1,583 distinct ids) and ten paths, and every test passing.

- [ ] **Step 6: Commit, with everything held back since Task 9**

This is the first commit the hook lets through since Task 9's, because check 3 and check 4 are green
only once the graph is acyclic and the paths order it. So it carries Task 10's three files, Task 11's
edits to `nodes/` and its prerequisite report, the plan amendments made meanwhile, and this task's
paths. Run `git status --short | grep -v '^?? nodes/\|^ M nodes/'` first and add, with an explicit
path, anything the list below has missed. Never `git add -A`.

```bash
git add nodes/ paths/ notes/prerequisite-report-2026-09-04.md notes/transcription-brief.md \
  scripts/alchemist/grain.py scripts/grain_audit.py tests/test_grain.py \
  docs/superpowers/plans/2026-09-04-alchemist-phase-1.md
git commit -m "feat(paths): build the ten initial paths and land the resolved corpus"
```

---

### Task 13: Seed the gap ledger

**Files:**
- Modify: `sources/wanted.yaml`

**Interfaces:**
- Consumes: the resolved corpus.
- Produces: a ledger whose every `needed_by` id resolves, so check 9 passes.

Phase 2 populates the ledger properly, node by node, once it has searched the vault. Phase 1 seeds only what it already knows, which is the sources the transcription itself established a need for and could not satisfy.

**Task 3 hardened the two checks that read this file, so a malformed entry is now a reported failure rather than a stack trace.** Seed with that in mind: every entry carries an `id`, and every `needed_by` is a list.

- [ ] **Step 1: Seed the entries Phase 1 knows about**

At minimum these three, each following spec section 4.4's schema:

```yaml
- id: renshaw-verrall-1998-glm-claims-reserving
  needed_by: [chain-ladder, over-dispersed-poisson-model]
  claim: >
    That the chain ladder reserve estimates coincide with the maximum
    likelihood estimates of an over-dispersed Poisson generalised linear model
    with a log link and additive origin and development effects.
  document: "Renshaw, A.E. and Verrall, R.J. (1998), A stochastic model underlying the chain-ladder technique, British Actuarial Journal"
  url: null
  expected_tier: T4
  acquisition: journal
  status: wanted
  note: >
    The claim itself is already citable through
    england-verrall-2002-stochastic-claims-reserving, which the vault holds at
    T4 public-free and which states it at sections 2.2.1, 2.3.4 and 7.2.14.
    This entry is for the primary rather than the survey, and a node may reach
    status drafted on the survey alone.
- id: ifoa-cs2-core-reading-2026
  needed_by: [cox-proportional-hazards-model, kaplan-meier-estimator, mortality-graduation]
  claim: >
    The worked treatment of proportional hazards, the Kaplan-Meier estimator
    and the methods of mortality-graduation, at the depth CS2 examines them.
  document: "IFoA CS2 Core Reading, 2026"
  url: null
  expected_tier: T4
  acquisition: purchased-personal
  primary_alternative: "Collett, D., Modelling Survival Data in Medical Research"
  status: wanted
- id: bcbs-d424-irb-risk-weight-functions
  needed_by: [irb-risk-weight-function, asset-correlation]
  claim: >
    The black-letter text of the IRB risk-weight functions and the supervisory
    asset correlation, as the standard states them rather than as an
    explanatory note paraphrases them.
  document: "Basel III: finalising post-crisis reforms (d424), Chapter CRE31"
  url: "https://www.bis.org/bcbs/publ/d424.pdf"
  expected_tier: T1
  acquisition: regulator
  status: wanted
  note: >
    The vault holds d424 already at markdown/bcbs/d424.md. Verify that the
    chapter the nodes need is present in the extraction before marking this
    ingested, because a partial extraction of a 160-page standard is the
    failure this entry exists to catch.
```

Add every further entry Wave 1's reports named. An agent that wrote "I could not confirm the section numbering for X" has named a gap.

- [ ] **Step 2: Verify every needed_by id resolves**

Run: `.venv/bin/python scripts/check.py`
Expected: check 9 `ok`. A failure here names a node id that does not exist, which is a typo in the ledger rather than a missing node: the whole point of rule 9 is that a mistyped id disables check 6 for that node silently and permanently.

- [ ] **Step 3: Verify the hardening still holds against the real file**

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python -c "
import yaml
from pathlib import Path
entries = yaml.safe_load(Path('sources/wanted.yaml').read_text())
assert isinstance(entries, list), 'the ledger must be a list of entries'
for position, entry in enumerate(entries, start=1):
    assert isinstance(entry, dict), f'entry {position} is not a mapping'
    assert 'id' in entry, f'entry {position} has no id'
    assert isinstance(entry.get('needed_by') or [], list), f\"{entry['id']}: needed_by is not a list\"
print(f'{len(entries)} ledger entries, every one well formed')
"
```

- [ ] **Step 4: Commit**

```bash
git add sources/wanted.yaml
git commit -m "feat(sources): seed the gap ledger with what Phase 1 established"
```

---

# Wave 3: gate 2

### Task 14: The review document

**Files:**
- Modify: `scripts/alchemist/site.py`
- Modify: `tests/test_site.py`
- Create: `site/review.md`, by generation only

**Interfaces:**
- Consumes: the finished `Corpus`.
- Produces: `render_review(corpus: Corpus) -> str`, wired into `build()`, writing `site/review.md`.

Gate 2 is the phase's whole justification and it is cheap only if it is passable. **A thousand markdown files cannot be read once.** This is the artefact that makes the gate real: nodes grouped by path, one line each, with the numbers at the head and the orphans at the foot.

It is markdown rather than HTML because it is read once and then thrown away, and because a diff of it between two Phase 1 revisions is legible in a way a diff of generated HTML is not.

- [ ] **Step 1: Write the three corpus fixtures the tests need**

`tests/test_site.py` builds its objects inline from `MathObject` and `Alias` and has **no corpus
fixture at all**, checked by reading it rather than assumed. The three helpers below come first,
because the orphan test in particular is meaningless against a fixture with no orphan.

```python
# tests/test_site.py, added beside the existing OBJECTS constant
def _node(node_id: str, *, title=None, domains=("credit",), requires=(), anchor=("chosen",)) -> Node:
    return Node(
        id=node_id, title=title or node_id.replace("-", " ").capitalize(),
        domains=domains, status="stub", requires=requires, spends=(), anchor=anchor,
        vault_articles=(), vault_sources=(), taught_in=None, body="A stub.",
        path=Path(f"nodes/{node_id}.md"),
    )


def _path(path_id: str, nodes: tuple[str, ...], *, builds_on=()) -> TeachingPath:
    return TeachingPath(
        id=path_id, title=path_id.replace("-", " ").capitalize(),
        builds_on=builds_on, preamble=f"The {path_id} path.", nodes=nodes,
    )


def two_path_corpus() -> Corpus:
    """Two paths, four nodes, every node placed. The baseline the review renders."""
    nodes = {
        n.id: n
        for n in (
            _node("conditional-probability", domains=("maths", "stats")),
            _node("survival-function", domains=("stats", "credit")),
            _node("hazard-rate", title="Hazard rate", domains=("stats", "credit"),
                  requires=("survival-function",), anchor=("ifoa.cs2.2.1-3",)),
            _node("discrete-time-hazard", requires=("hazard-rate",)),
        )
    }
    paths = {
        "maths-stats-prerequisites": _path(
            "maths-stats-prerequisites", ("conditional-probability",)
        ),
        "survival-braid": _path(
            "survival-braid",
            ("survival-function", "hazard-rate", "discrete-time-hazard"),
            builds_on=("maths-stats-prerequisites",),
        ),
    }
    return Corpus(nodes=nodes, paths=paths)


def corpus_with_an_orphan(node_id: str) -> Corpus:
    """The baseline plus one node in no path, which no check rejects and only the
    review document makes visible."""
    corpus = two_path_corpus()
    corpus.nodes[node_id] = _node(node_id, domains=("gi",))
    return corpus


def shared_node_corpus(node_id: str) -> Corpus:
    """One node earning a place in two paths, which spec section 4.3 permits
    outright and the review must therefore show under both."""
    corpus = two_path_corpus()
    braid = corpus.paths["survival-braid"]
    corpus.paths["credit-trunk"] = _path(
        "credit-trunk", (node_id,), builds_on=("maths-stats-prerequisites",)
    )
    assert node_id in braid.nodes, "the fixture only means anything if the node is in both"
    return corpus
```

Widen the module's import line, which today reads
`from scripts.alchemist.model import Alias, Corpus, MathObject, Node, Objects, Spend`, to add
`TeachingPath`, and add `render_review` to the `site` import.

- [ ] **Step 2: Write the failing tests**

Add to `tests/test_site.py`:

```python
def test_the_review_lists_every_node_under_its_path():
    corpus = two_path_corpus()
    review = render_review(corpus)
    for node in corpus.nodes.values():
        assert node.id in review
    for path in corpus.paths.values():
        assert path.title in review


def test_the_review_carries_the_counts_at_its_head():
    corpus = two_path_corpus()
    review = render_review(corpus)
    head = review.split("## ", 1)[0]
    assert str(len(corpus.nodes)) in head
    assert str(len(corpus.paths)) in head


def test_the_review_lists_orphans_separately():
    """A node in no path is a judgement for gate 2 and no check rejects one,
    so the review is the only place it becomes visible."""
    corpus = corpus_with_an_orphan("ruin-theory")
    review = render_review(corpus)
    assert "ruin-theory" in review.rsplit("Orphan", 1)[-1]


def test_a_node_line_carries_its_anchor_and_prerequisite_count():
    corpus = two_path_corpus()
    review = render_review(corpus)
    node = corpus.nodes["hazard-rate"]
    line = next(l for l in review.splitlines() if l.startswith(f"| `{node.id}`"))
    assert node.anchor[0] in line
    assert f"| {len(node.requires)} " in line


def test_a_node_in_two_paths_appears_under_both():
    corpus = shared_node_corpus("hazard-rate")
    review = render_review(corpus)
    assert review.count("`hazard-rate`") >= 2
```

- [ ] **Step 3: Run the tests and verify they fail**

Run: `.venv/bin/python -m pytest tests/test_site.py -k review -v`
Expected: FAIL, `ImportError: cannot import name 'render_review'`.

- [ ] **Step 4: Write the renderer**

Add to `scripts/alchemist/site.py`:

```python
def render_review(corpus: Corpus) -> str:
    """One document gate 2 can be read from.

    Spec section 9 makes gate 2 the whole justification for Phase 1 being a
    separate phase, on the argument that a wrong skeleton is cheap to fix now
    and ruinous once pages hang off it. That argument needs the gate to be
    passable, and a thousand markdown files are not readable once. So this is
    the node list, grouped by the paths that give it an order, with the
    numbers at the head and the nodes belonging to no path at the foot.
    """
    total_requires = sum(len(n.requires) for n in corpus.nodes.values())
    shared = sum(1 for n in corpus.nodes.values() if len(n.anchor) > 1)
    chosen = sum(1 for n in corpus.nodes.values() if "chosen" in n.anchor)
    domains: dict[str, int] = {}
    for node in corpus.nodes.values():
        for domain in node.domains:
            domains[domain] = domains.get(domain, 0) + 1

    out = [
        "# Phase 1 review",
        "",
        "The node list and the paths, for gate 2. Read the numbers, then the paths in",
        "order, then the orphans. Nothing here is generated from anything but the",
        "corpus itself, so a correction is an edit to a node file and a re-run.",
        "",
        f"- Nodes: **{len(corpus.nodes)}**",
        f"- Paths: **{len(corpus.paths)}**",
        f"- Prerequisite edges: **{total_requires}**",
        f"- Nodes anchored by more than one body: **{shared}**",
        f"- Nodes anchored `chosen`, meaning the floor is yours: **{chosen}**",
        "",
        "Nodes per domain: "
        + ", ".join(f"{d} {domains[d]}" for d in sorted(domains)),
        "",
    ]

    placed: set[str] = set()
    for path_id in sorted(corpus.paths):
        path = corpus.paths[path_id]
        out += [
            f"## {path.title}",
            "",
            f"`{path.id}`"
            + (f", builds on {', '.join(f'`{b}`' for b in path.builds_on)}" if path.builds_on else ""),
            "",
            path.preamble.strip(),
            "",
            "| Node | Title | Domains | Reqs | Anchor |",
            "| --- | --- | --- | ---: | --- |",
        ]
        for node_id in path.nodes:
            node = corpus.nodes.get(node_id)
            if node is None:
                out.append(f"| `{node_id}` | **MISSING** | | | |")
                continue
            placed.add(node_id)
            out.append(
                f"| `{node.id}` | {node.title} | {', '.join(node.domains)} "
                f"| {len(node.requires)} | {', '.join(node.anchor)} |"
            )
        out.append("")

    orphans = sorted(set(corpus.nodes) - placed)
    out += [
        "## Orphan nodes",
        "",
        f"{len(orphans)} nodes sit in no path. No check rejects one, so this is a",
        "judgement rather than a failure: each is either a path that is missing or a",
        "node that should not have been written.",
        "",
    ]
    if orphans:
        out += ["| Node | Title | Domains | Anchor |", "| --- | --- | --- | --- |"]
        for node_id in orphans:
            node = corpus.nodes[node_id]
            out.append(
                f"| `{node.id}` | {node.title} | {', '.join(node.domains)} "
                f"| {', '.join(node.anchor)} |"
            )
        out.append("")

    return "\n".join(out)
```

Wire it into `build()`, immediately after the index:

```python
    review = root / "site" / "review.md"
    review.parent.mkdir(parents=True, exist_ok=True)
    review.write_text(render_review(corpus))
    written.append(review)
```

- [ ] **Step 5: Run the tests and verify they pass**

Run: `.venv/bin/python -m pytest tests/test_site.py -v`
Expected: PASS, every test in the module including the pre-existing ones.

- [ ] **Step 6: Verify the tests would fail under the bug they name**

Change the orphan calculation to `orphans = []` and re-run: `test_the_review_lists_orphans_separately` must fail. Change the per-path loop to `for node_id in path.nodes[:1]` and re-run: `test_the_review_lists_every_node_under_its_path` must fail. Restore both. **Report which tests failed under each mutation and which did not**, because a test that survived a mutation was not testing what it names.

- [ ] **Step 7: Generate it**

Run: `.venv/bin/python scripts/build_site.py && wc -l site/review.md`
Expected: `site/review.md` among the written paths, and a document of roughly 1,300 to 1,700 lines. Read the head yourself before handing it over: if the domain counts are lopsided, meaning one domain carrying nine hundred nodes and another carrying four, that is a finding for gate 2 and worth naming in the handover rather than leaving for Mario to spot.

- [ ] **Step 8: Commit**

`site/` is gitignored, so the generated document is not committed and is regenerated on demand.

```bash
git add scripts/alchemist/site.py tests/test_site.py
git commit -m "feat(site): generate the review document gate 2 is read from"
```

---

### Task 15: Verify the phase and write the handover

**Files:**
- Create: `notes/phase-1-report.md`
- Modify: `README.md`, adding a corpus-size line where none exists today
- Modify: `index.html`, regenerated by `build_site.py`. It is a tracked build artefact and has read "3 nodes across 2 paths" since Phase 0; no check keeps it current (check 7 covers `notation/symbols.md` alone), which the phase report records as a gap for Phase 2 to close by extending check 7.

**Interfaces:**
- Consumes: everything above.
- Produces: the document Mario reads alongside `site/review.md` at gate 2.

- [ ] **Step 1: Run every gate the repo has**

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python -m pytest -q
.venv/bin/python scripts/check.py
.venv/bin/python scripts/build_site.py > /dev/null && echo "site built"
.venv/bin/python scripts/katex_sweep.py notation/objects.yaml notation/symbols.md nodes/*.md lectures/*.qmd
.venv/bin/python scripts/grain_audit.py | head -40
.venv/bin/python scripts/fetch_syllabi.py
```

Expected: every test passing, nine checks `ok`, the site building, `0 unsupported` from the sweep, a grain table, and `0 hash mismatches`. **Record the actual output of each rather than the fact that you ran it.**

One known flake is documented and may appear: on one of seven full-suite runs in Phase 0, `test_the_pdf_is_complete` failed with a `subprocess.CalledProcessError` and was not reproducible in six further runs. Three tests render the same probe path in sequence and the fixture's cleanup races the render script's own. If it appears, re-run the suite, record both results, and note that the fix is a unique probe path per test rather than a retry.

- [ ] **Step 2: Give the README a corpus-size line**

`README.md` states no corpus size today, which was right while three exemplar nodes stood and
is wrong now: a reader landing on the repo cannot tell whether the graph is a sketch or a
corpus. Add one sentence to the end of the opening section, before "Published at":

```markdown
The graph currently holds <N> nodes across <M> paths, anchored against 20 published syllabi
and standards. Every node carries a reference page, and the ones on the trunk carry a lecture
as well.
```

Substitute the figures the corpus actually reached rather than this plan's estimate.

- [ ] **Step 3: Write the phase report**

`notes/phase-1-report.md`, covering:

- What was produced: the node count, the path count, the object count, the ledger entry count, and the review document's path.
- **What `check.py` did not verify**, stated plainly: anchor accuracy against the source documents, grain consistency, and pedagogical ordering. Say which of the three were sampled by hand, how many samples, and what the samples found.
- The grain outliers, per body, with the decision taken on each and why.
- The merge report's title disagreements, unresolved, because they are Mario's to settle.
- The orphan nodes, with a view on whether each wants a path or wants deleting.
- Every node anchored `chosen`, because that is the list of places where the corpus's floor is a judgement rather than a syllabus, and it is the second thing gate 2 should read after the numbers.
- What Phase 2 inherits: the ledger's seed entries, the suspected overlaps that were merged and the ones that were not, and any body whose extraction was poor enough that its anchors are less reliable than the rest.
- The two decisions still open: whether committed lecture HTML stays inlined at 767 kB per revision, and the second scoping axis for the domain graphs, which measured at 600 nodes was already 31 kB with 599 edges and is now considerably worse.

- [ ] **Step 4: Commit and open the pull request**

```bash
git add notes/phase-1-report.md README.md index.html
git commit -m "docs(phase-1): record what the phase produced and what it did not verify"
git push -u origin feat/phase-1-skeleton
gh pr create --base feat/phase-0-machinery --title "Phase 1: the syllabus skeleton" \
  --body-file notes/phase-1-report.md
```

`--base feat/phase-0-machinery` is not optional. This branch was cut from Phase 0's, PR #1 is
still open, and defaulting the base to `main` would put all of Phase 0 into Phase 1's diff.

**Do not merge.** House rules forbid self-merging, and gate 2 is Mario's read.

---

## Self-review

**Spec coverage.** Section 4.1's node record is Task 8's schema and Task 9's renderer. Section 4.1a's grain rule is Task 7's brief and Task 10's audit. Section 4.2's notation contract is Tasks 4 and 5. Section 4.3's paths are Task 12. Section 4.4's ledger is Task 13, with Task 3 hardening the checks that read it. Section 5's nine checks gate every task through the pre-commit hook. Section 9's Phase 1 row names 20 bodies (Tasks 1 and 8), the initial paths (Task 12), the four requirements in `notes/uni-programme-anchors.md` (Task 5 seeds the objects, Task 11 builds the braid edges, Task 12 writes the braid path, and Task 8's UP dispatches replace the three `chosen` floors), and the review document (Task 14). The handoff's five open items are covered: the two Phase 0 decisions are settled in the spec amendment and Task 4, the branch question is answered in the plan header, the KaTeX extension is Task 6, and the chain-ladder verification landed before this plan was written. **One item is deliberately not covered:** the second scoping axis for the domain graphs, which is recorded in Task 15's report as still open, because it is a Phase 3 rendering question rather than a skeleton question and solving it now would guess at a node count nobody has yet.

**Placeholders.** None. Every code step carries the code, every YAML step the YAML, and the brief in Task 7 is written out in full rather than described. Task 12's path files carry an ellipsis inside a `nodes:` list, which is the one place a literal list cannot be written in advance because it depends on what Wave 1 produces; the surrounding text says exactly how to fill it and check 4 rejects a wrong answer.

**Type consistency.** `Node`, `TeachingPath`, `Corpus`, `Spend` and `Objects` are Phase 0's and are used unchanged. `merge` returns `tuple[Node, list[str]]` in Task 9's interface block, its docstring, its implementation and every test. `collect` returns `dict[str, list[Node]]` throughout. `spans_in` returns `list[tuple[int, bool, str]]`, matching `extract_spans`, which is what lets `sweep` call either. `audit` returns `GrainReport` and `render_review` returns `str`, both consistent between the interface blocks and the code.
