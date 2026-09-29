---
id: mean-value-theorem
title: Mean value theorem
domains: [maths]
status: drafted
requires: [differential-calculus-of-single-variable-functions]
spends: []
anchor: [up.wtw114.7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The mean value theorem states that a function continuous on a closed interval and
differentiable on the open interval it encloses attains, at some interior point, an
instantaneous rate of change equal to its average rate of change over the whole
interval.

## The expression

$$
f'(c) = \frac{f(b) - f(a)}{b - a}, \qquad c \in (a, b)
$$

Here $f$ is the function, $a$ and $b$ are the interval's endpoints, $f'(c)$ is the
derivative at the guaranteed point $c$, and the right-hand side is the average rate
of change of $f$ across $[a, b]$.

## Why this node exists

Bounding how far a function can move away from a known value needs a link between
its endpoint behaviour and its derivative, and the mean value theorem is that link:
it turns a bound on $f'$ into a bound on $f(b) - f(a)$. Every later argument that
controls an approximation error, or shows a function is uniquely determined by its
derivative, calls on exactly this guarantee.
