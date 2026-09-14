---
id: cold-start-problem
title: Cold start problem
domains: [credit, ml]
status: stub
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

A cold start arises where a model must price a segment, such as a new country or product, that has little or no default history of its own behind it in the training data. A pretrained prior or a retrieval mechanism can help where the new segment merely lacks data that resembles the rest of the book, but neither repairs a segment whose true risk level differs sharply from anything the model has seen, since retrieval measured in the model's own representation space tends to import the experience of segments the model considers similar rather than the segment's own.
