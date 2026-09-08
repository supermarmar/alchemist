---
id: layer-normalisation
title: Layer normalisation
domains: [ml]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

Layer normalisation standardises each time slice or token of a network's input across its own channels, using trainable scale and shift parameters, and depends on nothing outside that one slice. Because it carries no dependence on other members of a mini-batch, unlike batch normalisation, the transformation a given observation receives cannot depend on which other observations happened to share its batch.
