---
id: interest-rate-futures
title: Interest rate futures
domains: [fin-eng]
status: drafted
requires: [money-market-reference-rates]
spends: []
anchor: [ifoa.sp6.2.5-8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An interest rate future is an exchange-traded, cash-settled futures contract written on a
short-term interest rate benchmark, quoted on a price index that moves inversely with the rate
it references. It settles at expiry against the benchmark rate then prevailing, so no deposit or
loan is ever exchanged.

## The expression

$$
P = 100 - r
$$

Here $P$ is the contract's quoted price and $r$ is the annualised reference rate, expressed as a
percentage, that the contract is written on. Quoting the price this way lets a rate rise show up
as a price fall, so the contract trades, margins and settles exactly as any other futures
contract does.

## Why this node exists

A treasurer who wants to hedge a future borrowing rate without holding a cash deposit or loan
needs an instrument whose price moves with that rate on an exchange offering daily margining and
a central counterparty, and this price convention is what makes such an instrument possible.
Its cash settlement against the prevailing reference rate at expiry ties the contract's payoff
directly to the underlying benchmark it was written on.
