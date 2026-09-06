---
id: stochastic-gradient-descent
title: Stochastic gradient descent
domains: [ml]
status: stub
requires: [gradient-descent]
spends: []
anchor: [eth.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

Stochastic gradient descent replaces the exact gradient over a full training sample with a gradient computed on a small random mini-batch at every step, dividing training into epochs of such steps and trading a noisier direction for a far cheaper one. Adaptive variants such as Adam maintain a separate effective learning rate per parameter on top of this scheme, which is what a modern network training routine typically uses.
