---
id: cls-token
title: CLS token
domains: [ml]
status: stub
requires: [attention-mechanism, feature-tokenisation]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

A CLS token is a special, randomly initialised token appended to a tokenised sequence, carrying no information of its own before an attention layer runs, so that after the layer its row has attended to every other token and can be read out as a representation of the whole input. Borrowed from language-model pretraining, it lets a variable-length or unordered set of tokens be summarised into one fixed-size vector for a downstream prediction.
