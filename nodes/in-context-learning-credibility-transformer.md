---
id: in-context-learning-credibility-transformer
title: In-context learning credibility transformer
domains: [credit, ml]
status: stub
requires: [credibility-transformer, identity-initialisation, in-context-learning]
spends: []
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

The in-context learning credibility transformer retrieves similar borrowers' observed outcomes at prediction time and blends them with a target borrower's own representation through a causally masked attention layer, extending the credibility transformer's architecture with a retrieval step rather than relying only on what was learned during fitting. Where the retrieved neighbourhood is diluted or searched in a space that already encodes the base model's own prediction, the retrieved context can end up correlating strongly with what the base model already says, adding little accuracy while leaving the model's own explanations largely undisturbed.
