---
id: investment-guarantee-cost-methods
title: Investment guarantee cost methods
domains: [fin-eng, life]
status: drafted
requires: [embedded-options-and-guarantees, stochastic-versus-deterministic-modelling]
spends: []
anchor: [ifoa.sp2.4.3-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The cost of an investment guarantee is the present value of the shortfall the insurer must
make good if the underlying asset finishes below the guaranteed level, computed either as a
risk-neutral option value or as the average discounted shortfall across many simulated paths
of the underlying asset.

## The expression

$$
C_0 = E^{Q}\bigl[\, e^{-rT} \max(G - S_T, 0) \,\bigr]
$$

$$
\hat{C}_0 = \frac{1}{N} \sum_{k=1}^{N} e^{-rT} \max\bigl(G - S_T^{(k)}, 0\bigr)
$$

Here $G$ is the guaranteed level, $S_T$ is the underlying asset's value at the guarantee's
maturity $T$, $r$ is the risk-free rate, and $Q$ is the risk-neutral measure under which the
first, option-pricing expression is evaluated in closed form wherever $S_T$'s distribution
admits one. $N$ is the number of simulated paths, $S_T^{(k)}$ is the terminal asset value on
simulated path $k$, and $\hat{C}_0$ is the Monte Carlo estimator that approximates the same
quantity by averaging the discounted shortfall across those paths. Both expressions value the
same payoff, $\max(G - S_T, 0)$, which is a put option struck at $G$.

## Why this node exists

A guarantee written on a policy's maturity value creates an obligation only in the states
where the underlying asset falls short, and pricing that obligation at its expected shortfall
alone would understate the cost, since the guarantee is asymmetric: the insurer pays out below
$G$ and pays nothing above it. Recognising that payoff as a put option lets the insurer draw on
established option pricing theory wherever a closed form exists, and stochastic simulation
supplies the same figure wherever the guarantee's terms make no closed form available, which
between them cover every guarantee structure an insurer is likely to write.
