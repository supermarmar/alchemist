---
id: relative-performance-risk
title: Relative performance risk
domains: [fin-eng, fin-man]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.4.1-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Relative performance risk is the risk that a portfolio's return departs from that
of a stated benchmark or peer group, which is a separate question from whether the
portfolio's absolute return is a loss. A portfolio can suffer material relative
performance risk while still returning a profit, provided the benchmark returned
more.

## The expression

$$
\sigma_{\text{TE}} = \sqrt{\operatorname{Var}(R_p - R_b)}
$$

Here $R_p$ is the portfolio's return, $R_b$ is the benchmark's return over the same
period, and $\sigma_{\text{TE}}$ is the tracking error, the standard deviation of
their difference. A tracking error of zero means the portfolio moves in lockstep
with the benchmark, and any positive value quantifies the relative performance
risk the portfolio carries against it.

## Why this node exists

A manager judged against a benchmark needs a single figure that separates
underperformance driven by active positioning from underperformance driven by a
market-wide fall the benchmark shared. Without tracking error, a portfolio that
fell less than its benchmark in a downturn and one that simply held less risk
throughout are indistinguishable from the return series alone, so a mandate's risk
budget is set against this figure rather than against absolute volatility.
