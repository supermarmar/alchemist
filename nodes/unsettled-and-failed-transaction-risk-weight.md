---
id: unsettled-and-failed-transaction-risk-weight
title: Unsettled and failed transaction risk weight
domains: [credit, regulation]
status: drafted
requires: [standardised-approach-credit-risk]
spends: []
anchor: [bcbs.d424.sa.para-87]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A capital charge applies to a bank's exposure from a securities, commodities, or foreign
exchange transaction that remains unsettled past its contractual settlement date, calculated
on the positive replacement cost of the failed trade and scaled by a risk weight that rises
the longer the trade stays unsettled.

## The expression

$$
K = \max\bigl(P_{\text{market}} - P_{\text{contract}},\ 0\bigr) \times RW(d)
$$

Here $K$ is the capital charge, $P_{\text{market}}$ is the current market price of the
security, commodity, or currency being exchanged, $P_{\text{contract}}$ is the price fixed in
the original contract, and $RW(d)$ is the risk weight the framework prescribes once $d$ days
have elapsed since the contractual settlement date, rising in steps from 8% at five days to
100% once a trade has been unsettled for more than 45 days.

## Why this node exists

An unsettled trade leaves a bank exposed to the counterparty's failure to deliver for exactly
as long as the fail persists, and a charge that ignored how long the fail had lasted would
treat a trade one day late the same as one that had been failing for months. Scaling the risk
weight with the number of days elapsed is what makes the charge track that growing exposure,
and it gives a counterparty a standing capital incentive to resolve a failed settlement
quickly, since every additional day it drifts raises the charge against it.
