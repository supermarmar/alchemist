---
id: exponential-dispersion-family
title: Exponential dispersion family
domains: [stats]
status: drafted
requires: [binomial-distribution, exponential-distribution, gamma-distribution, normal-distribution, poisson-distribution]
spends:
  - {object: obj.dispersion, domain: stats}
  - {object: obj.response-mean, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l02, ifoa.cs1.4.2-1, up.wst221.18, up.wst311.7]
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: []
taught_in: null
---

## Definition

The exponential dispersion family is the class of response distributions whose density
factorises through a canonical parameter and a cumulant function, chosen precisely so that
maximising the likelihood of the mean is the same operation as minimising a deviance loss
built from that same cumulant function.

## The expression

$$
f(y; \theta, \varphi) = \exp\!\left( \frac{y\theta - \kappa(\theta)}{\varphi / v} + c(y, \varphi / v) \right)
$$

Here $y$ is the observed response, $\theta$ is the canonical parameter, $\kappa$ is the
cumulant function that identifies which member of the family is in play, $\varphi$ is the
dispersion parameter, and $v$ is the exposure weight. The cumulant function's first two
derivatives give the mean, $\mu = \kappa'(\theta)$, and the variance,
$\mathrm{Var}(Y) = (\varphi/v)\,\kappa''(\theta)$, so choosing $\kappa$ alone fixes the
Gaussian, binomial, Poisson, gamma or Tweedie case, along with how the response's variance is
allowed to grow with its mean.

## Why this node exists

A generalised linear model needs a response distribution before it can be fitted, and
choosing among the Gaussian, binomial, Poisson and gamma distributions one by one obscures
the fact that maximum likelihood estimation and a squared-error, cross-entropy or Poisson
deviance loss are, for each of them, the same fitting criterion in different clothing.
Writing all of them through one cumulant function is what exposes that equivalence, and the
generalised linear model needs it next to turn that fitted mean into a function of the
covariates.
