# Alchemist Phase 3 Pages design

**Status:** settled with Mario on 19 September 2026. The four open decisions (D3.1, D3.3, D3.4
and D3.8) were each taken on the recommended option, and the plan follows from this document.

**Parent spec:** `2026-09-03-alchemist-syllabus-design.md`, sections 4.1, 4.1a, 4.2, 9 and 10.
This document settles what that one left to Phase 3 and amends the lines section 14 below names.

## 1. What Phase 3 changes

Phase 3 replaces every stub body with a written tier-1 page and moves the node from
`status: stub` to `status: drafted`. Nothing else in a node record changes. `requires`, `anchor`,
`vault_articles` and `taught_in` were settled in Phases 1 and 2 and stay as they are, and
`status: reviewed` remains Mario's to set after the gate. The page is written against the
template Phase 0 locked, three sections under fixed headings, and every write goes through a
tool so the record's shape never varies across 1,557 files.

Two things are decided before a page is written. The first is which model writes, settled by the
measurement section 10 of the parent spec prescribes. The second is what a page is written from
where the vault holds nothing, a question the parent spec's phase table assumed Phase 2a would
have answered by now and which the measured coverage below shows it has not.

## 2. The measured starting position

Measured on 19 September 2026 at `main` `5187bfd`, eleven checks clean and 321 tests passing.

- 1,560 nodes, 3 drafted (the Phase 0 exemplars `conditional-probability`, `survival-function`
  and `hazard-rate`) and 1,557 stubs. Stub bodies run from 12 to 273 words with a median of 28:
  one paragraph stating the syllabus item's scope in the transcriber's words.
- 356 nodes carry at least one vault article and 1,204 carry none. Phase 2's cover bar was
  "enough to write the page from", so this is exactly the split between pages with a vault basis
  and pages without one.
- `notation/objects.yaml` holds 17 objects. Two nodes declare any `spends`, both exemplars.
- The `requires` graph has 453 roots and a maximum depth of 12. Depth 0 to 3 holds 1,187 nodes;
  depth 4 and beyond holds 373.
- The survival braid path holds five nodes, two already drafted, so the parent spec's "ten nodes
  from the survival braid" has to be read as the survival area of the graph rather than the path
  file. The area holds some thirty undrafted nodes across `ifoa.cs2`, `ifoa.cm1`, `up.ias` and
  `assa.f107` anchors.
- Fable 5.1 lists at 10 dollars per million input tokens and 50 per million output; Sonnet 5 at
  2 and 10. The measurement therefore decides a fivefold per-token difference over 1,557 pages.
- Gate 2's finding F8: 200 of the 1,580 original stub bodies, 12.7 per cent, carry "rather
  than", the phrase the Phase 1 brief prescribed in place of negated counterparts. G20 asks
  Phase 3's template to cap it.
- The grader, `writing-guidelines-grader`, grades eleven mechanical criteria (M1 to M11) and
  thirty judgement criteria (J1 to J30), seven of them withdrawn. Its J25 (connective density) is
  graded per section and warns rather than fails, so a page of three short sections will draw
  J25 warnings in both arms; they are noise the pairing cancels.

## 3. Decisions

Eight. Four were put to Mario and settled on 19 September 2026; the other four follow from the parent spec or from
Phase 2 precedent and are recorded so a later reader need not infer them.

**D3.1 The measurement is paired and blind.** Both models write the same ten nodes,
twenty pages in all, into two staging directories named by an arm letter, with the
letter-to-model mapping sealed in a third file until the verdict is recorded. The grader and
Mario's spot-read see arm letters only. The parent spec's wording admits twenty distinct nodes,
ten per model, and that design confounds the model with the subject: `kaplan-meier-estimator` is
harder to write than `life-table` whichever model draws it. Pairing costs the same twenty pages
and removes the confounder. The alternative, twenty distinct nodes, lands twenty pages rather
than ten and is the literal reading of the parent spec.

**D3.2 The decision rule is written down before the pages are.** Section 5 states it. A rule
chosen after reading the pages would be a preference dressed as a measurement, which is what
the parent spec's "by measurement rather than by preference" exists to rule out.

**D3.3 Every node is written this phase, with or without a vault article.** A covered
node is written from its attached articles; an uncovered node is written from its stub body,
its anchor, its graph neighbourhood and the model's own knowledge of standard material. Both
land as `drafted`. Check 6 already refuses `reviewed` while a gap-ledger entry names the node,
so acquisition still gates the status that matters and Phase 2a keeps its job. The alternative
writes the 356 covered nodes now and leaves 1,204 stubs standing until their documents arrive,
which at the ledger's current pace is months. Section 6 states what an uncovered page is
written from and what guards it.

**D3.4 Agents declare only the (object, domain) pairs `objects.yaml` already carries,
and report the collisions they met.** The write tool refuses any other pair, so check 1 cannot
fail on an agent's write. Each report fragment lists the symbols a page uses that the node's
domains would spell differently, with a proposed object id and per-domain spelling. After each
wave Mario reviews that list and adds the objects worth adding, and a short sweep declares the
new spends through the tool. The alternative lets agents write proposed objects into staged
fragments merged like the ledger, which is the ledger's unbounded case again: thirty-nine
agents naming objects independently, into the one file a reader trusts for spelling.

**D3.5 A write tool owns every record write, and check 12 owns the template.** Agents never
hand-edit a record, following `attach_articles.py`. The tool validates the body against the
template, sets `status: drafted` and `spends`, and re-renders the record through `render` so
every write is identical in shape. Check 12 then enforces the template on every non-stub node,
so a hand edit after the phase cannot break a page silently. The parent spec's gate row says
"the checker owns structure", and this is the check that makes the sentence true.

**D3.6 Batches run in depth-then-id order.** Sorting the 1,547 undrafted node ids by depth in
the `requires` graph and then alphabetically, before slicing into 39 batches of 40, puts every
prerequisite of a node in an earlier wave for 456 of the 1,107 non-root nodes, against 232 under
the alphabetical order Phase 2 used. An agent writing "Why this node exists" then reads a
drafted prerequisite page rather than a stub more often than not. The change is a sort key in
`batches.py`; the manifest records explicit ids either way.

**D3.7 `vault_sources` stays empty.** Nothing is quoted at tier 1. A page paraphrases what its
articles say, so check 5 has nothing to inspect and a `public-paid` article can inform a page
without any risk of its text reaching a public repo. The rule is in the brief.

**D3.8 The measurement runs as the implementation plan's first tasks.** The plan is
written now, with the writing model as the one parameter its wave tasks take, and its first
three tasks build the write tool, run the two arms and record the verdict. The alternative runs
the measurement before any plan exists, which means writing twenty pages without the tool and
without the brief the plan locks, so the pages measured are not the pages Phase 3 would write.

## 4. The locked template

The Phase 0 plan fixed the template at its Task 11, and `nodes/conditional-probability.md` is
the exemplar to copy. A body carries exactly three sections, in this order and under these
headings, and nothing else on the rendered page is the author's.

1. `## Definition`: one or two sentences a reader could quote, naming the object and giving a
   condition or degeneracy where one is worth stating. Not every object has one; leave the
   clause out sooner than invent it, which is the lesson `survival-function`'s first draft
   taught.
2. `## The expression`: the defining formula in a display block, in the rendering the node's
   `spends` declares, with every symbol named in the sentence beneath. One display block is the
   norm and two is the ceiling. A node wanting a third is a node wanting to be two nodes, and
   the agent reports it as a split candidate rather than writing it.
3. `## Why this node exists`: two or three sentences on what breaks without it, ending on the
   node that needs it next where the graph has one, and otherwise on the consequence.

Phase 3 adds four rules the exemplars imply and the brief states outright.

- **The forward reference names a real node.** The closing sentence's "needs it next" names an
  id from the node's derived unlocks, which the agent obtains by grepping `requires:` across
  `nodes/`, since `unlocks` is never stored. Nothing validates a forward reference in prose, so
  an invented id reads as fine writing and promises a page that will never exist.
- **"The prerequisite", never "the previous node".** A node sits in several paths, so it has no
  single previous node. `hazard-rate`'s body says "the previous node named" and reads correctly
  only from the survival braid.
- **"Rather than" at most once per page.** G20's cap, enforced by the tool.
- **`\lt` and `\gt` inside mathematics**, as `hazard-rate` writes them, so a comparison can never
  be read as an HTML tag.

The rules a page inherits from `CLAUDE.md` stand: British English, no em or en dashes, currency
with the unit word and never a bare dollar sign, no negated counterpart clauses.

## 5. The model measurement

**The ten nodes.** Chosen from the survival area for a spread of depth, coverage, domain count
and anchor body, and for two nodes that exercise the notation contract hard.

| Node | Depth | Vault article | Domains | Why it is in |
|---|---|---|---|---|
| `future-lifetime-random-variable` | root | none | life, stats | a root with no article |
| `life-table` | root | none | life, stats | a root; the stub is one sentence |
| `lifetime-distribution-function` | 1 | none | credit, life, stats | spends `obj.lifetime-cdf` in three domains, so the alias table renders |
| `survival-hazard-relationships` | 2 | none | life, stats | requires three nodes and spends three objects |
| `censoring` | root | one | credit, life, stats | covered, three domains, two anchor bodies |
| `empirical-survival-function` | 1 | none | life, stats | the plain case |
| `kaplan-meier-estimator` | 2 | none | life, stats | the stub names Greenwood's formula, which tempts a third block |
| `nelson-aalen-estimator` | 2 | none | life, stats | the cumulative-hazard twin of the row above |
| `proportional-hazards-model` | 2 | one | life, stats | covered, `ifoa` and `up` anchors |
| `survival-model-credit-risk` | root | one | credit, stats | covered, credit register, `assa` anchor |

Three covered and seven uncovered, close to the corpus's 23 to 77 split, so the measurement
tests both writing regimes of D3.3.

**The arms.** Two subagents, one on `model: "fable"` and one on `model: "sonnet"`, receive the
same prompt to the byte except the arm letter: read `notes/phase-3-pages-brief.md`, read the
three exemplars and `notation/objects.yaml`, then write each of the ten nodes' body, the three
sections and nothing else, to `.staging/phase-3/measurement/arm-<x>/<id>.md`, validating each
with the write tool's `--check` mode before moving on, and write
`.staging/phase-3/measurement/report-arm-<x>.md` naming per node the `spends` pairs the page
uses, the sources read, and any collision or split candidate. The body files are what the
grader reads, so no frontmatter sits in them to be graded as prose, and the report sits outside
the arm directory so the grader never grades it.
`.staging/phase-3/measurement/arms.yaml` records which letter is which model and is read only
when the verdict is written. Neither arm touches `nodes/`.

**The decision rule.** Fixed here, before either arm runs.

1. **Template filter.** Every page passes the write tool's validator or counts as a fail for its
   arm, since a page that breaks the template is a page a person has to repair.
2. **Grader.** `writing-guidelines-grader` runs non-interactively over each arm directory. An
   arm's primary score is its total `fail` verdicts across the ten pages, mechanical and
   judgement together; its secondary score is its total `warn` verdicts.
3. **Blind read.** Mario reads three pairs, drawn by a seeded draw recorded in the decision
   note, arm letters only, and records a preference per pair on correctness of the mathematics
   first and voice second.
4. **Verdict.** Sonnet writes Phase 3 unless Fable both records at least three fewer fails
   across the ten pages and takes at least two of the three blind pairs. Five times the
   per-token price needs a margin the grader can see; a tie or a one-fail edge is Sonnet's.
5. **Cost.** Each arm's reported token usage on completion is recorded beside the grades, since
   the measured tokens per page for each model are a better cost input than list price.

**The record.** `notes/phase-3-model-decision-2026-09.md` carries the grade table per arm and
per criterion, the blind-read verdicts, the token figures, the unsealed arm mapping and the
verdict. The parent spec's section 10 row is then filled in with a pointer to it.

**What happens to the pages.** The winning arm's ten land in `nodes/` through the write tool,
each call taking the body file and the `spends` pairs its report names, as Phase 3's first ten
pages. The losing arm's ten stay in staging until the branch merges and
are then discarded.

**Cost of the phase, to be replaced by measurement.** On the assumptions of some 2,000 output
tokens per page including thinking and a context that grows to a few hundred thousand tokens
over a forty-node batch, mostly served from cache, a wave of thirteen agents costs on the order
of tens of dollars API-equivalent on Sonnet and roughly five times that on Fable, so the phase
sits in the low hundreds on Sonnet and around a thousand on Fable. The measurement's token
figures replace this paragraph.

## 6. Writing without a vault article

Under D3.3 an uncovered page is written from five things the agent has in front of it: the stub
body, which is the transcriber's one-paragraph scope statement and is discarded once the page
replaces it; the anchor, which names the syllabus item and so the depth the page is examined
at; the node's `requires` and derived unlocks, which fix what the page may assume and what it
must end on; the notation contract; and the three exemplars. A covered page has all five and
its articles besides, read in full before writing.

Tier 1 asks for a definition and one formula, and every node in the corpus is anchored to a
published syllabus item, so the material is standard by construction. The risk is a
non-standard or wrong definition written from memory, and three things guard it. The gate's
spot-read is directed at correctness first. Check 6 holds `reviewed` back until the ledgered
document arrives, so an uncovered page is published as a draft and never as a reviewed one.
And the rendered page's Sources section is simply absent for an uncovered node, which tells the
reader the truth without a new field.

## 7. The notation contract at scale

Seventeen objects will not cover 1,557 pages, and they are not meant to. The contract exists
for the object that appears under different spellings in different domains, so that a bridge
table can be generated; a `\beta` in a single-domain regression node needs no object. Under
D3.4 the agent declares the pairs that exist and the tool refuses the rest, so no wave can
fail check 1. The report fragment then carries, per node, any symbol the page uses that the
node's domains would spell differently, with a proposed id, the spelling per domain and what
each domain calls it. Mario reviews the list after each wave, adds what is worth adding to
`objects.yaml`, regenerates `symbols.md` for check 7, and a sweep declares the new spends on the
affected nodes through the tool. The contract stays a reviewed file, and it grows at the pace a
reader can check.

## 8. The write tool and check 12

`scripts/alchemist/pages.py` holds the logic and `scripts/write_page.py` is the CLI over it,
following `checks.py` and `check.py`.

```
.venv/bin/python scripts/write_page.py --node <id> --body <path> [--spends obj.x:domain ...]
.venv/bin/python scripts/write_page.py --check <path>
```

The validator, shared by the tool and check 12, enforces the template mechanically: exactly the
three headings in order and no other heading of any level; one or two display blocks; no
currency amount written with a dollar sign, meaning a pattern such as `$2m` or `$1,500`, since
a bare `$` is a maths delimiter and `$1$` is legitimate inline mathematics; no em or en dash;
"rather than" at most once; and a non-empty body under each heading. The writer additionally refuses any `spends` pair absent
from `objects.yaml`, refuses to overwrite a `reviewed` node without `--force`, sets
`status: drafted`, replaces the body, and re-renders the record through `render`. It touches no
other field. `--check <path>` runs the validator alone on a body file, exits non-zero with
each breach named, and is what the measurement arms call.

Check 12, `check_template_conformance`, runs the validator over every node whose status is not
`stub` and fails on any breach. Stubs are exempt because their bodies are scope statements
awaiting replacement. Registering it moves the corpus from eleven checks to twelve, and the
sweep Phase 2 ran from ten to eleven runs again: `CLAUDE.md`, `README.md`, parent spec section 5,
the CI workflow's comment, the hook's message and the tests that count rules.

## 9. Batching and the agent contract

`build_manifest.py` gains `--phase 3`, which excludes drafted nodes, and `--order depth`, which
sorts by `requires` depth then id before slicing. The 1,547 undrafted nodes make 39 batches of
40 with the last of 27, run as three waves of thirteen, recorded in
`.staging/phase-3/manifest.yaml` as explicit ids. `stray_writes` verifies every wave as before.

The brief lives at `notes/phase-3-pages-brief.md`, tracked, because Phase 2's wave 1 brief
lived only in a session and had to be reconstructed. Each agent reads it, the three exemplars
and `objects.yaml` once, then for each node in its batch, in manifest order:

1. reads the record, and every attached article in full where there are any;
2. greps `requires:` across `nodes/` for the node's unlocks;
3. writes the body to a scratch file and calls `write_page.py`, which validates, declares
   `spends` and re-renders the record;
4. records in `.staging/phase-3/report-<NN>.md` what the page was written from, the pairs
   declared, any collision candidate for section 7, and any split candidate where the node
   wanted a third display block or a fourth section.

It never touches a node outside its batch, never sets `reviewed`, never writes
`vault_sources`, and finishes with `check.py`. The model is the one the decision note names,
set explicitly on every dispatch.

## 10. The gate

Per wave, and closing the phase: `check.py` clean at twelve rules; `build_site.py` builds;
`katex_sweep.py`, which already tests node bodies, passes over every drafted node; the grader
runs non-interactively over a stratified sample of five pages per batch, 65 per wave, drawn
by a seeded draw recorded in the gate note, with its reports kept in `.staging/phase-3/`;
and Mario spot-reads one page per batch on the built site, thirteen per wave, for correctness
first and voice second, in the order the parent spec's gate row gives. The report fragments'
collision candidates and split candidates are reviewed at the same sitting.

A small `build_pages_report.py` prints the gate note's numbers: pages per status and per
domain, the display-block and word-count distributions, the "rather than" count, pages whose
closing sentence names no unlock, and the sample draws. It follows `grain_audit.py` in reporting
a measurement rather than gating a commit.

Pull requests run one per wave, with the tools, the brief, the decision note and the measured
ten in a first pull request of their own, so `main` advances and Pages publishes pages as each
wave lands, and a wave's problem holds nothing already merged.

## 11. Failure handling and reproducibility

A stray write is reverted per file and its batch rerun, as in Phase 2. A page that fails check
12 cannot exist, since the tool refuses to write it; a page the grader fails is fixed by hand or
rewritten for that node alone through the tool. A batch whose agent stops early is rerun on its
remaining ids, which the manifest names. Reproducibility rests on the manifest's explicit ids,
the tracked brief, the seeded draws recorded in each gate note and the decision note's token
figures.

## 12. Testing

`tests/test_pages.py` covers the validator rule by rule, pass and fail, the writer's
byte-identical round trip, and each refusal arm. `tests/test_checks_template.py` covers check
12: a stub is exempt, a conforming drafted node passes, a drafted node missing a heading or
carrying three display blocks fails. `tests/test_batches.py` gains the depth ordering and the
drafted exclusion. `tests/test_pages_report.py` covers the statistics. The suite rises from 321
and never falls.

## 13. Out of scope

- No lecture is written; that is Phase 4, and `taught_in` is untouched.
- No vault ingest; that is Phase 2a, and the ledger is untouched except where a report fragment
  finds a claim wrong, which is raised rather than edited.
- No agent sets `reviewed`. The status is Mario's after the gate and after check 6 allows it.
- The three exemplars are not rewritten. `hazard-rate`'s "the previous node named" is left as a
  known reading for the survival braid and logged below.
- No change to `render_node_page`. The Sources section rendering a bare slug is logged below.

## 14. Amendments to the parent spec

Section 10's Phase 3 row reads "To be measured" and takes the decision note's verdict and a
pointer to the note. Section 9's phase table orders 2a before 3; under D3.3 a line records that
Phase 3 wrote uncovered nodes as drafts ahead of 2a, with check 6 the guard. Section 5's "eleven
rules" becomes twelve with rule 12 stated, and `CLAUDE.md`'s "The eleven checks" section and
count follow, along with the README's clone recipe where it counts the rules.

## 15. Order of work

Branch `feat/phase-3-pages` from `main`. The write tool and check 12 with their tests land
first, because both arms of the measurement call the tool and nothing downstream can be
measured without it. Then the manifest ordering, the brief, and the two measurement arms; the
grading and the blind read; the decision note and the ten landed pages; the first pull request.
Then wave one and its gate, waves two and three and theirs, each its own pull request. Tool
implementation runs on Sonnet per `~/.claude/CLAUDE.md`; the two arms run on their own models;
the waves run on the model the note names.

## 16. Backlog this design adds

- **G30:** After each wave, review the collision candidates and grow `objects.yaml`, then sweep
  the new spends onto the affected nodes.
- **G31:** Split the nodes the report fragments name as wanting a third display block, following
  the Phase 1 grain rule.
- **G32:** `render_node_page` prints a vault slug as bare text under Sources. Once pages are read
  it wants the article's title, since the vault is private and the slug leads a public reader
  nowhere.
- **G33:** `hazard-rate` says "the previous node named", which reads correctly only from the
  survival braid, and its closing sentence names "that discrete-time hazard", a node that does
  not exist; none of its six unlocks carries that title. The exemplar breaks the template's own
  forward-reference rule, and the page statistics report lists it. Reword both when the
  exemplars are next touched.
- **G20 closes** through the brief's cap and the tool's refusal.
