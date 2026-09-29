---
id: posterior-derivation-conjugate-cases
title: Posterior derivation in conjugate cases
domains: [stats]
status: drafted
requires: [bayesian-prior-and-posterior]
spends: []
anchor: [ifoa.cs1.5.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A conjugate prior is one whose posterior, once combined with the likelihood of the
observed data, belongs to the same distributional family as the prior itself, which
keeps the derivation of the posterior a matter of updating a small number of
parameters rather than a fresh integration.

## The expression

$$
\pi(\theta \mid x) \propto L(x \mid \theta)\, \pi(\theta)
$$

Here $\theta$ is the parameter being estimated, $x$ is the observed data, $\pi(\theta)$
is the prior density, $L(x \mid \theta)$ is the likelihood of the data given $\theta$,
and $\pi(\theta \mid x)$ is the resulting posterior density, proportional to the
product of the two.

## Why this node exists

Bayes' theorem gives the posterior in general, but the integral it implies is
rarely tractable by hand, and a conjugate prior is the case in which that
proportionality can be resolved into a closed-form update, a Beta prior updated by
Binomial data into another Beta being the standard worked example. Without a
conjugate case to practise on, the general theorem would remain a formula never seen
resolved to a number.
