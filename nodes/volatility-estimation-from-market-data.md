---
id: volatility-estimation-from-market-data
title: Estimating volatility from market data
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.4-4-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Historical volatility estimation measures the standard deviation of an asset's log
returns over a past window and annualises it to a rate comparable across horizons.

## The expression

$$
\hat\sigma = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (r_i-\bar r)^2} \times \sqrt{h}
$$

Here $r_i$ are the $n$ observed log returns over the sample period, $\bar r$ is
their mean, and $h$ is the number of return periods in a year, which converts the
sample standard deviation of a single period's return into an annualised rate.

## Why this node exists

An option pricing model needs a volatility figure before it can be run, and where
no liquid option market exists to read one out of quoted prices, this estimator is
the only route to a number at all. It gives a model builder a volatility for any
underlying with a price history, whether or not that underlying is ever traded
under an option contract.
