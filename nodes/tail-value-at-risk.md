---
id: tail-value-at-risk
title: Tail value at risk
domains: [fin-eng, fin-man, stats]
status: drafted
requires: [value-at-risk]
spends: []
anchor: [assa.f107.7.7-3, ifoa.cm2.2.1-1, ifoa.sp9.5.1-2]
vault_articles: [regulation/frtb-minimum-capital-market-risk]
vault_sources: []
taught_in: null
---

## Definition

Tail value at risk at confidence level $\alpha$ is the expected loss given that the loss
exceeds the value at risk at that level, so it summarises the severity of losses that value at
risk itself is silent on.

## The expression

$$
\mathrm{TVaR}_\alpha = E\bigl[L \mid L \gt \mathrm{VaR}_\alpha\bigr]
$$

Here $L$ is the portfolio's loss over the chosen horizon, $\mathrm{VaR}_\alpha$ is the value at
risk at confidence level $\alpha$, the loss threshold exceeded with probability $1-\alpha$, and
$\mathrm{TVaR}_\alpha$ is the average loss across that worst $1-\alpha$ proportion of outcomes.

## Why this node exists

Value at risk fixes a threshold loss but says nothing about how severe the losses beyond it
can get, so two portfolios that share the same value at risk can still carry very different
exposure to extreme outcomes. Tail value at risk answers that question directly, by averaging
over exactly the losses value at risk only bounds. Fat-tailed return distribution needs it
next, since a heavy tail is the case in which value at risk and tail value at risk diverge
most sharply.
