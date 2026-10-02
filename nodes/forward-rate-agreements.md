---
id: forward-rate-agreements
title: Forward rate agreements
domains: [fin-eng]
status: drafted
requires: [hedging]
spends: []
anchor: [assa.f107.7.5-4-1, ifoa.sp6.2.5-7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A forward rate agreement is an over-the-counter contract fixing an interest rate for a
specified future period. It settles at the start of that period, by the difference
between the fixed rate and the market rate observed at the fixing date, applied to a
notional amount and discounted forward from the period's end.

## The expression

$$
\text{Settlement} = \frac{N (L - K)\, \tau}{1 + L\tau}
$$

Here $N$ is the notional amount, $L$ is the reference rate observed at the fixing date,
$K$ is the fixed rate agreed in the contract, and $\tau$ is the accrual fraction of the
rate period; dividing by $1 + L\tau$ brings the settlement forward to the start of that
period.

## Why this node exists

Fixing a rate today for a period that starts later is what lets a borrower or a lender
remove the risk that market rates move before the period begins, without either party
lending or borrowing the notional amount itself. Discounting the settlement to the start
of the period is what lets the contract cash-settle cleanly, even though the interest
difference it compensates would ordinarily fall due only at the period's end.
