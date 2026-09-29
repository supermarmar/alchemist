---
id: total-return-swap
title: Total return swap
domains: [credit, fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A total return swap exchanges the total return on a reference asset for a floating funding
rate, transferring the market and credit risk of holding the asset without transferring its
ownership.

## The expression

$$
\Pi = (\Delta V + C) - (L + s)N
$$

Here $\Delta V$ is the change in the reference asset's market value over the period, $C$ is any
income it pays, $L$ is the floating reference rate, $s$ is the agreed spread over it, $N$ is the
notional on which the swap is written, and $\Pi$ is the net amount the total return receiver is
paid, which turns negative once the asset falls in value by more than the funding cost.

## Why this node exists

A lender wanting exposure to an asset's performance without funding its purchase, or wanting to
shed that exposure without selling the asset and disturbing the relationship with its
counterparty, needs a contract that separates ownership from economic exposure, and the total
return swap is that contract. It sits alongside the credit default swap as one of the two
principal off-balance-sheet ways to transfer an asset's credit risk, the difference being that a
total return swap transfers market risk on the asset as well.
