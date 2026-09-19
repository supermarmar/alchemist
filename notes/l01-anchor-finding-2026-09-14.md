# The l01 anchor is sound, the vault holds the wrong lecture 1

Written 14 September 2026, during Phase 2 wave 3, after three separate batches
across two waves reported `ucsc.dl-actuarial-2026.l01` as an unreliable anchor.

## What was reported

Wave 1's batch 1 ledgered `age-period-cohort` against Holford (1983) rather than
against its own anchor body, noting that "that lecture (l01) turned out to contain no
age-period-cohort content on direct inspection". Wave 3's batch 28 hit the same wall on
`outcome-window`, observed that no prior wave had derived a wiki article or a ledger
entry from l01 while l02 through l12 all had, and ledgered it `in-raw` with the
reliability concern flagged rather than silently substituting a source.

## What is actually true

Twelve nodes anchor to l01: age-period-cohort, censoring, confounding,
definition-of-default, multiple-decrement, outcome-window, point-in-time-probability-of-default,
probability-of-default, regression-function, through-the-cycle-probability-of-default,
vasicek-single-factor-model and vintage-analysis. Every one of them is anchored correctly.

The corpus derives its trunk from the credit recast of the summer school, in
`~/Documents/Repos/actuarial_deep_learning/credit_lectures/`. Its
`01_credit-use-case.qmd` opens "Credit risk modelling: a PD problem" and carries
sections titled "The definition of default", "Censoring", "A general outcome window"
and "Cohorts, vintages and calendar time", with vintage appearing twenty-one times,
censoring ten, the outcome window five and point-in-time six.

The vault holds the *original* summer-school lecture instead, as
`markdown/courses/2026_eth_deep-learning-actuarial-01-use-case.md`. That file is a
Poisson GLM claim-count example, 939 lines of it largely code, and a direct probe finds
zero occurrences of age-period-cohort, censoring, confounding, the definition of
default, the outcome window, vintage, point-in-time, through-the-cycle or Vasicek. An
agent searching the vault for l01's material therefore finds nothing, and infers the
anchor is wrong.

`sources/syllabi.yaml` records the discrepancy without drawing attention to it: its
`local` field points at `actuarial_deep_learning/lectures/`, the original series, while
the corpus's own trunk material comes from `credit_lectures/` beside it. The two share
a numbering scheme, so `l01` resolves to a different document depending on which series
you reach for.

## What follows

No anchor needs correcting. What needs a decision is the ledger: any entry proposing to
acquire l01 material is misconceived, because the material is not missing. It sits in
the repo this corpus already derives from, and the vault simply ingested the other
variant of the same lecture. The options are to ingest the credit recast into the vault
so these twelve nodes can attach an article, or to accept that the trunk's own lectures
are written from `credit_lectures/` directly and leave the twelve with no vault article.

Worth checking whether l02 through l12 have the same split. The vault's l02 is
`2026_eth_deep-learning-actuarial-02-edf-glm.md` and the recast is
`02_credit-edf-glm.qmd`, so the same two series exist at every lecture number; the other
eleven were not probed, because their wave 2 and wave 3 attachments succeeded, which
suggests the vault's copies carry enough shared material to clear the cover bar.

## Resolved, 18 September 2026

The recast of lecture 1 is now registered in the vault as `credit-recast-2026-l01-use-case`, a
separate source from `dl-actuarial-2026-l01-use-case` rather than an amendment to it, because
the two are different documents sharing a number. `methods/credit-default-outcome-construction`
carries what the recast adds and the original does not, and four of the twelve nodes attach it:
`age-period-cohort`, `censoring`, `multiple-decrement` and `outcome-window`. The other eight were
already covered, which is the part of this note that did not survive contact with the node
records: the finding read as twelve nodes blocked, and eight of them carried a public vault
article the whole time.

`sources/syllabi.yaml` now states the split in its note. The `local` path still points at
`lectures/`, deliberately, since that folder holds the summer school's own material and the
summer school is the anchor body; what was missing was any statement that `credit_lectures/`
exists beside it and that the corpus's trunk comes from there.

The `holford-1983-age-period-cohort` ledger entry stays open rather than being retired. Its
reasoning was wrong, in that it read the vault's insurance extraction as the anchor's own
content, and the note is corrected in both `sources/wanted.yaml` and the staging fragment that
would otherwise restore it on the next merge. The want itself survives: the attached article is
self-authored and T5, while Holford (1983) is the standard T4 reference for the identification
result, so acquiring it upgrades a citation rather than filling a gap.

Lectures 2 to 12 were probed rather than left open. Matching each anchored node's subject against
the vault's copy, lecture 1 fails nine of its twelve while every other lecture misses between one
and four, and those misses are spelling variants such as `regularisation` against
"regularization". The two series therefore exist at every number, and only lecture 1 diverges in
substance.
