---
id: factors-and-interactions
title: Factors and interaction terms
domains: [stats]
status: drafted
requires: [response-and-explanatory-variables]
spends:
  - {object: obj.coefficients, domain: stats}
anchor: [ifoa.cs1.4.2-4]
vault_articles: [methods/ols-predictor-importance]
vault_sources: []
taught_in: null
---

## Definition

A factor is a categorical explanatory variable entered into a linear predictor as a set of
indicator variables, one per level once a reference level is fixed. A model carrying only
main effects treats every variable's effect as additive and independent of the others;
adding an interaction term lets one variable's effect on the response depend on the level
or value of a second.

## The expression

$$
\eta = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12}\, x_1 x_2
$$

Here $\eta$ is the linear predictor, $\beta_0$ is the intercept, $\beta_1$ and $\beta_2$
are the main-effect coefficients on $x_1$ and $x_2$, and $\beta_{12}$ is the coefficient on
their product, the interaction term that lets $x_1$'s effect vary with $x_2$.

## Why this node exists

A categorical covariate such as region or occupation class cannot enter a linear model at
all until it is expressed as indicators, and without an interaction term the model is
forced to assume every variable's effect is the same at every level of every other
variable, an assumption a scorecard or a pricing model rarely satisfies in practice. Linear
predictor needs it next, since $\eta$ as written here is exactly the linear predictor the
next node names and builds on.
