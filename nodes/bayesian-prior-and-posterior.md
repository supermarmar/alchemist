---
id: bayesian-prior-and-posterior
title: Prior and posterior distributions
domains: [stats]
status: drafted
requires: [bayes-theorem]
spends: []
anchor: [ifoa.cs1.5.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The prior distribution states what is believed about a parameter before any data are seen,
and the posterior distribution states what is believed about it afterwards, once Bayes'
theorem has folded the data's likelihood into that belief. A conjugate prior is one chosen so
that the posterior falls in the same family as the prior, which turns the update into a
change of parameters and avoids a fresh derivation each time.

## The expression

$$
\pi(\theta \mid x) \propto L(x \mid \theta) \, \pi(\theta)
$$

Here $\pi(\theta)$ is the prior density of the parameter $\theta$, $L(x \mid \theta)$ is the
likelihood of the observed data $x$ given $\theta$, and $\pi(\theta \mid x)$ is the posterior
density. The proportionality hides a normalising constant, the marginal probability of $x$
integrated over every value of $\theta$, which does not depend on $\theta$ and so can be
recovered afterwards from the requirement that the posterior integrates to one.

## Why this node exists

A point estimate treats a parameter as a single unknown number, but a prior and a posterior
treat it as a quantity with its own distribution, so that data update belief rather than
replacing it outright. Bayesian point estimation needs that posterior settled before it can
summarise it as a single number, and a credible interval needs it settled before it can
summarise it as a range.
