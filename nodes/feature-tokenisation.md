---
id: feature-tokenisation
title: Feature tokenisation
domains: [ml]
status: stub
requires: [entity-embedding]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

Feature tokenisation places every covariate of a tabular row into a common vector space, a categorical covariate through an entity embedding and a continuous covariate through a small network of its own, so the covariate list becomes a sequence an attention layer can run over. Manufacturing a sequence this way lets attention learn which characteristics should modify the reading of which others, on data that carries no natural order of its own.
