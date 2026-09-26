---
id: credit-risk-modelling-approach
title: Credit risk modelling approach
domains: [credit, fin-eng]
status: drafted
requires: []
spends:
  - {object: obj.normal-cdf, domain: credit}
anchor: [ifoa.cm2.3.6-2]
vault_articles: [methods/structural-credit-risk-models]
vault_sources: []
taught_in: null
---

## Definition

A structural credit risk model treats default as occurring when a borrower's asset
value falls below the face value of its debt at the debt's maturity, so a default
probability is derived from the same lognormal asset-value process used to price the
borrower's equity as a call option on its assets.

## The expression

$$
PD = N(-d_2), \qquad d_2 = \frac{\ln(V_0/D) + \left(\mu - \tfrac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}
$$

Here $PD$ is the probability of default by time $T$, $N(\cdot)$ is the standard normal
distribution function, $V_0$ is the borrower's current asset value, $D$ is the face
value of its debt, $\mu$ is the expected return on the borrower's assets, $\sigma$ is
the volatility of that asset value, and $d_2$ is the borrower's distance to default,
measured in standard deviations.

## Why this node exists

A reduced-form model estimates a default intensity directly from observed spreads or
ratings without asking what happens inside the borrower, so it cannot explain why an
equity-heavy, low-leverage firm should default less often than an otherwise similar
firm funded mostly by debt. The structural approach supplies that mechanism, and the
Merton model needs it next, since it is the specific asset-value process this formula
assumes.
