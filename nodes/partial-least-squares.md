---
id: partial-least-squares
title: Partial least squares
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Partial least squares constructs a sequence of orthogonal directions in the
predictor space, each chosen to maximise covariance with the response, so the
response has a say in which structure the compression keeps rather than being
consulted only after the directions have already been fixed.

## The expression

$$
w_1 = \frac{X^{\mathsf{T}} y}{\lVert X^{\mathsf{T}} y \rVert}
$$

Here $X$ is the matrix of standardised predictors, $y$ is the response vector,
and $w_1$ is the weight vector defining the leading partial least squares
direction, the direction in predictor space most aligned with the predictors'
joint covariance with the response.

## Why this node exists

Without a compression step that lets the response steer which structure
survives, a data set with many correlated predictors and few observations has
no reduced representation the response actually needs, leaving a modeller to
drop predictors by hand or accept the unstable coefficients ordinary least
squares produces when predictors are collinear.
