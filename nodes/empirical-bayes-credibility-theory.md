---
id: empirical-bayes-credibility-theory
title: Empirical Bayes approach to credibility theory
domains: [actuarial, stats]
status: drafted
requires: [credibility-premium]
spends:
  - {object: obj.credibility-weight, domain: actuarial}
anchor: [ifoa.cs1.5.1-8]
vault_articles: [methods/credibility-theory]
vault_sources: []
taught_in: null
---

## Definition

Where a fully Bayesian approach fixes the prior distribution's parameters in advance, the
empirical Bayes approach estimates those same structural parameters from the portfolio's
own data, using the method of moments across every risk in the class before the
credibility premium for any one risk is formed.

## The expression

$$
Z = \frac{n}{n + \hat{k}}, \qquad \hat{k} = \frac{\hat{s}^2}{\hat{a}}
$$

Here $Z$ is the credibility weight placed on a risk's own experience, $n$ is the number of
years of that experience, and $\hat{k}$ is estimated from the portfolio as the ratio of
$\hat{s}^2$, the expected process variance within a risk, to $\hat{a}$, the variance of
the hypothetical means across the portfolio.

## Why this node exists

A practitioner rarely knows the prior distribution a fully Bayesian credibility formula
would need, and the empirical Bayes approach supplies the weight anyway by treating the
whole portfolio as evidence about that prior. Estimating $\hat{s}^2$ and $\hat{a}$ from
the data is what lets the same $Z = n/(n+\hat{k})$ formula run without ever writing the
prior down. Bayes versus empirical Bayes credibility needs it next, since comparing the
two approaches means having both an assumed prior and this data-estimated alternative on
the table together.
