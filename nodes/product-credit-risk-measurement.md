---
id: product-credit-risk-measurement
title: Product-level credit risk measurement
domains: [credit]
status: drafted
requires: []
spends: []
anchor: [assa.f107.6.1-5]
vault_articles: [methods/ifrs9-portfolio-segmentation]
vault_sources: []
taught_in: null
---

## Definition

Product-level credit risk measurement estimates expected loss for a defined
product segment, such as a mortgage or a credit card book, rather than for an
individual borrower or the portfolio as a whole, so that parameters reflect the
risk characteristics the product itself carries.

## The expression

$$
\mathrm{EL} = \mathrm{PD} \times \mathrm{LGD} \times \mathrm{EAD}
$$

Here $\mathrm{PD}$, $\mathrm{LGD}$, and $\mathrm{EAD}$ are the probability of
default, loss given default, and exposure at default estimated for the product
segment, and $\mathrm{EL}$ is the expected loss that segment is expected to
generate.

## Why this node exists

Without parameters estimated at the level of the product itself, a mortgage
book and a credit card book sharing one borrower-level average would understate
the risk of whichever product actually defaults more often, which is why
segmentation choices such as this one are, in practice, the single design
decision expected credit loss modelling is most sensitive to.
