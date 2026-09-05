---
id: quasi-complete-separation
title: Quasi-complete separation
domains: [stats]
status: stub
requires: [glm]
spends: []
anchor: [eth.dl-actuarial-2026.l02, eth.dl-actuarial-2026.l12]
vault_articles: []
vault_sources: []
taught_in: null
---

Quasi-complete separation occurs where a covariate class contains no events of one outcome, so the maximum likelihood estimate for that class is driven towards an infinite log-odds and the fitting algorithm runs to its iteration limit without converging properly. It is the standard failure mode of maximum likelihood on sparse categorical data, and merging or classing the offending levels is the usual remedy.
