---
id: potential-future-exposure
title: Potential future exposure
domains: [credit, fin-eng]
status: drafted
requires: [counterparty-credit-risk]
spends: []
anchor: [assa.f107.6.3-3]
vault_articles: [regulation/counterparty-credit-risk-saccr]
vault_sources: []
taught_in: null
---

## Definition

Potential future exposure estimates the further increase a derivative's replacement
cost could reach between now and a future date, over and above the replacement cost
already observed today, and it is added to that current cost to size the exposure a
counterparty default would leave behind.

## The expression

$$
\mathrm{PFE}_i = N_i \times a_i
$$

Here $\mathrm{PFE}_i$ is the potential future exposure add-on for transaction $i$,
$N_i$ is its notional amount, and $a_i$ is a supervisory add-on factor set by the
transaction's asset class and residual maturity.

## Why this node exists

A derivative's current replacement cost only measures what a counterparty's default
would cost today, and a book that ignores how far that cost could still move before
maturity understates the exposure a long-dated position carries. The exposure at
default a bank holds capital against combines this add-on with current replacement
cost, scaled by a supervisory multiplier, so a lender who tracked only today's
replacement cost would systematically understate the capital a derivatives book with
years left to run actually needs.
