---
id: causal-masking
title: Causal masking
domains: [credit, ml]
status: stub
requires: [attention-mechanism]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

A causal mask forces an attention layer's weights for any later position onto zero when they would otherwise fall on an earlier position, so an element at one point in a sequence can attend only to itself and to what came before it. On a monthly behavioural panel it is a leakage control rather than a technicality, since an unmasked model scoring an early month has in fact seen every later statement too.
