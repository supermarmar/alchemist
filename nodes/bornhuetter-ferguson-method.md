---
id: bornhuetter-ferguson-method
title: Bornhuetter-Ferguson method
domains: [gi]
status: drafted
requires: [chain-ladder]
spends:
  - {object: obj.cohort-index, domain: gi}
  - {object: obj.ultimate, domain: gi}
anchor: [ifoa.cm2.4.2-5]
vault_articles: [methods/bornhuetter-ferguson-reserving]
vault_sources: []
taught_in: null
---

## Definition

The Bornhuetter-Ferguson method estimates a cohort's ultimate claims by blending an a priori estimate of ultimate claims with the chain ladder's own development pattern, weighting
the two according to how much of the claims are already known to have emerged.

## The expression

$$
U_i = C_i + Q_i\left(1 - \frac{1}{f_i}\right)
$$

Here $U_i$ is the Bornhuetter-Ferguson estimate of ultimate claims for cohort $i$, $C_i$ is the
claims reported to date for that cohort, $Q_i$ is the a priori expected ultimate claims,
typically premium times an assumed loss ratio, and $f_i$ is the cumulative development factor
to ultimate. The term $1 - 1/f_i$ is the proportion of ultimate claims still unreported, so it
scales the a priori estimate down as a cohort matures and more of its claims have actually
emerged.

## Why this node exists

The chain ladder projects reported claims forward using development factors alone, so an
immature cohort's projection is highly leveraged: a single large early claim, or the absence of
one, can move the chain ladder's ultimate far more than the underlying exposure has actually
changed. Anchoring the unreported portion to a prior expectation removes that leverage, since a
swing in early reported claims no longer drives the unreported component at all. Assumptions
underlying reserving methods need it next, since choosing between the chain ladder and this
blended alternative is itself a judgement the reserving actuary has to justify.
