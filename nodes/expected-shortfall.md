---
id: expected-shortfall
title: Expected shortfall
domains: [fin-eng, fin-man, stats]
status: drafted
requires: [value-at-risk]
spends: []
anchor: [assa.f107.7.7-2, ifoa.sp9.5.1-4]
vault_articles: [regulation/frtb-minimum-capital-market-risk]
vault_sources: []
taught_in: null
---

## Definition

Expected shortfall at a given confidence level is the average loss on those outcomes where
the loss already exceeds the Value at Risk threshold at that level, so it reports the
severity of a tail event that Value at Risk itself is silent about.

## The expression

$$
\mathrm{ES}_\alpha(L) = E\bigl[L \mid L > \mathrm{VaR}_\alpha(L)\bigr]
$$

Here $L$ is the loss on the portfolio, $\alpha$ is the confidence level, $\mathrm{VaR}_\alpha(L)$
is the Value at Risk at that level, the loss threshold exceeded with probability $1-\alpha$,
and $\mathrm{ES}_\alpha(L)$ is the conditional expectation of the loss given that it exceeds
that threshold. Because it averages over the whole tail, expected shortfall is a coherent risk measure in the technical sense that Value at
Risk fails to satisfy, since it respects subadditivity across a diversified portfolio.

## Why this node exists

Value at Risk answers how bad a loss must be to occur with a stated probability, but it says
nothing about how much worse that loss could be once the threshold is crossed, and two
portfolios with identical Value at Risk can carry very different tail severity. The
Fundamental Review of the Trading Book replaced Value at Risk with expected shortfall at 97.5
per cent confidence in the internal models approach precisely because that blindness to tail
severity had left the pre-crisis capital framework under-calibrated to genuinely severe
losses.
