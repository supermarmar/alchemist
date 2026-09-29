---
id: barrier-option
title: Barrier option
domains: [fin-eng]
status: drafted
requires: [option-payoff-profile]
spends: []
anchor: [ifoa.sp6.2.6-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A barrier option comes into existence, a knock-in, or ceases to exist, a
knock-out, once the underlying trades through a specified barrier level, so its
value depends on the whole price path rather than on the terminal price alone.

## The expression

$$
\text{Up-and-out call payoff} = \max(S_T - K, 0) \cdot \mathbb{1}\{\max_{0 \le t \le T} S_t \lt B\}
$$

Here $S_T$ is the terminal price, $K$ is the strike, $B$ is the barrier level, and
the indicator equals one only where the underlying never traded at or above $B$
during the option's life, in which case the ordinary call payoff is paid; it is
zero otherwise.

## Why this node exists

Because the payoff depends on whether the barrier was ever touched and not only on
where the underlying ends up, no formula built for a terminal-price payoff can
price it. Pricing a barrier option needs a method that tracks the whole path, such
as a lattice carrying an absorbing boundary at the barrier or a Monte Carlo
simulation that checks each simulated path against it.
