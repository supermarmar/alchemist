# Phase 2 batch 2 attachment report

40 nodes worked. 5 attached, 35 uncovered. 6 total attachments.

## Attached

### auto-calibration
Candidates: `concepts/balance-property-and-auto-calibration` (open, matches exactly).
Attached: `concepts/balance-property-and-auto-calibration`. Its "Self-financing price cohorts" section states the node's own definition almost verbatim ("A regression function is auto-calibrated when the price it charges equals the expected claim conditional on that price... no cohort systematically cross-finances another"), sourced from the same UCSC lecture (l07) this node's requirement, balance-property, is anchored to.

### automated-decision-making-safeguards
Candidates: `regulation/automated-decision-making-uk-data-protection` (open, matches).
Attached: `regulation/automated-decision-making-uk-data-protection`. Treats the safeguards directly: Article 22C's four cumulative duties (information about the decision, a route to make representations, a route to obtain human intervention, a route to contest) map exactly onto the node's "duty to disclose the basis of the decision and to give the applicant a route to contest it". The article covers the UK GDPR/DUAA 2025 regime rather than the node's other named statute, the Consumer Credit Act 1974, but the core subject, statutory automated-decision safeguards, is substantively covered.

### artificial-intelligence-model-governance
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, matches), `regulation/eba-machine-learning-irb` (open, matches a narrower IRB-specific angle), `ai-agents/agentic-ai-governance-and-validation` (rejected).
Attached both: SS1/23's Principle 1 explicitly brings "machine learning and AI-based tools" within its complexity/interpretability tiering, and its practitioner-roundtable section describes the industry as underprepared for AI/ML validation; EBA's ML-IRB discussion paper and follow-up give a parallel, EU-specific treatment of the same extension (CRR Articles 171/175/179/189, management-body understanding, interpretability tooling). Rejected `agentic-ai-governance-and-validation`: it is about autonomous agentic systems specifically, a narrower and different subject than the node's general "AI model" scope.

### asset-liability-mismatch
Candidates: `regulation/bcbs-d368-irrbb-standard` (open, matches), `concepts/eve-and-nii` (open, close but assigned to the sibling node instead).
Attached: `regulation/bcbs-d368-irrbb-standard`. The standard's whole subject is repricing/maturity mismatch as the source of interest rate risk in the banking book, exactly the node's own statement, with the governance, measurement and shock-scenario apparatus built on that premise.

### asset-liability-modelling
Candidates: `concepts/eve-and-nii` (open, matches the interest-rate half).
Attached: `concepts/eve-and-nii`. EVE and NII are the two modelling approaches a bank uses to manage its balance sheet's interest rate exposure, including the behavioural modelling inputs (NMD repricing, prepayment) the node's "modelling a bank's assets and liabilities together" calls for. Partial-scope note: the node also names liquidity mismatches, which this article and the rest of the vault do not treat; the interest-rate half is the substantive part covered.

## Uncovered (35)

**No vault content at all**, confirmed by index search and full-text grep across `vault/wiki/`: analysis-of-surplus, analyst-capital-considerations, annuity-contract, annuity-factor-relationships, annuity-function, arbitrage-and-hedging, arbitrage-and-market-completeness, asian-and-lookback-option, asset-liability-committee, asset-liability-pricing-over-time, asset-pricing-parameter-estimation, asset-return-relationships, asset-share, assumption-setting, assumption-setting-for-embedded-value, assumption-setting-for-pricing, assumption-setting-for-reserving, assumption-setting-principles, assurance-and-annuity-factors, assurance-annuity-equation-of-value, assurance-contract, assurance-function, asymptotic-distribution-of-mle, asymptotic-normality.

**Passing mentions only, rejected:**
- analysis-of-variance: no ANOVA content anywhere in the vault (grepped directly; the vault's statistical material runs to GLMs, survival analysis and time series, not classical ANOVA).
- asset-liability-management: `regulation/bcbs-d368-irrbb-standard` covers the banking-book interest rate half in full, but the node spans actuarial, fin-eng, fin-man, gi and life domains and explicitly requires insurance investment-matching principles (health-care and life-insurance investment principles), which the vault does not touch. The narrower banking question is already captured more precisely by its own children, asset-liability-mismatch and asset-liability-modelling, above.
- audit-committee: `regulation/pra-ss5-16-corporate-governance` gives the audit committee one clause (financially literate chair, open channel with external auditor) inside a broader board-committee section; `concepts/three-lines-of-defence-assurance-model` cites it only as the reporting line for internal audit. Neither treats the committee's own structure and function.
- analysis-of-deviance: `methods/exponential-dispersion-family-and-glm` treats deviance as a loss function for fitting and out-of-sample model comparison (the node's own prerequisite, deviance-loss), not the analysis-of-deviance significance test for nested models this node is about.

**Considered and rejected on depth, with the closest candidate named:**
- archimedean-copula: `methods/default-correlation-copula-models` treats Li's normal-copula default-correlation framework in depth but never mentions the Archimedean family (Clayton, Gumbel, Frank) or their generator functions and tail-dependence patterns, which is this node's specific subject.
- arima, autoregressive-moving-average-process, autoregressive-process: `methods/forward-looking-information-modelling` has a real section on ARIMA(1,0,0) dynamic regression and ADF stationarity testing, but only as an IFRS 9 estimation-bias problem; it never states the general process definitions, order or the characteristic-equation stationarity condition these three nodes need, and never mentions a moving-average component at all.
- attention-mechanism: the node's own anchor lecture (UCSC l10-11, already ingested) has a full "Query, key and value" section stating the mechanism directly, but the only wiki article drawn from it, `methods/credibility-transformer`, uses attention as a given building block and gives the general mechanism one clause. Same pattern as the pilot's activation-function finding: a wiki-coverage gap, not an acquisition gap; logged in the ledger.
- autoencoder: the node's own anchor-adjacent lecture (UCSC l03, already ingested) states the node's definition almost verbatim on one slide, but the only wiki article citing that lecture, `concepts/deep-learning-foundations`, draws on a different source (Prince 2026) and mentions autoencoders once, in a chapter-listing clause. Same wiki-coverage-gap pattern; logged in the ledger.
- asset-correlation: `methods/asset-correlation-empirical-evidence` and `methods/vasicek-asset-correlation-estimation` cover empirical validation and statistical estimation of rho, not the BCBS regulatory calibration function itself (declining with PD, adjusted for SME size or large/unregulated financial institution exposure) that this node states. This gap is already seeded: `sources/wanted.yaml`'s `bcbs-d424-irb-risk-weight-functions` already lists asset-correlation in its needed_by, so no new ledger entry was added.

## Ledger (`ledger-02.yaml`)

18 entries: 9 new documents, 9 extending ids already seeded or introduced by batch 1 (`ifoa-cm1-core-reading-2026`, `ifoa-cs2-core-reading-2026`, `ifoa-cm2-core-reading-2026`, `ifoa-sp6-core-reading-2026`, `ifoa-sp2-core-reading-2026`, `ifoa-cp1-core-reading-2026`, `up-ias712-course-notes`, `assa-f107-study-material-2026`, `assa-f207-study-material-2026`), each with a `note` where this batch's nodes need a different chapter than the seeded claim describes. `merge_ledger.py --dry-run` reports "would write 30 entries (4 seeded)" with zero malformed-fragment or field-disagreement complaints. Two entries (`dl-actuarial-2026-l03-deep-learning-overview`, `dl-actuarial-2026-l10-11-transformers`) follow the pilot's `dl-actuarial-2026-l04-05-fnn` precedent: `status: ingested`, since the source lecture is already in the vault and the gap is wiki-article scope. `scripts/check.py` passes clean: `1560 nodes, 13 paths, 0 failures`.

## Notes on the brief

Working tree carries live concurrent edits to node files outside this batch (e.g. `balance-property`, several `basel-*`/`bank-*` nodes), timestamped alongside my own; presumably another wave agent running in parallel. Left untouched, per instructions. Nothing else in the brief was ambiguous.
