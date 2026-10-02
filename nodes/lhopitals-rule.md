---
id: lhopitals-rule
title: L'Hopital's rule
domains: [maths]
status: drafted
requires: [differential-calculus-of-single-variable-functions]
spends: []
anchor: [up.wtw114.8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

L'Hopital's rule evaluates a limit of a ratio of two functions that would otherwise take an
indeterminate form of $0/0$ or $\infty/\infty$, by replacing the numerator and denominator
with their derivatives before taking the limit.

## The expression

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}
$$

Here $f$ and $g$ are functions that are both differentiable near $a$, with $g'(x) \neq 0$
near $a$, and the limit of $f(x)/g(x)$ as $x \to a$ takes the indeterminate form $0/0$ or
$\infty/\infty$. The rule holds provided the limit of the derivatives' ratio, $f'(x)/g'(x)$,
exists, and it may be applied again to that new ratio if it is itself indeterminate.

## Why this node exists

A limit whose numerator and denominator both vanish, or both grow without bound, cannot be
evaluated by direct substitution, since the ratio $0/0$ or $\infty/\infty$ carries no defined
value on its own. L'Hopital's rule supplies a route past that obstruction by trading the
original ratio for one built from derivatives, which is often simple enough to evaluate by
substitution directly.
