---
id: lasso-regularisation
title: Lasso regularisation
domains: [ml, stats]
status: drafted
requires: [regularisation]
spends:
  - {object: obj.coefficients, domain: stats}
  - {object: obj.regularisation, domain: ml}
  - {object: obj.regularisation, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: [methods/icenet-smoothness-and-monotonicity-constraints]
vault_sources: []
taught_in: null
---

## Definition

Lasso regularisation fits a model by minimising its ordinary loss plus a penalty on the sum of
the absolute values of its coefficients, which can drive an individual coefficient to exactly
zero once the penalty weight is high enough.

## The expression

$$
\hat{\beta} = \arg\min_{\beta} \left\{ L(\beta) + \lambda_{\mathrm{reg}} \sum_{j=1}^{p} |\beta_j| \right\}
$$

Here $L(\beta)$ is the model's ordinary training loss, $\beta_j$ is the coefficient on the
$j$-th of $p$ covariates, $\lambda_{\mathrm{reg}}$ is the penalty weight controlling how
strongly the coefficients are shrunk, and $\hat{\beta}$ is the fitted coefficient vector once
the penalised objective is minimised. The intercept is excluded from the sum, since penalising
it would bias the fitted model's overall level. The penalty's non-differentiability at the
origin is what lets rising $\lambda_{\mathrm{reg}}$ send individual coefficients to exactly
zero, which is where lasso's variable selection comes from.

## Why this node exists

A model fitted with many covariates and limited data can overfit by spreading small, unstable
coefficients across variables that add little genuine signal, and a plain L2 penalty shrinks
every coefficient toward zero without ever setting one to exactly zero. Lasso's L1 penalty
supplies that missing mechanism, turning the penalty weight into a single control that both
regularises the fit and selects which covariates the model keeps. The elastic net needs it
next, since it combines lasso's sparsity with the L2 penalty's own stability where lasso alone
proves unstable.
