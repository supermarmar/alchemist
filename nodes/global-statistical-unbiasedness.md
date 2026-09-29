---
id: global-statistical-unbiasedness
title: Global statistical unbiasedness
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l07]
vault_articles: [concepts/balance-property-and-auto-calibration]
vault_sources: []
taught_in: null
---

## Definition

A fitting procedure is globally statistically unbiased if the expected value of its prediction on a
fresh observation, drawn independently of the sample it was fitted on, equals the expected value
of that observation's own response. The expectation runs over data the procedure has never seen,
so the property describes the fitting procedure itself and cannot be verified from a single
dataset.

## The expression

$$
E\bigl[\hat{Y}\bigr] = E[Y]
$$

Here $Y$ is a fresh response drawn independently of the training sample, $\hat{Y}$ is the fitting
procedure's prediction for it, and the equality states that the two share the same expectation
taken over repeated resampling. The in-sample counterpart, the balance property, checks the same
idea within a single realised sample, where the exposure-weighted predictions and the observed
claims must sum to the same total.

## Why this node exists

A model can reproduce a portfolio's total claims exactly while still overcharging one group to
subsidise another, and the two failures are distinguishable only once unbiasedness at the
portfolio level is separated from the checkable in-sample balance property. Verifying the property
directly needs the true mean and the ability to resample, which is why validation in practice
falls back on the balance property as its checkable proxy.
