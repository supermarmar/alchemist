# Sequencing the credit trunk by hand

The trunk carries a reader from the vocabulary a lender uses before any model exists to the
capital a supervisor requires and the governance built around that capital. It opens on the
lending business itself, on what credit risk is, who runs it, and how a bank organises policy,
pricing and monitoring around it. From there it moves to the instruments credit risk travels
on and the contracts that transfer it. Only then does it define default precisely enough to
count, name the three parameters that quantify it, and build the estimators that produce them.
Every estimator is followed by the means of checking it, because a number nobody has validated
is not yet an estimate. The last third of the trunk is the treatment those numbers receive:
first the accounting provision under IFRS 9, then regulatory capital under the standardised
approach, and finally the internal ratings-based approach together with the rating-system
governance, validation and disclosure a regulator expects around it. The order therefore puts
definitions before methods, methods before their regulatory treatment, and an estimator before
its validation.

## Stage 1: The lending business and the risk it runs

At the end of this stage a reader can state what credit risk is, describe how a bank sets its
credit strategy, appetite, underwriting rules and pricing, and assess a borrower from financial
statements, qualitative factors and a rating or score, all without fitting a model.

## Stage 2: Instruments, markets and the transfer of credit risk

At the end of this stage a reader can identify where credit risk sits in a bond, a loan
facility, a derivative or a securitisation, explain how a credit default swap, a special purpose
vehicle or a netting agreement moves that risk between parties, and separate credit risk from
the market and banking-book interest rate risk that travels on the same instruments.

## Stage 3: Default defined and the sample it is measured on

At the end of this stage a reader can turn a loan book's history into a modelling sample, by
applying a default definition, fixing an outcome window, separating vintage, age and calendar
effects, and naming the probability of default, loss given default and exposure at default that
the sample supports.

## Stage 4: Estimating the parameters

At the end of this stage a reader can choose between a structural, reduced-form or survival
formulation for a default model, fit it to a loan book, and extend it to a portfolio where
obligors default together rather than independently. The survival, life-table and multi-state
machinery the stage draws on is the same machinery the life corpus uses, which is why mortality
projection and multiple decrement sit here alongside default intensity, and it is the clearest
place in the trunk where the life material runs alongside the credit material.

## Stage 5: Calibrating and validating a credit model

At the end of this stage a reader can test a fitted model for balance and auto-calibration,
repair it where it fails, measure its discriminatory power, check it out of time, and explain
an individual decision back to the applicant it affected.

## Stage 6: Provisioning under IFRS 9

At the end of this stage a reader can classify a financial asset, measure it at amortised cost
through the effective interest method, allocate it to an IFRS 9 stage, and calculate the
expected credit loss provision that stage requires from the parameters of Stage 3.

## Stage 7: Regulatory capital under the standardised approach

At the end of this stage a reader can risk-weight any banking book exposure using supervisory
weights and eligible external ratings, and reduce that weight for collateral, a guarantee or a
credit derivative under the recognised mitigation rules.

## Stage 8: The internal ratings-based approach and the governance around it

At the end of this stage a reader can carry a bank's own probability of default, loss given
default and exposure at default through the risk-weight function to a capital requirement, and
state the rating-system design, quantification, validation, oversight and disclosure standards
a supervisor requires before permitting it.

## The stages as placed

| Stage | Nodes | First three ids |
|---|---:|---|
| 1. The lending business and the risk it runs | 48 | `financial-sector-functions`, `bank-credit-and-liquidity-risk-channels`, `shadow-banking-and-financial-innovation` |
| 2. Instruments, markets and the transfer of credit risk | 33 | `investment-asset-characteristics-and-markets`, `bond-markets`, `bond-credit-analysis` |
| 3. Default defined and the sample it is measured on | 10 | `definition-of-default`, `default-events-cross-border-lending`, `default-events-specialised-lending` |
| 4. Estimating the parameters | 33 | `statistical-modelling-portfolio-management`, `binning`, `frequency-severity-modelling-banking` |
| 5. Calibrating and validating a credit model | 11 | `balance-property`, `auto-calibration`, `calibration-repair` |
| 6. Provisioning under IFRS 9 | 32 | `accounting-for-impairments`, `impaired-assets`, `impairment-versus-default` |
| 7. Regulatory capital under the standardised approach | 49 | `pillar-1-minimum-capital-requirements`, `risk-weighted-assets`, `basel-i-credit-risk-quantification` |
| 8. The internal ratings-based approach and the governance around it | 57 | `internal-ratings-based-approach`, `expected-versus-unexpected-losses`, `irb-approach-choice-by-asset-class` |

The stages are deliberately uneven. Stage 3 holds ten nodes and Stage 8 holds fifty-seven,
because the Basel internal ratings-based material genuinely runs to that length in the corpus
while the definition of default and the three parameters it supports are a short hinge between
the business half of the trunk and the modelling half. Evening the counts out would have meant
either splitting the hinge or cutting the IRB run at an arbitrary point.

## Placements I was least sure of

**`credit-scoring` in Stage 1, at position 27, beside `credit-approval-cutoffs`.** The
alternative was to place it at the head of Stage 4 next to
`statistical-modelling-portfolio-management`, where the machinery that produces a score lives.
I rejected that because the record describes buying a bureau score or building one to support
an asset writing strategy, which is a policy statement a portfolio manager makes before any
model exists, and because `credit-approval-cutoffs` requires it and belongs firmly in the
lending-policy run. The cost is real, since some sixty-five nodes now separate the score from
the estimators that fit one, and a reader may reasonably want the two adjacent.

**`censoring` in Stage 4, immediately before `future-lifetime-random-variable`.** The
alternative was Stage 3, beside `outcome-window`, where the fixed-horizon default flag and the
censored duration make an instructive contrast. I placed it in Stage 4 because right-censoring
is the reason survival methods exist for a loan book at all, and the survival run reads as
incomplete without it. The contrast with `outcome-window` now spans a stage boundary.

**`binning` at position 2 of Stage 4 rather than in Stage 3.** Stage 3 is where a reader turns
raw history into a modelling sample, so binning could be read as sample preparation. I treated
it instead as a statement about a covariate's functional form, which makes it a modelling choice
and puts it with the estimators.

**The corporate governance run (`corporate-governance-principles`,
`corporate-governance-structure-factors`, `bank-board-governance`, `credit-risk-committee`) at
the end of Stage 8.** These four carry no prerequisites outside their own chain, so they could
have opened Stage 1 as foundational material. I put them last because the preamble ends on the
governance a regulator expects, because Stage 1 already carries the credit-policy machinery
(strategy, appetite limits, authorisation), and because a board's credit oversight reads better
once the reader knows what a rating system and a capital requirement actually are.

**IFRS 9 (Stage 6) placed before regulatory capital (Stages 7 and 8).** The alternative was to
run capital first and provisions afterwards, on the argument that the standardised approach is
the simpler framework and needs no parameter estimates at all. I followed the lecture set
instead, which runs R1 IFRS 9 point-in-time PD before R2 IRB capital, and the dependency
evidence agrees. `ifrs9-stage-allocation` needs only the parameters of Stage 3, whereas
`irb-versus-ifrs9-model-differences` needs both frameworks and therefore has to sit late
whichever way round they go.

**The IRB own-estimate quantification standards (`economic-loss-definition-for-lgd`,
`downturn-lgd-estimation`, `ead-quantification-standards`) in Stage 8 rather than Stage 3.**
Each attaches to one of the three parameters and could have followed it immediately. I held
them back to keep the rule that methods come before their regulatory treatment, so Stage 3
defines loss given default as a quantity and Stage 8 states the seven-year observation period
and the downturn condition a supervisor imposes on estimating it.

**The banking-book interest rate run (`market-risk`, `interest-rate-risk-banking-book`,
`forms-of-interest-rate-risk`, `embedded-loan-options`) and the prepayment run
(`prepayment-risk`, `prepayment-behaviour-modelling`, `loan-behavioural-tenor`) in Stage 2.**
Neither run is credit risk, and neither is risk transfer, so Stage 2 is the least-bad home
rather than an obviously right one. I kept them there because a reader meets these risks on the
same loan facilities and derivatives the stage is already describing, and because pulling them
into a stage of their own would leave seven nodes stranded between the lending business and the
definition of default. The stage sentence names them so the mismatch with the stage title is at
least visible.

**`automated-decision-making-safeguards` in Stage 5 beside `reason-codes` rather than in the
Stage 8 governance run.** It is a statutory obligation, which argues for the governance stage.
However, the duty it imposes, disclosing the basis of a declined decision, is discharged by
exactly the technique `reason-codes` describes, so a reader meets the obligation and the means
of meeting it together.

Ordered by hand on 8 September 2026; the six other domain paths stay in mechanical order until their pages exist (D1 a).
