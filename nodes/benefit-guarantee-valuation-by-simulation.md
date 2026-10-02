---
id: benefit-guarantee-valuation-by-simulation
title: Benefit guarantee valuation by simulation
domains: [fin-eng, life]
status: drafted
requires: [binomial-option-pricing-model]
spends: []
anchor: [ifoa.cm2.4.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A benefit guarantee embedded in an insurance contract, such as a promise that the maturity
value will not fall below a stated floor, is valued by simulating the underlying asset many
times and averaging the discounted guarantee payoff across those simulated paths.

## The expression

$$
V_0 = e^{-rT}\,\frac{1}{N}\sum_{i=1}^{N} \max\bigl(G - S_i(T),\, 0\bigr)
$$

Here $V_0$ is the guarantee's value today, $r$ is the risk-free rate, $T$ is the guarantee's
maturity, $G$ is the guaranteed amount, $S_i(T)$ is the simulated value of the underlying asset
at maturity under the $i$th path, and $N$ is the number of simulated paths. The payoff is zero
wherever the asset outperforms the guarantee, so only the paths that breach the floor
contribute to the average.

## Why this node exists

A guarantee whose payoff depends on the whole distribution of maturity outcomes has no
closed-form price once the underlying benefit carries features, such as path-dependent
charges or a with-profits smoothing mechanism, that break the assumptions a Black-Scholes-style
formula needs. Simulation prices the guarantee by brute force instead, averaging a payoff that
a formula cannot capture, and every stochastic reserving and Solvency II internal model
calculation that follows depends on being able to run this kind of valuation reliably.
