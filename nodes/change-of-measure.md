---
id: change-of-measure
title: Change of measure
domains: [fin-eng, stats]
status: drafted
requires: [radon-nikodym-derivative]
spends: []
anchor: [ifoa.sp6.3.3-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A change of measure replaces the probability measure an expectation is computed under with an
equivalent one, and Girsanov's theorem states exactly how a Brownian motion's drift changes
when the measure it is defined under is changed this way.

## The expression

$$
dW_t^{Q} = dW_t^{P} + \theta_t \, dt
$$

Here $W_t^{P}$ is a Brownian motion under the original measure $P$, $W_t^{Q}$ is a Brownian
motion under the new, equivalent measure $Q$, and $\theta_t$ is the market price of risk, the
process that absorbs the drift shift between the two measures. A process that carries drift
under $P$ can therefore be made driftless under $Q$ by choosing $\theta_t$ to cancel it
exactly.

## Why this node exists

A real-world price process drifts at whatever rate the market actually expects, but a pricing
argument needs the discounted price to be driftless so that today's price is simply an
expectation of tomorrow's payoff. Without a rule for how the driving Brownian motion itself
transforms, that risk-neutral drift could not be reached from the real-world model an
estimation exercise actually fits.
