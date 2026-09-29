---
id: diversifiable-and-non-diversifiable-risk
title: Diversifiable and non-diversifiable risk
domains: [fin-eng, fin-man, stats]
status: drafted
requires: []
spends:
  - {object: obj.coefficients, domain: stats}
anchor: [ifoa.cm2.3.3-3, ifoa.cp1.3.2-2, ifoa.sp9.3.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An asset's total risk splits into a systematic component tied to common market factors and a
diversifiable component specific to the asset itself, and only the diversifiable component is
removed by holding a large, well diversified portfolio.

## The expression

$$
\sigma_i^2 = \beta_i^2 \sigma_m^2 + \sigma_{\varepsilon_i}^2
$$

Here $\sigma_i^2$ is the total variance of asset $i$'s return, $\beta_i$ is the coefficient
measuring the asset's sensitivity to the market return, $\sigma_m^2$ is the variance of the
market return, and $\sigma_{\varepsilon_i}^2$ is the variance of the asset-specific residual
that diversification removes.

## Why this node exists

A portfolio manager holding a single asset carries both components of its risk, and only once
the two are separated can a manager judge how much of that risk a bigger, better spread
portfolio would actually take away. Diversification benefit needs this split next, since it
quantifies the reduction that spreading exposure across many such assets achieves.
