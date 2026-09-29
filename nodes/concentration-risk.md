---
id: concentration-risk
title: Concentration risk
domains: [life, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.3.1-18, ifoa.sp2.3.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Concentration risk is the risk that a portfolio's losses depend on a small number of
large or correlated exposures, so that a single event or a shared risk factor can move
a disproportionate share of the book at once.

## The expression

$$
HHI = \sum_{i=1}^{n} w_i^2
$$

Here $HHI$ is the concentration index, $n$ is the number of exposures making up the
portfolio, and $w_i$ is the share of the total sum insured or total exposure held by
exposure $i$. A value close to $1/n$ signals an evenly spread book, and a value close
to one signals that a handful of exposures dominate it.

## Why this node exists

A portfolio described only by an average claim size and an average frequency looks the
same whether its risk sits in one exposure or is spread across a thousand, and that
average hides the very failure a concentrated book produces: several losses
crystallising together. Measuring concentration directly is what checks whether
pooling has actually diversified the risk it was meant to, and that check on the
pooling assumption is the consequence the whole book's assumed independence depends
on.
