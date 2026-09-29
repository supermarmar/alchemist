---
id: sequences-and-series
title: Sequences and series
domains: [maths]
status: drafted
requires: [real-number-properties]
spends: []
anchor: [up.wtw220.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A sequence of real numbers converges to a limit where its terms can be made arbitrarily close
to that limit by going far enough along the sequence. A series converges where the sequence of
its partial sums does.

## The expression

$$
\forall\, \varepsilon \gt 0,\ \exists\, N \in \mathbb{N}: n \gt N \implies |a_n - L| \lt \varepsilon
$$

Here $a_n$ is the $n$th term of the sequence, $L$ is the candidate limit, $\varepsilon$ is an
arbitrarily small positive tolerance, and $N$ is the point beyond which every term lies within
that tolerance of $L$. A series $\sum a_n$ converges to $L$ exactly where its partial sums
$S_n = \sum_{k=1}^n a_k$ converge to $L$ in this same sense.

## Why this node exists

The real number properties node guarantees that a bounded monotone sequence has a real
supremum, but that guarantee says nothing yet about what it means for a sequence to approach a
limit in the first place, and this node supplies the definition that makes the guarantee usable.
Sequences of functions need it next, extending convergence from a single sequence of numbers to
a whole sequence of functions converging pointwise or uniformly.
