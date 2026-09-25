---
id: lognormal-security-price-model
title: Log-normal security price model
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.3.4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The log-normal security price model treats the logarithm of a security's future
price as normally distributed, so the price itself can never fall to zero or
below but has no upper bound.

## The expression

$$
\ln \frac{S_t}{S_0} \sim N\!\left(\left(\mu - \tfrac{1}{2}\sigma^2\right)t,\ \sigma^2 t\right)
$$

Here $S_0$ is the security's price now, $S_t$ is its price at a future time $t$,
$\mu$ is the continuously compounded expected rate of return, and $\sigma$ is the
volatility of that return. The variance term $\sigma^2 t$ grows with the horizon,
so uncertainty about the future price widens the further ahead $t$ is set.

## Why this node exists

Every closed-form option price and every simulated asset path in the corpus
starts from an assumption about how a security's future price is distributed, and
this is the assumption most of them make. It does not hold exactly: observed
returns show fatter tails and more volatility clustering than a constant $\sigma$
allows, and the standard treatment weighs the model's tractability against that
empirical shortfall rather than presenting it as settled.
