---
id: lee-carter-model
title: Lee-Carter model
domains: [life, stats]
status: drafted
requires: [mortality-projection-approaches]
spends: []
anchor: [ifoa.cs2.4.6-2, ifoa.cs2.4.6-3]
vault_articles: [methods/mortality-modelling]
vault_sources: []
taught_in: null
---

## Definition

The Lee-Carter model forecasts age-specific mortality by decomposing the log of the mortality
rate at each age into a fixed age effect and an age-specific sensitivity that scales a single
time-varying mortality index, so that a forecast of one index series generates a forecast of
every age's mortality rate at once.

## The expression

$$
\ln m_{x,t} = a_x + b_x k_t + e_{x,t}
$$

Here $m_{x,t}$ is the central mortality rate at age $x$ in year $t$, $a_x$ is the average
level of log mortality at age $x$ across the fitting period, $b_x$ is the sensitivity of age
$x$ to the general trend, $k_t$ is the time-varying mortality index common to every age, and
$e_{x,t}$ is the residual left once the bilinear term is fitted. Brouhns, Denuit and Vermunt's
Poisson maximum-likelihood reformulation is the estimation method current practice uses,
weighting each age and year by its exposure instead of fitting the bilinear form to the raw
log-mortality surface.

## Why this node exists

A single mortality curve fitted to one year says nothing about how mortality is moving, and an
insurer pricing an annuity or reserving a pension needs the whole future path, not a snapshot.
Reducing that path to one time series, $k_t$, is what turns mortality forecasting into a
standard time-series problem: $k_t$ is projected forward with confidence intervals, and every
age's forecast follows from it through the fixed $a_x$ and $b_x$ terms. Consequently the
model's whole forecast, and the uncertainty attached to it, rests on how well a chosen
time-series model extrapolates $k_t$ rather than on the age structure $a_x$ and $b_x$ capture,
which is fitted once and then held fixed.
