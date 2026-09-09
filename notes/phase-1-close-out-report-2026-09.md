# Phase 1 close-out report

Phase 1 closes here. The ten tasks that followed `notes/gate-2-decisions-2026-09-08.md` have
applied all thirteen gate 2 decisions to the corpus, and this note measures what they produced.
Three decisions, D8, D11 and D13, were applied by leaving the corpus unchanged, exactly as the
decisions note specified. `1d1fabb` added the mechanical path sequencer that D1 and D9 both
read, and `41c57e7` and `87741f3` record the plan and note amendments that carry the rulings
below. The table gives the option each decision took, the commit that carried it, and its
measured effect on the tree at `72844b6`.

## The thirteen decisions

| Id | Option | Commit | Measured effect |
|---|---|---|---|
| D1 | a | `636b3c9`, `72844b6` | Trunk of 273 nodes sequenced by hand across eight stages, recorded in `notes/credit-trunk-sequence-2026-09.md`. |
| D2 | a | `5febe7b` | Three path files drawn: enterprise-risk-and-regulation with 152 nodes, banking-and-financial-management with 161, economics with 99. |
| D3 | a | `c258f62` | Ninety records and ninety-six anchors renamed from `eth.dl-actuarial-2026` to `ucsc.dl-actuarial-2026`, with the manifest, brief, `CLAUDE.md`, `README`, spec and plan updated to match. |
| D4 | a | `74a9c29`, `b26c402` | Titles set to sentence case, with check 10 added and enforced against the `PROPER_NAMES` list. |
| D5 | b, read as the proposals | `74a9c29` | Seven retitles applied (T3, T4, T6, T7, T8, T12, T14); T1 followed D9's naming; T2, T5, T9, T10, T11 and T13 kept their titles. |
| D6 | c | `3950b2f` | Forty-token abbreviation list ratified in the brief: the thirty tokens of option (a) plus `pd`. |
| D7 | b, read as the sixteen merges, plus the rulings | `26c21d2`, `14471de` | Twenty-two merges were proposed. N75's `linear-model` was withdrawn during execution, so twenty-one merged into their survivors; N106 stays apart and gains an edge. |
| D8 | c | no change | Corpus left unchanged: the three ratios stand and the brief's band stays at 0.5 to 1.5. |
| D9 | b | `84ceae1` | `age-period-cohort` split. The identification problem keeps the id, the stats domain and the l01 anchor. A new `age-period-cohort-mortality-model` takes CS2's two anchors, the life domain and the mortality-projection edge, and requires the first. The claims-reserving braid drops `mortality-projection-approaches`. |
| D10 | b | `5dad988` | Twelve domain graphs kept, redrawn to include only the nodes with an edge inside their own domain. The three largest domains are detailed below. |
| D11 | b | no change | Corpus left unchanged: the nineteen four- and five-domain unions stand as reviewed. |
| D12 | a | `5febe7b` | Two banking records gain the fin-man domain and join the banking path; `stochastic-modelling-for-risk` gains `requires: [probability-distribution]`. |
| D13 | a | no change | Corpus left unchanged: the KaTeX split stays deferred until a second lecture renders. |

## Rulings during execution

Four rulings arose during execution and are recorded here for Mario to confirm or reverse.

N75's `linear-model` was kept apart, against the sixteen-plus-six merge list. Merging it into
`linear-regression` would have closed a cycle through `least-squares-estimation`, because
`linear-model` (anchor `up.wst311.6`) is the full-rank general linear model taught after
least-squares estimation, distinct from `linear-regression-model`, which still merged as N76.
Twenty-one merges went ahead instead of twenty-two, so 1,580 nodes less twenty-one plus the one
D9 split gives 1,560.

The merges exposed two prerequisites that no path had claimed. `risk-measurement` was pulled
into the general-insurance path and `credit-risk` into the life path, so both now settle inside
a path instead of standing as loose prerequisites.

The decisions note projected seventeen nodes left in no path after D12's placements. The
measured figure is sixteen, because the enterprise-risk-and-regulation path pulled in
`model-fitting` as a prerequisite of one of its own members, settling that node as well.

In the trunk, `credit-risk-model-validation` now opens Stage 5, and
`irb-risk-quantification-general-standards` follows its prerequisite
`internal-rating-system-regulatory-requirements`; both moved at review.

## Measurements

Measured with the brief's snippet against `scripts/check.py`, which reports all ten checks
`ok` and 208 tests passing under `pytest -q`.

| Metric | 8 September baseline | 72844b6 |
|---|---|---|
| Nodes | 1,580 | 1,560 |
| Paths | 10 | 13 |
| Edges | 1,424 | 1,418 |
| In no path | 427 | 16 |
| No edge | 257 | 250 |
| Neither | 109 | 0 |

## The domain graphs

Task 9's domain graphs follow the same rule throughout: draw only the nodes with an edge inside
their own domain. The three largest domains show the effect. Fin-man holds 450 members and now
draws 302. Stats holds 373 members and draws 298. Regulation holds 327 members and draws 270.

## What Phase 2 Attach inherits

Sixteen stats and actuarial nodes remain in no path: `archimedean-copula`,
`bayes-versus-empirical-bayes-credibility`, `bayesian-credibility-theory`,
`best-subset-selection`, `credibility-premium`, `deferred-annuity-certain`,
`empirical-bayes-credibility-theory`, `extreme-value-theory`, `gaussian-copula`,
`grouped-binomial-regression`, `increasing-annuity-certain`, `murphy-decomposition`,
`poisson-regression`, `quasi-complete-separation`, `stochastic-modelling-for-risk` and
`tail-dependence`. Every one of them already carries at least one edge, so placing each in a
path is Phase 2 Attach's job alone.

Phase 2 Attach also inherits the gate 2 backlog items this plan did not take:

- G1: Anchor-prefix registration check.
- G2: Extend check 7 to `index.html`.
- G3: Fix the six cadence-debt comments now on main.
- G4: Tests for `grain_audit.py`.
- G6: Post-union requires-length check.
- G7: Manifest local paths.
- G8: `render()` test with a non-empty vault field.
- G9: `merge_staging.py --report` outside the repo.
- G10: KaTeX sweep beyond dollar delimiters.
- G11: Near-miss detector and prefix pairs.
- G12: Thousands separator on `index.html`.
- G13: Acquire the four ledger sources.
- G17: Amend the transcription brief.
- G18: Spot-read the nineteen wide-domain nodes.
- G19: Spot-read `risk-management-process`.
- G20: Phase 3 style note on the overused connective flagged in the original 1,580 stub bodies (finding F8).
- G21: Retitle `cost-of-capital-banking`.
- G22: Resequence the five other domain paths.
- G23: Phrase-level proper-name list for check 10, once a title capitalises a listed word outside a defined term.
- G24: Vary the cadence of the three new path preambles, which all open on a noun phrase and a colon.
