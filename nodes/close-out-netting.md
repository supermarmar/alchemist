---
id: close-out-netting
title: Close-out netting
domains: [credit, fin-eng]
status: drafted
requires: [counterparty-credit-risk]
spends: []
anchor: [assa.f107.6.3-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Close-out netting is the contractual right, triggered on a counterparty's default, to combine
every outstanding derivative position under one agreement into a single net settlement amount,
so exposure to that counterparty is measured against the net position, and every transaction
under the agreement is settled together.

## The expression

$$
N = \max\!\left(\sum_{i} V_i,\ 0\right)
$$

Here $N$ is the exposure surviving under close-out netting, and $V_i$ is the mark-to-market
value of the $i$th transaction under the netting agreement, which can be positive or negative.
Without netting, exposure is instead the sum of each transaction's own floor at zero,
$\sum_i \max(V_i, 0)$, which is at least as large as $N$ and strictly larger wherever some
transactions are in the money and others are out of it.

## Why this node exists

A counterparty holding transactions of mixed sign against a bank owes the bank money on some
and is owed money on others, and without a netting agreement each of those transactions is a
separate unsecured claim in the counterparty's insolvency, so the bank can lose on transactions
where it was in the money while still owing in full on those where it was not. ISDA master
agreement needs it next, since it is the standard contract that makes this netting right
legally enforceable across every transaction it covers.
