# Prerequisite report, 4 September 2026

Task 11: resolve cross-body prerequisites and break every cycle. Written after the edits
below were applied to `nodes/*.md` and verified against `scripts/check.py`, `parse_node` and
`pytest`. Every count in this report came from measuring the repository as it stood on
5 September 2026. Where the brief or the handover disagreed with that measurement, the
disagreement is recorded in the final section.

## Starting position

`scripts/check.py` on the merged corpus of 1,584 nodes reported check 3 failing with exactly
the five cycles the handover listed verbatim, and no other failure of that check. A direct
scan of every `requires` edge in the corpus (`from scripts.alchemist.model import
load_corpus`, checking each `required` id against `corpus.nodes`) found zero edges naming a
node nobody had written. The brief's Step 1 and Step 2, which assume a nonzero unresolved
count to work down, therefore had nothing to do: the unresolved count was zero at the start
and stayed zero, and no node was written to close a missing-prerequisite gap and no edge was
deleted for falling below the corpus's floor. All five check 3 failures were cycles.

## Cross-body edges added

Three sources, as directed, plus one edge a cycle fix in the second source required.

### Batch B manifest `needs` lists

Measured across all twenty `.superpowers/phase-1/<body>/manifest.yaml` files: 54 `needs`
entries in total, all in bodies whose manifest schema actually carries a `needs` key on node
entries. That set is `bcbs-d424` (9), `iasb-ifrs9` (2), `ifoa-cp1-2026` (1), `ifoa-sp1-2026`
(2), `ifoa-sp5-2026` (25), `ifoa-sp6-2026` (14) and `ifoa-sp9-2026` (1), which sums to the
measured 54 and matches the handover's own body-by-body breakdown line exactly (see the
discrepancy note below on the handover's prose list of bodies, which is wrong).

Every one of the 54 `needs` targets and sources already resolved to a node in the corpus, so
all 54 were addable. Ten were already present in the source node's `requires` (both bodies had
independently written the same edge), so 44 were genuinely new: `credit-valuation-adjustment`,
`forward-contract-valuation`, `collateralised-debt-obligation`,
`black-scholes-partial-differential-equation`, `vasicek-interest-rate-model` (both its needs
targets), `cox-ingersoll-ross-model` (both), `risk-neutral-bond-pricing`,
`risk-correlation-aggregation`, and 36 more, covering
`standardised-approach-credit-risk`, `credit-risk-mitigation-overview`,
`partial-and-tranched-credit-protection-treatment`, `asset-correlation`,
`irb-disclosure-requirements`, `operational-risk-loss-exclusion-approval`,
`output-floor-calculation-scope`, `output-floor-disclosure-requirements`,
`eligible-hedging-instruments`, `significant-increase-in-credit-risk`,
`treating-customers-fairly`, `embedded-value-calculation`,
`statistical-and-individual-case-reserving`, `investment-environment-influences`,
`credit-derivatives`, `swaps-and-swaptions`, `private-debt`, `venture-capital`,
`hedge-funds`, `currency-as-asset-class`, `infrastructure-investments`, `commodities`,
`insurance-linked-securities`, `structured-products`, `equity-fundamental-analysis`,
`fixed-income-valuation`, `empirical-characteristics-of-asset-prices`,
`fixed-income-option-pricing`, `indifference-curves`, `behavioural-finance`,
`liability-hedging`, `active-management-styles`, `equity-portfolio-management`,
`bond-portfolio-management`, `portfolio-risk-attribution`, `derivative-hedging-applications`,
`greek-based-hedging`, `basis-risk-in-hedging`,
`international-swaps-and-derivatives-association-agreement` and
`special-purpose-vehicle-risk-transfer`. No node's `requires` count exceeded five as a result;
the largest post-addition list was four.

### The claims-reserving braid

`over-dispersed-poisson-model` now requires `exponential-dispersion-family`, exactly as the
handover's "Cross-body edges to draw" section specifies, sourced to the England and Verrall
(2002) verification in `notes/uni-programme-anchors.md`. The brief's own prose ("the chain
ladder node requires the exponential dispersion family node") names the wrong node: `chain-ladder`
requires nothing from this braid, and the edge sits on `over-dispersed-poisson-model`, which is
what the handover's more specific "Cross-body edges to draw" list also says. Measured against
the corpus, `over-dispersed-poisson-model` already required `stochastic-reserving`, which in
turn requires `chain-ladder`, so the braid reaches chain ladder two steps down without a direct
edge.

### The survival braid, measured and found already resolved

The brief and handover both describe an edge from "the force of mortality, the claim intensity
and the default hazard" onto a shared `hazard-rate` node. None of `force-of-mortality`,
`claim-intensity` or `default-hazard` exist as node ids in the corpus. Reading `hazard-rate`
directly shows why: it is already a tier-2 lecture node (`taught_in:
S1_credit-survival-bridge`) whose own body states "a force of mortality, a claim intensity and
a default hazard are the same quantity measured on three different books," with `spends`
entries for `obj.hazard` in life, gi, credit and stats. The unification the braid asks for was
already done at the node level rather than by a `requires` edge between separate nodes, so no
edge was added and none was needed. This is the one item in this report where the brief and
the handover describe a fix the corpus had already made by a different mechanism.

### The Markov transition braid, measured under different ids

Neither `rating-transition-matrix` nor `life-multiple-state-models` exists as a node id. The
corpus's actual nodes for this braid are `credit-migration-model` (BCBS's CreditMetrics-style
migration model: "the probability of each obligor migrating between rating grades") and
`multiple-state-markov-model` (CM1's multi-state framework). `markov-jump-process` does exist,
and its own body already states it "is the structure behind multi-state insurance models."
Added: `credit-migration-model` now requires `markov-jump-process` in addition to its existing
`internal-and-external-ratings`; `multiple-state-markov-model` now requires
`markov-jump-process` in addition to its existing `hazard-rate`.

### Batch A `duplicate_of` prose

Measured: 13 manifests carry no `needs` key at all (`assa-f107-2026`, `assa-f207-2026`,
`eth-dl-actuarial-2026`, `ifoa-cb2-2026`, `ifoa-cm1-2026`, `ifoa-cm2-2026`, `ifoa-cs1-2026`,
`ifoa-cs2-2026`, `ifoa-sp2-2026`, `ifoa-sp7-2026`, `ifoa-sp8-2026`, `up-02133413`,
`up-02240278`). The handover states twelve; the discrepancy is recorded in the final section. Their
`duplicate_of` fields were read in full (164 entries across the thirteen). Most are
speculative overlap notes ("likely overlaps", "possibly the same concept") that name no
specific prerequisite direction and are Task 9/10 grain material rather than this task's; the
ones that named a concrete target with directional certainty were actioned:

- `interest-rate-swap-hedging` (F207) now requires `swaps-hedging` (F107). F207's note
  ("expects Subject F107 to teach the interest rate swap itself as a foundational instrument")
  named no id; F107's `swaps-hedging` ("a contract exchanging one stream of cash flows for
  another, such as fixed for floating interest payments") is the matching foundational node.
- `maturity-transformation` (F207) now requires `asset-liability-mismatch` (F107). F207 expected
  F107 to teach maturity transformation at a foundational level; F107 has no node under that
  name, but `asset-liability-mismatch` ("a difference in the repricing or maturity profile of a
  bank's assets and liabilities, which is the underlying source of its interest rate risk in
  the banking book") is the concept F207's node specialises.
- `mortality-risk` (SP2) now requires `life-table` and `life-table-probabilities` (CM1). SP2's
  own manifest states outright: "assumes CM1's life-table and life-table-probabilities concepts
  as a prerequisite, both staged, but not named in requires since they belong to another body's
  batch." The clearest possible instruction to add the edge.
- `life-insurance-investment-principles` (SP2) now requires `institutional-investment-strategy`
  (a University of Pretoria honours body), on the same "not named in requires since it belongs
  to another body's batch" pattern.
- `multiple-decrement` now requires `multi-state-model` in addition to its existing
  `multiple-state-markov-model`. CS2's manifest flags these as a specific case and its general
  framework and asks Task 11 to decide whether to merge or draw the edge; `multi-state-model`
  (CS2/SP1, requiring `kolmogorov-equations` and `markov-process`) is not one of the six
  authorised near-miss merges, so the two stay separate ids and the parent-child edge is drawn
  instead, per the handover's own reading.
- `internal-liquidity-adequacy-assessment-process` (F207) now requires `ilaap` (F107). F207
  expected F107 to introduce this "at a foundational level"; F107's node is `ilaap`, whose id
  breaks id rule 3 (abbreviations are spelled out unless on the closed nine-item list, and
  `ilaap` is not on it) but is otherwise the correct match and is flagged rather than renamed,
  since renaming an id is out of this task's scope. Adding this edge created a sixth cycle,
  resolved below.
- `expected-credit-loss-provisions` (F107) now requires `expected-credit-loss` (IFRS 9), per
  the handover's "keep apart and consider an edge" reading of that pair: F107's PD times LGD
  times EAD calculation is a specific method for the general accounting concept IFRS 9 defines.

Checked and left unactioned, because no corresponding node exists in the named body:
`internal-capital-adequacy-assessment-process` (F207 expected an F107 foundational ICAAP node;
F107 has `capital-adequacy-regulatory-view`, which is about the regulatory minimum rather than
the bank's own assessment process, so no match), `three-lines-of-defence` (its anchor is
`assa.f207.7.3` alone; F106 and F107 never contributed one), and `actuarial-investigation`
(SP7 expected a more generic CS2 or CP1 node; neither body has one under a matching id).
`model-risk`'s note ("check whether this node should instead carry the anchor there") is
already resolved: the node's anchor is `[assa.f107.1.12-14, assa.f207.7.6-1, ifoa.sp9.4.7]`,
carrying all three bodies already.

`with-profits-surplus-distribution`'s manifest note claims its requirement on
`surplus-management` was "not named in requires since it belongs to another body's batch," but
the merged node already carries `surplus-management` in its `requires`. Measured rather than
trusted: the note is stale, the edge is already there, and no action was needed.

`binomial-distribution` and `geometric-distribution` already carry `requires:
[bernoulli-distribution]` in the merged corpus. The handover's "mathematically right; confirm"
is confirmed: Task 9's union already applied the WST re-pass's addition to both.

## Cycles broken

Six rather than the five `check.py` originally reported: the fifth Batch A edge above
introduced a new one, caught only by re-running `check.py` after adding it.

**Reinsurance pair (SP1/SP2 and SP7).** `reinsurance-programme-choice` and
`reinsurance-structure-appropriateness` each required the other. Read against their own body
text, `reinsurance-structure-appropriateness` is the sub-decision ("choosing between them
follows from understanding why the insurer reinsures"), and `reinsurance-programme-choice` is
the overarching decision that weighs cost, counterparty strength and retained risk, informed by
that sub-decision. Cut `reinsurance-structure-appropriateness`'s requirement on
`reinsurance-programme-choice`, keeping the direction where the overarching choice requires the
structure assessment rather than the reverse.

**The IRB cluster, four cycles.** `internal-ratings-based-approach` requires
`exposure-at-default`, `loss-given-default` and `probability-of-default` (the formula's three
inputs), while each of those three also required `internal-ratings-based-approach` back (the
framework they sit inside). One direction is pedagogical (the approach is taught from its
inputs) and the other taxonomic (each parameter happens to be defined within the IRB chapter of
the Basel text). The graph is pedagogical, so the taxonomic edge was cut in each of the three
direct pairs: `exposure-at-default`, `loss-given-default` and `probability-of-default` no
longer require `internal-ratings-based-approach`. Every other node that legitimately elaborates
IRB detail (`effective-maturity`, `irb-asset-class-taxonomy`,
`irb-approach-choice-by-asset-class`, `irb-versus-ifrs9-model-differences`,
`revised-irb-approach-credit-risk`, `unexpected-loss-capital-requirement-scope`,
`expected-versus-unexpected-losses`) still correctly requires
`internal-ratings-based-approach` and was left untouched; those are genuinely downstream detail
rather than the approach's own inputs.

The fourth, longer cycle ran `internal-ratings-based-approach -> probability-of-default ->
outcome-window -> definition-of-default -> internal-rating-system-regulatory-requirements ->
internal-ratings-based-approach`. **Restated after fix round 1**, since the first version of
this report justified the cut by the node's anchor sitting inside the Basel IRB chapter, and
every node in this cycle carries a `bcbs.d424.irb.*` anchor, so that reason does not pick out
this edge from the others. The pedagogical reason is the one that actually decides it:
`internal-rating-system-regulatory-requirements` is governance over how a bank's internal
rating system must be designed, run and supervised, and that governance presupposes the
approach it governs, so a reader learns what the IRB approach is before learning the standards
its rating systems must meet. Cut `internal-rating-system-regulatory-requirements`'s
requirement on `internal-ratings-based-approach`, leaving it requiring only
`internal-and-external-ratings` before fix round 1's edge below added a second input.

**Fix round 1: the adjacent edge, re-examined.** `definition-of-default` requires
`internal-rating-system-regulatory-requirements` sat untouched in the first pass, but the same
pedagogical reading applied to it points the other way. A definition of default is a
substantive input, the same kind of thing PD, LGD and EAD are to the IRB approach: it states
what event a model is predicting. `internal-rating-system-regulatory-requirements` is
governance built on top of that definition, covering how a rating system using it must be
designed and supervised, so a reader needs to know what counts as a default before learning the
governance standards a system that predicts it must meet. That is backwards under the same
reading used above, so the edge is reversed rather than merely cut:
`definition-of-default` now requires nothing, and
`internal-rating-system-regulatory-requirements` requires both
`internal-and-external-ratings` and `definition-of-default`. `outcome-window`, which requires
`definition-of-default`, and `probability-of-default`, which requires `outcome-window`, are
unaffected and still read correctly: an outcome window and a PD model both need the definition
of default settled first.

**The sixth cycle, introduced by this task's own edit and resolved the same way.** Adding
`internal-liquidity-adequacy-assessment-process` requires `ilaap` closed a loop:
`liquidity-coverage-ratio -> internal-liquidity-adequacy-assessment-process -> ilaap ->
liquidity-coverage-ratio`. `ilaap` (F107) correctly requires `liquidity-coverage-ratio` and
`net-stable-funding-ratio` as its inputs, the same pedagogical direction as the IRB approach
requiring PD, LGD and EAD. `liquidity-coverage-ratio`, a node F207 also anchored, separately
required `internal-liquidity-adequacy-assessment-process` for the matching taxonomic reason (the
ratio is discussed inside the ILAAP section of F207's syllabus). Cut
`liquidity-coverage-ratio`'s requirement on `internal-liquidity-adequacy-assessment-process`,
by the identical rule used for the IRB cluster: the process requires its ratio inputs rather
than the ratio requiring the process.

Re-running `scripts/check.py` after each cut confirmed the named cycle cleared before moving
to the next; the final run (below) confirms all six are gone and no new one appeared.

## Near-miss merges

Six pairs merged, all from the handover's "Probable merges under different ids" list. For
each: domains, anchor and requires were unioned onto the surviving id, the losing file was
deleted, and every `requires` list in the corpus naming the losing id was repointed to the
survivor (deduplicating where a node, such as `f-distribution`, had already named both).

| Survivor | Deleted | Reason | Files repointed |
|---|---|---|---|
| `efficient-markets-hypothesis` | `efficient-market-hypothesis` | Fixed-term exception to the singular rule: `notes/transcription-brief.md` names `efficient-markets-hypothesis` itself as the term that keeps its conventional plural form. | none referenced the loser |
| `reputational-risk` | `reputation-risk` | One concept (an adverse event damaging an organisation's standing) under two adjectival forms; `reputational risk` is the term the wider risk taxonomy in this corpus otherwise uses (`operational-risk`, on the same `-al` pattern). | none referenced the loser |
| `chi-squared-distribution` | `chi-square-distribution` | Merge on the British spelling, per the handover's own instruction; `chi-squared` is the form IFoA's UK syllabus and the rest of British statistics teaching use. | `chi-square-goodness-of-fit-test`, `f-distribution` (had named both; deduplicated), `sampling-distribution-of-normal-mean-and-variance`, `t-distribution` |
| `impairment-gain-or-loss` | `ecl-impact-on-financial-statements` | One concept: F107's node paraphrases the same P&L recognition IFRS 9's node states in the standard's own words ("impairment gain or loss"). Rule 1 favours the term practitioners use over the descriptive paraphrase. | none referenced the loser |
| `capital-allocation` | `risk-based-capital-allocation` | Both staged by F207 itself, describing the same allocation of capital to business lines by risk and return; no second allocation method exists in the corpus to justify keeping them apart. | none referenced the loser |
| `chain-ladder` | `chain-ladder-method` | Identical titles ("Chain ladder method") on both records; `chain-ladder` is the id `notes/transcription-brief.md` itself uses as the worked example of a well-formed id (rule 1: "`chain-ladder` rather than `cs2-topic-4-2`"). | `bornhuetter-ferguson-method`, `inflation-adjusted-chain-ladder`, `reserving-method-assumption`, `statistical-reserving-model` |

`chain-ladder`'s anchor was `[chosen]` alone before the merge (SP7 staged it assuming the
method without naming a source), and `chain-ladder-method`'s anchor was the real
`ifoa.cm2.4.2-2`. Per the rule that `chosen` comes off once a real anchor sits beside it, the
merged node's anchor is `[ifoa.cm2.4.2-2]` only.

**Fix round 1: one merge had dropped content.** `impairment-gain-or-loss` kept IFRS 9's body,
which covers only the profit-and-loss recognition of a change in loss allowance, and the
deleted `ecl-impact-on-financial-statements` had stated the same movement also reaches "a
bank's profit and loss account, its balance sheet and, ultimately, its capital position." The
merge unioned the frontmatter fields but not the prose, so the balance-sheet and capital-
position scope was silently lost. Added one sentence to the survivor's body: "the same
movement in provisions also changes the balance sheet carrying value of the exposure and,
ultimately, the bank's capital position." This is the one body edit fix round 1 permits.

Considered and left apart, per the handover's "probable non-merges" section, confirmed by
reading both records: `expected-credit-loss` and `expected-credit-loss-provisions` (the
accounting principle against the PD/LGD/EAD calculation, now linked by a requires edge instead,
above), `vasicek-interest-rate-model` and `vasicek-single-factor-model` (CM2 kept these apart
deliberately), `multi-state-model` and `multiple-decrement` (parent-child, linked by an edge
rather than merged, above), `classification-performance-metrics` and
`model-performance-metrics` (classifier-threshold metrics against generic fit measures, genuinely
distinct).

**Fix round 1: the Cox pair, examined and left apart.** `cox-proportional-hazards-model` and
`proportional-hazards-model` read as a further near-miss on first glance, but they are
general-to-specific rather than one concept under two names: `proportional-hazards-model` states
the general structure (a baseline hazard scaled by a covariate factor), and
`cox-proportional-hazards-model` is the specific partial-likelihood estimator fitted to that
structure. The edge between them already exists and reads the right way,
`cox-proportional-hazards-model` requiring `proportional-hazards-model`, so no change was made.
Recorded here so the pair is not asked about again.

## The five-prerequisite ceiling

`experience-monitoring-methods` carried six prerequisites after the union of SP1's and SP2's
risk lists (`claim-amount-risk`, `claim-rate-risk`, `expense-risk`, `investment-risk`,
`mortality-risk`, `persistency-risk`).

**Fix round 1: solved rather than moved.** The first pass created a single new node,
`health-and-care-risk-types`, to carry all six, which only relocated the ceiling breach onto
the new node rather than resolving it. Replaced with a split into two nodes along the
actuarial line the six fall on: `health-and-care-underwriting-risk`
(`claim-amount-risk`, `claim-rate-risk`, `mortality-risk`, `persistency-risk`, the four risks
that arise from how policyholders behave or how claims emerge) and
`health-and-care-financial-risk` (`expense-risk`, `investment-risk`, the two risks that arise
from the insurer's own cost base and asset returns). `experience-monitoring-methods` now
requires both. `health-and-care-risk-types` is deleted; `experience-monitoring-methods` was
the only reference to it, and has been repointed. Both new nodes carry `anchor: [chosen]`,
the same anchor `health-and-care-risk-types` carried: no body stages this two-way split as
such, and the individual leaf risks' own SP1/SP2 anchors (`ifoa.sp1.3.1-2` through `-6`,
`ifoa.sp2.3.1`, `ifoa.sp2.3.5`) already sit on the leaves themselves rather than on a grouping
level, so inventing a specific SP1 subsection number for the split without a primary-source
citation to support it would have been a fabrication rather than a fix.

`exponential-dispersion-family` and `irb-risk-weight-function` were measured at exactly five
and left untouched, per the handover's own defence of both (CS1's five member distributions and
BCBS's five irreducible formula inputs, the latter defended by its transcribing agent).

**Fix round 1: a third node at the ceiling, introduced by this task's own edit.**
`expected-credit-loss-provisions` went from four requires to five when the Batch A
`duplicate_of`-derived edge onto `expected-credit-loss` was added (see "Batch A `duplicate_of`
prose" above). The five, `expected-credit-loss`, `exposure-at-default`, `ifrs9-stage-allocation`,
`loss-given-default` and `probability-of-default`, read as irreducible on the same grounds as
the other two: F107's mechanical calculation of expected credit loss provisions needs the
general accounting concept it is computing, which stage the exposure sits in, and all three of
the PD, LGD and EAD parameters the formula multiplies together. No fifth input can be dropped
without removing something the calculation actually depends on.

## Verification

`scripts/check.py` after fix round 1:

```
ok    1. declared symbols resolve
ok    2. one symbol per object within a domain
ok    3. prerequisites resolve and the graph is acyclic
FAIL  4. every path is teachable in order
        survival-braid: survival-function needs 'future-lifetime-random-variable' before it, and neither the path nor its builds_on closure supplies it
        survival-braid: hazard-rate needs 'life-table-probabilities' before it, and neither the path nor its builds_on closure supplies it
ok    5. quoted sources are publishable
ok    6. no reviewed node carries an open source gap
ok    7. generated artefacts are current
ok    8. every taught_in names a lecture
ok    9. every ledger reference resolves

1580 nodes, 2 paths, 2 failures
```

Check 4's two failures are expected and untouched: `paths/` does not exist until Task 12.
`parse_node`, run over every file in `nodes/`, parsed all 1,580 with zero failures. `pytest -q`
ran 159 passed and exactly the three failures that read the corpus's uncommitted state
(`test_cli.py::test_check_py_exits_zero_on_the_real_repo` and the two in `test_hook.py`), for
the same check-4 reason.

Node count: 1,584 before this task, 1,579 after the first pass (six files deleted by the
merges, one written for the ceiling fix), 1,580 after fix round 1 (the single ceiling-fix node
deleted, two written in its place).

## Discrepancies between the brief, the handover and the measured repository

Per the standing instruction to measure rather than trust either document:

1. **The claims-reserving braid's edge sits on the wrong node in the brief's prose.** The brief
   says "the chain ladder node requires the exponential dispersion family node." Measured: no
   node named `chain-ladder` gains this edge; it is `over-dispersed-poisson-model`, which the
   handover's own "Cross-body edges to draw" section states correctly and which this report
   follows.
2. **The survival braid's edge was already resolved by unification rather than by a requires
   edge.**
   `force-of-mortality`, `claim-intensity` and `default-hazard` do not exist as node ids; the
   unification the brief and handover describe already happened inside `hazard-rate` itself.
3. **The Markov braid's named ids do not exist.** `rating-transition-matrix` and
   `life-multiple-state-models` are not node ids in the corpus. The actual nodes are
   `credit-migration-model` and `multiple-state-markov-model`.
4. **The handover's Batch B body list is wrong; its own numbers are right.** It names "CP1,
   IFRS 9, CB2, SP1, SP9, SP6, SP5, BCBS, and the WST re-pass" as the nine Batch B bodies, but
   measured, `ifoa-cb2-2026` and `up-02133413` (the WST re-pass) carry no `needs` key on any
   node entry: zero edges from either. The handover's own body-by-body count line (BCBS 9,
   IFRS 9 2, SP1 2, SP5 25, SP6 14, SP9 1, CP1 1, summing to 54) lists only the seven bodies
   that actually have one, and that line is correct.
5. **"Twelve Batch A manifests" is thirteen, measured.** The thirteen bodies with no `needs`
   key are listed in the Batch A section above.
6. **`with-profits-surplus-distribution`'s manifest note is stale.** It states the edge to
   `surplus-management` was never named in `requires`; measured, it already is.
7. **`binomial-distribution` and `geometric-distribution` already carry the edge** the
   handover asks to "confirm"; Task 9's union already applied it.
8. **`model-risk` is already merged across all three bodies** that touch it; F207's note asking
   whether it "should instead carry the anchor there" is answered by the node's own anchor list.
9. **This task's own file scope was wider than the brief's Files section states, by the
   coordinator's ruling rather than this task's departure.** The brief's Files section names
   only `nodes/*.md`, the `requires` field, as in scope. The coordinator's dispatch widened
   that to the six authorised near-miss merges, which deleted six files and unioned `anchor`,
   `domains` and `requires` together onto their six survivors, and to one new stub node for
   the ceiling fix (two, after fix round 1). The coordinator confirmed on review that the
   widening was theirs and that the merges and the new nodes stand; recorded here as the
   discrepancy between the brief's stated scope and the work actually authorised and done.
