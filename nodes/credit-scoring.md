---
id: credit-scoring
title: Credit scoring
domains: [credit, data-eng, stats]
status: drafted
requires: []
spends:
  - {object: obj.coefficients, domain: credit}
anchor: [assa.f107.6.2-1-1, assa.f207.1.5-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A credit score summarises a borrower's estimated creditworthiness in a single number,
built by combining a set of predictive characteristics into a linear function of the
log-odds of default.

## The expression

$$
\ln\!\left(\frac{p}{1-p}\right) = \beta_0 + \sum_{j=1}^{k} \beta_j x_j
$$

Here $p$ is the probability of default the score is built to predict, $x_1,\ldots,x_k$
are the borrower's characteristics entering the scorecard, and $\beta_0,\ldots,\beta_k$
are the scorecard coefficients, fitted so that the linear combination on the right
reproduces the log-odds observed in the data used to build the score.

## Why this node exists

A lender choosing between two applicants needs a single ranking that combines every
characteristic it holds on each of them, and a coefficient fitted to each
characteristic separately does not by itself say how they trade off against one
another. The scorecard's linear form combines them into one number, and credit
approval cut-offs need this score next, since a cut-off is only a threshold drawn
somewhere along the ranking this formula produces.
