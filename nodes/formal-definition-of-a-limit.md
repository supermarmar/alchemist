---
id: formal-definition-of-a-limit
title: Formal definition of a limit
domains: [maths]
status: drafted
requires: [functions-limits-and-continuity]
spends: []
anchor: [up.wtw124.8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The formal definition of a limit states that a function $f$ tends to $L$ as $x$ tends to
$a$ if, for every tolerance placed on the output, a tolerance on the input can be found
that forces the function within it. The definition excludes $x = a$ itself, so the limit
can exist even where $f$ is undefined at $a$.

## The expression

$$
\lim_{x \to a} f(x) = L \iff \forall\, \varepsilon \gt 0,\ \exists\, \delta \gt 0 : 0 \lt |x-a| \lt \delta \implies |f(x)-L| \lt \varepsilon
$$

Here $\varepsilon$ is the tolerance chosen on the output, $\delta$ is the tolerance on the
input that must be found to force the output within it, $a$ is the point $x$ approaches,
and $L$ is the value the function is claimed to tend to.

## Why this node exists

"Gets close to" is a phrase with no test attached to it, and this definition supplies the
test: a proof can now exhibit a specific $\delta$ for any $\varepsilon$ an opponent names,
or show that no such $\delta$ can exist. Every later result that leans on continuity,
differentiability or convergence rests on being able to produce that $\delta$ on demand,
which a gesture at closeness alone could never supply.
