---
id: conservation-laws-and-pde-modelling
title: Conservation laws and PDE modelling
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw386.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A conservation law states that a quantity's rate of change inside a region equals the
net flux crossing the region's boundary, so nothing is created or destroyed at any
interior point; writing that balance for an infinitesimal element turns it into a
partial differential equation for the quantity's density.

## The expression

$$
\frac{\partial u}{\partial t} + \frac{\partial F(u)}{\partial x} = 0
$$

Here $u(x,t)$ is the density of the conserved quantity at position $x$ and time $t$,
and $F(u)$ is the flux, the rate at which the quantity moves past a point, so the
equation says that any local increase in $u$ is matched exactly by a fall in the flux
carrying it away.

## Why this node exists

Without this balance, a model of heat, mass or any other transported quantity has no
equation linking its value at one point to its value at a neighbouring one, and every
named partial differential equation in this branch is one particular choice of flux
$F$ substituted into it. The heat equation needs it next, once the flux is written as
proportional to the density's own spatial gradient.
