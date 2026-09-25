---
id: credibility-premium
title: Credibility premium formula
domains: [actuarial, stats]
status: drafted
requires: []
spends:
  - {object: obj.credibility-weight, domain: actuarial}
anchor: [ifoa.cs1.5.1-6]
vault_articles: [methods/credibility-theory]
vault_sources: []
taught_in: null
---

## Definition

The credibility premium is a weighted average of a group's own claims experience and
the wider population's mean, with the weight reflecting how far the group's own data
can be trusted relative to that population.

## The expression

$$
P = Z\bar{X} + (1-Z)\mu
$$

Here $P$ is the credibility premium charged to the group, $\bar{X}$ is the group's own
observed mean experience, $\mu$ is the mean of the wider population the group belongs
to, and $Z$ is the credibility factor, a weight between zero and one that rises as the
group's own experience becomes more reliable.

## Why this node exists

A premium set from a group's own experience alone is unstable wherever that group is
small, since one large claim then dominates the average, and a premium set from the
population mean alone ignores everything the group's own experience says about it.
Blending the two according to how much each is trusted is what the credibility factor
achieves, and the Bayesian approach to credibility theory needs this weighted form
next to justify where $Z$ comes from.
