---
id: bias-variance-tradeoff
title: Bias variance trade-off
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.5.1-1, up.wst212.8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The bias-variance trade-off describes how a fitted model's expected prediction error splits into a systematic component from a model too simple to capture the true relationship and a component from the model's sensitivity to the particular sample it was trained on. The two move in opposite directions as model complexity increases, so total error is usually lowest at some intermediate complexity rather than at either extreme.

## The expression

$$
E\bigl[(y - \hat f(x))^2\bigr] = \bigl(\mathrm{Bias}[\hat f(x)]\bigr)^2 + \mathrm{Var}[\hat f(x)] + \sigma^2
$$

Here $y$ is the true outcome, $\hat f(x)$ is the fitted model's prediction at $x$, $\mathrm{Bias}[\hat f(x)]$ is the gap between the model's average prediction and the truth, $\mathrm{Var}[\hat f(x)]$ is how much that prediction moves across different training samples, and $\sigma^2$ is the irreducible noise variance no model can remove.

## Why this node exists

Without this decomposition, a rise in prediction error carries no information about whether the fix is a richer model or a more stable one, since the two failure modes point in opposite directions. Overfitting and underfitting needs it next, since those two labels name the two sides of the same trade-off this node decomposes.
