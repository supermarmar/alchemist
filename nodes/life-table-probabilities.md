---
id: life-table-probabilities
title: Life table probabilities
domains: [life, stats]
status: drafted
requires: [life-table]
spends:
  - {object: obj.lifetime-cdf, domain: life}
  - {object: obj.survival, domain: life}
anchor: [ifoa.cm1.3.2-2, ifoa.cm1.3.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A life table probability expresses the chance of surviving, or of dying, over a stated period
as a ratio of the life table's own survivor counts, so that no separate distributional formula
is needed once the table itself is known.

## The expression

$$
{}_np_x = \frac{l_{x+n}}{l_x}, \qquad {}_nq_x = 1 - {}_np_x
$$

Here $l_x$ and $l_{x+n}$ are the life table's survivor counts at ages $x$ and $x+n$, ${}_np_x$
is the probability that a life aged $x$ survives a further $n$ years, and ${}_nq_x$ is the
complementary probability that the same life dies within those $n$ years. Where the life was
selected at age $x$ rather than aged in the ordinary column, the select survivor counts
$l_{[x]+n}$ replace $l_{x+n}$ in the same ratio, giving the select equivalents ${}_np_{[x]}$ and
${}_nq_{[x]}$.

## Why this node exists

A life table on its own is a list of counts, and it says nothing about risk until those counts
are turned into probabilities a pricing or reserving calculation can use directly. Every
survival or mortality probability quoted in the life table tradition, select or ultimate, is
this ratio applied to a particular pair of ages. Mortality profit needs this node next, since
comparing actual against expected deaths over a period is a comparison against the ${}_nq_x$
this node defines.
