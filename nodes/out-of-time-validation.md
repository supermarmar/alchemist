---
id: out-of-time-validation
title: Out-of-time validation
domains: [credit, stats]
status: stub
requires: [out-of-sample-validation]
spends: []
anchor: [eth.dl-actuarial-2026.l02]
vault_articles: []
vault_sources: []
taught_in: null
---

An out-of-time validation split holds out the most recent cohorts rather than a random subset, so the test sample resembles the conditions a model will actually be scored under once deployed on business written after its development window. It exposes a vintage drift that a random split, which places every cohort on both sides of the partition, cannot reveal.
