---
id: interest-rate-swap
title: Interest rate swap
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.5-10, ifoa.sp6.2.7-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An interest rate swap exchanges a fixed-rate cash flow for a floating-rate cash
flow on the same notional principal, with no exchange of the principal itself, so
that only the interest rate basis of an exposure changes and its size does not.

## The expression

$$
V_{\text{swap}} = \sum_{i=1}^n N \bigl(f_i - K\bigr)\, \tau_i\, v(t_i)
$$

Here $N$ is the notional principal, $K$ is the fixed rate agreed at outset, $f_i$
is the floating rate applicable to period $i$, $\tau_i$ is the length of that
period expressed as a fraction of a year, and $v(t_i)$ discounts the net cash
flow at time $t_i$ back to today, so that $V_{\text{swap}}$ is the value to the
fixed-rate payer summed across the $n$ remaining exchanges.

## Why this node exists

An option granting the right, but not the obligation, to enter this swap at a
future date needs a well-defined swap value to reference as its exercise
decision. Swaption needs it next, since a swaption is defined only in relation to
the swap value this expression establishes.
