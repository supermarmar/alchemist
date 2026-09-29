---
id: cross-validation
title: Cross-validation
domains: [ml, stats]
status: drafted
requires: [bias-variance-tradeoff]
spends: []
anchor: [ifoa.cs2.5.1-2, up.wst212.8, up.wst311.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Cross-validation estimates a model's out-of-sample loss by splitting the available data into
several folds, fitting the model on all but one fold and evaluating it on the fold left out, then
averaging that evaluation across every choice of held-out fold.

## The expression

$$
CV_{(K)} = \frac{1}{K} \sum_{k=1}^{K} \frac{1}{n_k} \sum_{i \in \text{fold } k} \ell\bigl(y_i, \hat f^{(-k)}(x_i)\bigr)
$$

Here $K$ is the number of folds, $n_k$ is the number of observations in fold $k$, $y_i$ is the
observed response for observation $i$, $\hat f^{(-k)}$ is the model fitted with fold $k$ held
out, and $\ell(\cdot,\cdot)$ is the loss function comparing a prediction with the observed
response. $CV_{(K)}$ is the average of that loss over every fold, each evaluated on data the
fitted model never saw.

## Why this node exists

A single train-test split wastes data on whichever half is held out and leaves the resulting
estimate at the mercy of how that one split happened to fall, so a model selected on it can look
better or worse than it really is by chance alone. By contrast, averaging over every fold in turn uses each
observation for both fitting and evaluation without ever evaluating a model on the data that fit
it, which is exactly the comparison a hyperparameter such as a tree's depth or a penalty's weight
needs before it can be chosen.
