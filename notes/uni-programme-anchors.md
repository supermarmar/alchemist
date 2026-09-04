# The University of Pretoria programmes as anchor bodies

Written 3 September 2026, from two documents Mario supplied: the **BSc (Actuarial and
Financial Mathematics)** undergraduate yearbook entry (programme 02133413, 25 pages, four
curriculum years) and the **BScHons (Actuarial Science)** entry (programme 02240278, 5 pages,
final year). Both are University of Pretoria Yearbook 2023 extracts carrying module-level
content descriptions.

## Verdict

**Incorporate, as two further anchor bodies in Phase 1, and change nothing in Phase 0.**

The `anchor` grammar settled in Task 1 already accepts them. `up.ias121.3`, `up.wst322.1`,
`up.ias382.4` and `up.iashons712.2` all match `^[a-z0-9]+(\.[a-z0-9-]+){2,3}$`, tested against
the compiled regex in `scripts/alchemist/model.py`. So no schema amendment, no checker change,
and no reopening of a reviewed task.

Three reasons the programmes are worth anchoring against rather than reading for colour:

1. **They carry module-level content descriptions**, so a module maps to a handful of nodes
   almost one to one. That is exactly the input Phase 1's transcription wants, and it is the
   same shape as an IFoA syllabus item.
2. **They supply external anchors for the three areas the spec had to mark `chosen`.**
   Spec section 3, decision 5 concedes that financial engineering, data engineering and feature
   engineering have no published syllabus and that Mario picks the floor. WTW 354 and WTW 364
   anchor financial engineering, WST 212 anchors data engineering, and WST 311 anchors the
   GLM-and-regularisation floor. Replacing three `chosen` floors with an external anchor is a
   direct improvement to the stopping rule the whole corpus rests on.
3. **They are the actual provenance of the expertise the corpus teaches**, so the graph can say
   where its roots came from rather than asserting a floor.

## What the programmes supply that the IFoA and ASSA list would miss or under-serve

| Module | Content worth taking | Where it lands in the graph |
|---|---|---|
| `IAS 121` | General insurance reserving with **run-off triangles** | New claims-reserving braid, see below |
| `WST 322` Actuarial statistics | Loss distributions, reinsurance, risk models, **ruin theory**, **credibility theory**, EVT, **copulas** | Credibility theory is the direct ancestor of the trunk's Credibility Transformer (ETH lecture 11), and the plan names no root for it. Copulas and EVT feed credit concentration and the ERM branch |
| `IAS 382` Survival models | **Graduation** and methods of graduation, **exposed to risk**, binomial and Poisson models, proportional hazards | The life root of the survival braid that Task 11 makes the first exemplar. Graduation and exposed-to-risk are absent from the plan and are core |
| `WST 312` Stochastic processes | Markov chains, Chapman-Kolmogorov, **Markov jump processes**, first passage time, applications in insurance | Multi-state Markov machinery is shared by life multiple-state models and credit **rating transition matrices**. A second braid, and a strong one |
| `WST 321` Time series | ARMA and ARIMA, identification, estimation, forecasting, multivariate | The root of IFRS 9 forward-looking information. The credit trunk's `R1` conditions a point-in-time hazard on macro series and has no time-series root to point at |
| `WTW 354`, `WTW 364` | Mean-variance, CAPM, APT, measures of investment risk, binomial model, Black-Scholes, interest rate models, numerical procedures | The financial engineering floor, anchored rather than chosen |
| `WST 311` | EDF, link functions, deviance, Poisson and logistic regression, cross-validation, regularisation, PCA | An external anchor for the trunk node itself, ETH lecture 2 |
| `WST 212` | SQL, joins, data preparation, bias-variance, cross-validation, ROC, confusion matrix | The data engineering floor, anchored rather than chosen |
| Hons `IAS 712` Actuarial risk management | Surplus management, options and guarantees, contract design, valuing liabilities, pricing and financing strategies, discontinuance, insolvency and closure, the risk management process, capital management, monitoring | The actuarial control cycle end to end. This is the spine of the life and GI halves and the plan currently names none of it |
| Hons `LEW 700` Life assurance | Asset shares, with-profits surplus distribution, actuarial funding, cost of guarantees, policy data checks, the actuarial control cycle | Deep life content, and the `taught_in` targets for a life path |
| Hons `IAS 721` ERM | Risk appetite, risk classification, copulas, EVT, economic capital, risk optimisation | Bridges to the credit trunk's `R2` on IRB capital and to ICAAP |

## Run-off triangle claims reserving, specifically

Mario is right that it is missing from the trunk and invisible in the plan. Two qualifications
and then the case for adding it deliberately.

**Qualification one.** A faithful Phase 1 transcription should reach it anyway, because the
IFoA CS2 syllabus carries delay triangles, chain ladder, average cost per claim and
Bornhuetter-Ferguson. This is stated from memory and must be checked against the published CS2
syllabus before Phase 1 relies on it.

**Qualification two.** `IAS 121` covers it as an *introduction* in first year, so the programme
anchors its existence rather than its depth. Depth comes from CS2 and from the reserving
literature.

**Why it deserves naming rather than leaving to a list of six syllabi.** Chain ladder is not a
bolt-on to this corpus. The chain ladder reserve estimates coincide with the maximum likelihood
estimates of an over-dispersed Poisson generalised linear model with a log link and additive
row and column effects, one per accident period and one per development period.

**Verified 4 September 2026, and the attribution above was wrong.** The claim was checked by a
direct read of the vault's copy of England and Verrall (2002),
`markdown/journals/2002_england-verrall_stochastic-claims-reserving-general-insurance.md`,
rather than through a wiki summary or a subagent, per
`~/.claude/rules/subagent-verification.md`. Three passages carry it. Section 2.2.1 states that
"the aim of all of the models in this section is to give the same reserve estimates as the
chain-ladder technique". Section 2.3.4 gives the over-dispersed Poisson model re-parameterised
through a log link as `log m_ij = c + a_i + b_j`, a parameter per row and a parameter per
column, which is the additive-effects form asserted above. Section 7.2.14 states of the fitted
result that "the reserve estimates are identical to the chain-ladder results". Section 2.3.1
attributes the full treatment to **Renshaw and Verrall (1998)**.

**Mack (1991) is not the citation and must not be used.** England and Verrall present Mack's
model as specifying only the first two moments of incremental claims without assuming a
distribution, and they treat the Normal model, "and by implication Mack's model", as an
approximation to the negative binomial rather than as the generalised linear model result. A
node citing Mack for the Poisson equivalence would therefore be citing him for something he
did not claim. The vault registers Mack (1993) and Mack (1994) and holds no Mack (1991) at all.

One qualification the source itself supplies, worth carrying into the node. Section 2.3.5 notes
that the Poisson model does not restrict the data to positive integers, because a
quasi-likelihood approach extends it to non-integer and negative values, and that identical
parameter estimates follow from the full or the quasi-likelihood where the data are positive
integers. The crucial assumption is that the variance is proportional to the mean.

The citable source is `england-verrall-2002-stochastic-claims-reserving`, which the vault
registers at T4 with `confidentiality: public-free`, so it passes check 5 and needs no gap
ledger entry. Renshaw and Verrall (1998) itself is not held and is a ledger entry for Phase 2
where a node wants the primary rather than the survey.

The claim therefore holds, and run-off triangles hang directly off `obj.response-mean`,
`obj.dispersion` and the exponential dispersion family, meaning off ETH lecture 2, which is the
trunk node the entire corpus is built from. That makes claims reserving a branch rather than an
appendix.

**The credit twin is the reason this braid matters most.** A run-off triangle is an
accident-period by development-period array. Its credit analogue is the origination-cohort by
months-on-book array that IFRS 9 and IRB use daily: vintage curves, roll-rate matrices, and
above all the LGD recovery profile, which is recoveries by months since default per default
cohort. The objects collide the way the hazard does:

| Object | General insurance | Credit |
|---|---|---|
| Cohort index | accident period | origination vintage |
| Development index | development period | months on book, or months since default |
| Development factor | chain ladder link ratio | roll rate |
| Ultimate | ultimate claims | lifetime loss, or ultimate recovery |

Four objects the notation contract does not yet carry, and they belong to Phase 1's seeding
rather than to a Task 2 amendment: Task 2 seeded the twelve collisions the ETH course's own
framing exposes, and this is a thirteenth through sixteenth that the course never touches.

Worth recording that the twelve-object seed was built from credit, life and general insurance
**as the ETH course frames them**, which is a modelling frame rather than a reserving one. The
GI reserving vocabulary was missed entirely. Phase 1's seeding brief should sweep for whole
vocabularies the trunk's frame omits, not only for symbol clashes inside the frame it has.

## Four requirements to carry into Phase 1

1. **Add both programmes to the anchor body list** in spec section 9, Phase 1, beside ASSA F107,
   the IFoA CM, CS and SP series, the Basel and IFRS texts, and the twelve ETH lectures. Use
   `up.<module><number>.<section>` for the undergraduate modules and
   `up.iashons<number>.<section>` for the honours modules.
2. **Replace three `chosen` floors with anchors.** Financial engineering takes `WTW 354` and
   `WTW 364`, data engineering takes `WST 212`, and the GLM floor takes `WST 311`. Record in
   each node's `anchor` field that the floor is now externally set.
3. **Add a claims-reserving braid path**, running from the exponential dispersion family through
   chain ladder and Bornhuetter-Ferguson into credit vintage and roll-rate analysis and the LGD
   recovery profile. Its `builds_on` is the maths and statistics prerequisite path. Source the
   Poisson-GLM equivalence into the vault first, since the whole braid's claim to be a branch
   rather than an appendix rests on it.
4. **Seed four more notation objects** for the cohort index, the development index, the
   development factor and the ultimate, each with its general-insurance and credit aliases, and
   sweep for other whole vocabularies the ETH framing omits before Phase 3 writes any page.
