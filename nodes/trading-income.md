---
id: trading-income
title: Trading income
domains: [fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f107.1.7-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Trading income is the profit or loss a bank recognises on positions held in its trading book,
combining the change in their fair value with any cash flow crystallised on them during the
period.

## The expression

$$
TI_t = (V_t - V_{t-1}) + CF_t
$$

Here $V_t$ and $V_{t-1}$ are the fair value of the trading book position at the end and the
start of the period, $CF_t$ is any cash flow received or paid on it during the period, such as
a coupon or the realised proceeds of closing part of the position, and $TI_t$ is the trading
income recognised for the period.

## Why this node exists

A trading book is marked to fair value rather than held at cost, so its income cannot be read
off an accruals schedule the way a lending book's interest income can, and $TI_t$ is the
identity that turns a period's price movement and cash flows into a single profit figure.
Bank income statement needs this figure next, since it enters as one of the lines that make up a
bank's total income alongside net interest income and fee income.
