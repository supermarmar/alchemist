---
id: entity-embedding
title: Entity embedding
domains: [ml]
status: stub
requires: [categorical-encoding]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: [methods/entity-embedding-and-network-ensembling]
vault_sources: []
taught_in: null
---

Entity embedding learns a dense, low-dimensional vector per level of a categorical covariate, trained jointly with the rest of the model, rather than fixing the encoding in advance. It saves parameters at high cardinality and places every covariate in a common vector space, though a level's learned position need not reflect its similarity in outcome to another level once the following layers have room to absorb that structure.
