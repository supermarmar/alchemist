---
id: proportional-hazards-model
title: Proportional hazards model
domains: [life, stats]
status: drafted
requires: [hazard-rate, survival-model]
spends:
  - {object: obj.coefficients, domain: stats}
  - {object: obj.hazard, domain: life}
  - {object: obj.hazard, domain: stats}
anchor: [ifoa.cs2.4.2-5, up.ias382.3]
vault_articles: [methods/survival-analysis-macroeconomic-pd]
vault_sources: []
taught_in: null
---

## Definition

In a proportional hazards model, an individual's hazard is the product of a baseline
hazard common to everyone and a factor depending on that individual's covariates, so
the ratio of any two individuals' hazards holding fixed covariates stays constant over
time however the baseline itself moves.

## The expression

$$
\lambda(t \mid \mathbf{x}) = \lambda_0(t) \exp(\beta^\top \mathbf{x})
$$

Here $\lambda(t \mid \mathbf{x})$ is the hazard at time $t$ for an individual with
covariate vector $\mathbf{x}$, $\lambda_0(t)$ is the baseline hazard shared by every
individual, and $\beta$ is the coefficient vector the model estimates, written the same
way general statistics already spells its own regression coefficients. Life insurance
calls the hazard itself the force of mortality, $\mu_x(\mathbf{x})$ once covariates
enter, under the same product form.

## Why this node exists

Leaving the baseline hazard $\lambda_0(t)$ unspecified is what lets the effect of a
covariate such as age or an origination score be estimated by partial likelihood
instead of first committing to a parametric shape for the baseline itself, a freedom a
fully parametric survival model does not have. Bellotti and Crook extend this same
structure with time-varying macroeconomic covariates, so a fitted model can be
re-priced against a stressed economic scenario by substituting the scenario's values
for the historical series, a substitution the semi-parametric estimation leaves open
regardless of how the covariates move. The Cox proportional hazards model needs this
structure next, supplying the partial-likelihood method that estimates $\beta$ without
ever specifying $\lambda_0(t)$.
