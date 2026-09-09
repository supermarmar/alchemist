---
id: attention-mechanism
title: Attention mechanism
domains: [ml]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

An attention layer equips every element of a sequence with a query, a key and a value vector, then computes each element's output as a weighted average of every element's value, with the weights set by how closely each key matches the querying element's own query. The mechanism lets any two elements of a sequence interact directly, however far apart they sit, which recurrence and convolution cannot do without many intervening steps.
