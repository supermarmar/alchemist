# Phase 2 batch 3 attachment report

40 nodes worked. 10 attached, 30 uncovered. 11 total attachments.

This batch skews heavily to Basel I/II/III capital regulation and general banking-business
topics (ASSA F107/F207 anchors). The Basel/capital cluster hit the vault's strongest ground;
the general-banking-business cluster (income statements, pricing structures, dividend policy,
governance-adjacent-but-distinct topics, macroeconomics of banking) found almost nothing, as
expected for a credit-risk research base against finance-101 material.

## Attached

### bank-board-governance
Candidates: `regulation/pra-ss5-16-corporate-governance` (open, matches directly).
Attached. Node scope is "the roles and responsibilities of a bank's board of directors, the
distinction between executive and non-executive directors, and the skills and knowledge the
board needs collectively." The article treats board composition and NED independence,
the chairman's role, and board committee structure (risk/audit/remuneration) as dedicated
sections. Direct, substantive match.

### bank-capital-treatment
Candidates: `regulation/eu-crr-2013-own-funds` (open, matches directly).
Attached. Node scope is "how different instruments a bank issues, from ordinary shares to
subordinated debt, are treated and ranked as capital," naming no specific framework. The
article's dedicated sections on CET1 (ordinary shares), AT1 (contingent convertibles) and
Tier 2 (subordinated debt) eligibility and ranking are exactly this.

### balance-property
Candidates: `concepts/balance-property-and-auto-calibration` (open, near-exact match).
Attached. States the node's definition almost verbatim: "the exposure-weighted predictions
sum to the observed claims... a GLM estimated by maximum likelihood satisfies the balance
property if and only if the canonical link is used," and names it as an in-sample identity
distinct from out-of-sample unbiasedness. Same lecture the node's own anchor points to
(ucsc.dl-actuarial-2026.l07).

### banking-book-trading-book-boundary
Candidates: `regulation/frtb-minimum-capital-market-risk` (open, dedicated "Trading book
boundary" section), `regulation/bcbs-frtb-2012-consultative-document` (open, covers the same
ground from the superseded 2012 consultative document).
Attached `regulation/frtb-minimum-capital-market-risk` only: it is the current, in-force
standard (d457) with a section header matching the node exactly, stating that instruments
meeting trading-intent criteria must be assigned to the trading book, that banking-book
assignment is a narrow defined set, and that re-designation needs supervisory approval and a
capital penalty. The 2012 consultative document covers identical ground but superseded and
less current; not added alongside per the same reasoning the pilot applied to superseded
companion articles.

### basel-i-credit-risk-quantification / basel-i-minimum-capital-requirements / basel-i-shortcomings
Candidates: `entities/basel-accord-evolution` (open, dedicated "Basel I: the risk-weight
foundation" section covering all three).
All three attached to the same article, each to a different clause of the same paragraph:
credit-risk-quantification to "risk weights were deliberately simple: five buckets (0%, 10%,
20%, 50%, 100%)... sovereign 0%, corporate 100% regardless of creditworthiness";
minimum-capital-requirements to "a minimum total capital ratio of 8%, with Tier 1 core capital
... at no less than 4%"; shortcomings to "the flat risk-weight architecture provid[ed] no
mechanism for differentiating economic risk within asset classes, a limitation the Basel II
agenda explicitly set out to correct." Each clause is a complete, direct statement of that
node's narrow subject, so a thin (one-sentence) span was judged sufficient here: the node's
whole scope is that one fact. Flagged for the record that all three rest on the same
paragraph, so a spot-read does not mistake this for three independent sections.

### basel-ii-shortcomings
Candidates: `entities/basel-accord-evolution` (open, IRB-reliance weakness),
`methods/credit-risk-procyclicality` (open, procyclicality weakness).
Attached both: the node names two features exposed by the 2007-08 crisis (reliance on
internal models, procyclical capital requirements) and no single article covers both. The
first article states "the IRB framework was...the source of its principal weakness...
RWA calculations under internal models varied substantially across banks." The second states
the structural mechanism directly: "the single-factor credit risk model underpinning the
Basel IRB approach is one example of structural procyclicality: the regulatory capital formula
... is convex in PD," explicitly tied to "the Basel II IRB framework's accommodation" of both
calibration philosophies. Together the two clear the bar; neither alone would.

### basel-iii-2017-finalisation-rationale
Candidates: `entities/basel-accord-evolution` (open, matches directly).
Attached. The "Basel III finalisation: constrained IRB and the output floor" section states
the rationale (RWA variability across banks with similar portfolios), the output floor
mechanism (72.5%), A-IRB removal for banks and large corporates, and the operational-risk
framework's single standardised method. Direct, near-complete match to the node's stated
scope; the article does not separately name the leverage ratio as a backstop, but the rest of
the rationale is covered in full.

### basel-iii-liquidity-framework-overview
Candidates: `regulation/bcbs-liquidity-risk-framework` (open, matches directly).
Attached. States exactly the node's claim: "the LCR addressed the short-term dimension...
30-day stress," "the NSFR addressed the structural dimension... funded by adequately stable
liabilities rather than short-term wholesale borrowing," framed explicitly as Basel III's
"twin" liquidity standards.

## Rejected on jurisdiction/instrument mismatch (not attached despite strong content overlap)

Two nodes had a vault article stating the right numbers but citing the wrong instrument for
what the node names:

- **basel-iii-revised-minimum-capital-requirements**: `regulation/eu-crr-2013-capital-
  requirements-regulation` states "Article 92 of the original CRR set the three minimum
  capital ratios: 4.5% CET1, 6% Tier 1, and 8% Total Capital" -- the correct figures, but
  cited throughout as EU CRR Article 92, not the BCBS Basel III standard the node (anchored to
  ASSA F107, teaching the international framework) actually names. A writer citing this
  article would be citing the EU's transposing regulation as authority for a claim about the
  Basel Committee's own standard.
- **basel-iii-tier-1-and-tier-2-redefinition**: same issue with `regulation/eu-crr-2013-own-
  funds`, whose entire citation apparatus is CRR Articles 25-91, not the BCBS text.

Both rejected on reconsideration after an initial attach; recorded here rather than silently
dropped, since the content match is otherwise strong and a future batch or reviewer may judge
differently.

### bank-management-governance-structure (considered, not attached)
`regulation/pra-ss5-16-corporate-governance` covers the "control functions" half of the node
(three-lines-of-defence: first-line business, second-line risk/compliance, third-line internal
audit) but not the "executive committee" half ("the roles and responsibilities of a bank's
executive committee, how they differ from the board's"), which the article never addresses --
it is a board-governance statement, not a management/executive-committee one. Half-covered on
the weaker half; not attached.

### available-capital (considered, not attached)
`regulation/eu-crr-2013-own-funds` defines what counts as regulatory capital (own funds
composition) but the node's actual subject is the distinction between capital a bank holds
and capital a rule or model requires it to hold -- a contrast the article never draws. Passing
overlap on terminology, not on the node's point.

## Uncovered (30)

**No vault content at all** (index and full-text grep both empty): average-cost-per-claim-
method, backpropagation, balance-of-payments, bank-asset-transfer-to-staff-pension-fund,
bank-balance-sheet, bank-business-model, bank-credit-and-liquidity-risk-channels,
bank-dividend-policy, bank-financial-ratio-analysis, bank-income-statement,
bank-operational-expenses, bank-pricing-structures, bank-stakeholder-engagement,
bank-strategic-plan-lifecycle, bank-taxation, bank-trading-activities,
banking-risk-problem-integration, banks-and-investment-in-the-economy, banks-and-payments,
banks-deposits-and-lending-growth, barrier-option, barriers-to-entry-and-contestability,
available-capital, bank-management-governance-structure, basel-iii-revised-minimum-capital-
requirements, basel-iii-tier-1-and-tier-2-redefinition (last four per the rejections above).

**Passing mentions only, rejected:**
- backpropagation: `methods/mathematics-for-machine-learning` names it in one clause
  ("backpropagation is an application of" the multivariate chain rule) inside a survey of six
  maths chapters; no algorithm description (forward/backward pass, autodiff).
- basel-ii-risk-quantification: `entities/basel-accord-evolution`'s Basel II section covers
  the IRB/three-pillar structure fully but never states the node's specific claim -- that
  Basel II extended minimum capital requirements to credit, market and operational risk
  together rather than credit risk alone. Market risk is not mentioned in that section at all.
- basel-iii-2017-implementation-timeline: `entities/basel-accord-evolution` gives one generic
  sentence ("carries an implementation date of 1 January 2023") with no phase-in schedule; see
  the ledger note on the date discrepancy against the primary text.
- bank-exposure-risk-weights-ecra / -scra: no wiki article treats the standardised approach's
  bank-exposure hierarchy; see ledger.

## Ledger (`ledger-03.yaml`)

7 entries: 6 reuse ids already proposed in `ledger-01.yaml` (`assa-f107-study-material-2026`,
`assa-f207-study-material-2026`, `ifoa-cb2-core-reading-2026`, `ifoa-cm2-core-reading-2026`,
`ifoa-sp6-core-reading-2026`, `dl-actuarial-2026-l04-05-fnn`), every field copied verbatim
except `needed_by`, which carries only this batch's new node ids. One entry is new:
`bcbs-d424-sa-and-intro-provisions`, covering `bank-exposure-risk-weights-ecra`,
`bank-exposure-risk-weights-scra` and `basel-iii-2017-implementation-timeline`. This is a
different chapter of the same d424 standard the seeded `bcbs-d424-irb-risk-weight-functions`
entry already names (that entry's claim is the IRB chapter, CRE31), so it was not folded in.
Direct inspection of `vault/markdown/bcbs/d424.md` confirmed both spans are already ingested
(paragraphs 16-21 give ECRA/SCRA in full; paragraph 9 gives the implementation-date table and
the 1.06 scaling-factor removal), so status is `ingested` and the gap is wiki-article scope,
not acquisition. `merge_ledger.py --dry-run` reports "would write 21 entries (4 seeded)" with
no complaints and no disagreements.

## Notes for the record

- **Date discrepancy found and not resolved**: `entities/basel-accord-evolution` states BCBS
  d424's implementation date as "1 January 2023"; the primary text (`d424.md`, paragraph 9)
  states 1 January 2022 for the revised standardised/IRB/CVA/operational-risk approaches
  (matching the node's own text). This does not affect any attachment made here, since the
  implementation-timeline node was rejected on thinness independent of the date, but the
  discrepancy is worth a fact-check pass on that wiki article.
- Five unrelated modified files were present in the working tree before this batch started
  (`artificial-intelligence-model-governance.md`, `asset-liability-mismatch.md`,
  `asset-liability-modelling.md`, `auto-calibration.md`,
  `automated-decision-making-safeguards.md`) -- none are in batch 3's node list and none were
  touched by this session.
