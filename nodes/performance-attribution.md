---
id: performance-attribution
title: Performance attribution
domains: [fin-eng, fin-man]
status: drafted
requires: [portfolio-risk-return-analysis]
spends: []
anchor: [ifoa.sp5.8.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Performance attribution decomposes the excess return a portfolio earned over its benchmark into
the part contributed by choosing which sectors to overweight or underweight and the part
contributed by choosing which individual stocks to hold within each sector. The two effects are
additive, so together they account for the whole of the portfolio's relative return.

## The expression

$$
R_p - R_b = \sum_i (w_{p,i} - w_{b,i})(r_{b,i} - R_b) + \sum_i w_{p,i}(r_{p,i} - r_{b,i})
$$

Here $R_p$ and $R_b$ are the portfolio's and benchmark's total returns, $w_{p,i}$ and $w_{b,i}$
are the portfolio's and benchmark's weights in sector $i$, and $r_{p,i}$ and $r_{b,i}$ are the
portfolio's and benchmark's returns within sector $i$. The first term is the sector selection
effect, earned by over- or underweighting a sector against the benchmark, and the second is the
stock selection effect, earned by outperforming the benchmark's own return within a sector
actually held.

## Why this node exists

A portfolio manager who knows only the total excess return earned cannot tell whether it came
from calling the sector cycle correctly or from picking the right names inside a sector, and the
two skills are judged, and rewarded, separately. Without the split, a mandate cannot distinguish
a sector call from a stock call, and the fee a client pays for each is rarely the same.
