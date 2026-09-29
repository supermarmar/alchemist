---
id: bayesian-credibility-theory
title: Bayesian approach to credibility theory
domains: [actuarial, stats]
status: drafted
requires: [bayesian-prior-and-posterior, credibility-premium]
spends:
  - {object: obj.credibility-weight, domain: actuarial}
anchor: [ifoa.cs1.5.1-7]
vault_articles: [methods/credibility-theory]
vault_sources: []
taught_in: null
---

## Definition

The Bayesian approach to credibility theory derives the credibility premium as the exact
posterior mean of the risk parameter, for a wide family of prior and likelihood pairings,
rather than as an approximation justified only by a least-squares argument.

## The expression

$$
\hat{P} = Z \bar{X} + (1 - Z)\mu, \qquad Z = \frac{n}{n + k}
$$

Here $\hat{P}$ is the credibility premium, $\bar{X}$ is the mean of the individual risk's
own experience over $n$ periods, $\mu$ is the mean of the wider class the risk belongs
to, $Z$ is the credibility weight, and $k$ is a structural parameter set by the prior's
hyperparameters. For the single-parameter exponential family paired with its natural
conjugate prior, Jewell showed this weighted average is the exact Bayesian posterior
mean, and not merely its best linear approximation.

## Why this node exists

Bühlmann's original derivation justified the same weighted average only as the best
linear approximation to a posterior mean whose exact form was, in general, unknown, which
left open whether a more elaborate, nonlinear estimate might do better. Bayes versus
empirical Bayes credibility needs it next, since choosing between a fully Bayesian prior
and one estimated from the portfolio itself only matters once the exact posterior result
this node states is available to compare against.
