---
id: correlation-measures
title: Measures of correlation
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.1.2-2, ifoa.sp9.4.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A correlation measure summarises the strength and direction of association between two
variables in a single number, and the choice of measure depends on whether the
relationship of interest is linear or only monotonic.

## The expression

$$
r = \frac{\operatorname{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

$$
r_s = 1 - \frac{6\sum_{i=1}^{n} d_i^2}{n(n^2-1)}
$$

Here $r$ is Pearson's correlation coefficient, $\operatorname{Cov}(X,Y)$ is the
covariance between $X$ and $Y$, and $\sigma_X$ and $\sigma_Y$ are their standard
deviations; $r_s$ is Spearman's rank correlation, $n$ is the number of paired
observations, and $d_i$ is the difference between the ranks of the $i$th pair, so that
$r_s$ measures monotonic association even where the relationship between $X$ and $Y$
is not linear. Kendall's tau is a third such measure, built instead from the
proportion of concordant and discordant pairs.

## Why this node exists

A scatter plot that looks strongly related can still return a Pearson correlation near
zero wherever the relationship curves rather than runs in a straight line, and
Spearman's measure recovers the association in that case by working on ranks instead
of raw values. Choosing the measure that fits the relationship at hand is a
precondition for any inference drawn from it, since a hypothesis test built on the
wrong coefficient tests the wrong hypothesis.
