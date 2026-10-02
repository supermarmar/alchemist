---
id: best-subset-selection
title: Best-subset selection
domains: [stats]
status: drafted
requires: [regularisation]
spends:
  - {object: obj.coefficients, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Best-subset selection chooses the smallest set of covariates that keeps a model's fit
adequate, penalising the count of non-zero coefficients directly.

## The expression

$$
\hat{\beta} = \operatorname*{arg\,min}_{\beta} \left\| y - X\beta \right\|_2^2
\quad \text{subject to} \quad \left\| \beta \right\|_0 \le k
$$

Here $y$ is the response vector, $X$ is the design matrix, $\beta$ is the coefficient vector
being chosen, $\|\beta\|_0$ counts its non-zero entries, and $k$ is the maximum number of
covariates the fitted model is allowed to keep. Every subset of size up to $k$ is a candidate,
and the search picks whichever gives the smallest residual sum of squares.

## Why this node exists

Searching every subset up to size $k$ is combinatorially hard once the covariate count grows
past a few dozen, since the number of candidate subsets grows exponentially with it. Lasso
regularisation needs it next, as the tractable convex relaxation that keeps the same goal of a
sparse coefficient vector while replacing an intractable search with a penalty a solver can
optimise directly.
