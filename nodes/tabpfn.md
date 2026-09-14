---
id: tabpfn
title: TabPFN
domains: [ml]
status: stub
requires: [in-context-learning, tabular-foundation-model]
spends: []
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

TabPFN approximates Bayesian posterior predictive inference in a single forward pass, learning during pretraining to map a context dataset and a query directly to a predictive distribution rather than fitting parameters to that context at prediction time. Consequently there is no fitted parameter vector for a lender to document, monitor or re-estimate, even though the context dataset still determines the prediction completely.
