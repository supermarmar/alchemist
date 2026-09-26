---
id: risk-pooling-principle
title: Risk pooling principle
domains: [actuarial, gi, life, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cp1.4.7-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risk pooling shares an uncertain cost across a group so that each member faces the
group's average cost rather than the full variability of their own individual
claim. The larger the pool, the more predictable that average becomes, provided
the members' individual costs are independent of one another.

## The expression

$$
\operatorname{Var}(\bar{L}) = \frac{\sigma^2}{n}
$$

Here $\bar{L}$ is the pool's average loss per member, $\sigma^2$ is the variance
of an individual member's loss, and $n$ is the number of members in the pool. As
$n$ grows, $\operatorname{Var}(\bar{L})$ falls towards zero, so the average cost
each member is charged becomes progressively more certain even though no single
member's own loss has become any more predictable.

## Why this node exists

An insurer cannot promise a stable premium unless the cost it is pricing becomes
more predictable as more policies are written, and this is the mechanism that
makes that promise true. Insurance and pensions principles needs it next, since
every product that mutualises cost across a membership rests on the variance
reduction this node states.
