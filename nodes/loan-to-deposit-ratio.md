---
id: loan-to-deposit-ratio
title: Loan-to-deposit ratio
domains: [fin-man]
status: drafted
requires: [liquidity-risk-management-overview, sources-of-liquidity]
spends: []
anchor: [assa.f107.10.1-3-1, assa.f207.6.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The loan-to-deposit ratio measures how far a bank's lending book is funded by its own deposit
base, comparing total loans outstanding against total deposits held.

## The expression

$$
LDR = \frac{L}{D}
$$

Here $L$ is the bank's total loans outstanding and $D$ is its total deposits, so $LDR$ is the
proportion of lending covered by deposit funding. A ratio above one means loans exceed
deposits, so the shortfall must be funded from wholesale markets or other sources of
liquidity.

## Why this node exists

Deposit funding is generally cheaper and more stable than wholesale funding, so a bank whose
loan book has grown faster than its deposit base is exposed to whatever conditions prevail in
wholesale markets when that funding gap needs rolling over. The loan-to-deposit ratio gives a
board and a supervisor a single, easily monitored figure for how far a bank's lending has
outrun its own deposit-taking, which is what makes it a standard reference point alongside the
more detailed liquidity ratios a bank also reports.
