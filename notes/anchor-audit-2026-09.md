# The anchor audit, and the six anchors it corrected

Written 17 September 2026, on `fix/anchor-defects-and-audit`, after Phase 2's waves reported
four anchor defects and the gate asked for a correction pass.

## What changed

Six nodes carry a corrected anchor. Three come from the waves' reports, three the audit found
on its own, and one wave report does not stand.

| Node | Was | Now | Why |
|---|---|---|---|
| `corporate-exposure-risk-weights` | `sa.para-37` | `sa.para-39` | 37 is section 6, exposures to securities firms. Corporates are section 7, paragraphs 38 to 43, and 39 carries the risk weight determination and Table 10 |
| `downturn-lgd-estimation` | `irb.para-229` | `irb.para-235` | 229 opens subsection (vi), requirements specific to PD estimation. 235 opens (vii), own-LGD estimates, and is the downturn requirement itself |
| `dropout` | `l10` | `l04` | Lecture 10 to 11 cites Srivastava and Wager in its bibliography and nowhere else, in both series. The recast's 04-05 defines dropout in the body as the explicit alternative to early stopping |
| `quasi-complete-separation` | `l02` and `l12` | `l02` | Neither series mentions separation anywhere in lecture 12. The recast's 02 explains the numerical mechanism behind it twice |
| `multiple-external-ratings-treatment` | `sa.para-103` | `sa.para-105` | 103 requires consistent use of chosen ECAIs and forbids cherry-picking. 105 is the two-ratings rule, and 106 the rule for three or more |
| `lgd-foundation-approach-other-collateral` | `irb.para-84` | `irb.para-72` | 84 permits own internal estimates of LGD, which is the advanced approach. 72 defines eligible IRB collateral under the foundation approach: receivables, commercial and residential real estate, and other collateral |

`ead-quantification-standards` keeps `irb.para-241`. The wave reported it as the bare EAD
definition rather than the quantification standards, however 241 opens subsection (viii),
requirements specific to own-EAD estimates, standards for all asset classes. It is the right
entry point and the report does not stand. Every ruling above rests on reading
`vault/markdown/bcbs/bcbs_d424.md` and the lecture sources directly, per
`~/.claude/rules/subagent-verification.md`, rather than on an agent's summary.

## Why there is no twelfth check

A rule that a cited paragraph exists would have caught none of these. d424's paragraph numbers
restart at every section, so "37." occurs four times in the extraction, and 229, 241 and 103 are
all present and all wrong. Existence is not the property that fails. What fails is topic, and
topic is judgement.

Consequently `scripts/anchor_audit.py` reports rather than gates. It scores each anchor by how
much of its node's subject vocabulary appears where the anchor points, prints the weakest first,
and exits zero whatever it finds. A human rules on the top of the list. The corpus keeps eleven
checks and no document needed renumbering.

```
.venv/bin/python scripts/anchor_audit.py --top 40
```

## What it can see, and what it cannot

Of 2,249 anchor references, 238 can be audited: 143 point at d424, which the vault holds as a
full extraction, and 95 at the twelve lectures, which exist in two series, the summer-school
originals in the vault and the credit recast in `actuarial_deep_learning/credit_lectures/`. The
audit reads both and scores against the better, which is how a node anchored correctly against
the recast stops being reported as a defect.

The other 2,011 references cannot be checked at all: ifoa 1,065, assa 483, up 408 and iasb 55,
every one of them naming material in the gap ledger that nobody holds. Re-run the audit as that
material arrives.

**Read the yield with that in mind.** Six corrections have been found in the tenth of the corpus
that can be verified, and none anywhere else, because nowhere else can be looked at. At the rate
the visible tenth shows, 2,249 references would carry something like fifty bad anchors.

## The ranking as it stands, and the rulings on it

Fourteen weakest after the corrections. A low score is a prompt to read the paragraph, not a
verdict: a paragraph naming the board of directors and senior management is corporate governance
whether or not it uses the word.

| Node and anchor | Ruling |
|---|---|
| `irb-corporate-governance-and-oversight` at `irb.para-206` | Sound. 206 requires the board or a designated committee to approve all material aspects of the rating and estimation processes |
| `irb-permanent-partial-use` at `irb.para-49` | Unresolved. The phrase "partial use" occurs nowhere in d424's IRB section, and 49, which permits a bank to stay on slotting for some specialised lending sub-classes while moving others, is the nearest the standard comes. Left in place |
| `partial-and-tranched-credit-protection-treatment` at `sa.para-200` | Sound. 200 assigns the protected portion the protection provider's risk weight and the uncovered portion the counterparty's |
| `collateral-and-guarantee-mismatch-adjustments` at `irb.para-115` | Thin but sound. 115 is one sentence pointing at paragraphs 126 to 130, and the node's other anchor carries the substance |
| `collateral-and-guarantee-mismatch-adjustments` at `sa.para-126` | Sound. 126 defines a maturity mismatch, and 127 onwards give the adjustment |
| `multiple-external-ratings-treatment` at `sa.para-105` | Sound, corrected above. The score stays low because the paragraph says "two ratings" where the node says "multiple" |
| `guarantees-credit-risk-mitigation` at `sa.para-191` | Sound. 191 is the substitution of the guarantor's risk weight |
| `irb-rating-assignment-integrity-requirements` at `irb.para-190` | Sound. 190 requires a rating for each borrower and guarantor as part of loan approval |
| `irb-risk-quantification-general-standards` at `irb.para-214` | Sound. 214 states the broad standards for own estimates of PD, LGD and EAD |
| `public-sector-entity-exposure-risk-weights` at `sa.para-11` | Sound. 11 gives the two national-discretion options and the PSE risk weight table |
| `internal-ratings-based-approach` at `irb.para-1` | Sound. 1 opens the section and describes the approach |
| `loss-given-default` at `irb.para-69` | Sound. 69 requires an LGD estimate for each corporate and bank exposure |
| `irb-roll-out-requirements` at `irb.para-44` | Unruled |
| `pillar-1-minimum-capital-requirements` at `floor.para-2` | Unruled |

One further anchor outside the top fourteen is worth a look on the next pass:
`comprehensive-approach-collateral-haircut-method` points at `irb.para-72`, which the correction
above establishes is the foundation approach's eligible IRB collateral rather than the
comprehensive approach's haircut method.

## Two bugs the audit had first

Both were caught by reading its output against the primary text rather than by trusting it, which
is the working method this note recommends to whoever reads the ranking next.

The section map first resolved a paragraph number to the longest match in the section. The
leverage ratio section carries an annex whose paragraphs restart at one, so `lr.para-13` resolved
to the annex's trade letters of credit rather than to the implementation timeline, and a sound
anchor was reported as the corpus's worst. It now takes the first match that reads as prose,
which also skips the numbered headings that share the paragraph shape.

Term matching was whole-word, so a node called `backpropagation` could not see "back-propagation"
and `discriminatory-power` could not see "discrimination". Terms of eight letters or more now
match on their first eight, and every term is counted twice, once against the text as written and
once with the hyphens closed up.
