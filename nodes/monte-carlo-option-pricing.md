---
id: monte-carlo-option-pricing
title: Monte Carlo option pricing
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.5-1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Monte Carlo option pricing values a derivative by simulating many paths of the underlying
asset under the risk-neutral measure, computing the payoff on each path and averaging the
discounted result. It is especially suited to a payoff that depends on the whole path or on
several underlyings, where no closed-form valuation exists.

## The expression

$$
\hat{C} = e^{-rT} \frac{1}{N} \sum_{i=1}^{N} \text{payoff}\bigl(S^{(i)}\bigr)
$$

Here $\hat{C}$ is the simulated price estimate, $r$ is the risk-free rate, $T$ is the time to
expiry, $N$ is the number of simulated paths, and $S^{(i)}$ is the $i$th simulated path of the
underlying, drawn under the risk-neutral measure and fed into the payoff function. Averaging
over $N$ paths and discounting the average at $r$ gives an unbiased estimate whose standard
error shrinks with $\sqrt{N}$.

## Why this node exists

A payoff that looks back over a whole path, or that pays out only if a barrier is never
crossed, cannot generally be valued by an analytic formula, since the terminal value alone no
longer determines it. Simulating the path directly sidesteps that difficulty at the cost of
statistical rather than exact precision. Pricing American options needs this node next, since
an option exercisable before expiry requires deciding, path by path, when early exercise is
worth more than waiting.
