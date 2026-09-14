# Phase 2 batch 7 attachment report

40 nodes worked. 7 attached, 33 uncovered. 7 total attachments.

## Attached

### classical-credibility-model
Candidates: `methods/credibility-theory` (open, matches directly).
Attached: `methods/credibility-theory`. Its "Bühlmann's greatest-accuracy formulation" section states the node's own claim almost verbatim: the credibility factor Z = n/(n+k) rises with the risk's own experience n, shifting weight away from the class mean as that experience grows.

### climate-risk
Candidates: `concepts/climate-linked-mortality` (open, matches the mortality/morbidity half).
Attached: `concepts/climate-linked-mortality`. Its whole subject is the physical-risk channel (temperature, air quality) altering mortality and morbidity for a life insurer, which is the node's own definition. It does not name "transition risk" or investment experience explicitly, but the mortality/morbidity treatment is substantive and dedicated rather than a clause.

### cold-start-problem
Candidates: `concepts/in-context-learning-tabular-actuarial-models` (open, matches).
Attached. Its opening line ("a small portfolio, a new product or region ... with no history") and its dedicated zero-shot section (unseen-region test, retrieval by cosine similarity in representation space) directly match the node's own framing, including the retrieval-mechanism caveat. Domain differs (motor insurance pricing rather than credit default history), but the mechanism treated is the same one the node describes.

### collateral-management
Candidates: `regulation/eba-loan-origination-monitoring` (open, matches).
Attached. Its own "Collateral valuation and monitoring" section states independent valuation at origination, periodic revaluation through the loan's life, and ongoing monitoring of collateral value, directly on the node's subject.

### collective-risk-model
Candidates: `methods/aggregate-loss-models` (open, matches directly).
Attached. Its "The collective risk model" section states the node's definition verbatim (aggregate loss as the sum of a random number N of i.i.d. claim amounts, N random and independent of the amounts). Not extended to compound-distribution-moments, compound-poisson-distribution or compound-poisson-process (see rejections below): the moments paragraph gives only mean and variance, no skewness or reinsurance adjustment, and the Poisson-process node needs continuous-time arrivals this article does not cover.

### commercial-real-estate-lending
Candidates: `regulation/ecb-commercial-real-estate-bullet-loans` (open, matches).
Attached. Dedicated treatment of CRE lending's credit risk characteristics: refinancing risk, valuation cyclicality (revaluation cycles, outdated/biased valuations), sponsor analysis. Does not name "tenant concentration" specifically, but the valuation-cyclicality half the node names is treated at length.

### concentration-and-funding-source-reports
Candidates: `regulation/bcbs-liquidity-nsfr-monitoring-tools` (open, matches one of five tools it lists).
Attached. Its "concentration of funding tool" paragraph states the node's claim directly: reporting the proportion of funding from each significant counterparty, product type and currency to flag concentration not visible in aggregate metrics.

## Uncovered (33)

**Shared vocabulary or passing mention only, rejected:**
- classification-performance-metrics: `methods/discrimination-metrics-auc-and-somers-d` treats AUC/Somers' D as rank-discrimination statistics for credit validation, a narrower and differently-framed subject; it does not define a confusion matrix, precision, recall or F1. `methods/chang-2024-credit-risk-ml-deep-learning` names all six metrics (including precision/recall/F1) in one sentence as a benchmark's evaluation criteria, with no definition of any.
- climate-change-strategic-impact: `regulation/bcbs-d532-climate-principles` gives climate's effect on "the bank's strategy and business model" one clause inside Principle 12's scenario-analysis discussion; the rest of its 18 principles are governance/risk-management/supervision, not strategic impact.
- close-out-netting: `regulation/ccr-internal-models-method` uses "netting-set-level" exposure as a capital-modelling input; `concepts/credit-valuation-adjustment` cites close-out netting's role in one clause supporting CVA's netting-set computation. Neither treats the contractual mechanism itself.
- collateral: no definitional treatment found; regulatory articles use "collateral" only inside specific regimes (real estate, climate, ILAAP).
- collateralised-debt-obligation: `regulation/bcbs-securitisation-framework` treats SEC-IRBA/SEC-ERBA capital formulas for a securitisation tranche, not CDO structure or correlation dependence.
- concentration-risk: all vault concentration-risk articles (`methods/concentration-risk-partial-portfolio`, `methods/sector-concentration-hhi-capital-framework`, `regulation/eba-srep-concentration-risk`, `regulation/bcbs-large-exposures-framework`) are bank credit-portfolio Pillar 2 quantification frameworks (HHI, granularity adjustment); none treats general-insurance book concentration, the node's own domain.
- competition-policy / competition-risk: `regulation/ecb-eu-banking-competitiveness-regulatory-reform` is about EU banking-sector competitiveness policy (Savings and Investments Union), a different subject from competition-policy's market-power/merger-control framing; FCA fair-value articles use "competition" as a consumer-outcomes policy lever, not an insurer's own competition-risk exposure.
- combined-actuarial-neural-network, cls-token: the underlying UCSC lecture sources are already ingested and treat both subjects directly and at length (confirmed by direct read of the markdown extraction, not just the source's own topic list), but the only wiki articles built from those lectures (`methods/feed-forward-networks-claim-frequency`, `methods/credibility-transformer`) do not mention either. Logged in the ledger as a wiki-coverage gap, not an acquisition gap.
- collateral-and-guarantee-mismatch-adjustments, collateralised-transaction-general-requirements, commercial-real-estate-exposure-risk-weights, comprehensive-approach-collateral-haircut-method: all four anchor to specific bcbs.d424 paragraphs, directly verified present and correct in the vault's own extraction (markdown/bcbs/d424.md, SA paras 69/126/132/155 and IRB paras 72/115). `regulation/eu-crr-2013-credit-risk` and `regulation/crr-credit-risk-provisions` cover the same simple/comprehensive-method and CRM machinery substantively, but for the EU's CRR transposition rather than the international d424 standard these nodes cite; per this wave's lesson on jurisdiction-transposition mismatches, neither was attached. No d424-derived wiki article (`entities/basel-accord-evolution`, `regulation/operational-risk-capital-approaches`, `regulation/eba-output-floor-opinion`) treats any of the four paragraphs. Wiki-coverage gap, not acquisition.

**No vault content at all** (index and full-text grep both empty): chi-squared-distribution, chi-squared-test-for-graduation, chooser-and-binary-option, circular-flow-of-income, claim-amount-risk, claim-rate-risk, client-fact-finding-and-risk-attitude, cointegration, collective-investment-schemes, commercial-bank, commodities, common-utility-function, company-ownership-structures, completeness-of-a-statistic, complex-functions, complex-numbers-and-polynomial-factorisation, compound-distribution-moments (partial: `methods/aggregate-loss-models` gives mean/variance but omits skewness and the reinsurance-adjusted moments the node needs), compound-poisson-distribution (same article mentions it in one clause as a special case, no closure-property treatment), compound-poisson-process.

## Ledger (`ledger-07.yaml`)

19 entries: 3 genuinely new documents (up-wst212, up-fbs112, up-wtw124 course notes) plus 16 that extend already-proposed ids (ifoa-cs1/cs2/sp1/sp5/sp6/cb2/cm2/cp1 core reading, assa-f107/f207 study material, up-ias712/wst221/wtw320 course notes, the two dl-actuarial UCSC lecture ids, and bcbs-d424-irb-risk-weight-functions) with this batch's nodes added to `needed_by`. `merge_ledger.py --dry-run` reports "would write 44 entries (4 seeded)" with no malformed entries and no field-level disagreement beyond `note` (expected and non-blocking).

Two live corrections worth flagging: up-wtw320-course-notes was independently minted by batch 6 (running concurrently); an initial mismatch in what I'd read from its in-progress file was caught by re-running the dry-run and reconciled to batch 6's settled claim before finishing. bcbs-d424-irb-risk-weight-functions was reused (with a note, dropped by the merge in favour of the seed's own note, as designed) rather than minting a further new id the way batch 3's bcbs-d424-sa-and-intro-provisions did for the same document, per this wave's guidance.

## check.py

Last line: `11/11 checks pass`.

## Notes on the brief

None of it was wrong. Two things worth flagging for future batches: (1) re-running `merge_ledger.py --dry-run` right before finishing, not just once at the start, matters because concurrent batches mint and revise ids live; a stale read produced one transient claim conflict I had to reconcile. (2) The "reuse an existing id, add a note" guidance and a seeded/already-noted id's fixed note interact in a way worth naming explicitly: once an id already carries a `note` (from `wanted.yaml` or an earlier fragment), a differing note added later is always dropped by `union_entries` (first writer wins) and only surfaces as a dry-run disagreement line, not in the final ledger. I still wrote per-node notes in those cases for the audit trail, but the specific reasoning for a node riding under someone else's note lives in this report, not in `wanted.yaml`.
