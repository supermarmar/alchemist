# Phase 2 batch 4 attachment report

40 nodes worked. 8 attached, 32 uncovered. 8 total attachments.

## Attached

### basic-approach-cva-full-version
Candidates: `regulation/bcbs-d507-cva-framework` (open, matches directly), `concepts/xva-overview` (open, one clause), `concepts/credit-valuation-adjustment` (open, general CVA concept only).
Attached: `regulation/bcbs-d507-cva-framework`. Its own text states "The full version recognises single-name CDS, single-name contingent CDS and index CDS as eligible hedges, with hedging recognition capped by a parameter beta = 0.25... plus a hedging-misalignment quantity to capture residual basis risk", matching the node almost verbatim. Note: the node's own anchor points at d424 (the 2017 text), but d507 explicitly supersedes d424's CVA-specific provisions from 2020 onward; the BA-CVA reduced/full structure the node describes is the same mechanism, only recalibrated, so the article was judged to cover the node's actual subject rather than a different one under the same numbers.

### basic-approach-cva-reduced-version
Same source and reasoning as above. The article's text ("The reduced version eliminates hedge recognition... capital equals a supervisory discount scalar (DS_BA-CVA = 0.65) times the square-root sum of stand-alone CVA capital across counterparties") matches the node's own description directly.

### bayes-versus-empirical-bayes-credibility
Candidates: `methods/credibility-theory` (open, matches).
Attached: `methods/credibility-theory`. Its "Bühlmann's greatest-accuracy formulation" section frames Bühlmann's formula as a distribution-free least-squares approximation, and its "Jewell's exact Bayesian result" section shows the same formula is the exact Bayesian posterior mean for exponential families; the article states the term "empirical Bayes" explicitly elsewhere. This is a genuine comparison of the two approaches and their assumptions.

### bayesian-credibility-model
Candidates: `methods/credibility-theory` (open, matches).
Attached: `methods/credibility-theory`. Jewell's result section states the node's own claim directly: the linear credibility formula is the exact Bayesian posterior mean under a conjugate prior for the exponential family, giving the same weighted-average structure as the classical (Bühlmann) model.

### bayesian-credibility-theory
Same article and section as above; the derivation of the credibility premium from prior and likelihood, rather than as an assumption, is exactly Jewell's result.

### behavioural-tenor-modelling
Candidates: `concepts/eve-and-nii` (open, matches the mechanism), no dedicated FTP article found.
Attached: `concepts/eve-and-nii`. Its "Behavioural inputs" section treats the same estimation this node describes: non-maturity deposits assigned behavioural repricing and stability assumptions, and prepayable fixed-rate loans modelled with a conditional prepayment rate. The article frames the use case as IRRBB (EVE/NII) rather than funds transfer pricing, but the underlying behavioural-tenor estimation is the same technique the node names; no dedicated FTP article exists in the vault.

### best-estimate-reserve
Candidates: `regulation/solvency-ii-technical-provisions` (open, matches), `methods/stochastic-claims-reserving` (open, one clause: "UK working-party practice converges on the mean, not the median").
Attached: `regulation/solvency-ii-technical-provisions`. Its dedicated "Best estimate, contract boundaries and data quality" section and "Assumptions used to calculate the best estimate are only realistic where..." provision give the mean-based, no-margin definition a substantive, named treatment. Rejected `stochastic-claims-reserving` as a second citation: its best-estimate content is a single clause inside a broader reserving-uncertainty survey.

### binning
Candidates: `methods/risk-factor-binning` (open, matches directly), `methods/somers-d-binning-effects` (open, narrower: output binning for a discrimination statistic, not covariate binning).
Attached: `methods/risk-factor-binning`. Opens on a definition matching the node closely and gives a full, dedicated treatment: numeric-factor monotonic binning (isotonic regression, MAPA), U-shaped profiles via B-splines, and IV-driven categorical merging.

## Uncovered (32)

**No vault content at all** (confirmed by index search and full-text grep across `vault/wiki`): bermudan-swaption, bernoulli-distribution, beta-distribution, binomial-and-poisson-exposure-models, binomial-and-trinomial-trees, binomial-distribution, binomial-option-pricing-model, binomial-representation-theorem, birth-and-death-process, black-model-assumptions, black-model-interest-rate-derivatives, black-scholes-formula, black-scholes-martingale-approach, black-scholes-model-assumption, black-scholes-partial-differential-equation, behavioural-economics, behavioural-finance, benefit-guarantee-valuation-by-simulation, benefit-payment-moments, benefit-payment-risk-factors. All ledgered against their anchor's course/core-reading document.

**Passing mentions only, rejected:**
- basic-indicator-approach: `regulation/operational-risk-capital-approaches` and `regulation/operational-risk-business-indicator` both name the Basic Indicator Approach only as a superseded predecessor in one clause each ("replacing the earlier Basic Indicator, Standardised, and Advanced Measurement approaches"); neither states its own mechanics (fixed percentage of gross income).
- basis-risk / basis-risk-in-hedging / basis-risk-reference-rates: "basis risk" appears in `regulation/bcbs-d368-irrbb-standard`, `regulation/eba-gl-2022-14-irrbb-csrbb` and `regulation/cryptoasset-prudential-treatment` only as one item in a list of risk types with no definition; `regulation/solvency-ii-risk-mitigation-recognition` gives it a genuine legal test but scoped narrowly to Solvency II reinsurance recognition, not the general hedge/proxy-mismatch concept these nodes state; `methods/longevity-risk-transfer` explains the mechanism once but only as a supporting clause for a longevity-bond argument, not as its own subject. No article treats reference-rate basis risk (SONIA/LIBOR-style) specifically; `synthesis/scoring-model-transitions-precedents` covers the LIBOR-SONIA transition as a scoring-model analogy, not ongoing basis risk.
- bayes-estimator / bayes-theorem / bayesian-point-estimation / bayesian-prior-and-posterior: `methods/cap-slope-bayes-connection` states Bayes' theorem in closed form (f(x|D) = p(D|x)f(x)/p_D) but only as a step inside its own subject, the CAP-slope identity, not as a general treatment a Phase 3 writer could draft "Bayes' theorem" from. `methods/probabilistic-machine-learning` and `probabilistic-ml-advanced-topics` are chapter-by-chapter book guides that name "Bayesian estimation" and "posteriors" in passing without deriving them.
- behaviouralisation-exercise: `concepts/eve-and-nii` notes in one clause that "banks document and back-test these assumptions"; no treatment of the periodic re-estimation exercise itself.
- best-subset-selection: the node's own anchor lecture (`vault/markdown/courses/2026_eth_deep-learning-actuarial-08-ice-network-regularization.md`) has a dedicated section 1.8 on exactly this topic, but the only wiki article drawn from it, `methods/icenet-smoothness-and-monotonicity-constraints`, covers that lecture's ridge/LASSO material and omits best-subset selection entirely. Logged in the ledger as a wiki-coverage gap, not an acquisition gap, since the source is already ingested.
- bias-variance-tradeoff: `concepts/deep-learning-foundations` mentions it only as a foil to double-descent ("contradicts the classical bias-variance account"), with no treatment of the trade-off itself.
- binary-classifier-evaluation-metrics: `methods/discrimination-metrics-auc-and-somers-d` gives ROC/AUC substantive treatment but the node also requires precision, recall, F1 and the confusion-matrix cost trade-off, which no vault article defines; several ML-in-credit-scoring survey articles (`methods/deep-learning-credit-scoring`, `methods/ml-credit-scoring-empirical-and-review`, `methods/khandani-2010-consumer-credit-risk-ml`) name precision/recall/F1 only as benchmark-result columns, never defined.

## Notes on the brief

Reusing a seeded id and copying its `claim` field verbatim, even where this batch's node needs a different chapter of the same document, matches the precedent in `ledger-02.yaml` and `ledger-03.yaml` (e.g. `ifoa-sp6-core-reading-2026` extended for `asian-and-lookback-option` without changing its claim text). Followed the same pattern here; differences are captured in each entry's `note` instead. One ambiguity: `bayes-estimator` anchors to two course bodies (`up.wst221.15`, `up.wst322.1`); represented it under the first only, per the precedent set by batch 2's handling of `arbitrage-and-market-completeness` (anchored to `ifoa.cm2` and `ifoa.sp5`, ledgered under `ifoa.cm2` alone).

## check.py

Last line: `1560 nodes, 13 paths, 0 failures` (all eleven checks reported ok).
