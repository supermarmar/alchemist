---
id: black-model-interest-rate-derivatives
title: Black's model for interest rate derivatives
domains: [fin-eng]
status: drafted
requires: [interest-rate-cap-and-floor, swaption]
spends: []
anchor: [ifoa.sp6.3.6-3-1, ifoa.sp6.3.6-3-2, ifoa.sp6.3.6-3-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Black's model for interest rate derivatives prices a bond option, a cap or floor, and a
European swaption by treating the underlying forward rate or forward bond price as log-normal
at the option's expiry, and applying the Black-76 formula to that forward.

## The expression

$$
c = DF(T)\bigl[F\,\Phi(d_1) - K\,\Phi(d_2)\bigr], \qquad
d_{1,2} = \frac{\ln(F/K) \pm \tfrac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}
$$

Here $c$ is the price of a call on the forward, $DF(T)$ discounts from expiry $T$ back to
today, $F$ is the forward rate or forward bond price observed today, $K$ is the strike, $\sigma$
is the forward's volatility, and $\Phi(\cdot)$ is the standard normal distribution function. A
caplet, a floorlet and a European swaption each substitute their own forward and their own
day-count and annuity conventions into this same pair of expressions.

## Why this node exists

Black-Scholes prices an option on a traded asset, but a forward rate is not itself a traded
asset with a well-defined spot price and cost of carry, so pricing a rate option needs a model
built on the forward directly. The assumptions this substitution relies on, above all that a
single forward can be treated as log-normal in isolation from the rest of the curve, are
exactly what break down once the option's payoff depends on more than one point on that
curve. Assumptions underlying Black's model need it next, working through exactly which of
them fails and when.
