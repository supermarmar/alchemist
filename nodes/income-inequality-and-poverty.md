---
id: income-inequality-and-poverty
title: Income inequality and poverty
domains: [eco]
status: drafted
requires: []
spends: []
anchor: [up.ekn110.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Gini coefficient measures income inequality as the extent to which the
distribution of income across a population departs from perfect equality, taking
the value zero where every individual receives an identical income and
approaching one as the whole of it concentrates on a single individual.

## The expression

$$
G = \frac{\displaystyle\int_0^1 \bigl(x - L(x)\bigr)\,dx}{\displaystyle\int_0^1 x\,dx}
  = 2\int_0^1 \bigl(x - L(x)\bigr)\,dx
$$

Here $L(x)$ is the Lorenz curve, giving the cumulative share of total income
received by the poorest fraction $x$ of the population, and $x$ itself runs from
zero to one across the population ranked from poorest to richest. The numerator
is the area between the line of perfect equality, $L(x) = x$, and the Lorenz
curve, and $G$ expresses that area as a fraction of the area under the equality
line.

## Why this node exists

A poverty measure such as a headcount ratio states how many people fall below a
fixed income threshold, but it says nothing about how unequally income is shared
among everyone above it. Without a summary measure of the whole distribution's
shape, two countries with identical poverty rates can look identical even where
one has a small gap between its poorest and its median household and the other
has a vast one.
