# Phase 3 batch 06 report

Nodes written: 14
Nodes written from articles: 3 (hedge-accounting, ifrs9, interest-rate-regime-and-net-interest-income)
Nodes written without: 11
Nodes not landed: 25 (all qualitative, 0 uncertain)

## gradient-descent

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## group-theory-fundamentals

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## heath-jarrow-morton-model

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## hedge-accounting

Sources read: regulation/ifrs9-financial-instruments (confirms the 80-125% effectiveness range at inception).
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## hedging

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## ifrs9

Sources read: regulation/ifrs9-financial-instruments (confirms PD x LGD x EAD framework, three-stage model, discounting requirement).
Spends declared: none.
Collision candidates: obj.exposure holds a credit alias EAD_i but no fin-man or regulation alias; ifrs9's domains are fin-man and regulation, so PD/LGD/EAD on this page carry no declared spend. Worth adding a fin-man or regulation alias to obj.exposure if further fin-man/regulation nodes need the same notation.
Split candidates: none.

## illiquid-asset-index-construction

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## income-inequality-and-poverty

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## inflation-swap

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## insurance-risk-transfer

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## interest-discount-relationship

Sources read: stub and anchor only.
Spends declared: obj.discount-factor:actuarial.
Collision candidates: none.
Split candidates: none.

## interest-rate-regime-and-net-interest-income

Sources read: concepts/eve-and-nii (confirms repricing-based approach to NII sensitivity under a constant balance sheet).
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## interest-rate-swap

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## international-trade-and-exchange-rates

Sources read: stub and anchor only.
Spends declared: none.
Collision candidates: none.
Split candidates: none.

## Not landed

- graduation-rationale: qualitative: the reasons for graduating mortality rates and the desirable properties of a graduated set are a discussion, not a single measured object.
- green-finance: qualitative: underwriting and pricing considerations for green lending are descriptive, with no formula standing for the topic itself.
- group-and-individual-health-cover: qualitative: a distinction between two distribution and underwriting routes, not a defined quantity.
- health-care-distribution-channels: qualitative: a survey of routes to market, with no formula the standard treatment attaches to it.
- health-care-insurance-investment-principles: qualitative: the investment principles applied to health and care business (matching term and nature of assets to liabilities) are a set of principles, not a single formula; the immunisation conditions the vault article gives belong to a separate node this one does not require.
- health-care-insurance-model-features: qualitative: the objectives and building blocks of a health and care model are descriptive.
- health-care-market-economic-political-influences: qualitative: a survey of external influences on demand and cost, with no formula.
- health-care-pricing-considerations: qualitative: a list of considerations (data, group versus individual assessment, external influences), not a single priced expression.
- health-care-product-design-principles: qualitative: competing stakeholder interests in product design are a discussion, not a formula.
- health-care-regulatory-and-tax-regime: qualitative: a survey of regulatory and tax rules, jurisdiction-dependent and not reducible to one expression.
- health-care-risk-mitigation-actions: qualitative: a list of mitigation actions beyond reinsurance and underwriting, process-descriptive.
- health-cash-plan: qualitative: a product description (fixed cash benefits against routine costs), with no formula defining it beyond its benefit schedule.
- health-insurance-benefit-structures: qualitative: describes premium and benefit structure types; a premium equation would need multi-state machinery this node does not require, so a formula would be invented rather than the standard treatment's own.
- high-level-risk-management-role: qualitative: the case for a board-level risk function is governance, confirmed qualitative by both vault articles read (three lines of defence, BCBS d328).
- income-protection-insurance: qualitative: a product description (income replacement during incapacity), with no formula defining it as such.
- information-asymmetry: qualitative: a general economic concept (adverse selection, moral hazard) with no single formula measuring the asymmetry itself.
- information-security-risk-mitigation: qualitative: a list of technical and behavioural controls, process-descriptive.
- initial-and-variation-margin: qualitative: the vault article (SA-CCR) gives a formula for EAD, not for initial or variation margin as such; IM methodology varies by approach (SIMM, schedule, CCP model) and VM is a restatement of the stub's own prose, so no single standard expression covers both halves of the node.
- insurance-regulation: qualitative: a survey of a regulatory regime's constraints on product design, pricing, capital and governance, confirmed qualitative by both vault articles read (general insurance pricing practices, Solvency II framework).
- insurance-risk: qualitative: a category-level risk definition (claims or liabilities differing from pricing and reserving assumptions), not a single measured expression.
- insurer-accounting-and-disclosure: qualitative: a survey of reporting and disclosure requirements, confirmed qualitative by both vault articles read (IFRS 17, Solvency II reporting and disclosure); the IFRS 17 CSM decomposition and the SFCR's five sections belong to standards this node surveys rather than defines.
- interest-rate-risk-in-the-banking-book-management-actions: qualitative: discretionary treasury actions and how a regulator expects them evidenced, process-descriptive.
- internal-and-external-ratings: qualitative: a comparison of two sources of credit standing, confirmed qualitative by the vault article read (CRR credit risk provisions), which treats ratings as an input to risk weights rather than giving a formula for this node's own object.
- investment-asset-characteristics-and-markets: qualitative: a survey of asset class characteristics and market behaviour, with no single formula covering the class.
- investment-bank: qualitative: an institutional definition (capital markets activity versus deposit-taking), not a measured object.
- investment-management-principles: qualitative: principles and objectives shaping a suitable investment approach, confirmed qualitative by the vault article read (prudent person principle), which is a governance standard with no formula.
