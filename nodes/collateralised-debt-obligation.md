---
id: collateralised-debt-obligation
title: Collateralised debt obligation
domains: [credit, fin-eng]
status: drafted
requires: [securitisation]
spends: []
anchor: [assa.f207.2.6-2, ifoa.sp6.2.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A collateralised debt obligation pools a portfolio of debt instruments and tranches the
resulting cash flows into layers of differing seniority, so that the correlation between
defaults in the underlying pool drives how loss is shared between tranches far more than the
average default rate does on its own.

## The expression

$$
L_{[A, D]} = \min\bigl(\max(L - A, 0),\ D - A\bigr)
$$

Here $L$ is the portfolio's total percentage loss, $A$ and $D$ are the tranche's attachment
and detachment points, expressed as a percentage of the pool, and $L_{[A, D]}$ is the loss
allocated to that tranche. A tranche absorbs nothing until the pool's loss reaches its
attachment point, and it is wiped out entirely once loss reaches its detachment point.

## Why this node exists

A single default rate applied uniformly to a pool cannot say how a structure with several
tranches shares the resulting loss, since a senior tranche is protected precisely by the
tranches below it absorbing loss first. Without a rule for allocating loss by attachment and
detachment, a securitisation could describe its cash flows but not who bears a shortfall when
one occurs.
