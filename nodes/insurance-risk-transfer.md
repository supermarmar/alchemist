---
id: insurance-risk-transfer
title: Insurance risk transfer
domains: [eco, gi]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.2.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Insurance risk transfer is the pooling of many independent risks so that the loss
any one policyholder would otherwise bear alone is replaced by a small,
predictable contribution shared across the pool, reducing the relative
variability of the total outcome as the pool grows.

## The expression

$$
\mathrm{Var}\!\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{\sigma^2}{n}
$$

Here $X_i$ is the loss borne by the $i$-th of $n$ independent, identically
distributed risks in the pool, each with variance $\sigma^2$, and the left-hand
side is the variance of the average loss per policyholder once the pool absorbs
them collectively. As $n$ grows, this variance falls towards zero even though
$\sigma^2$ itself does not change.

## Why this node exists

A single household facing its own house fire alone must set aside the full
potential loss to be safe against it, which ties up far more capital than the
fire is likely to cost in any one year. Pooling lets an insurer hold capital
against the pool's much smaller variance instead, which is the arithmetic that
makes insurance viable as a business rather than a private saving scheme.
