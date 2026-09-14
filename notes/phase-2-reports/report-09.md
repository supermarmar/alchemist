# Phase 2 batch 9 attachment report

40 nodes worked. 13 attached, 27 uncovered. 13 total attachments.

## Attached

### countercyclical-capital-buffer
Candidates: `regulation/countercyclical-capital-buffer` (open, matches directly).
Attached. Its own definition ("raise capital requirements during periods of excess aggregate credit growth... and release them during downturns to sustain lending") restates the node almost verbatim.

### counterparty-credit-risk
Candidates: `regulation/counterparty-credit-risk-saccr` (open, matches directly), `regulation/ccr-internal-models-method`, `concepts/credit-valuation-adjustment` (both rejected as narrower).
Attached `regulation/counterparty-credit-risk-saccr`. Its opening sentence, "Counterparty credit risk (CCR) is the risk that a counterparty to a derivatives or securities financing transaction defaults before final settlement of cash flows," is the node's own definition verbatim.

### credit-concentration-risk
Candidates: `methods/credit-risk-concentration-bcbs` (open, matches), `methods/concentration-risk-partial-portfolio`, `regulation/bcbs-large-exposures-framework` (both weaker/narrower).
Attached `methods/credit-risk-concentration-bcbs`. Treats name concentration and "sector or geographic concentration" directly as its own subject, with dedicated sections on each.

### credit-migration-model
Candidates: `methods/creditmetrics-portfolio-model` (open, matches directly).
Attached. Opens by describing CreditMetrics as valuing a portfolio through "the full set of credit quality changes, treating upgrades, downgrades and default as one distribution of outcomes weighted by transition probabilities," matching the node's own definition.

### credit-adjusted-effective-interest-rate
Candidates: `concepts/ifrs9-poci-assets` (open, matches directly).
Attached. Carries a dedicated "Credit-adjusted effective interest rate" section stating the node's exact definition and its distinction from the standard EIR.

### credit-facility-drawdown-profile
Candidates: `methods/ifrs9-ead-ccf-modelling` (open, matches directly).
Attached. Its "Behavioural drawdown methodology" section treats exactly how undrawn commitment converts to drawn exposure as conditions change.

### credibility-theory, credibility-premium, credibility-pricing-application
Candidates for all three: `methods/credibility-theory` (open, matches).
Attached to all three. The article states Bühlmann's credibility factor Z = n/(n+k) as "a weighted average of an individual risk's experience and the class mean," which is credibility-theory's and credibility-premium's subject directly, and its "Role in experience rating and pricing" section names experience rating and classification ratemaking as the general-insurance pricing application credibility-pricing-application asks for.

### credibility-transformer
Candidates: `methods/credibility-transformer` (open, matches directly; same anchor lecture, ucsc.dl-actuarial-2026.l10).
Attached. Covers the dual-CLS-token construction, the random-gate training mechanism, and the attention-derived weight decomposing into "a weighted average of a covariate-driven vector and the token's own value." Partial-scope note: the node's specific empirical claim, that the attention weight varies with training run rather than borrower thinness of experience, is not stated in this source; the mechanism itself is fully covered.

### credibility-weighted-encoding
Candidates: `methods/entity-embedding-and-network-ensembling` (open, matches; same anchor lecture, ucsc.dl-actuarial-2026.l06).
Attached. Its "Five ways to encode a categorical covariate" section states: "Credibility repairs it. Each level's mean is shrunk towards the global weighted mean with a weight increasing in that level's exposure, governed by a shrinkage hyper-parameter," matching the node directly.

### credit-capital-requirement-from-parameters
Candidates: `methods/vasicek-loan-portfolio-value` (open, matches), `regulation/irb-approach` (rejected, governance not mechanics).
Attached `methods/vasicek-loan-portfolio-value`. Its "Role in the Basel framework" section states the formula "gives the 99.9% conditional loss quantile, which after scaling for LGD and a maturity adjustment yields the capital requirement." Partial-scope note: EAD and the final RWA = 12.5 x K x EAD step are not made explicit; a Phase 3 writer would need to supply that last conversion step itself.

### credit-losses-over-the-cycle
Candidates: `methods/credit-risk-procyclicality` (open, matches).
Attached. Its core-mechanism paragraph states plainly that "during a downturn... defaults rise, collateral values fall," directly supporting the node's basic claim, though the article's own framing is the more analytical procyclicality feedback loop rather than the exam-level fact alone.

## Uncovered (27)

**Passing mentions only, rejected:** credit-default-swap/-bond-spread-relationship/-delta-hedging/-pricing (CDS appears only inside CVA proxy-spread and SA-CCR hedging discussions, never as its own payoff, pricing or hedging mechanism); credit-derivatives, credit-derivative-valuation, credit-enhancement-agency (credit derivatives appear only as one clause inside CRM eligibility text or basket-copula pricing, never their own payoff structure or valuation); credit-rating-use-and-limitations (`concepts/economic-value-of-rating-systems` treats internal rating systems, not external-agency reliance and its conflicts-of-interest/lag limitations); credit-event-and-recovery-rate (`methods/npl-recovery-rate-modelling` and `methods/single-factor-credit-risk-model-vasicek-and-belkin` use both terms in passing without defining either); credit-risk (no article defines the general term; `regulation/bcbs-core-principles-banking-supervision` covers supervisory principles, not a definition); credit-risk-appetite-limits (`concepts/risk-appetite-framework` is generic RAF/RAS architecture with no credit-specific limit-setting or benign/stress split); credit-financial-analysis (`methods/corporate-default-prediction-models` uses financial ratios as model inputs, not the general credit-assessment reading skill); credit-approval-cutoffs, credit-authorisation-process (policy/mandate language appears only inside model-shift and loan-origination articles, one clause each); credit-derivative-recognition-conditions (CRM text names "guarantees and credit derivatives" as one bracket, never the derivative-specific eligibility conditions).

**No vault content at all** (index and full-text grep both empty): cost-management-for-providers, cost-of-capital, cost-of-capital-banking, cost-of-credit, counting-process, covariance-and-correlation, covered-bond, covered-bond-exposure-risk-weights, cox-ingersoll-ross-model, cramer-rao-inequality, credible-interval.

**Considered and deliberately not attached despite surface similarity:** cox-proportional-hazards-model: `methods/lgd-survival-analysis` and `methods/ifrs9-lifetime-pd-term-structure` both apply and extend Cox regression (pseudo-Cox, recurrent-event Cox) but assume the base method rather than teaching the partial-likelihood construction and asymptotics the node needs; already closed by the seeded `ifoa-cs2-core-reading-2026` entry in `sources/wanted.yaml`, no ledger action needed.

## Ledger (`ledger-09.yaml`)

13 entries, all reusing ids seeded or minted by earlier batches except two new ones. None of the reused ids received a `note` field from me: every one already carries a note from an earlier batch, so following batch 6's precedent, adding a competing note would only be reported as a disagreement and dropped. What each of this batch's nodes specifically needs from a reused document: `assa-f107-study-material-2026` for cost-of-capital-banking (bank's own cost of capital), cost-of-credit (expense for expected/realised credit losses) and credit-risk (general definition; secondary anchors ifoa.sp5.4.1-3, ifoa.sp9.3.2-1 not separately represented); `assa-f207-study-material-2026` for covered-bond, credit-approval-cutoffs, credit-authorisation-process, credit-default-swap (secondary anchor ifoa.sp6.2.9), credit-financial-analysis, credit-risk-appetite-limits; `ifoa-cp1-core-reading-2026` for cost-management-for-providers; `ifoa-cs1-core-reading-2026` for covariance-and-correlation (secondary anchors up.wst121.4, up.wst211.15-16) and credible-interval; `ifoa-cs2-core-reading-2026` for counting-process; `ifoa-cm2-core-reading-2026` for cox-ingersoll-ross-model (secondary anchor ifoa.sp6.3.7-3) and credit-event-and-recovery-rate; `ifoa-sp5-core-reading-2026` for credit-derivatives and credit-derivative-valuation; `ifoa-sp6-core-reading-2026` for credit-default-swap-bond-spread-relationship/-delta-hedging/-pricing, credit-enhancement-agency and credit-rating-use-and-limitations; `up-wst221-course-notes` for cramer-rao-inequality; `up-fbs122-course-notes` (minted by batch 6 for capital-project-appraisal/capital-structure) for cost-of-capital, which needs a different chapter again: the weighted average cost of capital itself.

Two new entries, both a further chapter of the already-ingested BCBS d424 standard, both `status: ingested` after direct inspection of `vault/markdown/bcbs/d424.md`: `bcbs-d424-covered-bond-risk-weights` (paragraphs 32-36, covered-bond eligibility and risk-weight tables, confirmed present) for covered-bond-exposure-risk-weights, and `bcbs-d424-credit-derivative-recognition` (paragraphs 195-198, credit-derivative CRM operational requirements) for credit-derivative-recognition-conditions. `merge_ledger.py --dry-run` exits 0 and reports "would write 49 entries (4 seeded)"; the `note differs` lines it prints are all pre-existing disagreements among batches 1-8's own entries, none introduced by this file.

## check.py

`.venv/bin/python scripts/check.py` -> `1560 nodes, 13 paths, 0 failures`. All 11 checks report `ok`.

## Brief notes

Nothing ambiguous found. The "group many nodes under one document" guidance worked cleanly here: credit-default-swap's five SP6-anchored sibling nodes collapsed into one `ifoa-sp6-core-reading-2026` extension. One thing worth flagging for later batches: `up-fbs122-course-notes` (batch 6) now serves three unrelated FBS122 chapters (project appraisal, capital structure, cost of capital) across three batches with no shared note; a future batch adding a fourth should expect the same "note differs" pattern.
