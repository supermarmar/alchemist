---
id: vintage-analysis
title: Vintage analysis
domains: [credit, stats]
status: drafted
requires: [age-period-cohort]
spends:
  - {object: obj.cohort-index, domain: credit}
  - {object: obj.development-index, domain: credit}
anchor: [ucsc.dl-actuarial-2026.l01]
vault_articles: [methods/breeden-2016-lifecycle-environment-loan-level-forecasts]
vault_sources: []
taught_in: null
---

## Definition

Vintage analysis decomposes a loan-level outcome into an age effect, a vintage effect
and a calendar effect, on the understanding that a loan's position along each of the
three axes is set independently of the other two once the loan has been originated.

## The expression

$$
g\bigl(\pi_{i,j,c}\bigr) = f_{\mathrm{age}}(j) + f_{\mathrm{vintage}}(i) + f_{\mathrm{env}}(c)
$$

Here $\pi_{i,j,c}$ is the outcome probability for a loan from origination cohort $i$, at
development index $j$ months on book, observed in calendar period $c$; $g$ is a link
function such as the logit; and $f_{\mathrm{age}}$, $f_{\mathrm{vintage}}$ and
$f_{\mathrm{env}}$ are the three offset curves the decomposition estimates, one per axis.
The identity $c = i + j$ ties the three indices together, which is what makes separating
their three effects an estimation problem rather than a bookkeeping exercise.

## Why this node exists

A single origination-to-date default rate mixes how far a loan has aged with how the
economy has moved since it was booked and with how sound that origination cohort was to
begin with, and no lending decision can be traced to the right cause until those three
effects are pulled apart. The consequence of leaving them mixed is a scorecard that
ranks borrowers well in sample and degrades once it is applied out of time, because the
calendar effect it absorbed during training has moved on.
