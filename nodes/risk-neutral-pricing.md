---
id: risk-neutral-pricing
title: Risk-neutral pricing
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [assa.f107.5.5-4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risk-neutral pricing values a derivative as the discounted expectation of its
payoff, taken under a probability measure in which every traded asset earns the
risk-free rate. The measure is a pricing device rather than a claim about the
market's actual view of the odds, so it need not match the real-world probabilities
an investor would assign to the same outcomes.

## The expression

$$
V_0 = e^{-rT}\, E^{\mathbb{Q}}[\,X_T\,]
$$

Here $V_0$ is the derivative's value today, $r$ is the risk-free rate, $T$ is the
time to the payoff, $X_T$ is the payoff at $T$, and $E^{\mathbb{Q}}$ is expectation
under the risk-neutral measure $\mathbb{Q}$, the measure under which every asset's
discounted price is a martingale.

## Why this node exists

A derivative's value cannot be pinned down by its expected payoff under the
real-world measure alone, since two investors with different views of the odds
would then disagree on price, and no traded instrument can have two prices at
once. Option pricing and dynamic hedging needs this node next, since an option's
price is exactly this expectation evaluated against the option's own payoff
function.
