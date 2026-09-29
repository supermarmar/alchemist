---
id: tracking-error
title: Tracking error
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.7.7-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Tracking error is the standard deviation of the difference between a portfolio's return and its
benchmark's return, measuring how closely the portfolio has followed the benchmark over a
sample of periods.

## The expression

$$
\mathrm{TE} = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (d_i - \bar{d})^2}, \qquad d_i = R_{p,i} - R_{b,i}
$$

Here $R_{p,i}$ and $R_{b,i}$ are the portfolio's and the benchmark's returns in period $i$,
$d_i$ is their difference, $\bar{d}$ is the mean of those differences over the $n$ periods
sampled, and $\mathrm{TE}$ is the sample standard deviation of $d_i$.

## Why this node exists

A portfolio manager mandated to follow a benchmark closely needs a single number that says how
far the portfolio has actually strayed from it, since the average of the return differences can
sit near zero even while individual periods swing widely either side. Portfolio risk
attribution needs it next, since decomposing where that tracking error came from requires the
aggregate figure to already be in hand.
