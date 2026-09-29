# Batch 07 report

Nodes written: 12
Nodes written from articles: 0
Nodes written without: 12
Nodes not landed: 28

## Nodes written

- investment-returns-theoretical-relationships: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.
- isotonic-regression: sources: concepts/balance-property-and-auto-calibration (read, not counted as "written from" since the formula is standard knowledge and the article's own passage on isotonic regression is descriptive rather than a defining expression). spends: none. no collision candidates. no split candidates.
- k-means-clustering: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.
- labour-market-and-wage-determination: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.
- leverage-ratio: sources: stub and anchor only. spends: none. no collision candidates. first draft used "rather than" twice; fixed before landing. no split candidates.
- lift-chart: sources: concepts/balance-property-and-auto-calibration (read; formula for the binned pair is standard, article confirms the three readings). spends: none. no collision candidates. no split candidates.
- liquidity-coverage-ratio: sources: regulation/bcbs-liquidity-coverage-ratio-original (read). spends: none. no collision candidates. no split candidates.
- lognormal-security-price-model: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.
- longevity-hedging-with-derivatives: sources: methods/longevity-risk-transfer (read). spends: none. no collision candidates. no split candidates.
- loss-given-default: sources: regulation/irb-lgd-estimation (read). spends: none. no collision candidates. no split candidates.
- macroeconomic-measurement: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.
- market-consistent-valuation: sources: stub and anchor only. spends: none. no collision candidates. no split candidates.

Note on the "written from articles" count: five of the twelve landed nodes have a
non-empty `vault_articles` field and were read in full (isotonic-regression, lift-chart,
liquidity-coverage-ratio, longevity-hedging-with-derivatives, loss-given-default), and are
listed above as "written without" because the displayed formula in each is the field's
standard defining expression rather than a figure drawn from the article; the article
supplied context for the "Why this node exists" paragraph (basis risk for the longevity
node, the balance-property readings for lift-chart and isotonic-regression, the 30-day
stress structure for LCR, the discounted-recoveries-net-of-costs structure for LGD). If
the intended test for the opening counts is instead "vault_articles non-empty and read",
the split is: written from articles 5, written without 7. Both readings are given because
the brief does not pin the boundary down further.

## Not landed

- investment-regulatory-framework: qualitative: legislative and regulatory framework survey, no defining formula in the standard treatment.
- investment-return-taxation: qualitative: describes tax bases and investor-behaviour effects, no defining formula.
- investment-risk: qualitative: names a risk category (asset return shortfall against liability assumptions), not a measured object with one standard formula.
- investment-strategy-development: qualitative: a process (objective, constraints, allocation), governed by the prudent person principle read in the vault article, no formula.
- large-portfolio-reallocation-challenges: qualitative: market impact and trading cost at scale, discussed qualitatively in the standard treatment with no single defining expression.
- lease-financing: qualitative: describes an arrangement (asset-backed lending with a retained interest), not a measured quantity.
- legacy-information-technology-modernisation: qualitative: a strategic choice between maintaining and replacing systems, no formula.
- legal-regulatory-and-tax-risk: qualitative: a risk-category definition, no formula.
- legal-risk: qualitative: a risk-category definition, no formula.
- lending-exposure-legal-entity: qualitative: a recording and measurement practice (exposure attributed to the legal entity), not itself a formula-bearing object.
- liability-categorisation-for-asset-liability-management: qualitative: a grouping practice (by guarantee type or valuation certainty), no formula.
- life-insurance-model-features: qualitative: the objectives and generic features of a model, no formula.
- life-insurance-product-overview: qualitative: a product taxonomy, no formula.
- liquidity-risk: qualitative: a risk-category definition (inability to meet payment obligations), read against regulation/bcbs-liquidity-risk-framework; the standard treatment is qualitative even though the LCR that measures it is quantitative.
- liquidity-risk-management-overview: qualitative: governance and process elements of liquidity risk management, read against regulation/bcbs-liquidity-governance-principles (BCBS 144's 17 principles), no formula.
- loan-facility-structuring: qualitative: choosing facility type and terms, no formula.
- long-term-care-insurance: qualitative: a product description, no formula.
- low-frequency-high-severity-events: qualitative: the standard treatment discusses why frequency-severity statistical methods are limited by data scarcity, without settling on one defining expression at this syllabus depth.
- machine-learning-risk-in-banking: qualitative: risks of applying ML (opacity, bias), read against regulation/eba-machine-learning-irb, no formula.
- macroeconomic-policy-targets: qualitative: a list of policy objectives (growth, unemployment, inflation, balance of payments), no formula.
- macroeconomics-and-microeconomics-distinction: qualitative: a distinction between two fields of study, no formula.
- major-medical-expenses-insurance: qualitative: a product description, no formula.
- management-action-risk: qualitative: a risk-category definition, no formula.
- management-information-and-escalation: qualitative: governance process (preparation and escalation of management information), read against regulation/bcbs-d328-corporate-governance, no formula.
- market-behaviour-in-financial-crises: qualitative: a descriptive account of rate and correlation behaviour in named crises, no single defining expression at this syllabus depth.
- market-outcomes-and-the-public-interest: qualitative: a normative question about markets and the public interest, no formula.
- market-risk: qualitative: a risk-category definition spanning several price types, no single defining formula for the category as a whole.
- ml-in-banking-risk-management: qualitative: the use of ML across banking risk tasks, read against methods/ml-credit-risk-methods, no formula for the category itself.

## Finish

`.venv/bin/python scripts/check.py` last line: `1560 nodes, 13 paths, 0 failures`
