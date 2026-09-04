# KaTeX compatibility sweep

This report covers the sweep run on 3 September 2026, against KaTeX 0.16.11 (the
version recorded in `vendor/katex/VERSION`). The sweep passes every mathematics
span in a `.qmd` file through KaTeX's own parser with `throwOnError: true`,
rather than grepping for a list of suspect commands, because KaTeX itself is the
only authority on what it accepts. Run against the sibling repository's credit
lecture corpus, it found 1,760 spans across eighteen `.qmd` files. KaTeX
accepted all of them, so the sweep returned zero unsupported spans.

The task brief and description both describe the corpus as seventeen lectures
held in seventeen files. The glob `../actuarial_deep_learning/credit_lectures/*.qmd`
returned eighteen files at the time the sweep ran. Git history in the sibling
repository shows five of those eighteen files were first committed on
3 September 2026, the same day this task ran: `09_credit-localglmnet.qmd`,
`10-11_credit-transformer.qmd`, `D1_credit-default-definition.qmd`,
`F1_credit-classing-and-characteristic-analysis.qmd` and
`R3_credit-sampling-and-representativeness.qmd`. The seventeen-file count in the
brief had most likely already gone stale by the time of the sweep, since the
corpus was still growing on the day the brief was written. This is worth
flagging to the task owner rather than reconciling silently. The sweep ran over
every file the stated glob matched, and the finding holds regardless of which
count is authoritative.

A preliminary grep, verified independently as part of this task, confirmed the
brief's finding. The corpus carries three MathJax environments. `\begin{gathered}`
appears twice, in `03_credit-deep-learning-overview.qmd`. `\begin{cases}` appears
once, in `S1_credit-survival-bridge.qmd`. `\begin{aligned}` appears once, in
`07_credit-calibration.qmd`. None of `\label`, `\eqref`, `\require`, `\tag`,
`\newcommand`, `\mathrlap` or `\bm` appears anywhere in the eighteen files. KaTeX
supports all three environments, and the sweep confirms it: every span
containing one parsed cleanly, along with everything else in the corpus. There
is nothing to record in a construct-and-replacement table for Phase 4, because
no substitution is needed anywhere in the corpus as it stands today.

## Span and file counts, per file

A sweep that finds nothing because it extracted nothing looks identical to a
clean sweep, so the per-file breakdown below is the evidence that the
extraction did real work. No file returned zero spans.

| File | Spans |
|---|---:|
| `01_credit-use-case.qmd` | 223 |
| `02_credit-edf-glm.qmd` | 233 |
| `03_credit-deep-learning-overview.qmd` | 57 |
| `04-05_credit-fnn.qmd` | 76 |
| `06_credit-covariate-engineering.qmd` | 110 |
| `07_credit-calibration.qmd` | 45 |
| `08_credit-icenet-regularisation.qmd` | 131 |
| `09_credit-localglmnet.qmd` | 48 |
| `10-11_credit-transformer.qmd` | 148 |
| `C1_credit-interaction-and-causation.qmd` | 12 |
| `D1_credit-default-definition.qmd` | 109 |
| `F1_credit-classing-and-characteristic-analysis.qmd` | 23 |
| `R1_credit-ifrs9-pit-pd.qmd` | 178 |
| `R2_credit-irb-capital.qmd` | 100 |
| `R3_credit-sampling-and-representativeness.qmd` | 71 |
| `S1_credit-survival-bridge.qmd` | 87 |
| `S2_survival-insurance-to-credit.qmd` | 63 |
| `S3_deep-survival-credit.qmd` | 46 |
| **Total** | **1,760** |

## Command run

```bash
.venv/bin/python scripts/katex_sweep.py ../actuarial_deep_learning/credit_lectures/*.qmd
```

## Raw sweep output

```
1760 spans across 18 files, 0 unsupported
```
