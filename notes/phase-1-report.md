# Phase 1 report: the syllabus skeleton

The skeleton stands. `scripts/check.py` reports all nine checks ok against 1,580 nodes and 10
paths with 0 failures, `pytest -q` reports 174 tests passing, and `scripts/build_site.py`
regenerates `site/review.md` and `index.html` cleanly from the committed tree. Twenty published
syllabi and standards anchor the corpus, against the spec's original estimate of 1,100 to 1,400
nodes across 23 bodies: the true body count settled at 20 during Task 1 and Task 8, and the true
node count came out well above the estimate's own ceiling. Three questions remain for this gate:
the grain outliers, the merge report's title disagreements, and the two open scoping decisions
below. None of them blocks the corpus; all three are Mario's to settle rather than the checks'.

Gate 2 is `site/review.md`, read once alongside this report. Run `scripts/build_site.py` first,
since the file is gitignored and generated on the reader's own machine in a few seconds.

## Gates run this session

Every command below ran directly in this session; the figures quoted throughout the report trace
to one of these six runs rather than to memory or to the handover that preceded this task.

- `pytest -q`: **174 passed**.
- `scripts/check.py`: all nine checks `ok`, **1,580 nodes, 10 paths, 0 failures**.
- `scripts/build_site.py`: builds cleanly; regenerates `index.html`, `site/review.md`, ten path
  pages, 1,580 node pages and twelve domain graph SVGs.
- `scripts/katex_sweep.py` over `notation/objects.yaml`, `notation/symbols.md`, every node and
  every lecture: **202 spans across 1,583 files, 0 unsupported**.
- `scripts/grain_audit.py`: a 20-row grain table (three bodies outside the 0.5 to 1.5 band, below),
  prerequisite counts of 463/870/206/25/13/3 nodes at zero to five prerequisites, and **257 titles
  of 1,580 carrying "and" or a comma**. The handover this task inherited quoted 255; 257 is what
  the script prints against the committed tree today, and 257 is the figure this report uses.
- `scripts/fetch_syllabi.py`: **20 bodies, 0 hash mismatches**.

## What the phase produced

- **1,580 nodes** (`ls nodes/*.md | wc -l`), each a reference page with citation-backed
  frontmatter.
- **10 paths** (`ls paths/*.yaml | wc -l`): maths-stats-prerequisites, credit-trunk, life,
  general-insurance, machine-learning, financial-engineering, data-engineering, and the three
  braids (claims-reserving, markov-transition, survival).
- **17 canonical objects** in `notation/objects.yaml`, the corpus's single spelling of every
  symbol a domain otherwise gives its own notation.
- **4 entries** in the gap ledger, `sources/wanted.yaml`: an IFoA CM1 core-reading citation, the
  Renshaw-Verrall 1998 paper behind the chain ladder's GLM equivalence, an IFoA CS2 core-reading
  citation, and the BCBS d424 IRB risk-weight chapter's black-letter text.
- **`site/review.md`**, 2,001 lines (`wc -l`), gitignored and rebuilt by `build_site.py`: 1,580
  nodes, 10 paths, 1,424 prerequisite edges, 405 nodes anchored by more than one body, 2 anchored
  `chosen`. Every one of those head figures is bound by a test in `tests/test_site.py`, after an
  earlier review found seven rendered elements no test constrained.

The 20 anchor bodies: two ASSA papers (F107, F207), thirteen IFoA papers (CB2, CM1, CM2, CP1,
CS1, CS2, SP1, SP2, SP5, SP6, SP7, SP8, SP9), BCBS d424, the IFRS 9 standard, the twelve ETH
`dl-actuarial-2026` lectures transcribed as one body, and two University of Pretoria programmes
(BSc Mathematical Statistics, BCom Financial Analysis and Risk Management).

## What check.py verified, and what it did not

The nine checks cover referential integrity and acyclicity of `requires`, symbol resolution and
uniqueness per domain, path teachability, publishable citations, ledger closure, generated-artefact
currency for `notation/symbols.md`, and every `taught_in` and gap-ledger reference resolving to a
real target. They verify nothing about whether an anchor points at a section that actually exists
in the source, whether grain is consistent from one body to the next, or whether `requires` is
pedagogically ordered rather than merely acyclic. Those three questions were covered by hand and
no further.

Anchor accuracy was spot-checked against source text rather than verified exhaustively: the
coordinator checked anchors for five bodies directly, reviewers checked several more, and the
convention every one of the 21 transcription report files followed was to quote three anchors
verbatim against the source document, with the line number the quote sits on. Reading a sample
of them (bcbs-d424, ifoa-sp6-2026, up-02133413 and its WST re-pass) found the quoted text
matching the source in every case checked.

Grain was measured by Task 10's script and is reported below rather than assumed. Ordering inside
the six domain paths is a topological sort with alphabetical tie-breaking, which guarantees
acyclicity but not pedagogical sequence; only the three braid paths were hand-sequenced against
their own narrative.

## The three grain outliers

| Body | Ratio | Why it sits outside 0.5 to 1.5 |
| --- | ---: | --- |
| `bcbs-d424` | 0.20 | A Basel paragraph is a far finer unit than a syllabus item. Whole runs of paragraphs state one technique (six paragraphs of residential real estate risk weights become one loan-to-value-banded node), and IRB Section H's 147 minimum-requirements paragraphs produced 20 nodes. |
| `ifoa-sp5-2026` | 2.33 | Enumeration grain: SP5's own item structure counts an instrument or product family as one item where the syllabus reads as a list, so more nodes than items result where each instrument earns its own node. |
| `ifoa-sp6-2026` | 1.63 | The same enumeration pattern as SP5, worked against a derivatives syllabus. |

These are findings rather than defects, because the ratio is a structural consequence of how
finely each source document is itself divided, rather than a sign that grain was applied
inconsistently within a body. The transcribers who produced them argued the ratio through
explicitly (bcbs-d424's report walks all seven of its chapters' individual ratios) rather than
folding or splitting nodes to hit the band artificially. A second cause sits underneath the two IFoA outliers specifically:
the denominator itself is inconsistent across the SP series, because SP1 and SP9 counted a bullet
under a numbered item as a separate item where SP5 and SP8 did not. That denominator
inconsistency is carried into the known gaps below, since it means the ratio compares two SP
papers less cleanly than it compares two bodies whose own item-counting agrees.

## Title disagreements, unresolved

Fourteen node ids carry two different titles across the bodies that anchored them; the merge kept
the first body's title in every case, listed here in the order the bodies were merged rather than
by any judgement about which title is correct. Settling them is Mario's job rather than the
checks': a title choice is an editorial call the corpus has no rule for.

| Node | Kept | Also seen |
| --- | --- | --- |
| `age-period-cohort` | Age-period-cohort identification problem | Age period cohort model |
| `arima` | ARIMA | ARIMA process |
| `asset-liability-modelling` | Asset-liability modelling | Asset liability modelling |
| `credit-risk-mitigation` | Other credit risk mitigation techniques | Credit and counterparty risk mitigation |
| `esg-risk` | Environmental, Sustainability and Governance risk | Environmental, sustainability and governance risk |
| `f-distribution` | F distribution | F-distribution |
| `liability-categorisation-for-asset-liability-management` | Liability categorisation for asset liability management | Liability categorisation for asset-liability management |
| `market-consistent-valuation` | Market-consistent valuation | Market consistent valuation |
| `mean-variance-portfolio-theory` | Mean-variance portfolio theory | Mean variance portfolio theory |
| `risk-concentration` | Concentration | Risk concentration |
| `t-distribution` | t-distribution | T-distribution |
| `tail-value-at-risk` | Tail Value at Risk | Tail value at risk (two further bodies) |
| `time-series-forecasting` | Time series forecasting | Time-series forecasting |
| `value-at-risk` | Value at Risk | Value at risk (three further bodies) |

## Orphan nodes: path or deletion

427 nodes sit in no path. No check rejects that state, so it is a judgement rather than a failure,
and the judgement is the same for the great majority of them: every orphan's domain set is
`fin-man`, `regulation`, `eco` or `actuarial` in some combination, and none of the four has a
dedicated domain path in this plan. Read plainly, that means these nodes want a path in Phase 2
rather than deletion, since each one still carries a citation-backed anchor and sits correctly
placed against its prerequisites; the corpus has simply not yet drawn the path that would collect
them. `site/review.md` groups the 427 by domain set, largest first, so a reviewer can dispatch a
block in one judgement:

- `fin-man`: 118
- `fin-man, regulation`: 113
- `eco`: 77
- `actuarial, fin-man`: 22
- `eco, fin-man`: 21
- `regulation`: 20
- `fin-man, stats`: 17
- `actuarial, fin-man, regulation`: 10
- `stats`: 10
- `actuarial, stats`: 5
- `actuarial`: 4
- `actuarial, fin-man, stats`: 4
- `eco, fin-man, regulation`: 2
- `actuarial, eco`: 1
- `actuarial, eco, fin-man`: 1
- `actuarial, fin-man, regulation, stats`: 1
- `actuarial, regulation`: 1

## Nodes anchored `chosen`

Two nodes carry `anchor: [chosen]`: `health-and-care-financial-risk` and
`health-and-care-underwriting-risk`. Both were created when Task 11 split a single fused node into
these two risk groups; no syllabus states the split at this granularity, so the depth is the
corpus's own judgement rather than a syllabus floor. This is the full list, and it is the second
thing gate 2 should read after the headline numbers, because every other node's depth traces to a
named syllabus section.

## Corrections the phase made to its own inputs

The spec and the plan estimated 23 anchor bodies; the true count, settled once every source was in
hand, is 20. Separately, sixteen specifications the coordinator wrote into the plan were wrong and
were caught by implementers, reviewers, or a pre-dispatch check rather than shipping uncaught: four
such checks now exist as a result, verifying that a specification carries no banned construction or
dash, that a stated count matches what the source actually holds, that every verification command
in a brief has been run against a fixture built to fail it, and that every fact a brief states about
a body is read off that body's own manifest rather than assumed. The fifteenth was found inside
Task 14's own brief: its test for every node appearing under its path searched the whole document
rather than each path's own section, so a path truncated to one node still passed while the dropped
node surfaced lower down, in the orphan table. The sixteenth was the plan's README template, which
asserted every trunk node carries a lecture; this task's README edit states the one node that
actually does instead.

## Provenance of the transcription reports

Twenty bodies produced 21 report files (twenty bodies plus one WST re-pass on the University of
Pretoria undergraduate programme). Eleven of the 21, two from Batch A and all nine from Batch B,
were written to disk by the coordinator from the agent's returned text after the harness refused
the agent's own file write. Each of the eleven carries its own provenance header stating this and
naming any clause it rewrote to clear the banned-construction rule; the content is otherwise the
agent's own.

## The Co-Authored-By trailer

The trailer sits on 41 of the 50 commits between `feat/phase-0-machinery` and this branch
(measured directly with `git log`, counting commits whose body carries a `Co-Authored-By:` line).
The handover this task inherited quoted 36 of 45; five further commits landed after that count was
compiled, all carrying the trailer, which accounts for the whole of the difference on both sides.
The nine commits without it are unchanged from the handover's own explanation: they are the Task 1
to Task 5 implementer commits, made before the dispatch briefs named the trailer as a requirement.
`git-conventions.md` is silent on the trailer, so this is an inconsistency for Mario to rule on
rather than a breach of anything written down. A rebase to add it is possible on this unpushed
branch, and the choice is his call rather than this task's.

## What Phase 2 inherits

The gap ledger's four seed entries (above) name what Phase 2 should locate first: the IFoA CM1 and
CS2 core readings, the Renshaw-Verrall paper, and the d424 IRB chapter's black-letter text.

The merge report lists 122 near-miss id pairs, one token apart, that the exact-match reuse check
could not see. Six were merged: `efficient-markets-hypothesis`/`efficient-market-hypothesis`,
`reputational-risk`/`reputation-risk`, `chi-squared-distribution`/`chi-square-distribution`,
`impairment-gain-or-loss`/`ecl-impact-on-financial-statements`,
`capital-allocation`/`risk-based-capital-allocation`, and `chain-ladder`/`chain-ladder-method`.
The remaining 116 were read and left apart as parent-child pairs or coincidences (for example
`cox-proportional-hazards-model` and `proportional-hazards-model`, which the near-miss detector
cannot tell apart from a real duplicate by design); they stand as a human list for Phase 2 to work
through rather than a queue this phase cleared.

On extraction quality: no body's transcription report flagged its own anchors as unreliable, and a
targeted read of the reports found one incident rather than a pattern. `ifoa-sp6-2026`'s report
notes a PDF line-wrap artefact, a lost bullet marker that concatenated two source items into one
line ("Convertibles property derivatives"), caught and split correctly before the node was
written. The transcriber flagged that other SP-paper bodies could hit the same artefact
undetected, and recommended the brief state the resolution directly rather than leaving each body
to rediscover it. No further incident of this kind turned up in the reports read for this task.

## Known gaps, for Phase 2

- `index.html` is a tracked build artefact with no currency check; this task regenerates and
  commits it (below), and check 7 should be extended to cover it.
- `render()` in `staging.py` has no test exercising a non-empty vault field; every staged record's
  is empty today.
- `merge_staging.py` raises after writing when `--report` points outside the repo.
- `grain_audit.py` has no test of its own; a duplicate manifest `body` key overwrites silently, and
  a missing `items_in_document` cannot be told apart from an explicit zero.
- Node title casing is stated nowhere as a rule, and the KaTeX sweep catches only `$`-delimited
  spans.
- The six domain paths carry mechanical (topological, alphabetical-tie) order; pedagogical
  resequencing of roughly 1,300 placements is Phase 2 and Phase 3 work.
- 427 orphans want paths for `fin-man`, `regulation`, `eco` and `actuarial`, or a decision that
  they wait (above).
- The near-miss detector is blind to prefix-style pairs by design: `cox-proportional-hazards-model`
  and `proportional-hazards-model` are correctly apart, but the detector would give the same
  silence to a genuine duplicate pair sharing that shape.

## Abbreviation candidates parked for a decision

The closed list of nine abbreviations a node id may use unexpanded is `glm`, `gam`, `arima`,
`garch`, `gev`, `gpd`, `mcmc`, `pca`, `svd`. Transcribers flagged further candidates rather than
extending the list themselves, per the brief's own rule: `lasso-regularisation`, `cls-token`,
`arma`/`arima` as a pair, `sql`, `sicr`, `ecl`, `eir`, `fvoci`, `fvpl`, `poci`, `otc`, `cds`, `isda`.
`ilaap` already breaches the rule as a committed node id, so the decision is not purely
prospective.

## Two decisions still open

Whether the one committed lecture's HTML stays inlined at 785,013 bytes (roughly 767 KiB) per
revision is still open. That is the measured size of `lectures/S1_credit-survival-bridge.html`
today, unchanged from the figure Phase 0 recorded, since no further lecture has rendered since.

The second scoping axis for the domain graphs is also open, and has moved since it was last
measured. `build_site.py` now writes twelve domain SVGs totalling 2.3 MB (`du -sh site/graphs/`),
against an earlier measurement of one 31 kB graph with 599 edges at 600 nodes. The largest single
file today is `fin-man.svg` at 305,422 bytes, the domain carrying 450 nodes, the most of any of
the twelve. The corpus has grown past the point where one graph per domain is obviously the right
scope, and nothing in this phase decides what the right scope is instead.

## index.html

`build_site.py` rewrites `index.html` at the repo root, and this task ran it and committed the
result: 1,580 nodes across 10 paths, in place of the "3 nodes across 2 paths" the file had read
since Phase 0. No check keeps this file current; check 7 covers `notation/symbols.md` alone.
Extending check 7 to cover `index.html` as well is a Phase 2 item, recorded above under known gaps.
