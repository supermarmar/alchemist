---
id: standardised-approach-market-risk
title: Standardised approach for market risk
domains: [fin-eng, regulation]
status: drafted
requires: [market-risk]
spends: []
anchor: [assa.f107.7.6-1]
vault_articles: [regulation/frtb-minimum-capital-market-risk]
vault_sources: []
taught_in: null
---

## Definition

The standardised approach for market risk sums a set of prescribed risk-factor charges to
produce a capital requirement, without relying on a bank's own internal model. Its
sensitivities-based method is the core of the three components the approach comprises.

## The expression

$$
K_b = \sqrt{\max\Bigl(0,\ \sum_k WS_k^2 + \sum_{k \ne l} \rho_{kl}\, WS_k\, WS_l\Bigr)}
$$

Here $WS_k$ is the weighted sensitivity of the trading book to risk factor $k$ within bucket
$b$, $\rho_{kl}$ is the regulator-prescribed correlation between risk factors $k$ and $l$ in the
same bucket, and $K_b$ is the bucket's own capital charge, aggregated across every bucket and
risk class to give the sensitivities-based method's total. The $\max$ against zero guards
against a negative sum, which a low correlation assumption can otherwise produce.

## Why this node exists

A bank without approval to run an internal expected shortfall model still needs a market risk
capital figure, and the standardised approach builds one from sensitivities the bank must
compute in any case for its own risk management. The fundamental review of the trading book
needs this node next, setting this standardised charge alongside the internal models approach
it exists to fall back from.
