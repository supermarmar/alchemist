---
id: standardisation
title: Standardisation
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l06, ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Standardisation rescales a covariate to mean zero and unit variance, using the mean and
standard deviation estimated on the training data alone.

## The expression

$$
z_j = \frac{x_j - \bar{x}_j}{s_j}
$$

Here $x_j$ is a covariate's raw value, $\bar{x}_j$ and $s_j$ are its sample mean and sample
standard deviation as estimated on the training set, and $z_j$ is the standardised value passed
to the model.

## Why this node exists

A gradient-based fitting routine shares one learning rate across every covariate, so a
covariate that sits on a naturally large scale, a monetary balance next to a binary flag, would
dominate the gradient and either destabilise the update or force the learning rate down for
every other covariate. Standardising every covariate onto a common scale before fitting removes
that dependence on units. A heavy-tailed monetary covariate can still dominate the standardised
design matrix even after this rescaling, which is why a logarithmic transform or censoring is
usually applied before it rather than instead of it.
