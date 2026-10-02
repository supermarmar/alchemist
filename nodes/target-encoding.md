---
id: target-encoding
title: Target encoding
domains: [ml, stats]
status: drafted
requires: [categorical-encoding]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: [methods/target-based-encoding-lgd-ead]
vault_sources: []
taught_in: null
---

## Definition

Target encoding replaces each level of a categorical covariate with the mean of the response
variable observed on that level, compressing an arbitrarily large number of levels into a
single numerical column. Estimated on the same data the encoding is later evaluated on, it
leaks information invisibly, since an in-sample check cannot detect the resulting overstatement
of fit.

## The expression

$$
\bar{y}_k = \frac{1}{n_k} \sum_{i:\, x_i = k} y_i
$$

Here $x_i$ is the categorical covariate observed on row $i$, $y_i$ is that row's response, $k$
is one level the covariate can take, $n_k$ is the number of rows carrying level $k$, and
$\bar{y}_k$ is the mean response among them, the value every row at level $k$ is encoded to.

## Why this node exists

A one-hot encoding of a covariate with hundreds of levels produces hundreds of sparse columns a
model must then learn a coefficient for. Target encoding collapses that whole covariate into one
informative number. Weight of evidence needs this node next, as the log-odds variant of the same
target-driven construction built for a binary response.
