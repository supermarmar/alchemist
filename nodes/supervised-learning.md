---
id: supervised-learning
title: Supervised learning
domains: [ml, stats]
status: drafted
requires: []
spends:
  - {object: obj.response-mean, domain: ml}
anchor: [ifoa.cs2.5.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Supervised learning fits a model that predicts a response from a set of features by minimising
a chosen loss function over a training sample of features paired with observed responses,
covering both a continuous response, regression, and a categorical one, classification.

## The expression

$$
\hat{f} = \arg\min_f \frac{1}{n} \sum_{i=1}^n L\bigl(y_i,\, \hat{y}_i\bigr), \qquad \hat{y}_i = f(x_i)
$$

Here $x_i$ is the feature vector for observation $i$, $y_i$ is its observed response, $\hat{y}_i$
is the model's prediction for it, $L$ is the loss function penalising a discrepancy between the
two, $n$ is the number of training observations, and $\hat{f}$ is the fitted function chosen to
minimise the average loss over the sample.

## Why this node exists

A statistical model only becomes a usable predictive tool once fitting it is treated as a
software task with a specified loss function and a training routine, and this node is where
CS2 makes that shift explicit for problems the candidate already understands statistically as
regression or classification. Different choices of $L$ recover familiar special cases, squared
error loss recovers ordinary least squares and log-loss recovers logistic regression, and binary
classifier evaluation metrics needs a fitted classifier from exactly this process before it can
assess how good it is.
