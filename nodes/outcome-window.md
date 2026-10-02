---
id: outcome-window
title: Outcome window
domains: [credit]
status: drafted
requires: [definition-of-default]
spends: []
anchor: [ucsc.dl-actuarial-2026.l01]
vault_articles: [methods/credit-default-outcome-construction]
vault_sources: []
taught_in: null
---

## Definition

A fixed-horizon outcome window turns a loan's continuous time to default into a single binary
flag, by asking whether default occurs within a stated number of months of origination. The
flag is a worst-ever aggregation: a loan that breaches the default definition and later cures
within the window still scores as a default.

## The expression

$$
y_i = \max_{1 \le m \le k} \mathbf{1}\{\text{default}_i(m)\}
$$

Here $y_i$ is loan $i$'s outcome flag, $k$ is the outcome window's length in months,
$\text{default}_i(m)$ is the monthly default indicator for loan $i$ at month $m$ on book, and
$\mathbf{1}\{\cdot\}$ is the indicator function, taking the value one where its argument holds
and zero otherwise. Only loans with at least $k$ months of observation behind them can be scored
this way, since a younger loan has not yet had the chance to breach the window.

## Why this node exists

Without a fixed window, two loans reaching different ages by the extract date would carry
outcome flags measured over different lengths of exposure, and neither the measured default
rate nor the sample it is measured on would be comparable across loans. Probability of default
needs this node next, since a PD model's target label is exactly the outcome flag this window
constructs.
