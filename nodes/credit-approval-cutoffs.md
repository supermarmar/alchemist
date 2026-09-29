---
id: credit-approval-cutoffs
title: Credit approval cut-offs
domains: [credit, fin-man]
status: drafted
requires: [credit-scoring]
spends: []
anchor: [assa.f207.1.5-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A credit approval cut-off is the score, or the odds it implies, at which an application moves
from decline to approval, set consistently with the bank's asset writing strategy rather than
at an arbitrary round number.

## The expression

$$
O(s^{*}) = \frac{L}{G}
$$

Here $O(s)$ is the good-to-bad odds implied by score $s$, the ratio of expected good accounts
to expected bad accounts at that score, $L$ is the loss the bank expects to incur on a bad
account it approves, $G$ is the profit it expects to earn on a good account it approves, and
$s^{*}$ is the break-even cut-off score at which expected profit from approving is exactly
zero. A bank tightening its cut-off above $s^{*}$ trades away marginal good accounts to reduce
bad-account losses further.

## Why this node exists

A credit score only ranks applicants by risk, and ranking alone says nothing about where to
draw the line between approving and declining until the cost of a bad account is weighed
against the profit from a good one. Without a cut-off fixed this way, an asset writing
strategy could describe the risk it wants to take on but not the score at which that risk
appetite actually binds.
