---
id: frequency-severity-modelling-banking
title: Frequency and severity modelling for credit and operational risk
domains: [credit, stats]
status: drafted
requires: []
spends: []
anchor: [assa.f107.3.5-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Frequency and severity modelling treats a portfolio's aggregate loss as the sum of a random number
of individual losses, each drawn from its own severity distribution, and models how often losses
occur separately from how large each one is. Applied to a bank's book, the same structure prices
credit losses as defaults times loss given default and operational losses as event counts times
loss amounts.

## The expression

$$
S = \sum_{i=1}^{N} X_i, \qquad E[S] = E[N]\,E[X]
$$

Here $N$ is the random number of loss events, $X_i$ is the severity of the $i$th event, $S$ is the
aggregate loss the two combine into, and the second equality holds whenever $N$ and the severities
are independent of one another. $E[N]$ is the frequency and $E[X]$ is the mean severity, so the
expected aggregate loss factorises into the two components the modelling separates.

## Why this node exists

A single distribution fitted to aggregate losses conflates a rise in how often losses occur with a
rise in how large they are, and the two drivers behave differently under stress, which a combined
model cannot distinguish. Splitting frequency from severity is the consequence this node exists to
enable, since each component can then be modelled, and stressed, on its own terms.
