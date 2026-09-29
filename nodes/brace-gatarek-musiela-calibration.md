---
id: brace-gatarek-musiela-calibration
title: Calibrating the Brace-Gatarek-Musiela model with Black's model
domains: [fin-eng]
status: drafted
requires: [black-model-interest-rate-derivatives, brace-gatarek-musiela-model]
spends: []
anchor: [ifoa.sp6.3.7-10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Calibrating the Brace-Gatarek-Musiela model with Black's model sets each forward rate's
instantaneous volatility function so that the model reproduces the market's quoted Black
implied volatility for the corresponding caplet.

## The expression

$$
\frac{1}{T_i}\int_0^{T_i} \sigma_i(t)^2\, dt = \sigma_{\text{Black},i}^2
$$

Here $\sigma_i(t)$ is the Brace-Gatarek-Musiela model's instantaneous volatility for the
$i$-th forward Libor rate, $T_i$ is that rate's fixing date, and $\sigma_{\text{Black},i}$ is
the Black implied volatility quoted in the market for the caplet on the same rate. Choosing
$\sigma_i(t)$, often piecewise constant, so that its time average matches
$\sigma_{\text{Black},i}^2$ reproduces the caplet's market price exactly.

## Why this node exists

A caplet's price depends only on the volatility of its own single forward rate, so matching
that one number per rate is enough to calibrate every cap in the market exactly. A swaption's
price depends on a weighted combination of several forward rates moving together, so the same
volatility functions that reproduce every cap perfectly need not reproduce a swaption's market
price at the same time. That gap between the two calibration targets is the inconsistency the
Brace-Gatarek-Musiela model carries whenever caps and swaptions are calibrated from the same
volatility structure.
