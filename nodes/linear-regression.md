---
id: linear-regression
title: Linear regression
domains: [stats]
status: drafted
requires: [response-and-explanatory-variables]
spends:
  - {object: obj.coefficients, domain: stats}
  - {object: obj.response-mean, domain: stats}
anchor: [ifoa.cs1.4.1-2, up.wst121.4, up.wst212.11]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Linear regression models a response variable's expectation as a straight-line function of one
or more explanatory variables, fitting the line's coefficients by minimising the sum of
squared deviations between observed and fitted values.

## The expression

$$
E[Y \mid \mathbf{x}] = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p
$$

Here $Y$ is the response variable, $\mathbf{x} = (x_1, \dots, x_p)$ is the vector of
explanatory variables, $\beta_0$ is the intercept, the expected response when every
explanatory variable is zero, and $\beta_1, \dots, \beta_p$ are the coefficients giving the
change in the expected response for a one-unit change in the corresponding explanatory
variable, holding the others fixed. Correlation measures the strength of the linear
association between a single pair of variables and is closely related to, but distinct from,
the fitted slope $\beta_1$ in the one-variable case.

## Why this node exists

A response and its explanatory variables are only vocabulary until a functional form links
them, and the linear form is the one every later regression method either extends or departs
from deliberately. Fitting the straight line that minimises squared error gives a baseline
model that is easy to interpret and easy to diagnose, which is why it is the first model fitted
even where a more flexible method is eventually chosen. Local regression needs this node next,
relaxing the single global line into a curve built from many local linear fits.
