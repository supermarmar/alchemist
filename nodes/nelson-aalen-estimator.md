---
id: nelson-aalen-estimator
title: Nelson-Aalen estimator
domains: [life, stats]
status: stub
requires: [censoring, hazard-rate]
spends: []
anchor: [ifoa.cs2.4.2-4]
vault_articles: []
vault_sources: []
taught_in: null
---

An estimator of the cumulative hazard rate in the presence of censoring, built as a running sum of the ratio of observed events to individuals at risk at each event time. It is computed from the same censored data as the Kaplan-Meier estimator and carries its own estimate of variance.
