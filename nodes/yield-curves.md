---
id: yield-curves
title: Yield curves
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [assa.f107.7.1-1-2, ifoa.sp6.3.6-1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A yield curve is the function relating the annualised yield on a zero-coupon bond
to its maturity, read off the market prices of instruments trading at each
maturity along the curve.

## The expression

$$
P(t) = (1+y(t))^{-t}
$$

Here $P(t)$ is the price today of a zero-coupon bond maturing at $t$, and $y(t)$ is
the spot yield the curve assigns to that maturity. Reading the curve at a given $t$
therefore fixes the rate at which a unit payment due at $t$ is discounted back to
today.

## Why this node exists

A bank's interest rate risk position is exposed to shifts in level and shape along
the whole curve, so no such position can be measured until the curve itself has a
functional form to shift. Interbank rates needs it next, since an interbank rate is
the yield curve read at the short maturities interbank lending actually trades at.
