---
id: functions-limits-and-continuity
title: Functions, limits and continuity
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw114.1, up.wtw114.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A function of a single real variable is continuous at a point when its limit there equals its
value there, so the function has no jump, gap or hole at that point. A function can fail to be
continuous at a point either because the limit does not exist there or because it exists but
disagrees with the function's actual value.

## The expression

$$
\lim_{x \to a} f(x) = f(a)
$$

Here $f$ is the function, $a$ is the point in question, $f(a)$ is the function's value there, and
$\lim_{x \to a} f(x)$ is the value the function approaches as $x$ approaches $a$ from either side.
The function is continuous at $a$ exactly where this equality holds, so continuity rests entirely
on the limit's existence and its agreement with the function's own value.

## Why this node exists

Differentiation and integration are both defined through limits, so neither can be built on a
function that jumps or breaks at the point in question. The formal definition of a limit needs
this node next, since it makes the informal "approaches" in the statement above precise enough to
prove theorems from.
