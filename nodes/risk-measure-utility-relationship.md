---
id: risk-measure-utility-relationship
title: Relationship between risk measures and utility
domains: [eco, fin-eng]
status: drafted
requires: [risk-aversion]
spends: []
anchor: [ifoa.cm2.2.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The relationship between risk measures and utility asks which shape of utility function makes a given investment risk measure the right summary of what an investor cares about, so that maximising expected utility and applying the risk measure select the same portfolio.

## The expression

$$
U(W) = W - \frac{b}{2}W^2 \quad\Rightarrow\quad E[U(W)] = E[W] - \frac{b}{2}\Bigl(\operatorname{Var}(W) + E[W]^2\Bigr)
$$

Here $W$ is terminal wealth, $b \gt 0$ is the investor's absolute risk aversion coefficient under this quadratic utility function, and the right-hand side rewrites expected utility using only the mean and the variance of $W$. An investor with quadratic utility ranks every portfolio exactly as a mean-variance criterion would, since nothing beyond the mean and the variance enters the expression on either side.

## Why this node exists

A mean-variance criterion, or any risk measure built from a single moment of the return distribution, is a legitimate stand-in for expected utility only where the utility function or the return distribution makes higher moments irrelevant to the ranking. Quadratic utility is the case where that holds exactly, and it is also the case whose declining marginal utility at high wealth economists find least plausible, which is the standard objection raised against every risk measure this equivalence is used to justify.
