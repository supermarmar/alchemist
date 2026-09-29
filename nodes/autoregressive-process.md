---
id: autoregressive-process
title: Autoregressive process
domains: [stats]
status: drafted
requires: [filtered-time-series]
spends: []
anchor: [ifoa.cs2.2.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An autoregressive process of order $p$ writes each observation as a weighted sum of its
own $p$ most recent past values plus a white noise term; it degenerates to plain white
noise where every one of those weights is zero.

## The expression

$$
X_t = \phi_1 X_{t-1} + \phi_2 X_{t-2} + \cdots + \phi_p X_{t-p} + \varepsilon_t
$$

Here $X_t$ is the value of the series at time $t$, $\phi_1, \ldots, \phi_p$ are the
autoregressive coefficients, $p$ is the order of the process, and $\varepsilon_t$ is a
white noise term uncorrelated with the series' own past. The process is stationary
exactly when the roots of its characteristic equation, formed from the $\phi$ coefficients,
lie outside the unit circle.

## Why this node exists

A filtered series can still carry structure in how each value depends on its own recent
past, and the autoregressive process is the simplest model that captures that dependence
directly through the $\phi$ coefficients rather than through an assumption about the
noise alone. The autoregressive moving average process needs it next, since it adds a
moving-average term onto exactly this structure.
