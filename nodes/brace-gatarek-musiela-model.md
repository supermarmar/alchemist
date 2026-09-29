---
id: brace-gatarek-musiela-model
title: Brace-Gatarek-Musiela model
domains: [fin-eng, stats]
status: drafted
requires: [heath-jarrow-morton-model]
spends: []
anchor: [ifoa.sp6.3.7-8, ifoa.sp6.3.7-9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Brace-Gatarek-Musiela model rewrites the Heath-Jarrow-Morton framework in terms of a
discrete set of observable forward Libor rates instead of the instantaneous forward rate the
original framework models directly, which keeps every modelled rate one an interest rate
market can actually quote.

## The expression

$$
dL_i(t) = \sigma_i(t) \, L_i(t) \, dW_i^{(i+1)}(t)
$$

Here $L_i(t)$ is the forward Libor rate for the accrual period ending at $t_{i+1}$, observed
at time $t$, $\sigma_i(t)$ is its instantaneous volatility, and $W_i^{(i+1)}(t)$ is a Brownian
motion under the forward measure associated with the bond maturing at $t_{i+1}$, the measure
under which $L_i$ carries no drift. Each forward Libor rate is driftless only under its own
forward measure, so pricing an instrument spanning several rates requires a single change of
measure to bring them all under one.

## Why this node exists

The instantaneous forward rate at the heart of the Heath-Jarrow-Morton framework is never
directly observed in a market, so a model built only from it cannot be calibrated to quoted
prices without an extra step. Writing the dynamics in terms of Libor rates that are quoted directly is what makes
calibrating the Brace-Gatarek-Musiela model with Black's model possible on caps and
swaptions.
