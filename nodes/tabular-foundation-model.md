---
id: tabular-foundation-model
title: Tabular foundation model
domains: [ml]
status: stub
requires: [foundation-model]
spends: []
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

A tabular foundation model is pretrained across many synthetic tables rather than one real dataset, learning a cross-table prior over how tabular relationships tend to behave that it then reuses on a table it has never seen. The approach answers tabular data's resistance to the language and vision recipe, since a table's columns share no common vocabulary or grid across different datasets the way tokens and pixels do.
