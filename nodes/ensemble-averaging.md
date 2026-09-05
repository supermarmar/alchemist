---
id: ensemble-averaging
title: Ensemble averaging
domains: [ml, stats]
status: stub
requires: []
spends: []
anchor: [eth.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Averaging several conditionally independent and identically distributed predictors shrinks the standard deviation of the average in proportion to the inverse square root of their number, which is a statement about variance alone and says nothing about bias. Where every member of the ensemble shares the same systematic error, averaging leaves that shared error untouched even as it removes the noise that varies from member to member.
