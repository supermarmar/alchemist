---
id: differential-calculus-of-single-variable-functions
title: Differential calculus of single-variable functions
domains: [maths]
status: drafted
requires: [functions-limits-and-continuity]
spends: []
anchor: [up.wtw114.3, up.wtw114.4, up.wtw114.5, up.wtw114.6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The derivative of a single-variable function at a point is its instantaneous rate of change
there, the limit of the function's average rate of change over an interval as that interval
shrinks to the point itself. It is undefined at a point where the function has a corner, a jump
or a vertical tangent, since the limit then differs depending on the direction of approach.

## The expression

$$
f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}
$$

Here $f$ is the function, $a$ is the point at which the derivative is taken, $h$ is a small
change in the input, and $f'(a)$ is the derivative at $a$, the slope of the line the function's
graph approaches as $h$ shrinks to zero.

## Why this node exists

A rate of change stated only as a ratio over a finite interval blurs together every rate the
function takes within that interval, and a derivative is what isolates the rate at one point
alone. Mean value theorem needs it next, since it is the result that connects a function's
average rate of change back to a derivative taken at some point inside the interval.
