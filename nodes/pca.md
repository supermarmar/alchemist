---
id: pca
title: Principal component analysis
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l03, ifoa.cs1.1.2-3, ifoa.cs2.5.1-6, up.wst311.5]
vault_articles: [methods/ols-predictor-importance]
vault_sources: []
taught_in: null
---

## Definition

Principal component analysis finds the linear direction of greatest variance in
a set of standardised predictors, then repeats the search in the subspace
orthogonal to every direction already found, giving the optimal linear
compression of the data at any chosen width.

## The expression

$$
\Sigma w_1 = \lambda_1 w_1, \qquad w_1 = \arg\max_{\lVert w \rVert = 1} w^{\mathsf{T}} \Sigma w
$$

Here $\Sigma$ is the covariance matrix of the standardised predictors, $w_1$ is
the leading eigenvector giving the first principal component's direction, and
$\lambda_1$ is its eigenvalue, equal to the variance the component captures.

## Why this node exists

Compressing a wide predictor set to a handful of components lets a model with
far fewer parameters than raw features still fit, at the cost of discarding
whatever variance the discarded components carried. The next node names the
reconstruction-discrimination gap, which asks whether that discarded variance
mattered to the task.
