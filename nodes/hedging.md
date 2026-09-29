---
id: hedging
title: Hedging
domains: [fin-eng, fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f107.3.6-2, assa.f107.7.8-1, ifoa.sp9.6.3-1, ifoa.sp9.6.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Hedging is taking a position in one instrument that offsets the change in value
of an existing exposure, so that a loss on the exposure is compensated by a gain
on the hedge rather than eliminated by closing the exposure itself. A hedge is
judged by how closely its payoff tracks the exposure it offsets, not by whether
the two instruments are identical.

## The expression

$$
h^{*} = \rho\, \frac{\sigma_S}{\sigma_F}
$$

Here $h^*$ is the minimum-variance hedge ratio, the number of units of the
hedging instrument held per unit of the exposure, $\rho$ is the correlation
between changes in the value of the exposure and changes in the value of the
hedging instrument, $\sigma_S$ is the standard deviation of changes in the
exposure's value, and $\sigma_F$ is the standard deviation of changes in the
hedging instrument's value.

## Why this node exists

A hedge ratio below one is the signature of a hedge that tracks its exposure
imperfectly, and quantifying how far short of a perfect offset a given
instrument falls is the next question a hedging programme has to answer. Basis
risk in a hedging strategy needs it next, since it is exactly the residual risk
this ratio leaves unhedged.
