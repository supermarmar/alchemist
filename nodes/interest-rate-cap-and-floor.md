---
id: interest-rate-cap-and-floor
title: Interest rate cap and floor
domains: [fin-eng]
status: drafted
requires: [interest-rate-swap]
spends: []
anchor: [ifoa.sp6.2.5-12, ifoa.sp6.2.5-13, ifoa.sp6.3.6-3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A cap is a strip of caplets, each paying the excess of a floating rate over a fixed strike for
one period, and a floor is the mirror strip paying the shortfall of the floating rate below the
strike. A caplet is degenerate once the floating rate is fixed below the strike throughout its
life, where it pays nothing.

## The expression

$$
\text{caplet payoff} = N \tau \max(f - K, 0)
$$

Here $N$ is the notional principal, $\tau$ is the period's length expressed as a fraction of a
year, $f$ is the floating rate observed for that period, and $K$ is the strike rate fixed at
outset. A floor's corresponding payoff replaces $\max(f - K, 0)$ with $\max(K - f, 0)$, and a
cap or a floor's value is the sum of its caplets' or floorlets' discounted expected payoffs.

## Why this node exists

A borrower on a floating-rate loan who buys a cap limits the rate paid without giving up the
benefit of a rate fall, which a swap into a fixed rate would give up. Black's model for interest
rate derivatives needs it next, since it supplies the pricing formula that values a caplet under
a lognormal assumption for the forward rate.
