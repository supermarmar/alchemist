---
id: equilibrium-versus-no-arbitrage-interest-rate-models
title: Equilibrium versus no-arbitrage interest rate models
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.7-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An equilibrium interest rate model derives the term structure from assumed economic dynamics with
fixed parameters, and the curve it produces need not match today's observed market curve exactly.
A no-arbitrage model instead lets one of its parameters vary with time and chooses that
time-dependent function so the model's curve is calibrated to fit the observed curve by
construction.

## The expression

$$
dr_t = a\bigl[\theta(t) - r_t\bigr]\,dt + \sigma\,dW_t
$$

Here $r_t$ is the short rate, $a$ is the speed of mean reversion, $\sigma$ is the volatility, and
$W_t$ is a Wiener process. The model is an equilibrium model, such as Vasicek's, when $\theta(t)$
is held constant at a fixed long-run level $b$, and it becomes a no-arbitrage model, such as
Hull-White's, once $\theta(t)$ is instead chosen as a function of time that forces the model's
curve to reproduce today's observed one.

## Why this node exists

A model priced off assumed dynamics alone can misprice a bond the market already trades, since
nothing forces its curve to agree with the one actually observed today, and that mismatch is
exactly what a no-arbitrage model's time-dependent drift is built to remove. Which family suits a
given task depends on whether the model is being used to price instruments consistently with
today's market or to explore the economic behaviour of rates over time.
