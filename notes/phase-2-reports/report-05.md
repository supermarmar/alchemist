# Phase 2 batch 5 attachment report

40 nodes worked. 12 attached, 28 uncovered. 13 total attachments.

This batch skews heavily to an ASSA F207 ICAAP cluster and a UCSC deep-learning-actuarial
cluster (canonical link, calibration repair), both of which hit the vault's strongest ground
(bank regulatory capital and credit-model calibration), plus a general-insurance reserving
cluster (Bornhuetter-Ferguson, bootstrap) that hit its established GI reserving coverage. The
fixed-income and stochastic-calculus cluster (bonds, Brownian motion, Brace-Gatarek-Musiela,
Cameron-Martin-Girsanov, CAPM) and the general-banking/economics cluster (business cycle,
business risk, capital allocation) found almost nothing, as expected for a credit-risk
research base against quant-finance and finance-101 material.

## Attached

### bornhuetter-ferguson-method
Candidates: `methods/bornhuetter-ferguson-reserving` (open, dedicated article).
Attached. The article is entirely about this method: origin, mechanics, the credibility
interpretation (Z = percentage developed), and the three conditions favouring it over the
chain ladder. Direct, complete match.

### bootstrap-reserving
Candidates: `methods/stochastic-claims-reserving` (open, dedicated ODP-bootstrap section).
Attached. Its "Chain-ladder-consistent models" section states the node's own claim directly:
"the over-dispersed Poisson (ODP) model... its bootstrap implementation resamples Pearson
residuals to build a full predictive distribution."

### bootstrap-method
Candidates: `methods/statistical-power-analysis` (open, dedicated bootstrap section).
Attached. Its "Bootstrap hypothesis testing" section explains the general mechanism
(resampling from observed data, computing the statistic on each resample, deriving the
result from the empirical quantile rather than a parametric assumption) substantively,
even though the article's own framing is PD-validation hypothesis testing rather than
general estimator properties. Flagged as the least certain of this batch's attachments.

### burning-cost-approach
Candidates: `methods/reinsurance-pricing` (open, dedicated "burn-cost analysis" clause).
Attached. "Experience rating, or burn-cost analysis, gathers roughly ten years of premium and
losses, trends premium to a common level, applies loss development and inflation to cap
losses at the layer" is a direct, complete statement of the node's own claim.

### business-indicator-component
Candidates: `regulation/operational-risk-business-indicator` (open, dedicated BIC section).
Attached. States the marginal-rate band structure exactly: "applying marginal rates to BI
bands (12% to EUR1 billion, 15% to EUR30 billion, 18% above)."

### calibration-repair
Candidates: `concepts/balance-property-and-auto-calibration` (open, matches directly).
Attached. Same UCSC lecture (l07) the node is itself anchored to. States both repairs in the
node's own hierarchy: "the standard remedy adjusts the intercept" for the balance property,
and isotonic regression as the auto-calibration remedy, "with over-fitting at the two ends of
the range the residual concern," matching the node's floor-and-cap point.

### canonical-link
Candidates: `methods/exponential-dispersion-family-and-glm` (open, matches directly).
Attached. Same UCSC lecture (l02) the node is itself anchored to. States the definition and
both consequences verbatim: "the canonical link is the inverse of kappa-prime... the maximum
likelihood estimate is unique, and the fitted model satisfies the balance property."

### capital-adequacy-assessment-process-guidelines / capital-adequacy-assessment-regulatory-requirements
Candidates: `regulation/pra-icaap-and-pillar-2` (open, matches both).
Attached both to the same article's "ICAAP expectations" and "SREP and Pillar 2 reporting"
sections: proportionality and the use test read as "what distinguishes a strong assessment
from a weak one," and the SS31/15 Chapter 2 expectations plus the FSA071-FSA082/PRA111
reporting items read as "the principal requirements a regulator sets... and the documentation
a bank must produce to evidence it." UK PRA-specific rather than ASSA-general, but ICAAP
mechanics are a nationally-implemented instantiation of Basel Pillar 2 rather than a BCBS text
with its own canonical wording, so this is not the jurisdiction-transposition mismatch batch 3
flagged for Basel III's own numeric ratios.

### capital-adequacy-risk-appetite-indicators
Candidates: `concepts/risk-appetite-framework` (open, matches directly).
Attached. States the node's own claim: "Risk limits are quantitative measures... that
allocate the aggregate risk appetite to business lines, legal entities and specific risk
categories," with escalation on breach.

### capital-adequacy-stress-testing
Candidates: `regulation/pra-icaap-and-pillar-2` (open, stress-testing chapter) and
`regulation/reverse-stress-testing` (open, reverse scenarios and management actions).
Attached both: the first covers base-case-to-severe scenarios, forward-looking, idiosyncratic
and systemic; the second covers the reverse-scenario half and "mitigating measures... as part
of the ICAAP results," which is the node's "management actions that would follow." Neither
alone covers the full node.

### capital-buffer-quantification
Candidates: `regulation/pra-icaap-and-pillar-2` (open, matches almost verbatim).
Attached. "The PRA Buffer (Pillar 2B) quantifies the firm-specific capital needed above the
minimum to absorb ICAAP stress impacts" restates the node's claim directly.

## Uncovered (28)

**No vault content at all**, confirmed by index search and full-text grep across
`vault/wiki/`: bolzano-weierstrass-and-heine-borel-theorems, bond-credit-analysis,
bond-markets, bond-portfolio-management, bond-price-bounds, bond-pricing-and-yield,
bond-stripping, bootstrap-confidence-interval, brace-gatarek-musiela-calibration,
brace-gatarek-musiela-model, brownian-motion, business-application-of-economic-concepts,
business-cycle, cameron-martin-girsanov-theorem, capital-adequacy-fundamentals,
capital-adequacy-risk-register, capital-allocation, capital-and-provisioning-influence-on-
pricing, capital-asset-pricing-model, capital-diversification-benefit,
capital-impact-on-reinsurance-purchasing, capital-management.

**Passing mentions only, rejected:**
- board-governance-risk: `concepts/risk-appetite-framework`'s "Board responsibilities" section
  covers board ownership of a risk appetite framework generally, not the node's specific claim
  (the risk that a board's own strategy/oversight/conflict-of-interest decisions turn out
  wrong).
- business-continuity-planning: `regulation/operational-resilience-regime` explicitly treats
  business continuity planning only as a foil it is contrasted against ("Operational
  resilience inverts the question business continuity planning had been asking"), never as
  its own subject.
- business-risk: no article defines the bank-earnings-shortfall concept; "business risk" as a
  search term returns nothing relevant.
- capital-adequacy-regulatory-view: `regulation/pillar-2a-capital-framework` states the
  Pillar 1 plus Pillar 2A plus buffer stack, but never frames it as "one input among several
  to the board's own judgement," which is the node's actual claim.
- capital-adequacy-assessment-components: none of the ICAAP articles state the "financial
  forecast including capital available" component the node names, only the P1/P2A/buffer
  stack.
- capital-conservation-buffer: `regulation/pra-capital-buffers-ccyb-srb` names the Capital
  Conservation Buffer only as one of five listed instruments while its own substantive content
  covers CCyB/G-SII/O-SII/SRB legal-basis history; `regulation/eu-crr-2013-capital-
  requirements-regulation` names it once in a parenthetical list. Neither states the 2.5%
  figure or the distribution restriction. Direct inspection of `vault/markdown/bcbs/d424.md`
  (not a wiki article) confirms the node's own anchor, bcbs.d424.floor.para-3, is in fact
  correct and states the 2.5% figure exactly; ledgered as a wiki-article gap against an
  already-ingested source (see ledger-05.yaml).
- capital-impact-on-reinsurance-purchasing: `concepts/reinsurance` names "capital relief" as
  one of three general functions of reinsurance in one clause, not the node's specific claim
  that purchasing and capital decisions are made jointly.

Twenty-eight uncovered nodes proposed thirteen ledger documents (eleven reused, two new); see
ledger-05.yaml for the full claims and per-entry notes.

## check.py

`.venv/bin/python scripts/check.py` last line: `1560 nodes, 13 paths, 0 failures`. All 11 checks report `ok`.

## Ambiguities in the brief

None encountered that changed the approach. One judgement call worth flagging: the ICAAP
attachments (`pra-icaap-and-pillar-2`, `reverse-stress-testing`) are UK-PRA-specific articles
standing in for ASSA-F207-anchored generic nodes; I judged this different from the batch 3
jurisdiction-transposition trap because ICAAP has no single BCBS canonical text being
transposed, only a general Pillar 2 principle each jurisdiction implements natively, but a
spot-read may weigh this differently.
