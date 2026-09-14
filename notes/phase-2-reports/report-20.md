# Phase 2 batch 20 attachment report

40 nodes worked. 15 attached, 25 uncovered. 15 total attachments.

## Attached

### internal-and-external-ratings
Candidates: `regulation/crr-credit-risk-provisions` (open, covers both halves), `regulation/irb-approach` (open, covers the internal half only), `regulation/eu-crr-2013-credit-risk` (rejected, superseded 2013 duplicate of the same ground).
Attached: `regulation/crr-credit-risk-provisions`. Its "Standardised approach" section states the external half ("Articles 108 and 109 govern how institutions apply the approach and where external credit assessments (ECAI ratings) are used") and its "Internal ratings-based approach" section states the internal half (own PD/LGD/CCF estimates under IRB permission). One article carrying both halves is preferred over citing `irb-approach` alongside it for the internal half alone, which would only duplicate ground this article already covers. `eu-crr-2013-credit-risk` treats the same two halves but is the pre-CRR3 2013 text; not added alongside the current one.

### internal-capital-adequacy-assessment-process
Candidates: `regulation/pra-icaap-and-pillar-2` (open, matches exactly).
Attached: `regulation/pra-icaap-and-pillar-2`. Opens "The Internal Capital Adequacy Assessment Process (ICAAP) is a firm-led self-assessment of all material risks, the capital and other resources needed to cover them, and the adequacy of internal processes to manage them on an ongoing basis," which is the node's own definition almost verbatim, plus dedicated sections on stress testing, capital planning and SREP.

### internal-liquidity-adequacy-assessment-process
Candidates: `regulation/pra-ilaap` (open, matches exactly).
Attached: `regulation/pra-ilaap`. "The Internal Liquidity Adequacy Assessment Process (ILAAP) is a firm-led self-assessment of all material liquidity and funding risks, the internal liquidity buffers needed to cover them, and the processes for managing liquidity" matches the node directly, with dedicated sections on stress testing and L-SREP.

### internal-loss-multiplier
Candidates: `regulation/operational-risk-business-indicator` (open, matches).
Attached: `regulation/operational-risk-business-indicator`. States the mechanism directly: "An Internal Loss Multiplier (ILM) can scale the BIC upward for institutions with disproportionate loss experience, but CRR3 exercises the Basel discretion to exclude the ILM from mandatory requirements." One sentence, but a dedicated definition and use rather than a passing mention, so it clears the cover bar; the article's main subject is the wider Business Indicator Component the ILM scales.

### internal-models-approach-market-risk
Candidates: `regulation/frtb-minimum-capital-market-risk` (open, matches), `regulation/basel-3-1-market-risk` (not opened, subsumed by the FRTB article for the IMA-specific ground).
Attached: `regulation/frtb-minimum-capital-market-risk`. Its dedicated "Internal models approach" section covers supervisory approval, desk-level permission, the P&L attribution suitability gate and the shift from VaR to expected shortfall. Partial-scope note: the node's own anchor (assa.f107.7.6-2) is framed around VaR, the pre-2023 basis; the article covers the current expected-shortfall-based IMA, which is the same regulatory approach in its present form rather than a different one.

### internal-models-for-capital-assessment
Candidates: `regulation/solvency-ii-internal-models` (open, matches exactly).
Attached: `regulation/solvency-ii-internal-models`. "An insurance or reinsurance undertaking may calculate its Solvency Capital Requirement using a full or partial internal model in place of the standard formula, subject to prior supervisory approval" is the node's own claim almost word for word, and the node's anchor (ifoa.cp1) and domains ([actuarial, fin-man, regulation]) point to the insurance reading rather than the banking IRB reading.

### internal-rating-system-regulatory-requirements
Candidates: `regulation/pra-ss4-24-irb-approach-2026` (open, matches), `regulation/irb-model-validation` (rejected, validation is a downstream obligation not the design/governance-before-use standard the node asks for).
Attached: `regulation/pra-ss4-24-irb-approach-2026`. Its "Rating systems and data representativeness" section states design requirements (grade count, defaulted/non-defaulted treatment, time horizon, annual review, independent validation) and the use test in section 4 gates reliance on the system for capital purposes, matching the node's "before a bank may rely on it for capital purposes" framing.

### internal-ratings-based-approach
Candidates: `regulation/irb-approach` (open, matches exactly), `regulation/crr-credit-risk-provisions` (open, covers the same ground at black-letter-article depth).
Attached: `regulation/irb-approach`. Opens "The internal ratings-based (IRB) approach permits institutions to use internally developed statistical models to estimate the probability of default (PD), loss given default (LGD), and exposure at default (EAD)... with those estimates feeding directly into regulatory capital requirements... conditional on explicit supervisory approval," matching the node's own wording closely. `crr-credit-risk-provisions` covers the same approach through its Articles 142-191 treatment; not attached alongside since it would duplicate this article's ground for this node (its distinct F-IRB/A-IRB choice-by-size content is used instead for `irb-approach-choice-by-asset-class` below).

### intraday-liquidity-risk
Candidates: `regulation/bcbs-liquidity-governance-principles` (open, matches), `regulation/bcbs-liquidity-risk-framework` (rejected, one-clause mention), `regulation/bcbs-liquidity-risk-principles-evolution` (rejected, one-clause mention).
Attached: `regulation/bcbs-liquidity-governance-principles`. States the concept directly: "BCBS 144 recognised that the real-time mechanics of large-value payment systems meant that a firm could face critical shortfalls within a trading day even if its overnight position appeared adequate. The principles required that firms measure and manage their intraday liquidity positions against projected daily peak requirements," matching the node's definition exactly. The other two candidates mention "intraday liquidity" only inside a list of topics BCBS 144 covered, with no comparable treatment, so were not attached alongside it.

### irb-approach-choice-by-asset-class
Candidates: `regulation/crr-credit-risk-provisions` (open, matches), `regulation/irb-approach` (open, weaker: one clause naming F-IRB/A-IRB in a History section).
Attached: `regulation/crr-credit-risk-provisions`. Its "Internal ratings-based approach" section states the choice directly: "the general principle is that Foundation IRB (F-IRB) is the minimum level of internal modelling; under F-IRB only PD is estimated by the institution, while LGD and CCF are set by supervisory values. Advanced IRB (A-IRB) permits institution-estimated LGD and CCF as well. CRR3 restricts A-IRB availability for large corporates, institutions, and other financial sector entities above specified thresholds, for which mandatory F-IRB applies." Partial-scope note: this states the choice constrained by exposure size and type rather than by the node's own "for most asset classes" framing, but is the more developed treatment of the two candidates.

### irb-corporate-governance-and-oversight
Candidates: `regulation/bcbs-credit-risk-principles` (open, partial match).
Attached: `regulation/bcbs-credit-risk-principles`. States board and senior-management responsibilities directly ("the board of directors is responsible for approving and annually reviewing the credit risk strategy... senior management is accountable for implementing that strategy"), independent assessment of credit risk management processes, and supervisors' duty to "assess internal rating systems and credit risk models." Partial-scope limit: this is the general BCBS credit risk governance standard (d595, 2025), not IRB-specific; it does not name an "independent credit risk control unit" or an internal-audit review cadence of at least annually, both specific to the node's own anchor (BCBS d424 IRB minimum requirements, paragraph 206).

### irb-disclosure-requirements
Candidates: `regulation/pillar-3-disclosure-framework` (open, partial match).
Attached: `regulation/pillar-3-disclosure-framework`. Covers the general Pillar 3 disclosure framework the node invokes, and names the IRB-specific instance directly: "Dedicated flow statements explain period-on-period variation in risk-weighted assets for internally modelled exposures, through templates covering IRB credit risk[, ]... CR8 (IRB credit risk)." Partial-scope limit: the article does not state the node's specific "eligible to use IRB only where the disclosure requirements are also met" conditionality; it treats Pillar 3 as a parallel obligation rather than an IRB-permission gate.

### irb-permanent-partial-use
Candidates: `regulation/pra-ss4-24-irb-approach-2026` (open, partial match), `regulation/eba-specialised-lending-risk-weights` (rejected, tangential).
Attached: `regulation/pra-ss4-24-irb-approach-2026`. States it directly in a named section: "Permanent partial use, addressed in section 3, is permitted where a firm has a clear and credible roll-out plan... Permanent partial use requires specific PRA approval and is available only in narrow circumstances." Partial-scope limit: the "narrow circumstances" are not enumerated; the node's own list (immaterial size and risk, specialised-lending data limitations, central counterparty exposures) is not named. Rejected `eba-specialised-lending-risk-weights`: it mentions permanent partial use only as a side effect of a proposed CRR3 amendment's knock-on relevance to the supervisory slotting approach, not as a treatment of the concept itself.

### investment-management-principles
Candidates: `regulation/prudent-person-principle` (open, partial match, insurer-specific).
Attached: `regulation/prudent-person-principle`. Its "Investment strategy" provision requires firms to align investment strategy "with the business model and liability profile, and alignment with board risk appetite," matching the node's own framing that liabilities, liquidity needs and risk appetite shape a suitable investment approach. Partial-scope limit: this is the Solvency II prudent person principle, a UK insurer-specific compliance standard, not the general cross-sector investment management theory the node's anchor (ifoa.cp1) covers; it does not treat liquidity needs as a distinct third factor, only liabilities and risk appetite. Judgement call: attached because the substantive overlap on liability- and risk-appetite-driven investment approach is real and named in a dedicated section, not a passing mention, but flagged here for the gate reviewer given the narrower regulatory framing.

### investment-strategy-development
Candidates: `regulation/prudent-person-principle` (open, partial match, insurer-specific).
Attached: `regulation/prudent-person-principle`. Its "Investment strategy" bullet states the same three-part process the node describes: "Firms must develop and document a strategy covering investment objectives, strategic asset allocation, alignment with the business model and liability profile, and alignment with board risk appetite" maps to the node's "stating an objective, assessing constraints and choosing an asset allocation to meet it." Partial-scope limit: as above, this is a Solvency II insurer compliance standard rather than the general actuarial process the node's anchor (up.ias712) teaches; also attached to `investment-management-principles` above for a different, overlapping part of the same node cluster.

## Uncovered (25)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`, including a search on "investment bank" and "investment banking" that returned zero hits outside one unrelated ICB Vickers source-metadata entry): intermediate-value-theorem, international-trade-and-exchange-rates, investment-asset-characteristics-and-markets, investment-bank, investment-bank-products, investment-banking-activities, investment-banking-loan-pricing, investment-banking-overview, investment-environment-influences, investment-guarantee-cost-methods, investment-index-uses, investment-performance-management, investment-regulatory-framework, investment-return-taxation, investment-returns-theoretical-relationships, investment-risk, investment-risk-budgeting, investment-risk-measures, investment-valuation, inwards-reinsurance-reserving, irb-asset-class-taxonomy, irb-rating-assignment-criteria.

**Passing mentions only, rejected:**
- international-swaps-and-derivatives-association-agreement: `concepts/credit-valuation-adjustment`, `concepts/debit-valuation-adjustment` and `concepts/funding-valuation-adjustment` all cite ISDA as a source of industry commentary on CVA/DVA/FVA and wrong-way risk, and `regulation/ccr-internal-models-method` cites an ISDA netting-benefit statistic; none treats the ISDA master agreement itself as the legal document that makes close-out netting enforceable, which is the node's actual subject.
- inverse-transform-method: `methods/witzany-2013-vasicek-logistic-distribution` uses "the normal inverse CDF" as one term inside the Vasicek single-factor formula; it is a component of a different derivation, not a treatment of the inverse transform method as a general simulation technique.

**Considered and deliberately not attached despite surface similarity:**
- internal-external-rating-consistency: `regulation/crr-credit-risk-provisions` and `regulation/eu-crr-2013-credit-risk` both cover how ECAI ratings feed the standardised approach, but neither treats the specific check the node names, that a bank's internal rating must line up with a borrower's external rating with an explanation required where they diverge; that consistency-check requirement is absent from both articles' IRB and SA sections alike.

## Ledger (`ledger-20.yaml`)

13 entries: 10 reuse an id already in `ledger-ids.yaml` (needed_by extended with this batch's node ids only, every other field copied verbatim, a note naming the different section this batch draws on), 3 are new (`up-wtw354-course-notes`, `bcbs-d424-irb-asset-class-taxonomy`, `bcbs-d424-irb-rating-assignment-criteria`). `merge_ledger.py --dry-run` reports "would write 73 entries (4 seeded)" with no blocking complaint.

Proposed documents, grouped by the node's own anchor body per the brief's default rule: ASSA F107 Study Material 2026 (6 nodes), IFoA CP1/SP5/SP1/SP2/SP7/SP6/CS1 Core Reading 2026 (5, 4, 1, 1, 1, 1, 1 nodes respectively), University of Pretoria WTW220/EKN120/WTW354 Course Notes (1 node each), and two new BCBS d424 IRB-chapter entries (asset-class taxonomy, rating-assignment criteria) at T1. No departure from the anchor-default rule was needed this batch; every uncovered node's own anchor body was also the right acquisition target.

One judgement call the brief did not cover: `up-wtw354-course-notes`, proposed here as a new id for `investment-risk-measures`, collided with an identical id independently proposed by batch 18 for a different WTW354 section (factor models and arbitrage pricing theory). `merge_ledger.py` handled this as a non-blocking field disagreement (keeping batch 18's claim, since ledger-18.yaml sorts first) while still unioning both batches' node ids into `needed_by`, so no action was needed, but it is worth flagging that two batches researching the same course number under the generic `up-<code>-course-notes` convention will collide whenever the course teaches more than one node's material, which is expected given the convention is per-document rather than per-section.
