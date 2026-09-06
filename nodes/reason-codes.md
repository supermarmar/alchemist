---
id: reason-codes
title: Reason codes
domains: [credit, regulation]
status: stub
requires: [localglmnet]
spends: []
anchor: [eth.dl-actuarial-2026.l09]
vault_articles: []
vault_sources: []
taught_in: null
---

Reason codes rank the covariates whose contribution to a declined applicant's score most exceeds the population average, giving an exact decomposition of the decision when the underlying model's prediction is itself a sum of per-covariate terms. Refitting the same architecture on the same data from a different random seed typically reproduces only the single leading reason reliably, so a policy issuing more than one code should draw its ranking from an ensemble and state how many codes it can actually defend.
