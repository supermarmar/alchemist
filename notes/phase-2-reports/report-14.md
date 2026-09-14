# Phase 2 batch 14 attachment report

40 nodes worked. 9 attached, 31 uncovered. 10 total attachments.

## Attached

### esg-risk
Candidates: `regulation/climate-risk-management` (open, covers the environmental third), `regulation/eba-esg-green-brown-prudential-factors` (open, rejected), `concepts/4most-esg-impact-report-2026` (open, rejected).
Attached: `regulation/climate-risk-management`. States physical and transition risk as "a standing component of the prudential supervisory framework" and, in "Proposed changes", that banks and insurers "face structurally similar exposures to physical and transition risk, even though the transmission channels differ", the credit and market risk transmission the node's body names. Rejected `regulation/eba-esg-green-brown-prudential-factors`: it argues a narrower policy question, whether capital should be adjusted for green or brown exposures, not the risk category itself, and its content is already surfaced as one paragraph inside the attached article. Rejected `concepts/4most-esg-impact-report-2026`: it documents a firm's own B Corp certification, not a bank's ESG risk exposure; its own text states it "contains no credit risk modelling content, regulatory analysis, or quantitative methodology." Partial-scope note: the node covers environmental, sustainability and governance risk together; the attached article treats only the environmental/climate third. Ledgered.

### excess-and-retention-limit
Candidates: `concepts/reinsurance` (open, matches directly).
Attached: `concepts/reinsurance`. States both halves of the node in one passage: "the cedant bears all losses up to a deductible" (the excess) and "Surplus reinsurance instead lets the cedant retain the whole of each risk up to a fixed amount, its retention or 'line'" (the retention limit).

### excess-of-loss-reinsurance
Candidates: `concepts/reinsurance` (open, matches the arrangement), `methods/reinsurance-pricing` (open, matches the tail-dependency claim).
Attached both. `concepts/reinsurance` defines the arrangement itself: "the reinsurer pays the balance up to an agreed limit... Excess-of-loss (XL) cover comes in two units: per-risk XL indemnifies losses on individual policies above the deductible, while catastrophe XL responds to the aggregate loss." `methods/reinsurance-pricing` covers the second half of the node's claim, that the reinsurer's exposure "depends on the shape of the tail of the loss distribution rather than on its overall scale": its exposure-rating and exposure-curve sections (Miccolis 1977, Bernegger 1997) quantify exactly that tail dependency for pricing a layer.

### expected-credit-loss
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches directly), `methods/credit-loss-modelling-frameworks` (open, considered and left off).
Attached: `concepts/ifrs9-expected-credit-loss`. Its "three-stage model" section states the node's claim directly: an allowance "recognised at all times, with measurement varying according to the assessed change in credit risk", 12-month ECL for Stage 1 and lifetime ECL once an asset moves stage, and "must incorporate forward-looking information, including forecasts of future macroeconomic conditions." `methods/credit-loss-modelling-frameworks` was considered and left off: it surveys ECL alongside CECL and Basel A-IRB as a comparative framework, which is broader than this node needs and would have been a weaker second citation for the same ground the dedicated article already covers.

### expected-credit-loss-governance
Candidates: `regulation/eba-gl-ecl-credit-risk-management` (open, matches directly).
Attached: `regulation/eba-gl-ecl-credit-risk-management`. Its "Governance and methodology" section states the node's claim verbatim in substance: "The management body and senior management bear responsibility for approving the credit risk management strategy, maintaining an effective internal control system, and ensuring that allowance methodologies result in timely and adequate ECL recognition", with validation required to be "independent of model development, with findings reported promptly to senior management."

### expected-credit-loss-provisions
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches directly).
Attached: `concepts/ifrs9-expected-credit-loss`. Its "Component models and implementation methodology" section states the claim: "The ECL formula combines PD, LGD, and EAD components, each typically modelled separately and aggregated per time bucket", with the stage-dependent horizon (12-month for Stage 1, lifetime for Stages 2 and 3) given earlier in the same article.

### expected-shortfall
Candidates: `regulation/frtb-minimum-capital-market-risk` (open, matches the regulatory use), `methods/asrf-capital-foundation` (open, rejected as a passing mention).
Attached: `regulation/frtb-minimum-capital-market-risk`. States the shift the node's body implies: "expected shortfall at 97.5 per cent confidence, replacing the pre-FRTB 99 per cent VaR", motivated because "the shift from VaR improves tail-risk capture under adverse market conditions", the direct regulatory instance of VaR's blindness to breach severity. Rejected `methods/asrf-capital-foundation`: its one sentence, "expected shortfall remains portfolio-invariant... whereas expected excess loss is not invariant", is a passing mention inside an argument about Gordy's portfolio-invariance proof, not a treatment of expected shortfall itself. Partial-scope note: the attached article gives the regulatory application (why ES replaced VaR, and at what confidence level) but not the measure's own tail-average definition. Ledgered.

### exponential-dispersion-family
Candidates: `methods/exponential-dispersion-family-and-glm` (open, matches directly).
Attached: `methods/exponential-dispersion-family-and-glm`. States the node's claim in full: the density form "exp((yθ − κ(θ))/(φ/v) + c(y, φ/v))", the cumulant function determining "the mean is κ′(θ) and the variance is (φ/v)κ″(θ)", and the deviance-MLE equivalence. Sourced from the same lecture (`ucsc.dl-actuarial-2026.l02`) this node is itself anchored to.

### exposure-at-default
Candidates: `methods/ifrs9-ead-ccf-modelling` (open, matches the definition).
Attached: `methods/ifrs9-ead-ccf-modelling`. Opens with the node's claim: "the exposure at default (EAD) component... captures how much of a facility will be drawn at the point of default... EAD must be estimated behaviourally", i.e. it need not equal today's outstanding balance. Partial-scope note: the article frames EAD within IFRS 9 ECL measurement; the node also carries a prudential-capital anchor (`bcbs.d424.irb.para-98`) that this accounting-side article does not state. Ledgered.

## Uncovered (31)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): environmental-policy-instruments, equation-of-value, equilibrium-versus-no-arbitrage-interest-rate-models, equity-fundamental-analysis, equity-markets, equity-portfolio-management, estimator-efficiency-and-consistency, estimator-properties, example-outflow-assumptions, exchange-rate-determination, exchange-rate-intervention, exchange-traded-versus-over-the-counter-contracts, exotic-derivative-risk-management, expectation-of-life, expected-utility-theorem, expected-value, expense-allowance-and-allocation, experience-monitoring-methods, experience-monitoring-rationale, exploratory-data-analysis, exponential-distribution, exposed-to-risk, external-business-environment-forces.

**Passing mentions only, rejected:**
- equity-exposure-standardised-treatment-under-irb: `regulation/recognised-exchanges-uk` states, in one clause, that an equity exposure attracts a 400% weight "only when it is not listed on an exchange meeting the market structure condition above"; it does not treat the IRB exclusion or the wider standardised-approach equity risk-weight schedule the node's body describes.
- expected-loss-amount-calculation: `regulation/irb-approach` names "the expected loss best estimate (ELBE)" in one clause while describing the EBA guidelines' scope; it does not state the PD times LGD times EAD calculation itself.
- expense-risk: `concepts/ifrs-17-general-measurement-model` lists "expense risk" once among mortality, longevity and lapse as a source of the IFRS 17 risk adjustment; no treatment of a health and care insurer's own expense-versus-loading risk.

**Considered and deliberately not attached despite surface similarity:**
- example-lcr-calculation: `regulation/bcbs-liquidity-coverage-ratio-original` states the LCR's formula and structure ("the ratio of a firm's stock of high-quality liquid assets to its total net cash outflows") in full, but the node's own subject is a worked calculation with figures, and the article carries none. Judged not to meet the bar a formula restatement would not add to what the node's body already states; ledgered together with example-outflow-assumptions as one gap.
- expected-credit-losses-for-revolving-facilities: `methods/ifrs9-ead-ccf-modelling` treats revolving-facility EAD and CCF estimation at length, but on a different question (how much will be drawn) from the node's (over what period exposure is measured). The EBA's CRR3 CCF allocation RTS, referenced in the same article, states an analogous unconditional-cancellability test but explicitly "governs capital calculation, not accounting measurement."
- expected-versus-unexpected-losses: `methods/granularity-adjustment-gordy-lutkebohmert` puts the pieces the node needs side by side in one formula gloss, "Kᵢ is the obligor's IRB unexpected-loss capital charge per unit of exposure, Rᵢ is the loan-loss reserve requirement", but never states the expected-versus-unexpected distinction as a claim in its own right.
- exchange-traded-derivative-counterparty-exposure: `regulation/bcbs-sa-ccr-standard` and `regulation/ccr-internal-models-method` are substantial treatments of counterparty exposure measurement, but both are bilateral, netting-set frameworks; neither names a central counterparty or clearing member, the specific source of residual exposure the node's body describes.
- experience-rating-markov-chain: `methods/credibility-theory` treats experience rating as a Bühlmann credibility-weighting problem, not a Markov chain over discount states; `methods/loan-recovery-decision-timing` uses an eight-state Markov chain, but over loan arrears categories for recovery-timing optimisation, not a no-claims-discount scale.

## Ledger (`ledger-14.yaml`)

17 entries, all reusing an existing id from `ledger-ids.yaml`; none is new. Three entries ledger the uncovered remainder of a partial attachment rather than a fully uncovered node: `assa-f107-study-material-2026` carries the sustainability-and-governance two-thirds of esg-risk and the tail-average definition of expected-shortfall alongside its own line for example-lcr-calculation and example-outflow-assumptions; `bcbs-d424-irb-risk-weight-functions` carries the prudential-capital half of exposure-at-default alongside expected-loss-amount-calculation and equity-exposure-standardised-treatment-under-irb; `iasb-ifrs9-standard-cash-shortfall-and-hedge-types` carries expected-credit-losses-for-revolving-facilities, noted as a wiki-coverage gap since the standard is already ingested.

Every entry departs from its seeded claim's chapter or section, because each id is shared across many batches' different needs from the same document; each departure is named in the entry's own `note`. Two nodes matched a seeded claim exactly with no departure: equation-of-value (`ifoa-cm1-core-reading-2026`, "the equation-of-value formulation") and exposed-to-risk (`up-ias382-course-notes`, "relating the number of deaths observed... to the total time its members were exposed to the risk of dying"). `merge_ledger.py --dry-run` reports "would write 73 entries (4 seeded)" with three pre-existing disagreement notes, none touching an id this batch used.

The one judgement call outside the brief's scope: `stray_writes` reports many changed nodes outside batch 14, because other agents' batches are writing uncommitted changes to the same shared working tree concurrently and nobody commits mid-wave. Filtering `git diff --name-only` to the nine files this batch's `attach_articles.py` calls actually touched confirms all nine, and only those nine, are batch 14 nodes.
