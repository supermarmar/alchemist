---
id: tail-risk-management
title: Tail risk management
domains: [actuarial, fin-man, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cp1.4.7-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Tail risk management addresses losses that occur with low probability but high severity,
using measures that summarise the far end of the loss distribution instead of its centre.

## The expression

$$
\mathrm{ES}_\alpha = E\bigl[L \mid L \gt \mathrm{VaR}_\alpha\bigr]
$$

Here $L$ is the loss on a portfolio or a business over a stated horizon, $\mathrm{VaR}_\alpha$
is the loss that is exceeded with probability $1 - \alpha$, and $\mathrm{ES}_\alpha$, the
expected shortfall, is the average loss conditional on that threshold being breached.

## Why this node exists

A risk measure built around the mean and the standard deviation of a loss distribution
describes its ordinary behaviour but says nothing about how bad the worst outcomes are once
they occur, and $\mathrm{VaR}$ alone stops at the threshold without saying how far beyond it
losses can run. Expected shortfall answers that question directly, which is why it, rather than
$\mathrm{VaR}$ alone, has become the standard basis for setting capital and liquidity buffers
against low-probability, high-impact events.
