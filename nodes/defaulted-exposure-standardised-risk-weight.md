---
id: defaulted-exposure-standardised-risk-weight
title: Defaulted exposure risk weight under the standardised approach
domains: [credit, regulation]
status: drafted
requires: [definition-of-default, standardised-approach-credit-risk]
spends: []
anchor: [bcbs.d424.sa.para-90]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An exposure that has defaulted receives a risk weight set by the size of the specific provision
already held against it: once default occurs the exposure class it would otherwise have fallen
into no longer governs the weight.

## The expression

$$
RW =
\begin{cases}
100\% & SP \ge 0.2 \times E_u \\
150\% & SP \lt 0.2 \times E_u
\end{cases}
$$

Here $RW$ is the risk weight applied to the defaulted exposure, $SP$ is the specific credit
risk adjustment, the provision the bank has recognised against that exposure, and $E_u$ is the
exposure's unsecured amount, net of any eligible collateral or guarantee. A provision covering
at least a fifth of the unsecured amount earns the lower weight, on the view that the bank has
already recognised enough of the expected loss for a smaller add-on to suffice.

## Why this node exists

Once an exposure has defaulted, the external rating or exposure-class weight that applied
beforehand no longer reflects its risk, since default itself is the event those weights were
set to anticipate, and a provision-linked rule replaces them with a measure tied to what the
bank has actually recognised as lost. A larger provision lowers the risk weight precisely
because it signals the bank has already absorbed more of the expected loss through its
accounts already.
