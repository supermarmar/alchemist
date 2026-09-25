---
id: bootstrap-method
title: Bootstrap method
domains: [stats]
status: drafted
requires: [estimator-properties]
spends: []
anchor: [ifoa.cs1.3.1-6]
vault_articles: [methods/statistical-power-analysis]
vault_sources: []
taught_in: null
---

## Definition

The bootstrap estimates the sampling properties of an estimator by resampling with
replacement from the observed data itself, standing in for a theoretical sampling
distribution wherever one is unavailable or relies on an approximation that performs poorly
in finite samples.

## The expression

$$
\widehat{\mathrm{se}}_{\text{boot}} = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} \bigl(\hat{\theta}^{*}_b - \bar{\theta}^{*}\bigr)^2}
$$

Here $\hat{\theta}^{*}_b$ is the estimator recomputed on the $b$-th resample drawn with
replacement from the original data, $B$ is the number of resamples drawn, and
$\bar{\theta}^{*}$ is the mean of the $B$ resampled estimates. The resampled distribution of
$\hat{\theta}^{*}_b$ around $\bar{\theta}^{*}$ stands in for the true sampling distribution of
the estimator around the unknown parameter.

## Why this node exists

An estimator's standard error is what turns a single fitted number into a statement with
known uncertainty, but many statistics used in practice carry no clean analytical formula
for that uncertainty. A population stability index and an area under a curve are two
examples. A bootstrap confidence interval needs a resampled distribution settled before it
can turn it into an interval with a stated coverage.
