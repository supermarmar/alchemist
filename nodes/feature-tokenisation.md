---
id: feature-tokenisation
title: Feature tokenisation
domains: [ml]
status: drafted
requires: [entity-embedding]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: [methods/credibility-transformer]
vault_sources: []
taught_in: null
---

## Definition

Feature tokenisation maps every covariate of a tabular row into a vector of the same fixed
dimension, so that the row of covariates becomes a sequence of tokens an attention layer can
run over, on data that carries no natural order of its own.

## The expression

$$
e_j =
\begin{cases}
\mathrm{Embed}_j(x_j) & x_j \text{ categorical} \\
f_j(x_j; w_j) & x_j \text{ continuous}
\end{cases}
$$

Here $x_j$ is the $j$-th covariate of the row, $e_j$ is the token it is mapped to, a vector
of the model's fixed embedding dimension, $\mathrm{Embed}_j$ is an entity embedding lookup
where $x_j$ is categorical, and $f_j(\,\cdot\,; w_j)$ is a small feed-forward network with its
own parameters $w_j$ where $x_j$ is continuous. Every covariate is tokenised independently, so
the tokens $e_1, \dots, e_p$ may be permuted arbitrarily before entering the attention layer
with no loss of information, unlike a time series, where the sequence order carries meaning
in its own right.

## Why this node exists

An attention layer was built for a sequence, and a covariate vector has no sequence to
offer it until each covariate is placed in a common vector space of its own. Continuous
covariates are given a small network rather than a bare linear embedding precisely because
that network can absorb a nonlinear functional form the way a generalised additive model
would, which is otherwise the hardest part of fitting an unstructured network directly. The
CLS token needs feature tokenisation next, since it is appended to the sequence of tokens
this node produces and read out after the attention layer has let them interact.
