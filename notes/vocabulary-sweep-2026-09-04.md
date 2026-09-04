# Vocabulary sweep, 4 September 2026

Task 5 seeds the four general-insurance reserving objects `notes/uni-programme-anchors.md`
names, and it also asks for the sweep that document promises. The twelve objects Task 2
seeded came from the ETH course's modelling frame rather than a reserving one, so if that
frame omitted the reserving vocabulary by construction, it is worth checking what else it
omits. This note is that check.

The sweep reads the 17 extracted syllabus texts under `data/syllabi/*.txt`. Three of the 20
anchor bodies in `sources/syllabi.yaml`, namely `bcbs-d424`, `iasb-ifrs9` and
`eth-dl-actuarial-2026`, hold no local text extract, so the ETH-course candidate below is
checked instead against the trunk lecture source itself, in
`~/Documents/Repos/actuarial_deep_learning/credit_lectures/`. That directory sits outside the
20 anchor bodies' text extracts but is one of the bodies, since `eth-dl-actuarial-2026`'s
entry in `sources/syllabi.yaml` names it as the local material.

**The rule applied to every row.** A vocabulary earns a place in the contract where a second
domain spells the same object differently, or a second meaning already claims the same
symbol. Short of that, an entry is a glossary item, and the bridge table `objects.yaml`
builds is not a glossary.

## The six named candidates

| Candidate | Source checked | Verdict |
|---|---|---|
| Multi-state and Markov | CS2 topic 3; UP WST 312 | Rejected |
| Time series | CS2 topic 2; UP WST 321; trunk lecture R1 | Rejected |
| Credibility | UP WST 322; SP8 topic 4; trunk lectures 6 and 10 to 11 | Seeded |
| Ruin theory | CM2 topic 4.1; UP WST 322 | Rejected |
| Interest and discount | CM1 topics 1 and 2 | Rejected |
| Capital | F107 topics 3.3 and 10; trunk lecture R2 | Verified, not seeded |

### Multi-state and Markov, rejected

CS2 topic 3 confirms transition intensities and Markov jump processes as syllabus content,
and UP WST 312's module content lists Markov chains, Chapman-Kolmogorov equations and Markov
jump processes directly. Life's transition intensity, conventionally $\mu_{ij}$, and a
credit rating-transition matrix are a real future collision, in the same family as the
hazard and the reserving objects. The reason to reject seeding it now is narrower than that
collision, though. This sweep's material names no credit-side spelling for a transition
probability or a generator-matrix entry, and none of the syllabus texts or the trunk lectures
gives one either. Task 4's brief is explicit that inventing a spelling for a field, rather
than sourcing the one the field already uses, is the mistake the strict alias rule exists to
force a reviewer to catch. A second, narrower point stands for Phase 3 to carry forward.
Whichever indices a future Markov braid gives its states, `i` and `j` are already claimed in
the `credit` domain by `obj.cohort-index` and `obj.development-index`, so a Markov-specific
rendering will need its own letters there.

### Time series, rejected

CS2 topic 2 and UP WST 321 both confirm ARMA and ARIMA content, identification, estimation
and forecasting. The trunk lecture `R1_credit-ifrs9-pit-pd.qmd` names ARIMA directly, at
line 458, in the form `ARIMA(1,0,0)`, unchanged from the general statistical convention.
`notes/uni-programme-anchors.md` calls this a missing root for IFRS 9's forward-looking
conditioning. That is true, and it names a content gap rather than a notation one. Nothing in
the material read spells the backward shift operator or the ARIMA orders differently across
domains, so there is no collision for an object entry to resolve.

### Credibility, seeded

UP WST 322 lists credibility theory as module content, and SP8 topic 4 asks a candidate to
compare the Classical and Bayes credibility models. That much only confirms the topic exists,
which on its own would not clear the seeding bar above. The trunk lectures do, directly.

`credit_lectures/06_credit-covariate-engineering.qmd`, lines 584 to 587, gives Bühlmann
credibility in exactly its classical two-parameter form:

```
\overline{y}^{\rm cred}_k = \alpha_k \overline{y}_k + (1 - \alpha_k) \overline{y},
\alpha_k = \frac{n_k}{n_k + \tau} \in (0, 1]
```

`credit_lectures/10-11_credit-transformer.qmd`, lines 1101 to 1116, then names the collision
this creates inside the corpus's own trunk material. That lecture fixes $\alpha \in [0, 1]$
and draws $Z \sim \text{Bernoulli}(\alpha)$ as a gate between two tokens, then adds what it
calls "a notation warning": lecture 6's $\alpha_k$ carries a subscript and is a credibility
weight on the data, while lecture 10 to 11's bare $\alpha$ is a gate probability, a different
kind of object. The lecture's own words, quoted rather than adopted, are that "the classical
actuarial literature also writes the Bühlmann credibility factor as $Z$", and that in this
lecture "$Z$ is the Bernoulli variable and never a credibility factor" (line 1116). The
credibility weight and the Bernoulli gate are one symbol carrying two live meanings inside
material this corpus will transcribe, which is the same shape of collision the hazard and the
regularisation weight already resolve.

`obj.credibility-weight` seeds two aliases. `gi`, symbol `Z`, carries the classical Bühlmann
spelling that WST 322 and SP8 teach. `ml`, symbol `\alpha_k`, carries the trunk's own
subscripted spelling, with a note recording why the subscript is not optional here. Bare
alpha is already the gate probability in the same lecture pair. This leaves a consequence for
Phase 3 worth stating plainly rather than leaving implicit. A node that tags itself `credit`
alone and tries to spend this object will fail check 1, because neither alias sits in that
domain. That is the intended review moment, on the same reasoning Task 4 gives for the
hazard's `ml` alias. The trunk's credibility material is lectures written for an `ml`
audience about a `credit` dataset, and the alias belongs where the symbol is actually spelled
that way.

One symbol is deliberately left unclaimed. `credit_lectures/R2_credit-irb-capital.qmd` uses
$Z_u$ for the Vasicek systematic factor, in the `credit` domain, which is a plausible future
contract object in its own right. The `gi` alias seeded here does not block it, since the
domain and the meaning both differ and check 2 is scoped per domain.

### Ruin theory, rejected

CM2 topic 4.1 names the adjustment coefficient and Lundberg's inequality directly, and UP
WST 322 lists ruin theory as module content, so the topic is confirmed in both bodies. The
primary reason to reject seeding it now is that no braid or lecture in the current plan
spends this vocabulary, unlike credibility's Credibility Transformer or the reserving
objects' claims-reserving braid. `notes/uni-programme-anchors.md` gives neither ruin theory
nor its adjustment coefficient a landing point in the graph. A second reason follows from
the same evidence gap as the multi-state candidate. The adjustment coefficient is
conventionally denoted $R$ in the wider actuarial literature, which would pre-collide with
`obj.asset-correlation`'s credit alias `R`, but nothing in the syllabus texts or the trunk
lectures read for this sweep states the symbol, so recording it here would rest on recall
rather than a source this sweep can point to. Phase 3 should confirm the symbol against a
primary ruin-theory source before any node spends it, precisely because of that collision
risk. The capital row below shows the risk is real rather than hypothetical. Bare $R$ is
already unavailable in the trunk's own credit lecture series, since
`S1_credit-survival-bridge.qmd` spends it, subscripted, on a four-level exit category.

### Interest and discount, rejected

CM1 topics 1 and 2 add annuity and accumulation functions well beyond the discount factor:
$a_n$, $s_n$, the force of interest, and the rate of interest or discount payable $p$-thly,
$i^{(p)}$ and $d^{(p)}$. `obj.discount-factor` already resolves the one real collision this
area of the syllabus touches, $v$ as the actuarial discount factor against the
general-insurance exposure weight, recorded in that object's own note. Nothing else CM1 adds
is spelled differently by another domain in this corpus. The annuity functions are
actuarial-only notation, so an entry for them would be a glossary row rather than a bridge
row.

### Capital, verified rather than seeded

F107 topic 10 lists risk-weighted assets and topic 3.3 lists correlation as banking-risk
content, confirming the topic. `credit_lectures/R2_credit-irb-capital.qmd`, lines 94 to 119,
is worth reading in full for what it confirms rather than what it adds. On the correlation,
lines 99 to 100: "This series writes $\rho$. The regulation writes $R$. They are the same
quantity, and the letter $R$ is already spent in this series as lecture S1's four-level exit
variable, so $\rho$ stays." That reason for keeping $\rho$ is stronger than a mere
preference. `S1_credit-survival-bridge.qmd`, line 148, already uses $R_{ij}$, subscripted,
for a four-level competing-risks exit category, so bare $R$ was unavailable in this lecture
series before Basel's own use of it was even a consideration. Lines 95 to 96 add that the
regulation writes $N(\cdot)$ and $G(\cdot)$ where this corpus's canonical spelling is
$\Phi(\cdot)$ and $\Phi^{-1}(\cdot)$. All three, the correlation and the two normal
functions, are `obj.asset-correlation` and the pair `obj.normal-cdf`, `obj.normal-quantile`,
seeded already in Task 2. R2 is a direct, independent confirmation that the seeded aliases
already match the trunk's own working convention.

R2 does add symbols beyond those three objects: the capital requirement per unit of exposure
$K$, the risk-weighted exposure amount $\mathrm{RWA}$, and expected and unexpected loss
(lines 83 to 84). None of them is spelled differently anywhere else in the material read for
this sweep, general insurance and life included, so under the rule above they are glossary
entries rather than bridge entries, and this sweep does not seed them.

## One candidate beyond the six

SP9 lists "Tail Value at Risk (TVaR)" and "Expected shortfall" as separate bullet points
under its risk-measurement content. For a continuous loss distribution the two coincide, so
this looked, before checking, like a same-object-two-spellings candidate the brief's six did
not name. SP9 itself argues against seeding it. The syllabus lists both terms as distinct
named measures rather than presenting one as the other domain's spelling of the same thing,
and nothing in the material read splits the two terms cleanly by domain, the way "chain
ladder" and "roll rate" split cleanly between general insurance and credit. Rejected under
the same rule as the six above.

## Outcome

One object is seeded beyond the four reserving ones the brief specifies:
`obj.credibility-weight`. The contract carries 17 objects after this task, one more than the
16 the count test requires as a floor.

Two rejected candidates, multi-state Markov and ruin theory, share a specific unresolved
risk worth flagging for whoever writes the corresponding node in Phase 3. Both would want a
symbol already claimed elsewhere in the contract, `i` and `j` in the `credit` domain for a
Markov braid, and `R` in the `credit` domain for a ruin-theory braid, so `objects.yaml` will
need the same review Task 4 gave the hazard's `ml` alias before either node can spend the
symbol its own field expects.
