---
id: survival-model
title: Survival model
domains: [life, stats]
status: drafted
requires: []
spends:
  - {object: obj.survival, domain: stats}
anchor: [up.ias121.2, up.ias221.1, up.ias382.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A survival model describes the random future lifetime of an individual through the
probability that they survive beyond any given age, treating the age at death as a random
variable rather than a fixed quantity.

## The expression

$$
S_0(x) = P(X \gt x)
$$

Here $X$ is the age at which death occurs, $x$ is a given age, and $S_0(x)$ is the probability
of surviving from birth to at least age $x$. It equals one at age zero and falls to zero as $x$
increases without bound, and every life table entry and every insurance calculation that
follows is a statement built out of this one function.

## Why this node exists

An insurer pricing a policy or valuing a reserve needs a probability for how long a given life
will survive, and that probability has no meaning until survival from birth to any age is named
as a single function. Lifetime distribution estimation needs it next, since estimating $S_0$
from observed data is the step that turns this definition into a life table a fund can actually
price against.
