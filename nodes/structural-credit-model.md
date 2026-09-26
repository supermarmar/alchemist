---
id: structural-credit-model
title: Structural credit model
domains: [credit, stats]
status: drafted
requires: []
spends:
  - {object: obj.normal-cdf, domain: credit}
anchor: [assa.f107.6.2-1-2]
vault_articles: [methods/structural-credit-risk-models]
vault_sources: []
taught_in: null
---

## Definition

A structural credit model treats a firm's default as the event that its asset value falls
below its liabilities, and derives the firm's default probability from the dynamics of that
asset value rather than from a fitted default rate.

## The expression

$$
\mathrm{PD} = N(-d_2), \qquad d_2 = \frac{\ln(V_0 / D) + (\mu - \sigma^2/2)T}{\sigma\sqrt{T}}
$$

Here $V_0$ is the firm's current asset value, $D$ is the face value of its debt falling due at
horizon $T$, $\mu$ and $\sigma$ are the drift and volatility of the firm's asset returns, and
$N(\cdot)$ is the standard normal distribution function. $\mathrm{PD}$ is the probability that
asset value has fallen below the debt's face value by $T$, in Merton's original construction of
equity as a call option on the firm's assets.

## Why this node exists

A model fitted only to observed default rates cannot say why a firm's default probability moved,
whereas a structural model attributes that movement to a balance-sheet change, a fall in asset
value or a rise in its volatility, which is what makes it useful for stress testing and for
attributing a credit spread to its economic drivers. The model's demand on continuous trading and
on asset value following a diffusion with no jumps is also where it is most often challenged,
since a firm whose asset value can jump can default in ways the model cannot represent.
