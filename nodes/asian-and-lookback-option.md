---
id: asian-and-lookback-option
title: Asian and lookback options
domains: [fin-eng]
status: drafted
requires: [option-payoff-profile]
spends: []
anchor: [ifoa.sp6.2.6-5, ifoa.sp6.2.6-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An Asian option's payoff depends on the underlying's average price over the
option's life, and a lookback option's payoff depends on the highest or lowest
price the underlying reaches, so neither can be priced from the terminal price
alone.

## The expression

$$
\text{Asian call payoff} = \max(\bar S - K, 0), \qquad \bar S = \frac{1}{n}\sum_{i=1}^n S_{t_i}
$$

$$
\text{Lookback call payoff} = S_T - \min_{t \le T} S_t
$$

Here $S_{t_i}$ are the underlying's prices at the $n$ averaging dates, $K$ is the
strike, $\bar S$ is their average, $S_T$ is the terminal price, and
$\min_{t \le T} S_t$ is the lowest price reached over the option's life.

## Why this node exists

Both payoffs depend on the whole price path rather than on the terminal price
alone, so neither a lattice built for a European or American payoff nor a
closed-form terminal-price formula can be applied unchanged. A path-dependent
method, such as a Monte Carlo simulation over the full path, is what these two
option types force into the pricing toolkit.
