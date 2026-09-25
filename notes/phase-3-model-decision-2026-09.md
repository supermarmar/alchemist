# Phase 3 model decision

Measured on 25 September 2026 to the rule in section 5 of
`docs/superpowers/specs/2026-09-19-alchemist-phase-3-pages-design.md`, which was fixed before
either arm ran. Both arms wrote the same ten survival-area pages from
`notes/phase-3-pages-brief.md`, into staging directories named by arm letter; the graders ran on
Opus 5.5 and saw letters only, as did the blind read.

The blind read saw fresh labels. The arm letters had appeared beside their models in the
executing session's own output, so the three drawn pairs were copied to
`.staging/phase-3/measurement/blind/` as `<id>-x.md` and `<id>-y.md`, each pair's order set by
an unprinted random draw and sealed in `blind-key.yaml`. Mario read x and y only.

## The ten nodes

- `future-lifetime-random-variable`: root, no article, life and stats.
- `life-table`: root, no article, life and stats.
- `lifetime-distribution-function`: depth 1, no article, credit, life and stats.
- `survival-hazard-relationships`: depth 2, no article, life and stats.
- `censoring`: root, one article, credit, life and stats.
- `empirical-survival-function`: depth 1, no article, life and stats.
- `kaplan-meier-estimator`: depth 2, no article, life and stats.
- `nelson-aalen-estimator`: depth 2, no article, life and stats.
- `proportional-hazards-model`: depth 2, one article, life and stats.
- `survival-model-credit-risk`: root, one article, credit and stats.

## Template filter

arm-a: 10 of 10 passed `write_page.py --check`. arm-b: 10 of 10.

## Grades

Counts are criteria at that verdict, one per criterion per file, from each arm's
`grading-report.md`. `J25` takes a file's worst section.

| Criterion | arm-a fails | arm-a warns | arm-b fails | arm-b warns |
|---|---|---|---|---|
| `M10` serial comma | 1 | 0 | 5 | 0 |
| `J16` subject and verb apart | 0 | 2 | 1 | 1 |
| `J17` negated counterpart | 4 | 0 | 2 | 0 |
| `J18` unpacking colon | 1 | 2 | 0 | 0 |
| `J25` connective density | 0 | 6 | 1 | 9 |
| `J28` unnamed source | 0 | 0 | 0 | 2 |
| `J30` figurative phrasing | 0 | 1 | 0 | 2 |
| **Total** | **6** | **11** | **9** | **14** |

The two graders ruled differently on two points, and each report states its calls. The arm-a
grader exempted a verbatim node title from `M10` and applied a function test to mid-sentence
"rather than" and "instead of" under `J17`, passing seven spans that contrast a method or a
source. The arm-b grader applied `M10` to the same kind of title citation and failed every
paired counterpart in its arm, a source contrast included.

The verdict below is therefore not robust to the graders' readings. Five of arm-a's seven passed
spans sit in pages carrying no other `J17` fail (`empirical-survival-function`,
`kaplan-meier-estimator`, `life-table`, `nelson-aalen-estimator` and
`proportional-hazards-model`), and its `lifetime-distribution-function` cites the title the
arm-b grader failed under `M10`. Graded on the arm-b grader's calls, arm-a would carry
6 + 5 + 1 = 12 fails against arm-b's 9, exactly the three-fail margin the rule asks of Fable.
Taking only the `M10` call, or only the "instead of" spans, leaves Sonnet ahead. The rubric's
`J17` text leaves the judgement to the grader, so neither reading is plainly wrong.

## Regrade in one pass

The first grades were not robust, since the two graders read `J17` and `M10` differently and on
the arm-b grader's calls the margin reached the rule's threshold. At Mario's instruction both
arms were regraded by one Opus 5.5 grader in a single pass, from clean copies of the twenty
bodies with no earlier report in reach. The grader fixed both rulings from the rubric's text
before opening any page, then applied them identically to both arms.

- **`J17`.** The original forms ("X, not Y") fail on surface form. The added forms ("rather
  than", "instead of", "in place of") take the judgement test the rubric's line 270 requires:
  a span fails where the two halves are rival answers to what the subject is, gives or is for,
  and passes where they are rival choices of input, data source, estimator or operation.
- **`M10`.** A page title reproduced verbatim is a cited title, so the comma the title itself
  lacks is exempt.

| Criterion | arm-a fails | arm-a warns | arm-b fails | arm-b warns |
|---|---|---|---|---|
| `M10` serial comma | 1 | 0 | 4 | 0 |
| `J16` subject and verb apart | 0 | 0 | 1 | 2 |
| `J17` negated counterpart | 5 | 0 | 1 | 0 |
| `J18` unpacking colon | 2 | 0 | 0 | 0 |
| `J25` connective density | 0 | 7 | 2 | 8 |
| `J28` unnamed source | 0 | 0 | 0 | 2 |
| `J30` figurative phrasing | 1 | 0 | 0 | 0 |
| **Total** | **9** | **7** | **8** | **12** |

The regrade supersedes the first grades for the verdict. Reversing the `M10` ruling adds one
fail to each arm and leaves the order unchanged. Reading `J17` on surface form alone would give
arm-a 14 fails against arm-b's 9, but the rubric's line 270 rules that reading out for the added
forms, so it is recorded here and not applied.

## Blind read

| Pair | Preference | Mario's reason |
|---|---|---|
| `life-table` | x (arm-b) | none given |
| `lifetime-distribution-function` | x (arm-b) | none given |
| `empirical-survival-function` | not recorded | the reply named `lifetime-distribution-function` twice |

The draw was `random.Random(20260919).sample` over the ten ids in the order of spec section
5's table, which is the order the list above gives. The unrecorded pair cannot move
the verdict, since arm-b already takes two of three.

## Tokens

| Arm | Input | Output | Source |
|---|---|---|---|
| arm-a | not reported | not reported | harness completion notice: 159,368 tokens in total, 48 tool uses |
| arm-b | not reported | not reported | harness completion notice: 135,665 tokens in total, 21 tool uses |

The notice gives a total with no split between input and output, and the total probably
includes cache reads, so the cost of each arm cannot be computed from it. The list prices
differ fivefold on input and on output alike, so the cost ratio is near four times only if the
two arms split their tokens alike, and the totals alone cannot show that.

## Verdict

arm-a was Sonnet and arm-b was Fable. The key was opened after the first grades were tabulated
and Mario's preferences were in hand, and before this note was written.

Under the rule, applied to the one-pass regrade, Sonnet writes Phase 3. Fable took two of the
three blind pairs but recorded one fail fewer than Sonnet, where the rule requires three fewer,
and both conditions must hold. The first grades gave the same verdict. The blind read preferred
Fable, and the rule was fixed in advance so that a preference could not overturn the grades.

## What the pages showed

Both arms dropped the serial comma in running prose, one page in arm-a and five in arm-b, while
keeping it in their symbol glosses. The brief never stated it, so it now does under Writing
rules.

Both arms drew `J17` fails on a mid-sentence "rather than" or "instead of", four in arm-a and two
in arm-b. The brief and the tool allow one "rather than" per page under G20, while the grader
fails the construction outright, so the brief and the grader disagree. The brief is left alone
here, because tightening it changes the spec's G20 cap and is Mario's decision.

The page statistics report lists three of arm-a's ten as naming none of their unlocks:
`life-table`, `lifetime-distribution-function` and `survival-model-credit-risk`. Read directly,
all three do name one (life table probabilities, the survival, density and hazard
relationships, and the market-implied survival curve). In each the title wraps across a line
break, and the report matches the title without normalising whitespace, so these are false
candidates.
