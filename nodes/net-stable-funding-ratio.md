---
id: net-stable-funding-ratio
title: Net stable funding ratio
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.10.4-3, assa.f107.2.3-9]
vault_articles: [regulation/bcbs-liquidity-nsfr-monitoring-tools]
vault_sources: []
taught_in: null
---

## Definition

The net stable funding ratio measures whether a bank's funding is stable enough, relative to
the liquidity of its assets, to survive a one-year horizon without relying on fresh wholesale
borrowing, and Basel III requires it to stay at or above 100 per cent.

## The expression

$$
\text{NSFR} = \frac{\text{ASF}}{\text{RSF}} \ge 100\%
$$

Here ASF is available stable funding, calculated by applying stability weights to the bank's
liabilities and capital so that equity and long-dated liabilities count in full while
short-term wholesale funding counts for nothing, and RSF is required stable funding, calculated
by applying illiquidity weights to the bank's assets so that an unencumbered government bond
needs little stable funding behind it while a long-dated loan needs most of its value covered.

## Why this node exists

A bank can hold ample liquid assets for a thirty-day stress and still be structurally exposed
if it funds long-dated, illiquid loans with short-term wholesale borrowing that must be rolled
over continuously. The NSFR reaches that structural mismatch on a one-year horizon, where a
short-term coverage ratio cannot. NSFR calculation needs this node next, since it works through
how the stability and illiquidity weights are actually assigned to specific liability and asset
categories.
