---
id: smoothness-test
title: Smoothness test
domains: [life, stats]
status: drafted
requires: [graduation-rationale]
spends: []
anchor: [ifoa.cs2.4.5-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A smoothness test examines the higher order differences of a set of graduated rates, checking
that they progress steadily, as evidence that graduation has removed the sampling roughness
present in the crude data. It is judged separately from a test of
fit against a standard table, since a smooth set of rates need not fit the observed data well.

## The expression

$$
\Delta^3 q^g_x = q^g_{x+3} - 3 q^g_{x+2} + 3 q^g_{x+1} - q^g_x
$$

Here $q^g_x$ is the graduated rate at age $x$ and $\Delta^3 q^g_x$ is its third order
difference. A smooth graduation produces a sequence of these third differences that changes
sign only a few times and progresses without large jumps between consecutive ages; frequent
sign changes indicate that roughness from the crude data has survived into the graduated rates.

## Why this node exists

A graduation that fits the crude data well can still be too rough to use for pricing, since
sampling noise it has not smoothed out will feed directly into a reserve or a premium calculated
age by age. This node supplies the check that catches exactly that failure, applied after
graduation and before the graduated rates are accepted for use.
