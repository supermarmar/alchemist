---
id: confounding
title: Confounding
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l01]
vault_articles: [methods/adjustment-set-selection]
vault_sources: []
taught_in: null
---

## Definition

A confounder is a variable that is a common cause of both an exposure and an outcome,
so the crude association between the two mixes the causal effect with a spurious
component running through the confounder.

## The expression

$$
\text{bias} = P(Y \mid X = x) - P(Y \mid do(X = x))
$$

Here $Y$ is the outcome, $X$ is the exposure whose effect is wanted, $P(Y \mid X = x)$
is the observed, associational probability, and $P(Y \mid do(X = x))$ is the causal
probability that would be observed under an intervention setting $X$ to $x$; the
difference between them is nonzero whenever an open path runs from $X$ to $Y$ through
an unblocked confounder.

## Why this node exists

A regression run on the raw data reports a coefficient that mixes the covariate's own
effect with whatever passes through the confounder it shares with the response, and a
sign that flips once a relevant grouping variable is held fixed is exactly this bias
surfacing. Naming the confounder and the bias it produces is what makes correcting for
it possible, and any model fitted on observational rather than randomised data carries
this risk until an adjustment set is chosen deliberately.
