# Batch 14 report

Nodes written: 13. Nodes written from articles: 0. Nodes written without: 13. Nodes not landed: 27.

## Nodes written

- credit-default-swap-pricing: sources: stub and anchor only. Spends: obj.hazard:credit, obj.discount-factor:fin-eng. Extends the CDS approximation on `credit-default-swap` to a full premium-leg-equals-protection-leg valuation under constant hazard.
- cross-validation: sources: stub and anchor only. Spends: none (follows `bias-variance-tradeoff`'s precedent of no spend). No unlocks found; ends on consequence.
- curtate-future-lifetime: sources: stub and anchor only. Spends: obj.survival:life. Unlocks: expectation-of-life.
- definite-and-indefinite-integrals: sources: stub and anchor only. Spends: none. Two display blocks (indefinite and definite definitions), deliberately withholding the fundamental-theorem-of-calculus evaluation formula, which belongs to that sibling node. Unlocks: fundamental-theorem-of-calculus (also unlocks integration-by-substitution, integration-techniques, ordinary-differential-equations-and-ivps; picked the most direct).
- differential-calculus-of-single-variable-functions: sources: stub and anchor only. Spends: none. Unlocks: mean-value-theorem (also unlocks lhopitals-rule, multivariable-calculus-and-directional-derivatives; picked the pedagogically direct next step).
- direct-methods-for-linear-systems: sources: stub and anchor only. Spends: none. Unlocks: iterative-methods-for-linear-systems-and-eigenvalue-problems.
- determinants-of-economic-growth: sources: stub and anchor only. Spends: none. No unlocks found; ends on consequence.
- dcf-use-lifetime-roe-raroc: sources: stub and anchor only. Spends: none. No unlocks found; ends on consequence. Edited after `--check` flagged two "rather than" uses.
- dcf-assumption-expected-credit-losses: sources: stub and anchor only. Spends: obj.exposure:credit, obj.exposure:fin-man. No unlocks found; ends on consequence.
- dcf-assumption-capital-required: sources: stub and anchor only. Spends: none. No unlocks found; ends on consequence.
- dcf-use-risk-based-pricing: sources: stub and anchor only. Spends: none. No unlocks found; ends on consequence. Edited after `--check` flagged two "rather than" uses. Reuses $r_{\text{ftp}}$ from `funds-transfer-pricing` for continuity, though that node is not a formal prerequisite.
- double-lift-chart: sources: `concepts/balance-property-and-auto-calibration` read in full (already the vault article on `lift-chart`, its requires). Spends: none. No unlocks found; ends on consequence.
- early-stopping: sources: stub and anchor only. Spends: obj.coefficients:ml. No unlocks found; ends on consequence. Reuses $\hat L_{\text{test}}$ from `out-of-sample-validation`, a direct prerequisite that already named early-stopping as its own unlock.

## Not landed

- credit-default-swap-delta-hedging: qualitative: the generic delta-hedge-ratio formula belongs to the sibling node `greek-based-hedging` (also a stub); this node is a specific application, not a distinct measure.
- credit-derivatives: qualitative: taxonomy overview of instrument types; valuation formula belongs to `credit-derivative-valuation`, its unlock.
- credit-risk-appetite-limits: qualitative: policy and limit-setting, no standard measure of its own.
- crr-eu: qualitative: regulatory-landscape item (regime history and UK/EU divergence, confirmed against the vault article); the capital-ratio formulas belong to nodes that own risk weights and RWA.
- currency-as-asset-class: qualitative: descriptive asset-class scope; unlocks forward-foreign-exchange-hedging.
- currency-risk: qualitative: a risk-taxonomy item (assa.f107.1.12 list) at the same depth as cybercrime-and-fraud-risk; an FX sensitivity formula would be generic to the subject, not this node's own measure.
- cybercrime-and-fraud-risk: qualitative: risk-taxonomy item, no formula.
- data-analysis-process: qualitative: process stages; unlocks exploratory-data-analysis.
- data-grouping-for-homogeneity: qualitative: methodological principle, no single formula.
- data-quality-checks-and-limitations: qualitative: checks and workarounds, no formula.
- dcf-assumption-discount-rate: qualitative: the rate's own quantity is the discount factor $v$ that the parent `discounted-cashflow-model-pricing` already spends and defines; no distinct measure.
- dcf-assumption-funding-and-ftp: qualitative: the funds-transfer-pricing margin formula belongs to the sibling node `funds-transfer-pricing`.
- dcf-assumption-income: qualitative: projected income composition is generic to the subject, not a distinct standard measure.
- dcf-assumption-operational-costs: qualitative: likewise generic; no standard formula of its own.
- dcf-use-marginal-pricing: qualitative: a pricing policy (cover direct costs, contribute to overheads) rather than a measure.
- default-events-cross-border-lending: qualitative: application of `definition-of-default` to a jurisdictional context, no formula of its own.
- default-events-specialised-lending: qualitative: likewise an application of `definition-of-default`.
- deposit-pricing-considerations: qualitative: factors weighed in setting a rate; unlocks price-elasticity-of-deposits (also unlocks term-liquidity-premium; picked one).
- derivative-collateral-arrangements: qualitative: legal and operational arrangements, no formula.
- derivative-hedging-applications: qualitative: overview of how instruments are combined for hedging.
- derivative-market-participants: qualitative: the three trading motives (hedging, speculation, arbitrage), no formula.
- derivative-portfolio-risk-profile-change: qualitative: descriptive effect on a portfolio's risk profile.
- derivative-pricing-assumption-breakdown: qualitative: circumstances in which pricing assumptions fail, no formula.
- derivatives-and-hedging-credit-risk: qualitative: terminology node (confirmed against the vault article `regulation/counterparty-credit-risk-saccr`); the EAD = alpha x (RC + PFE) formula it cites belongs to whichever node owns SA-CCR, not this one.
- discontinuance-terms-principles: qualitative: principles rather than the calculation methods; unlocks discontinuance-terms-methods and surrender-value-calculation-methods, which own the formulas.
- dynamic-funds-transfer-pricing: qualitative: adjusting FTP dynamically, illustrated by a case study; the FTP formula belongs to the parent `funds-transfer-pricing`.
- ead-quantification-standards: qualitative: regulatory standard text (BCBS d424 paragraph), prescriptive rather than formulaic; the CCF/EAD formula belongs to the parent `exposure-at-default`, already drafted.