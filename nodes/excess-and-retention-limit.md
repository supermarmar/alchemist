---
id: excess-and-retention-limit
title: Excess and retention limit
domains: [gi]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.1.1-2]
vault_articles: [concepts/reinsurance]
vault_sources: []
taught_in: null
---

## Definition

An excess, also called a deductible, is the amount a policyholder bears on a loss before an
insurer pays a claim, and a retention limit is the same construction one layer up, the amount an
insurer bears before a non-proportional reinsurance treaty responds. Both truncate the loss the
payer actually faces from below, and the treaty's limit truncates the recovery from above.

## The expression

$$
R = \min(X, d), \qquad C = \min\bigl(\max(X - d, 0),\, L\bigr)
$$

Here $X$ is the loss, $d$ is the excess or retention, $R$ is the amount the payer below the
threshold retains, $C$ is the amount recovered above it, capped by the treaty's limit $L$. Where
$X$ never exceeds $d$ the recovery is zero and the payer bears the whole loss, and where $L$ is
unbounded the recovery is simply the loss in excess of $d$.

## Why this node exists

Without a stated retention, a cedant could hand every loss to its reinsurer and hold no capital
against its own book, which is precisely what a treaty's retention prevents by keeping the
cedant's own money at risk below the threshold. Excess of loss reinsurance needs this node next,
since it is the retention and limit applied at the level of a whole treaty rather than a single
policy.
