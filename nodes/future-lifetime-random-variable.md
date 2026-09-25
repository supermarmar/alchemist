---
id: future-lifetime-random-variable
title: Future lifetime random variable
domains: [life, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.4.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The future lifetime of a life currently aged $x$ is the length of time remaining until
that life's death, treated as a random variable whose value is unknown rather than a
number waiting to be read off. It is nonnegative by construction, since no life already
dead at age $x$ can be conditioned on in the first place.

## The expression

$$
T_x = X - x, \qquad \text{given } X \gt x
$$

Here $X$ is the total lifetime measured from birth, the age at which death occurs, $x$
is the life's current age, and $T_x$ is the future lifetime random variable, defined
only conditional on the life having survived to age $x$ in the first place.

## Why this node exists

Every probability a survival model states is a probability about this one random
variable: how much of it has elapsed by a given time, and at what instantaneous rate it
is likely to end next. Without $T_x$ named as an object in its own right, a syllabus has
no subject for those probabilities to be about, and the lifetime distribution function
needs it next.
