---
id: regularisation
title: Regularisation
domains: [ml, stats]
status: drafted
requires: [bias-variance-tradeoff]
spends:
  - {object: obj.regularisation, domain: ml}
  - {object: obj.regularisation, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l08, ifoa.cs2.5.1-3, up.wst212.8, up.wst311.10]
vault_articles: [methods/icenet-smoothness-and-monotonicity-constraints]
vault_sources: []
taught_in: null
---

## Definition

Regularisation adds a penalty on the parameter vector to a model's fitting objective, trading a
small increase in training loss for a model that is smoother, sparser or otherwise simpler than
the unconstrained fit. The penalty weight controls how much simplicity is bought at that cost,
and the intercept is conventionally excluded from the penalty so that the fitted overall level
is not itself shrunk.

## The expression

$$
L_{\mathrm{pen}}(\beta) = L(\beta) + \lambda_{\mathrm{reg}} \sum_j |\beta_j|^p
$$

Here $L(\beta)$ is the unpenalised training loss as a function of the coefficient vector
$\beta$, $\lambda_{\mathrm{reg}}$ is the regularisation weight, and $p$ selects the penalty's
shape: $p=2$ gives the ridge penalty, which shrinks every coefficient towards zero without
reaching it, and $p=1$ gives the LASSO penalty, whose non-differentiability at the origin sets
some coefficients exactly to zero.

## Why this node exists

Bias and variance move in opposite directions as a model grows more flexible, and a penalty on
the coefficients is the mechanism that pulls a fit back from the variance side of that trade-off
without changing the model class itself. Ridge regularisation needs this node next, fixing
$p=2$ in the penalty this node defines and working through the shrinkage that choice produces.
