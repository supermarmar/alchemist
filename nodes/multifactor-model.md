---
id: multifactor-model
title: Multifactor model
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.3.3-1, ifoa.cm2.3.3-4, ifoa.cm2.3.3-5, ifoa.sp5.7.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A multifactor model explains an asset's return from its sensitivity to several sources of
systematic risk, with a residual left over that is specific to the asset and uncorrelated
with every factor.

## The expression

$$
R_i = \alpha_i + \sum_{k=1}^{K} \beta_{ik} F_k + \varepsilon_i
$$

Here $R_i$ is the return on asset $i$, $\alpha_i$ is the intercept the factors leave
unexplained, $F_k$ is the return on the $k$th of $K$ systematic factors, $\beta_{ik}$ is asset
$i$'s sensitivity to factor $k$, and $\varepsilon_i$ is the idiosyncratic residual, assumed
uncorrelated across assets and with every $F_k$. Macroeconomic, fundamental, and statistical
factor models differ only in where the $F_k$ come from: an observed economic series, a firm
characteristic such as size or value, or a statistically extracted component.

## Why this node exists

A model that explains return through a single factor cannot separate two assets that move
together for different reasons, one through a shared exposure to interest rates and another
through a shared exposure to oil prices. By contrast, allowing several factors at once
recovers that distinction and lets a portfolio's risk be decomposed factor by factor. The
single-index model needs this node next, since it is the special case reached by collapsing
every factor here into one.
