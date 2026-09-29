---
id: cameron-martin-girsanov-theorem
title: Cameron-Martin-Girsanov theorem
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.3-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Cameron-Martin-Girsanov theorem gives the conditions under which changing the probability measure removes the drift from a Brownian motion, so that a process which is Brownian motion with drift under one measure becomes a standard, driftless Brownian motion under the new one.

## The expression

$$
\left.\frac{dQ}{dP}\right|_{\mathcal F_t} = \exp\left(-\int_0^t \theta_s \, dW_s - \frac{1}{2}\int_0^t \theta_s^2 \, ds\right)
$$

Here $dQ/dP$ restricted to the information available at $t$ is the Radon-Nikodym derivative defining the new measure $Q$ in terms of the original measure $P$, $\theta_s$ is the drift being removed, and $W_s$ is the Brownian motion under $P$. Under $Q$, the process $W_s + \int_0^s \theta_u \, du$ is a standard Brownian motion.

## Why this node exists

Pricing a derivative under the risk-neutral measure requires moving from the real-world drift an asset actually earns to the risk-free drift the no-arbitrage argument demands, and that move is a change of measure. Without this theorem, discarding a drift by changing the measure would have no formal justification, so every risk-neutral valuation in this corpus rests on a change of measure this theorem licenses.
