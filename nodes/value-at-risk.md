---
id: value-at-risk
title: Value at risk
domains: [fin-eng, fin-man, stats]
status: drafted
requires: [market-risk]
spends: []
anchor: [assa.f107.7.5-2, ifoa.cm2.2.1-1, ifoa.sp5.7.7-1, ifoa.sp6.4.4-3, ifoa.sp9.5.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The value at risk of a portfolio at confidence level $\alpha$ is the smallest loss level
that the portfolio's loss is expected not to exceed over a given horizon with probability
$\alpha$; it is undefined for a loss distribution with no finite quantile at that level,
which a sufficiently heavy-tailed distribution can produce.

## The expression

$$
\mathrm{VaR}_\alpha(L) = \inf \{\, l : P(L \gt l) \le 1 - \alpha \,\}
$$

Here $L$ is the random loss over the chosen horizon, $l$ ranges over candidate loss
levels, and $\alpha$ is the confidence level at which the loss is not expected to be
exceeded. Value at risk is therefore a quantile of the loss distribution, read off at the
point where the exceedance probability falls to $1 - \alpha$.

## Why this node exists

A risk limit stated only as an expected loss says nothing about how bad a bad day can
get, and value at risk is the standard single number a trading desk or a regulator uses
to cap that tail. Its own construction, a single quantile with nothing said about the
loss beyond it, is exactly what weaknesses of value at risk goes on to examine.
