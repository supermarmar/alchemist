# Gate 2 decisions, 8 September 2026

The reply against `notes/gate-2-review-2026-09-06.html`, received 8 September 2026, reads
`D1 b D2 a D3 a D4 a D5 b D6 c D7 b D8 c D9 b D10 b D11 b D12 a D13 a`. A follow-up the same
day ruled on the seven open near-miss pairs, moved D1 to (a), and confirmed the narrow D12
scope. Ten of the thirteen now take the recommended option. D8, D10, and D11 depart from it.

Two ids carried a reading. D5 and D7 have no lettered options on the review page, which asks
for per-row replies (T1 to T14, N1 to N122). The interactive corpus map of 8 September listed
their positions in order, so `b` was read as the second position on each: D5 applies the four
substantive proposals and D7 merges the sixteen proposed merges. Neither reading was
corrected in the follow-up, so both stand.

## The thirteen decisions

| Id | Option | Decision | Against the recommendation |
|---|---|---|---|
| D1 | a | Hand-sequence the credit trunk in Phase 2, 277 placements, before Phase 3 writes a page. The other five domain paths, the foundation path, and the three D2 paths stay in tier-then-alphabetical order until their pages exist. | Recommended. (b) was chosen first and reversed the same day. |
| D2 | a | Three Phase 2 path files: banking and financial management, economics, and enterprise risk and regulation. | Recommended. |
| D3 | a | Rename `eth.dl-actuarial-2026` to `ucsc.dl-actuarial-2026` now, with a scripted sweep over nodes, brief, `CLAUDE.md`, spec, plan, and `sources/syllabi.yaml`. | Recommended. |
| D4 | a | Sentence case throughout, with capitals only for proper names and for a body's defined term where the term is the node. | Recommended. |
| D5 | b, read as the proposals | T1 follows D9. T2 keeps ARIMA. T3 retitles `credit-risk-mitigation` to Credit risk mitigation. T4 retitles `risk-concentration` to Risk concentration. T5 to T14 follow the D4 rule. | Recommended. |
| D6 | c | Ratify the list as the corpus stands, adding the thirty tokens of (a) and `pd`, forty tokens in all. Every committed id stands. | Departs from (a) by `pd` only. |
| D7 | b, read as the sixteen merges, plus the rulings | Merge N14, N31, N40, N53, N58, N64, N75, N76, N79, N98, N101, N107, N111, N114, N118, and N120 into the survivors the review page names. Of the seven open pairs, N18 stays apart and N42, N73, N82, N88, N109, and N110 merge; the survivors are in the table below. Twenty-two files go in all. N33, N52, N90, and N113 stay apart. N106 stays apart and gains the edge. | Recommended. |
| D8 | c | Accept the three ratios and leave the brief's band at 0.5 to 1.5. | Yes. (a) was a band per source type. |
| D9 | b | Split `age-period-cohort`. The identification problem keeps the id, stats, and the l01 anchor. A new `age-period-cohort-mortality-model` takes CS2's two anchors, life, and the mortality-projection edge, and requires the first. | Recommended. |
| D10 | b | Keep the twelve domain graphs, drawn only for nodes with at least one edge inside the domain. | Yes. (a) was one graph per path. |
| D11 | b | Accept the nineteen four- and five-domain unions as they stand. | Yes. (a) was a spot-read and trim. |
| D12 | a | D2's paths collect the pathless isolates. The three nodes left with no edge and no path get at least one edge or a written reason; they are named below. A node with no edge that sits inside a path is an ordinary root or leaf and needs nothing. | Recommended. |
| D13 | a | Defer the KaTeX split until a second lecture renders. | Recommended. |

## The six ruled merges

The reply said `merge` without naming a survivor, so the shorter id survives in each pair and
the general concept absorbs its qualified variant. That is the pattern the review page's own
proposals follow in N14, N58, N111, and N118, and it stands unless overridden.

| Row | Absorbed | Survivor | Repointing | Note |
|---|---|---|---|---|
| N42 | `credit-scoring-model` | `credit-scoring` | 0 requires, 1 path line | The survivor is titled Credit scoring and bureau data, which names only F207's half; retitle to Credit scoring on merge. |
| N73 | `level-annuity-certain` | `level-annuity` | 4 requires, 2 path lines | |
| N82 | `markov-jump-process` | `markov-process` | 4 requires, 2 path lines | The markov-transition-braid carries the absorbed id; its line repoints. |
| N88 | `named-probability-distribution` | `probability-distribution` | 8 requires, 1 path line | |
| N109 | `risk-identification-techniques` | `risk-identification` | 1 requires, 2 path lines | |
| N110 | `risk-measurement-methods` | `risk-measurement` | 2 requires, 0 path lines | |

## The three nodes D12 reaches

After D2 collects 106 of the 109 nodes that touch nothing, three remain with no edge and no
path: `actuarial-professionalism-in-banking` (actuarial, four F207 anchors),
`actuarial-techniques-in-banking` (actuarial, one F107 anchor), and
`stochastic-modelling-for-risk` (actuarial and stats, one CP1 anchor). The first two are
banking material carrying only the actuarial domain, so adding fin-man to their domains puts
them in the banking path and settles them without an edge; the third wants an edge or a
sentence saying why it has none.

## What the configuration measures to

Measured on the tree at `origin/main` on 8 September 2026. The node count becomes 1,559: 1,580
less the twenty-two merged, plus the one split. Paths become thirteen. Nineteen nodes remain in
no path today, and D12 resolves three of them; the other sixteen are stats and actuarial
material that no path claims. The twelve graphs stay, with the largest falling from 450 drawn
nodes to 301. Placements made by hand come to 277. Node files rewritten come to at least 125:
ninety anchor rewrites, twenty-two merges, two for the split, seven casing retitles, and four T
retitles.

## Order for the Phase 2 plan

Mechanical sweeps come first, because every later step reads the ids and titles they settle:
the D3 rename, the D6 list into the brief, the D7 merges with the N106 edge, the D9 split, the
D4 rule into the brief and `CLAUDE.md` with the G5 title check behind it, and the D4 and D5
retitles. Structure follows: the three D2 path files with preambles and `builds_on`, the D10
(b) change to `site.py` with its tests, and the three D12 nodes. D1 (a) sequencing of the trunk
comes last, over the final node set, so no placement is made twice. `check.py` runs after every
step, and the never-renamed rule is untouched under D6 (c).
