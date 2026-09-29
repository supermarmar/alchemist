# Batch 01 report

Nodes written: 19
Nodes written from articles: 3
Nodes written without: 16

21 of the batch's 40 nodes were not landed: their anchor items are qualitative business,
professional-practice or governance topics with no defining formula the template's
"## The expression" section could honestly hold. They are listed at the end of this report
and remain `status: stub`.

## accounting-for-impairments
Sources: concepts/ifrs9-expected-credit-loss
Spends: none
Collision candidates: none
Split/other: PD, LGD, EAD have no corresponding objects in objects.yaml despite appearing across fin-man, regulation and credit domains; candidate objects obj.pd, obj.lgd, obj.ead worth adding if ECL-adjacent nodes recur.

## activation-function
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## actual-versus-potential-growth
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## actual-versus-predicted-plot
Sources: concepts/balance-property-and-auto-calibration
Spends: none
Collision candidates: obj.response-mean's stats alias (mu) is the mean response; this page's bin-average symbols y-bar_k and yhat-bar_k are a different notation for a related idea, so no spend was declared to avoid over-claiming the object.
Split/other: no unlock found by the brief's grep; the page ends on the consequence rather than a forward reference.

## actuarial-cash-flow-model
Sources: stub and anchor only
Spends: obj.discount-factor:actuarial
Collision candidates: none
Split/other: no unlock found by the brief's grep; the page ends on the consequence.

## age-period-cohort
Sources: methods/credit-default-outcome-construction
Spends: none
Collision candidates: none
Split/other: none

## annuity-contract
Sources: stub and anchor only
Spends: obj.discount-factor:actuarial, obj.survival:life
Collision candidates: none
Split/other: none

## arbitrage-and-hedging
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## arbitrage-and-hedging
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## arbitrage-and-market-completeness
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## assumption-setting-for-embedded-value
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: ANAV and VIF have no corresponding objects in objects.yaml; candidates obj.anav, obj.vif worth adding if embedded-value nodes recur.

## assumption-setting-for-pricing
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## assumption-setting-for-reserving
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## assurance-contract
Sources: stub and anchor only
Spends: obj.discount-factor:actuarial, obj.survival:life
Collision candidates: q_{x+t}, the one-year mortality rate, has no object in objects.yaml (obj.lifetime-cdf is the cumulative t-year form, {}_tq_x, not the one-year rate); candidate obj.mortality-rate worth adding if more life nodes need it.
Split/other: none

## balance-of-payments
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## bank-business-model
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## bank-dividend-policy
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: no unlock found by the brief's grep; the page ends on the consequence.

## bank-operational-expenses
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: no unlock found by the brief's grep; the page ends on the consequence.

## bank-pricing-structures
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: none

## bank-taxation
Sources: stub and anchor only
Spends: none
Collision candidates: none
Split/other: no unlock found by the brief's grep; the page ends on the consequence.

## Nodes not landed: template blocked by the absence of a defining formula

The following twenty-one nodes are qualitative business, professional-practice or
governance topics. Their standard syllabus treatment carries no expression that would
appear in the standard reading for the anchor item; the only way to fill "## The
expression" would be prose dressed as LaTeX, which is the risk spec section 6 names.
Left as `status: stub` for Mario's template decision, per the advisor's guidance for this
batch. Bodies were not drafted to scratch for these, since no defensible expression exists
to write against.

- accounting-regulatory-and-risk-approaches: contrasts three valuation bases with no shared formula.
- acquisitions-and-disposals-assessment: a strategic and financial assessment framework, not a valuation formula.
- actuarial-advisory-roles: a survey of business functions and sectors.
- actuarial-control-cycle: a recurring qualitative cycle (specify, develop, monitor).
- actuarial-funding: a specialist reserving method whose recursive funding-factor formula is too specific to state reliably from memory; flagged for a covered rewrite rather than an uncovered guess.
- actuarial-modelling-process: a qualitative process description.
- actuarial-problem-solving-approaches: a qualitative approach description.
- actuarial-professional-standards: professional conduct requirements.
- actuarial-professionalism-in-banking: professional conduct requirements applied to banking.
- actuarial-techniques-in-banking: a survey node naming techniques taught elsewhere.
- agency-risk: the principal-agent problem, stated qualitatively at this anchor.
- alternative-bank: a description of a lender type.
- aml-and-sanctions-compliance: a compliance and regulatory-process topic.
- asset-liability-committee: a governance and committee-structure topic.
- assumption-setting-principles: qualitative principles for choosing assumptions.
- automated-decision-making-safeguards: statutory disclosure and contestability duties, no formula.
- bank-asset-transfer-to-staff-pension-fund: a transaction description.
- bank-stakeholder-engagement: a governance and reporting topic.
- bank-trading-activities: a qualitative description of trading-desk activity.
- banking-book-trading-book-boundary: a regulatory classification test, not a formula.
- banking-risk-problem-integration: a meta node applying knowledge taught elsewhere.

