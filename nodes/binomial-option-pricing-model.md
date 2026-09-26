---
id: binomial-option-pricing-model
title: Binomial option pricing model
domains: [fin-eng]
status: drafted
requires: [arbitrage-and-hedging]
spends: []
anchor: [ifoa.cm2.5.2-1, ifoa.sp6.3.2, ifoa.sp6.3.2-1, up.wtw364.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The binomial option pricing model values an option by building a tree of possible underlying
prices over discrete steps, moving up or down by a fixed factor at each step, and working
backwards from the option's known payoff at expiry to its value today.

## The expression

$$
f_0 = e^{-r \Delta t} \bigl[ p \, f_u + (1 - p) \, f_d \bigr], \qquad
p = \frac{e^{r \Delta t} - d}{u - d}
$$

Here $f_0$ is the option's value at the start of the step, $f_u$ and $f_d$ are its values at
the end of the step after an up or a down move, $u$ and $d$ are the up and down factors the
underlying price is multiplied by, $r$ is the risk-free rate, $\Delta t$ is the length of the
step, and $p$ is the probability that makes the discounted underlying price a martingale
rather than the probability of an up move actually occurring. Stepping this recursion back
from expiry to today prices the whole tree.

## Why this node exists

An option's payoff at expiry is known, but its value today is not, and a market with no
arbitrage between the option and the underlying is what pins that value down to a single
number instead of a range. Extending a single step into many, and letting the number
of steps grow, is how the risk-neutral pricing measure this recursion already uses gets its
name and its continuous-time counterpart.
