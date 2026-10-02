# Batch 21 report

Nodes written: 25. Nodes written from vault articles: 3 (bornhuetter-ferguson-method,
credit-risk-mitigation, credit-valuation-adjustment). Nodes written without vault articles: 22
(from the stub, anchor, node neighbourhood and standard treatment of the subject). Nodes not
landed: 15.

## Nodes written

- benefit-guarantee-valuation-by-simulation: sources read: stub and anchor only. Spends: none.
- bermudan-swaption: sources read: stub and anchor only. Spends: none.
- best-subset-selection: sources read: stub and anchor only. Spends: obj.coefficients:stats.
- binomial-and-trinomial-trees: sources read: stub and anchor only. Spends: none.
- black-model-interest-rate-derivatives: sources read: stub and anchor only. Spends: none.
  Collision candidate: the formula names $\Phi(\cdot)$, the standard normal distribution
  function, but `objects.yaml`'s `obj.normal-cdf` has no `fin-eng` alias (only `credit` and
  `stats`). Proposed: add a `fin-eng` alias, symbol `\Phi(\cdot)`, name "standard normal CDF",
  matching the stats spelling, since Black-76 and every other fin-eng option formula in the
  corpus will need it.
- bolzano-weierstrass-and-heine-borel-theorems: sources read: stub and anchor only. Spends: none.
  Split candidate declined: two theorems share one page at two display blocks, the ceiling, and
  belong together as the syllabus item states them jointly.
- bornhuetter-ferguson-method: sources read: methods/bornhuetter-ferguson-reserving. Spends:
  obj.ultimate:gi, obj.cohort-index:gi.
- capital-adequacy-assessment-components: sources read: stub and anchor only. Spends: none.
- capital-performance-metrics: sources read: stub and anchor only. Spends: none.
- capital-structure-and-dividend-policy: sources read: stub and anchor only. Spends: none.
- catastrophe-reinsurance-pricing: sources read: stub and anchor only. Spends: none.
- cauchys-integral-theorem: sources read: stub and anchor only. Spends: none.
- close-out-netting: sources read: stub and anchor only. Spends: none.
- cointegration: sources read: stub and anchor only. Spends: none.
- common-utility-function: sources read: stub and anchor only. Spends: none.
- compound-distribution-moments: sources read: stub and anchor only. Spends: none.
- continuous-function-properties: sources read: stub and anchor only. Spends: none.
- contract-alterations: sources read: stub and anchor only. Spends: none.
- convergence-in-probability: sources read: stub and anchor only. Spends: none.
- corporate-loan-pricing: sources read: stub and anchor only. Spends: obj.exposure:credit.
- credible-interval: sources read: stub and anchor only. Spends: none.
- credit-derivative-valuation: sources read: stub and anchor only. Spends: obj.hazard:credit,
  obj.survival:credit.
- credit-risk-mitigation: sources read: regulation/crr-credit-risk-provisions. Spends: none.
  The comprehensive-approach symbols ($E^{*}$, $E$, $C$, $H_e$, $H_c$, $H_{fx}$) are local to
  this formula and not held in `objects.yaml`.
- credit-valuation-adjustment: sources read: concepts/credit-valuation-adjustment,
  regulation/bcbs-d507-cva-framework. Spends: obj.hazard:credit, obj.survival:credit.
- defaulted-exposure-standardised-risk-weight: sources read: stub and anchor only (confirmed
  against regulation/crr-credit-risk-provisions, read for credit-risk-mitigation, which states
  the same Article 127 rule). Spends: none.

## Not landed

- capital-adequacy-assessment-process-guidelines: qualitative: process and best-practice
  guidance for running an ICAAP well; no formula, the standard treatment is descriptive.
- capital-adequacy-assessment-regulatory-requirements: qualitative: a list of regulatory
  requirements and evidencing documentation; no formula defines or measures the node's object.
- capital-adequacy-risk-appetite-indicators: qualitative: a set of indicators, triggers and
  limits across risk types; no single formula, each indicator has its own measure defined on
  its own node.
- capital-adequacy-risk-register: qualitative: a governance artefact, the risk register itself;
  no formula.
- capital-adequacy-stress-testing: qualitative: a process for running and acting on stress
  scenarios; no formula for "stress testing" as an object, the individual scenario mechanics
  belong to other nodes.
- capital-management: qualitative: an overview of the tools and objectives for managing capital
  over time; no single formula of its own. Sibling capital-performance-metrics carries the
  return-on-capital measure and capital-structure-and-dividend-policy carries gearing and
  payout.
- capital-management-strategy: qualitative: the overarching strategic approach tying targets,
  allocation and business plan together; no formula, process and governance topic.
- capital-modelling-approach: qualitative: describes deterministic versus stochastic capital
  modelling and the need to validate assumptions; a method choice and a process, not an object
  with a defining formula.
- capital-versus-liquidity-distinction: qualitative: a conceptual distinction between solvency
  and liquidity; no formula of its own. The liquidity coverage ratio and capital ratios each
  belong to their own nodes.
- central-bank-funding: qualitative: describes a funding facility and the conditions attached
  to it; no formula.
- central-clearing: qualitative: describes the CCP structure, margining and clearing mandate; no
  single formula stated as the standard treatment for this syllabus item.
- concentration-and-funding-source-reports: qualitative: describes the reports a bank produces
  to track funding concentration; the object is the report itself rather than a measure with one
  standard formula.
- corporate-exposure-risk-weights: qualitative: the standardised-approach risk weight is set
  from a lookup table by external rating band (or a flat weight, or the SME threshold-based
  weight), not from a formula; the anchor is the standardised approach, not IRB, so no risk-weight
  function applies.
- credit-enhancement-agency: qualitative: describes what a credit enhancement agency is and
  does; no formula.
- credit-risk-due-diligence-requirements: qualitative: due diligence obligations, internal
  policy and escalation requirements; no formula.

## Check

`.venv/bin/python scripts/check.py` last line: `1560 nodes, 13 paths, 0 failures`
