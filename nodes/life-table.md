---
id: life-table
title: Life table
domains: [life, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm1.3.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A life table tabulates, for each integer age, the number of an initial cohort of lives
expected to survive to that age, from which the number dying between consecutive ages
follows as their difference.

## The expression

$$
d_x = l_x - l_{x+1}
$$

Here $l_x$ is the number of lives from an initial cohort, sized $l_0$ at age zero,
expected to survive to age $x$, $l_{x+1}$ is the analogous count at age $x+1$, and
$d_x$ is the number who die between those two ages.

$$
l_{[x]+s} = l_{x+s}
$$

Here $l_{[x]+r}$ is the select equivalent of $l_{x+r}$, counting survivors $r$ years
after a life was selected at age $x$, a distinct count from ordinary ageing alone
until the select period ends, and $s$ is the length of that select period, at which
point the select column merges back into the ultimate one this node already
tabulates.

## Why this node exists

Every survival or mortality probability in the life table tradition is read off these
columns instead of computed from a distributional formula, which is what lets a life
office price a policy from tabulated experience rather than a fitted curve. Life table
probabilities need this tabulation next, since a select or an ultimate mortality
probability is defined as a ratio of the $l_x$ values this node names.
