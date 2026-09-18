---
id: multiple-decrement
title: Multiple decrement
domains: [actuarial, credit, life, stats]
status: stub
requires: [life-table, multi-state-model, multiple-state-markov-model, survival-model]
spends: []
anchor: [ucsc.dl-actuarial-2026.l01, ifoa.cm1.3.5-1, ifoa.cm1.3.5-2, up.ias353.4]
vault_articles: [methods/credit-default-outcome-construction]
vault_sources: []
taught_in: null
---

A cohort leaves observation through more than one exit route, such as default and settlement for a loan book or death and withdrawal for a life table, and a survival probability computed from the combined decrement counts is only a default probability once the other exits are treated as independent censoring. Where that independence assumption fails, the decrements must be modelled as competing risks rather than folded together.
