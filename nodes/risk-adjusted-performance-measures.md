---
id: risk-adjusted-performance-measures
title: Risk-adjusted performance measures
domains: [fin-eng, stats]
status: drafted
requires: [portfolio-risk-return-analysis]
spends: []
anchor: [ifoa.sp5.8.3-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Sharpe ratio measures a portfolio's excess return per unit of total risk taken, dividing
the return earned above the risk-free rate by the standard deviation of that return. It is
undefined for a portfolio whose return has zero variance, since a riskless portfolio has no
risk to divide by.

## The expression

$$
\mathrm{SR} = \frac{E[r_p] - r_f}{\sigma_p}
$$

Here $E[r_p]$ is the portfolio's expected return, $r_f$ is the risk-free rate, and $\sigma_p$
is the standard deviation of the portfolio's return, so $\mathrm{SR}$ is the reward earned per
unit of total volatility carried. The ratio penalises volatility from any source, so it treats a
portfolio's idiosyncratic risk the same as its systematic risk, a limitation a measure built on
beta alone is designed to avoid.

## Why this node exists

Knowing how much risk a holding contributes to a portfolio says nothing about whether the
return earned for that risk was adequate, and a risk-adjusted performance measure is what
converts a risk contribution into a verdict on performance. Without one, two managers earning
the same return cannot be compared once one of them took on materially more risk to earn it.
