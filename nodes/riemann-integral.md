---
id: riemann-integral
title: Riemann integral
domains: [maths]
status: drafted
requires: [sequences-and-series]
spends: []
anchor: [up.wtw220.6, up.wtw310.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Riemann integral of a bounded function over a closed interval is the common limit of its upper and lower sums as the partition of the interval is refined without bound, where that limit exists and does not depend on how the interval is partitioned.

## The expression

$$
\int_a^b f(x)\,dx = \lim_{\lVert P \rVert \to 0} \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i
$$

Here $P = \{a = x_0 \lt x_1 \lt \cdots \lt x_n = b\}$ is a partition of $[a,b]$, $\Delta x_i = x_i - x_{i-1}$ is the width of the $i$-th subinterval, $x_i^*$ is any point chosen within it, and $\lVert P \rVert$ is the width of the partition's widest subinterval. The sum is a Riemann sum, and the integral is the value this sum converges to as $\lVert P \rVert \to 0$, whatever sequence of partitions and sample points is used.

## Why this node exists

A function's average value, the area beneath its graph and the total accumulated from a continuously varying rate are all quantities a finite sum can only approximate, and the Riemann integral is what makes that approximation exact in the limit. Every later construction that integrates over a continuous distribution, discounts a continuously paid cash flow, or accumulates a hazard into a survival probability rests on this limit already being well defined.
