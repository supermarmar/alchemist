---
id: multi-head-attention
title: Multi-head attention
domains: [ml]
status: stub
requires: [attention-mechanism]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

Multi-head attention runs several independent attention heads in parallel, each with its own query, key and value parameters, and recombines their outputs through a further learned projection. Running several heads lets the layer attend to different kinds of relationship at once, at the cost that no single head's attention weights can then be read as the model's one credibility or importance measure.
