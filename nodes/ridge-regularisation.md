---
id: ridge-regularisation
title: Ridge regularisation
domains: [ml, stats]
status: drafted
requires: [regularisation]
spends:
  - {object: obj.coefficients, domain: ml}
  - {object: obj.coefficients, domain: stats}
  - {object: obj.regularisation, domain: ml}
  - {object: obj.regularisation, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Ridge regularisation penalises a fitting objective by the squared Euclidean norm of the coefficient vector, shrinking every coefficient towards zero without ever setting one exactly to zero. It reduces to the unpenalised fit where the penalty weight is zero.

## The expression

$$
\hat\theta = \arg\min_{\theta} \; \lVert y - X\theta \rVert^2 + \lambda_{\mathrm{reg}} \lVert \theta \rVert_2^2
$$

Here $y$ is the response vector, $X$ is the design matrix, $\theta$ is the coefficient vector, written $\beta$ in statistics, and $\lambda_{\mathrm{reg}}$ is the regularisation weight penalising the squared norm of $\theta$. Increasing $\lambda_{\mathrm{reg}}$ shrinks every fitted coefficient further towards zero, and setting it to zero recovers the unpenalised least-squares fit.

## Why this node exists

A design matrix with many collinear covariates leaves the unpenalised fit free to assign huge, offsetting coefficients to correlated columns, and the squared-norm penalty is what pulls that fit back to something stable without discarding any covariate outright. Elastic net needs it next, since it blends this squared-norm penalty with the absolute-value penalty that produces exact sparsity, combining the smooth shrinkage this page describes with a mechanism for dropping a covariate altogether.
