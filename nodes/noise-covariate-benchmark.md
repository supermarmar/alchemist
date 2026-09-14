---
id: noise-covariate-benchmark
title: Noise covariate benchmark
domains: [ml, stats]
status: stub
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l09]
vault_articles: [methods/localglmnet]
vault_sources: []
taught_in: null
---

Adding a purely random, independent covariate to a design matrix supplies a benchmark for how much fluctuation in a fitted quantity is attributable to noise alone, which turns a variable importance ranking into a testable claim rather than an assertion. A term whose importance sits close to the noise covariate's own is a candidate for dropping, and one well clear of it is not.
