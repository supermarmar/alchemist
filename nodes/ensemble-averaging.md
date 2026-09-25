---
id: ensemble-averaging
title: Ensemble averaging
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: [methods/entity-embedding-and-network-ensembling]
vault_sources: []
taught_in: null
---

## Definition

Ensemble averaging is the practice of fitting the same specification several times under
independent sources of randomness and averaging the resulting predictions. It reduces the
estimation variance of the average relative to a single fit and leaves any error the fits
share untouched, since averaging cannot cancel a bias every member carries alike.

## The expression

$$
\operatorname{Var}\left(\frac{1}{M}\sum_{m=1}^{M} \hat{y}_m\right) = \frac{\sigma^2}{M}
$$

Here $\hat{y}_m$ is the prediction from the $m$th independent fit, $M$ is the number of fits
averaged, and $\sigma^2$ is the variance each fit shares under the conditional independence
assumption. The variance of the average falls in inverse proportion to $M$, so the standard
deviation of the ensemble prediction falls with $\sqrt{M}$.

## Why this node exists

A network's fit depends on its random initialisation, its sample splits and its mini-batch
order, so a single trained network is one draw among infinitely many equally good ones on the
same data. Two analysts running an identical specification would otherwise price the same risk
differently, and ensemble averaging is what removes that instability without needing a better
model. Nagging, ensemble averaging applied specifically to neural network fits, needs this node
next.
