---
id: time-distributed-layer
title: Time-distributed layer
domains: [ml]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

A time-distributed layer applies one identical feed-forward network, with one shared set of weights, to every time slice or token of a sequence independently, so its parameter count does not grow with the sequence length. On its own it lets no two slices interact, which is what makes the attention layer that follows it the only place a sequence model can combine information across time or across tokens.
