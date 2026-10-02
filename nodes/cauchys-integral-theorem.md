---
id: cauchys-integral-theorem
title: Cauchy's integral theorem
domains: [maths]
status: drafted
requires: [cauchy-riemann-equations]
spends: []
anchor: [up.wtw320.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Cauchy's integral theorem states that the integral of a function differentiable throughout a
simply connected region is zero around any closed path lying in that region.

## The expression

$$
\oint_{\gamma} f(z)\, dz = 0
$$

Here $f$ is a function holomorphic, meaning complex differentiable, throughout a simply
connected region, and $\gamma$ is any closed contour lying entirely within that region. The
result holds regardless of the contour's shape, provided it stays inside the region on which
$f$ is holomorphic and encloses no point where $f$ fails to be.

## Why this node exists

A holomorphic function's values inside a region are entirely determined by its values on the
region's boundary, and this theorem is what makes that determination possible: once the
integral around any closed path vanishes, the difference between two paths with the same
endpoints must also vanish, so the integral from one point to another is path-independent.
Residue theorem needs it next, since it recovers a non-zero contour integral by isolating the
points where holomorphy fails and measuring exactly how much each one contributes.
