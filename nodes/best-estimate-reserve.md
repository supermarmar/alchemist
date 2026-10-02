---
id: best-estimate-reserve
title: Best estimate reserve
domains: [gi]
status: drafted
requires: [reserving-basis]
spends: []
anchor: [ifoa.sp7.3.6-1]
vault_articles: [regulation/solvency-ii-technical-provisions]
vault_sources: []
taught_in: null
---

## Definition

The best estimate reserve is the actuary's unbiased estimate of the mean of the
probability-weighted range of possible outcomes for a liability, discounted where the
valuation basis requires it, and carrying no deliberate margin for prudence or optimism.

## The expression

$$
\mathrm{BE} = \sum_{t} v^t\, E[CF_t]
$$

Here $CF_t$ is the net cash flow the liability is expected to generate at future time $t$,
$E[CF_t]$ is its probability-weighted mean under the reserving basis, $v^t$ is the discount
factor applied to a cash flow due at time $t$, and $\mathrm{BE}$ is the sum of these discounted
expected cash flows across every future period the liability could still generate one.

## Why this node exists

A single mean figure says nothing about how wide the range of outcomes around it actually is,
and a reserve set only at the mean gives no sense of how likely it is to prove too low.
Reserve range estimation needs this node next, since the best estimate is the central figure
that range is built around, whether the range itself comes from a percentile of a stochastic
model or from a scenario-based spread of deterministic assumptions.
