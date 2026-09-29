---
id: probability-of-default
title: Probability of default
domains: [credit, regulation, stats]
status: drafted
requires: [outcome-window, regression-function]
spends:
  - {object: obj.response-mean, domain: stats}
anchor: [assa.f107.6.1-3-1-1, assa.f107.6.1-9-1, bcbs.d424.irb.para-67, ucsc.dl-actuarial-2026.l01]
vault_articles: [regulation/irb-pd-estimation]
vault_sources: []
taught_in: null
---

## Definition

The probability of default is the probability that a borrower defaults within a chosen outcome window, given the information available at the point the probability is assessed.

## The expression

$$
\mathrm{PD}(x) = E[Y \mid X = x] = P(Y = 1 \mid X = x)
$$

Here $Y$ is the binary indicator equal to one where the borrower defaults within the outcome window and zero otherwise, $X = x$ is the information available at origination or at the assessment date, and $\mathrm{PD}(x)$ is the resulting probability. Credit and regulation write this quantity $\mathrm{PD}$ throughout; statistics reads the same conditional expectation as the regression function evaluated on a binary response.

## Why this node exists

A default flag alone says only what happened to the loans already observed, and a probability of default is what turns that observed rate into a forward-looking estimate for a loan that has not yet had the chance to default. The outcome window fixes what counts as the event, and once the event is fixed this regression function evaluated on it is what every IRB model, every scorecard and every survival curve in the corpus ultimately estimates. Point-in-time probability of default needs it next, since a point-in-time estimate is this same probability conditioned additionally on the current stage of the economic cycle.
