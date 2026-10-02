---
id: p-spline-mortality-model
title: P-spline regression model for mortality
domains: [life, stats]
status: drafted
requires: [mortality-projection-approaches]
spends:
  - {object: obj.hazard, domain: life}
  - {object: obj.regularisation, domain: stats}
anchor: [ifoa.cs2.4.6-2, ifoa.cs2.4.6-3]
vault_articles: [methods/mortality-modelling]
vault_sources: []
taught_in: null
---

## Definition

A P-spline mortality model represents the log mortality surface across age and calendar year as
a linear combination of B-spline basis functions, with a roughness penalty on the fitted
coefficients controlling how sharply the surface can bend. The penalty is chosen by
cross-validation or an information criterion, trading a small loss of fit for a surface that
extrapolates smoothly beyond the observed data.

## The expression

$$
\log \mu_{x,t} = \sum_{j} \sum_{k} \theta_{jk}\, B_j(x)\, B_k(t), \qquad
\text{penalty} = \lambda_{\mathrm{reg}} \sum \bigl(\Delta^d \theta\bigr)^2
$$

Here $\mu_{x,t}$ is the force of mortality at age $x$ in calendar year $t$, $B_j(x)$ and
$B_k(t)$ are B-spline basis functions in age and time respectively, $\theta_{jk}$ is the
coefficient attached to the basis pair $(j,k)$, and $\lambda_{\mathrm{reg}}$ is the
regularisation weight multiplying the sum of squared $d$-th order differences $\Delta^d\theta$
across neighbouring coefficients, the penalty that enforces smoothness.

## Why this node exists

Two coarser models already sit on either side of this one: Lee-Carter and age period cohort
separate age and time into a small number of factors, and neither lets the modeller choose
directly how smooth the resulting surface should be. The penalty here buys that choice at the
cost of a smoothing parameter the actuary must set, so the surface can be fitted as tightly or
as loosely as the data and judgement together warrant.
