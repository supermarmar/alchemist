# Decisions I took on your behalf, Phase 0

Written 3 September 2026, at the end of the fourteen-task Phase 0 build of `alchemist`. This is
the complete record of every decision the build made without asking you, in the order it made
them, each with what it costs if it turns out wrong. It lives here rather than in the session's
scratch workspace, because that workspace is deleted at the finish and these should not go with
it.

Read it as a list of things to overturn if you disagree. Reversing any single one would not
unpick the branch. The ones genuinely your call rather than mine are marked
**DECISION FOR YOU**, and each is also recorded in the spec as an open question, so the documents
do not pretend to be settled.

Roughly a third of this branch's commits are corrections to the plan and the spec recording these
decisions as the work went, which is why the plan is a much longer document than it started as.

---

### 1.

branch rather than git worktree, nothing else is in flight in this repo and a worktree adds a
second checkout to manage for no isolation gain. Cost if wrong: none material; a worktree can
be added later without touching history.

### 2.

implementers run model="sonnet"; controller stays Opus at Mario's instruction (3 September
2026), which relaxes his own "implement on Sonnet" rule for the main thread only. Cost if
wrong: controller tokens cost more than necessary.

### 3.

check 1 keys its collision map on object identity, so two spends of the SAME object that
happen to share a rendering across domains pass, and only two DISTINCT objects sharing a
symbol fail. The spec's wording ("no two entries in one node render as the same symbol") is
the defect; the intent throughout section 4.2 is one meaning per symbol, and one object in two
domains is one meaning. Plan amended in T3 with an added test. Cost if wrong: a node could
spell one object two ways in one page without the checker objecting, which a human reviewer
would catch at gate 1.

### 4.

T6 imports only `Objects` into `site.py`, T7 extends that line to `Corpus, Objects` and
`REPO`, and `check_generated_current` imports `render_symbols` at the top of `checks.py`
rather than inside the function. No circular import exists to justify the lazy form. Cost if
wrong: if a future task makes `site.py` import `checks.py`, the top-level import becomes
circular and has to move back.

### 5.

T12's Pages job runs `build_site.py` before `check.py`, so generated artefacts are rebuilt
before the checks verify them and a stale `index.html` cannot publish. Cost if wrong: the job
rebuilds two small files it did not need to.

### 6.

repaired a code fence I broke in Task 6 while applying ruling R2 (two consecutive ```python
openers with no close, which ran Task 6's brief to 1400 lines by swallowing every task after
it). Verified fence balance across the whole plan afterwards. Cost if wrong: none; the defect
was in the plan document only and no implementer had read it yet. BASE for Task 1 revised to
8d37ccf after committing the fence repair separately, so the implementer's `git add -A` could
not absorb my plan edit into its diff.

### 7.

the plan's `tests/test_model.py` imports `Node` and never uses it, which Pyright flagged the
moment the implementer wrote the file. The import is plan-mandated, so the implementer is not
at fault; ruling is to drop it, since an unused import in the first test file of the repo sets
the wrong precedent for eleven later test modules. Passed to the implementer mid-task rather
than held for the review loop. Cost if wrong: none. Task 1: implemented (commit 1e864c4, 5/5
tests passing, output pristine, DONE) Task 1: review dispatched (task reviewer, model=sonnet,
diff review-8d37ccf..1e864c4.diff)

### 8.

Pyright cannot resolve `pytest` or `scripts.alchemist.model` because nothing points it at
`.venv`, which will emit diagnostics on every remaining task. Fixing it in Task 1 would be
scope creep, so it is added to Task 12, where repo configuration belongs. Cost if wrong:
eleven tasks of harmless editor noise. Task 1: complete (commits 8d37ccf..1e864c4, review
clean, spec compliant, Approved) Task 1: minor (deferred): one commit bundles scaffolding with
the model feature. Plan-mandated by the brief's own Step 6 message. For final-review triage.
Task 1: minor (acted on): no committed test exercises `parse_path`. Ruling: `parse_path` is
never exercised by ANY task in the plan (Task 4 constructs `TeachingPath` directly, Task 11
only consumes it through `load_corpus`), so three tests were added to Task 11, where the first
real path files appear. The reviewer's other half, empty-repo `load_corpus`, IS covered by
Task 7's subprocess test and needs nothing. Cost if wrong: three tests in the wrong module.
BASE for Task 2 = a6b5b77 Task 2: dispatched (implementer, model=sonnet, brief
task-2-brief.md, report task-2-report.md) Task 2: implemented (commit 6d08199, 5/5 new and
10/10 full suite passing, DONE, no concerns) Task 2: review dispatched (task reviewer,
model=sonnet, diff review-a6b5b77..6d08199.diff) Task 2: complete (commits a6b5b77..6d08199,
review clean, spec compliant, Approved) Task 2: minor (acted on): the reviewer noted
`KeyError` is a subclass of `LookupError`, so a bare try/except in Task 3 would collapse the
two failure modes the contract distinguishes. Checked the plan: Task 3's code guards with an
explicit `if spend.object not in objects.by_id` BEFORE calling `rendering`, so `KeyError`
never reaches the `except LookupError`. No amendment needed; carried into Task 3's dispatch as
a warning against "simplifying" that guard away. BASE for Task 3 = 6d08199 Task 3: dispatched
(implementer, model=sonnet, brief task-3-brief.md, report task-3-report.md) Task 3:
implemented (commit c3d818a, 7 new and 17 full suite passing, DONE)

### 9.

the implementer flagged that Task 3's step 4 predicted "6 passed" while its own step 1 lists
seven tests. My error: ruling R1 added the eighth test case without updating the count.
Corrected the plan to 7. The implementer used the code verbatim as instructed and was right to
flag rather than drop a test to match the prose. Cost if wrong: none, documentation only. Task
3: review dispatched (task reviewer, model=sonnet, diff review-6d08199..c3d818a.diff) Task 3:
review returned spec compliant and Approved, with two Important findings, both plan-mandated
and both about my test file's inability to catch a regression rather than about the
implementer's code.

### 10.

fix both now in Task 3 rather than deferring to "a plan amendment", because checks.py is Task
3's own deliverable, four later tasks append to it, and a deferred amendment with no task
attached does not happen. The reviewer's analysis is correct on both: (1) `"obj.ghost" in
failures[0]` also passes under the bare-except bug, since KeyError is a LookupError subclass
and its message is `"n: 'obj.ghost'"`, so the assertion now matches the prefix "spends unknown
object"; (2) check 1's domain-membership branch had zero coverage and could be deleted with
every test still green, so a test was added. Plan amended to 9 tests. Cost if wrong: two extra
tests in a file that already exists. Task 3: minor (deferred): `Result.ok` is unexercised.
Task 7's runner consumes it; for final review triage. Task 3: fix round 1/5 dispatched
(original implementer resumed; FIX_BASE c3d818a)

### 11.

my fix message predicted 9 tests; the implementer verified 8 and was right (7 original,
finding 1 replaces one in place, finding 2 adds one). It applied both fixes verbatim rather
than adjusting tests to hit my number, which was correct. Plan corrected to 8. Cost if wrong:
none, documentation only. Task 3: fix round 1/5 (commits c3d818a..5895505, 8 file tests and 18
suite passing); scoped re-review dispatched (model=sonnet, diff review-c3d818a..5895505.diff)
Task 3: complete (commits 6d08199..5895505, 1 fix round, review clean, both findings
ADDRESSED) BASE for Task 4 = f068993 Task 4: dispatched (implementer, model=sonnet, brief
task-4-brief.md, report task-4-report.md) Task 4: implemented (commit 517d52a, 10 new and 28
suite passing, DONE) Note (no action): the implementer flagged that the brief names
`check_requires_resolve_and_acyclic` as the RED ImportError symbol while Python named
`check_path_teachability`, which is simply the first name in the test file's import tuple.
Both were absent, so the failure was for the expected reason. Not worth a plan amendment. Task
4: review dispatched (task reviewer, model=sonnet) Task 4: review returned spec compliant but
Needs fixes, with two Important findings, both plan-mandated test-quality gaps proven by the
reviewer building mutant implementations.

### 12.

fix both. (1) `test_builds_on_is_transitive` passed under a one-level closure because `c`
required only the parent's node; `c` now requires the grandparent's too, so the test can only
pass if the walk traverses the chain. (2) the two-path builds_on cycle resolved via the `nxt
== path_id` early return, so the `seen` guard was never exercised; a triangle test was added
where the cycle sits between two paths other than the queried one, which is the only shape the
guard prevents hanging on. Accepted that the triangle test HANGS rather than fails under the
mutant, and said so in its docstring, because the alternative is adding a timeout plugin for
one test. Plan amended to 11 tests. Cost if wrong: a hung CI job instead of a red one, if the
guard is ever removed. Task 4: minor (deferred): the recursive cycle walk has no depth guard
and would raise RecursionError rather than return a Result on a very long chain. Ruling: not
converting a correct algorithm to an explicit stack for a bound that cannot be reached, since
Python's default limit is 1000 frames and the corpus is 400 to 600 nodes whose longest single
prerequisite chain is an order of magnitude shorter. For final-review triage. Task 4: fix
round 1/5 dispatched (original implementer resumed; FIX_BASE 517d52a) Note (no action): the
Task 4 reviewer created two mutant scripts in the working tree despite the read-only
instruction, then removed them itself. Tree verified clean, nothing entered a commit. Worth
watching if it recurs, but its mutant testing found two real gaps that hand reading had missed
in three prior reviews, so the method found what four hand readings did not. Task 4: fix round
1/5 (commits 517d52a..8cc7780, 11 file tests and 29 suite passing, implementer verified both
by mutation); scoped re-review dispatched (model=sonnet) Task 4: complete (commits
f068993..8cc7780, 1 fix round, review clean, both findings ADDRESSED)

### 13.

from Task 5 onward, every implementer dispatch carries a standing instruction to check, for
each test the brief specifies, whether it would actually FAIL under the bug it names, and to
report any that would not rather than shipping it silently. Tasks 3 and 4 each shipped two
such tests and both were caught only at review, costing a fix round each. Moving the check
left is cheaper than two more rounds. Cost if wrong: implementers spend a little longer per
task and may raise a false positive I have to rule on. BASE for Task 5 = 8cc7780 Task 5:
dispatched (implementer, model=sonnet, first dispatch carrying the standing test-
discrimination instruction) Task 5: implemented (commit 8f659b9, 8 new and 37 suite passing,
DONE_WITH_CONCERNS)

### 14.

the standing test-discrimination instruction worked on its first outing. The implementer found
two gaps itself and reported rather than patching, which is what I asked for. Both are real
and both get fixed before review rather than after, saving a review seat. (1) no test covered
`check_gap_closure`'s missing-ledger skip; (2) no test covered the `vault_articles` exemption,
so mutating check 5's loop to walk `vault_articles` too would have stayed green. The second
matters most: that mutation would block purchased material from informing a node at all,
inverting the rule the whole provenance design rests on. Plan amended to 10 tests. Cost if
wrong: two extra tests. Note (no action, third occurrence): the brief's predicted RED
ImportError names a different symbol than Python reports, because Python resolves an import
tuple left to right. Cosmetic in every case so far. Not amending the plan for it. Task 5: pre-
review fix dispatched (original implementer resumed; addressing its own two reported gaps
before the review seat, FIX_BASE 8f659b9) Task 5: fix landed (commit ac128de, 10 file tests
and 39 suite passing); combined review dispatched over 8cc7780..ac128de (model=sonnet) Task 5:
complete (commits 8cc7780..ac128de, review clean, spec compliant, Approved, 0 fix rounds after
the pre-review fix) Task 5: minor (deferred): `_register_entry` returns None both when a
register file is absent and when its frontmatter fails to parse, and both land on the message
"is not in the vault register", which is untrue for the second. Worse, `yaml.safe_load` on a
scalar or list frontmatter yields a non-dict, so `entry.get(...)` raises AttributeError
instead of failing closed. One `isinstance(entry, dict)` guard plus a distinct message fixes
both. For final-review triage. Task 5: minor (deferred, self-closing): no test covers
`check_gap_closure`'s `.get()` returning None, which is the live state of the real
`sources/wanted.yaml` today (needed_by names `compound-interest`, a node Phase 0 never
creates).

### 15.

no change. Task 7's `test_check_py_exits_zero_on_the_real_repo` runs `check.py` against the
real repo, where that entry names a node `nodes/` does not contain, so swapping `.get()` for a
strict lookup would raise KeyError, exit non-zero and fail that test. The gap closes at Task 7
without a new test, and Task 7's dispatch will say that its subprocess test is load-bearing
for more than it appears. Cost if wrong: the path stays untested until someone removes that
test. Note (no action): the reviewer corrected my prompt's per-file figure, 75 insertions and
1 deletion in checks.py rather than 2, the second deletion being in the plan document. Right.
BASE for Task 6 = ac128de Task 6: dispatched (implementer, model=sonnet, brief
task-6-brief.md) Task 6: implemented (commit cf2b638, 5 new and 44 suite passing,
DONE_WITH_CONCERNS)

### 16.

three findings, all from the implementer, all accepted. (1) my stability test
`test_the_output_is_stable_across_calls` passed with `sorted()` removed, because a dict walks
in insertion order deterministically within one process, so it never tested the ordering it
was named for. Replaced with a test that inserts two objects out of id order and asserts the
rendered order. (2) my drifted test matched on "build_site", which BOTH messages contain, so
it would pass if the drifted case wrongly emitted the missing message. Now matches "drifted".
(3) the implementer removed an unused `from pathlib import Path` from site.py, which was
right, and that cascades: Task 7's `build()` and `render_node_page` need `Path` for their
annotations, so Task 7's instruction now says to re-add it. Cost if wrong: Task 7 has one more
import line to write.

### 17.

Pyright flagged a fourth finding on Task 6 that neither the implementer nor I caught: my
`tests/test_site.py` block imports `pathlib.Path` and never uses it, since the tests take the
`tmp_path` fixture. Same defect class as Task 1's unused `Node`. Removed. That makes two
unused imports I wrote into plan test code, so the pattern is mine rather than any
implementer's. Cost if wrong: none. Task 6: pre-review fix dispatched (original implementer
resumed; three test-side fixes, FIX_BASE cf2b638) Task 6: fix landed (commit 1a0e3ec, 5 file
tests and 44 suite passing, both mutations verified); combined review dispatched over
ac128de..1a0e3ec (model=sonnet) Task 6: complete (commits ac128de..1a0e3ec, review clean, spec
compliant, Approved, ZERO findings at any severity, first task with none. The reviewer also
checked out of diff whether `Objects.__init__` pre-sorts, which would have made the new
ordering test pass even with `sorted()` removed; it does not, so the test genuinely exercises
render_symbols.) Pending (parallel): Mario forked a subtask to read his university syllabus
and yearbook PDFs and advise what to incorporate and where, flagging claims modelling with
run-off triangles as a likely gap. Not duplicating that work here. When it reports, fold the
answer into Phase 1's syllabus list rather than Phase 0, which is machinery only. BASE for
Task 7 = 1a0e3ec Task 7: dispatched (implementer, model=sonnet, largest task in the plan,
395-line brief) CORRECTION: BASE for Task 7 is 68c1ffa, not 1a0e3ec. The syllabus fork
committed notes/uni-programme-anchors.md onto this branch between Task 6's head and Task 7's
work, so the earlier BASE would have pulled that note into Task 7's review diff.

### 18.

the fork's verdict stands, incorporate as two Phase 1 anchor bodies and change nothing in
Phase 0. It verified the Task 1 anchor grammar already accepts `up.ias121.3` and three
siblings, so no schema amendment and no reopening of a reviewed task. Its four Phase 1
requirements live in notes/uni-programme-anchors.md and are not duplicated here.

### 19.

one spec correction accepted from it, because the spec overstated what the notation seed
covers. The twelve objects were derived from the ETH course's MODELLING frame, so GI reserving
vocabulary (cohort index, development index, development factor, ultimate) is absent by
construction rather than by oversight. Section 4.2 now says so, and Phase 1 sweeps for other
vocabularies the trunk's frame omits. Declined to amend Task 2: it is reviewed and closed, and
the contract is designed to grow. Cost if wrong: the four objects arrive in Phase 1 rather
than now, which is where the nodes that need them arrive anyway. Flagged for verification: the
fork asserts chain ladder reserve estimates coincide with the MLE of an over-dispersed Poisson
GLM with log link and additive accident and development effects (Mack 1991; Renshaw and
Verrall 1998), which would hang claims reserving directly off ETH lecture 2. It flagged this
as needing a direct vault read before any node relies on it, per ~/.claude/rules/subagent-
verification.md. Do NOT let a node cite it until that read happens. Task 7: implemented
(commit cb708c2, 8 new and 52 suite passing, DONE_WITH_CONCERNS)

### 20.

both substantive concerns accepted and fixed before review. My
`test_the_index_lists_every_path_and_counts_the_nodes` asserted "2 nodes" against a corpus of
exactly two nodes, so the summary sentence "2 nodes, 0 of them taught in full" satisfied the
assertion and deleting the per-path count entirely still passed. The corpus now holds three
nodes against a two-node path, so the two figures are different strings, and the third node
carries `taught_in` so the "taught in full" figure gets its first coverage. That is the
seventh non-discriminating test of mine found across five tasks. Cost if wrong: none. Task 7:
minor (deferred): `render_index` emits "across 1 paths" when there is one path. Ungrammatical
on the corpus's front page. Declined to fix inside a test-only fix round rather than expanding
scope into reviewed code. For final-review triage. Note (no action, fifth occurrence): brief's
predicted RED symbol differs from Python's, an artefact of import ordering. Task 7: pre-review
fix dispatched (original implementer resumed; FIX_BASE cb708c2) Task 7: fix landed (commit
c49855b, 8 file tests and 52 suite passing, mutation verified) Task 7: review dispatch 1
FAILED (agent stalled, no progress for 600s, watchdog did not recover). Infrastructure rather
than the task. Re-dispatching once with the same brief; if it stalls again, split the review
into two passes, the checks-and-CLI half and the generators half, since the diff is 33 kB and
the largest in the plan. Task 7: review dispatch 2 sent (model=sonnet, same diff, told the
previous reviewer stalled). Verified myself: `.venv/bin/python scripts/check.py` reports ok on
all seven rules against the real repo, 0 nodes, 0 paths, 0 failures. Check 5 says ok rather
than SKIP, so the vault is present at the default path and its register directory resolves.
The entry point works end to end; the review is about whether it is right and well-built. Task
7: review dispatch 2 returned spec compliant but Needs fixes, with two Important findings,
both plan-mandated and both in PRODUCTION code rather than tests, a first for this plan.

### 21.

fix both, and a third the reviewer only half-found. (1) Every generator interpolates author-
supplied strings straight into markup with no escaping. That matters here specifically because
the corpus is mathematical and the repo is public: "PD < 1%" is ordinary credit-risk prose and
corrupts a page the moment real content lands, and a double quote in a node title ends a DOT
label early so `dot` fails on the rest of the line. (2) `build()` uses `check=True`, which
converts a non-zero exit into CalledProcessError and does nothing for the FileNotFoundError a
missing `dot` binary raises, so a stranger cloning this public repo without graphviz gets an
opaque traceback. (3) the reviewer rated the CSS path mismatch Minor because it is inert
today; tracing it showed the same bug in the lecture link, and both bite the moment Task 8
lands `assets/lecture.css` at the repo root. A page in `site/paths/` is two levels down, so
`../assets/` resolves to `site/assets/` and `../lectures/` to `site/lectures/`, neither of
which anything creates. Raised to fix now rather than leaving a known-broken link for a later
task to trip over. Task 7: minor (acted on): `build_site.py`'s docstring claimed it verifies
the checks, which `main()` never does. Corrected in the same round, since a reader trusting it
would skip running check.py. Plan amended with Task 7 steps 8 and 9, plus three tests covering
escaping, the DOT label and the two-levels-down paths. Task 7: fix round 1/5 dispatched
(original implementer resumed; escaping, three relative paths, missing-dot handling,
docstring; FIX_BASE c49855b) Task 7: fix round 1/5 (commits c49855b..394a69f, 11 file tests
and 55 suite passing; implementer verified the DOT-escaped label round-trips through the real
`dot` binary to valid SVG, and that `build()` raises a clear error with `dot` stripped from
PATH); scoped re-review dispatched Note (my error, corrected): my step text predicted
regenerating would change `index.html`'s bytes. It did not, because the corpus is empty in
this phase so there is no author-supplied text on the index for the escaping to alter. The
implementer's explanation was right and the plan now says so. Task 7: complete (commits
68c1ffa..394a69f, 1 fix round, all findings ADDRESSED, no new breakage) Task 7: the re-
reviewer independently reproduced both verification claims rather than accepting them: it
piped the quoted-title DOT output through the real `dot -Tsvg` and it parsed, and it
reproduced the except block with PATH stripped and confirmed the actionable message with the
original as __cause__. It also computed that escaping backslash before double quote is the
order that survives a round trip, and that the reverse corrupts it. Task 7: the re-reviewer
caught a FACTUALLY WRONG claim in the implementer's self-review, the first in seven tasks: the
report said `MarkdownIt()` defaults to `html=False`. It does not, the default is `html=True`
per CommonMark, so a recognised raw HTML tag in a node body passes through unescaped.

### 22.

(deferred to the final fix wave, and MUST be fixed there rather than merely triaged)
`render_node_page` calls `MarkdownIt().render(node.body)` with the library default
`html=True`. Two consequences. On a public repo publishing to Pages, raw markup in a body
reaches the page verbatim, and Phase 3 has agents writing roughly 500 bodies from vault
content. More immediately, this is a MATHEMATICAL corpus: a body carrying `$a <b$` risks the
`<b` being consumed as a tag, silently corrupting mathematics on a published page. The fix is
one argument, `MarkdownIt(options_update={"html": False})`, plus a test. Not extending Task
7's loop for it, because the skill's discipline is that out-of-scope observations do not
extend a fix loop, and not putting it in Task 11 either, because that task is content rather
than machinery. Cost if wrong: one round in the final wave instead of now. BASE for Task 8 =
8c5f857 Task 8: dispatched (implementer, model=sonnet; vendoring, font embedding,
inline_assets) Task 8: implemented (commit 4aeb85b, 4 new and 59 suite passing, DONE)

### 23.

three concerns, all accepted, one of them a cross-task catch. (1) The implementer noticed that
`test_no_external_reference_survives` passes only against its inert stub, because the REAL
`vendor/katex/katex.min.js` contains a legitimate `src=` substring in its own image-rendering
code. Its own test is fine, but my Task 9 test used the same `'src="' not in html` form and
would have failed spuriously the first time a genuine asset was inlined. Task 9's test now
asserts the specific vendor and asset paths are absent, plus two positive checks that maths
and the stylesheet survived. That is a defect found one task before it would have fired. (3)
The missing-asset test asserted only that the exception fires, not that the file was left
untouched, so a half-writing implementation would pass while leaving a corrupt lecture for the
printer. Added an on-disk assertion, which needs `import pytest` in that test file. Cost if
wrong: one extra assertion. Task 8: no action on concern 2. `vendor/katex/fonts/` keeps all 60
files after embedding, as `katex_embed_fonts.py`'s re-run input. They are strictly redundant
once the data URIs are in the stylesheet, since restoring the original CSS means re-vendoring
anyway, but they are harmless and deleting them would make the script non-rerunnable after a
`git checkout` of the CSS. Recorded for final-review size triage rather than spending a round.
Task 8: pre-review fix dispatched (on-disk assertion only; FIX_BASE 4aeb85b) Measured the
vendored KaTeX, which sharpens the concern-2 ruling with real numbers: katex.min.css 359 kB
(20 woff2 faces base64-embedded, zero `url(fonts/` references remaining), katex.min.js 269 kB,
fonts/ 1.1 MB across 20 ttf, 20 woff and 20 woff2. Per-lecture inlined payload is therefore
roughly 630 kB, which is the price of a page that opens with no network and is acceptable;
`lectures/*.html` is gitignored so it costs the repo nothing, and the trunk repo's Pages site
already carries 30 MB.

### 24.

(final fix wave, not now) `katex_embed_fonts.py`'s regex matches `.woff2` only and it strips
the woff and ttf `url(...)` sources from the CSS, so the 40 ttf and woff files are referenced
by nothing, ever. Deleting them saves about 850 kB and keeps the script rerunnable, since it
reads only the woff2. I am not reopening the round for it, having already told the implementer
concern 2 needed no action, and reversing that mid-round is churn. Queued for the final wave
with the measurement attached so it cannot be triaged away on a guess. Task 8: fix landed
(commit 15302a2, 4 file tests and 59 suite passing, mutation verified by writing incrementally
and confirming the on-disk assertion fails)

### 25.

built a vendor-excluded review package for Task 8 rather than handing the reviewer the full
diff. The full range is 697 kB of which 657 kB is minified third-party KaTeX and binary fonts;
excluded it runs to 41 kB. A reviewer told to read the diff once cannot usefully read 657 kB
of minified vendor code, and reviewing third-party bytes is not what a review seat is for.
Verified the vendored content myself instead: VERSION reads 0.16.11, katex.min.css carries
exactly 20 `data:font/woff2;base64` occurrences and zero `url(fonts/` references, katex.min.js
is the expected UMD bundle, and assets/lecture.css is byte-identical to the trunk repo's
sheet. Told the reviewer to take those as established. Cost if wrong: nobody independently
reads the vendored bytes, which is the normal treatment for a pinned dependency. Task 8:
review dispatched (model=sonnet, vendor-excluded diff) Task 8: complete (commits
8c5f857..15302a2, review clean, spec compliant, Approved, no Critical or Important findings)

### 26.

the reviewer's ⚠️ is real and goes to Task 9. `assets/lecture.css` was copied byte-for-byte
from a repo that renders with MathJax, so its only maths rules target `.math.display` and
`mjx-container[display="true"]` at lines 670, 677 and 791. KaTeX wraps a display equation in
`.katex-display`, which no rule mentions, so a wide equation may overflow the column unboxed
instead of scrolling. Byte-identity was the means of carrying the sheet across rather than the
goal, so Task 9 now confirms the symptom against its own rendered probe and adds `.katex-
display` to all three selector lists if it fires. Cost if wrong: one CSS selector nobody
needed.

### 27.

the same Task 9 step rewrites the sheet's header comment, which as copied reads "Deep Learning
for Actuarial Modeling, Milano 2026 / Shared presentation layer for the seven Quarto lecture
documents". That describes the other repo rather than this corpus and carries an American
spelling this repo forbids. The reviewer recommended no action on the spelling because byte-
identity was mandated; since the KaTeX fix breaks byte-identity anyway, fixing the header in
the same breath is free and makes the provenance accurate. Task 8: minor (deferred): `inline`
splices asset text between `<style>` and `<script>` tags with no check for an embedded closing
tag. Verified dormant today across all three assets, and a base64 woff2 payload cannot contain
`<` at all, but a future KaTeX bump or lecture.css edit could introduce one and the browser
would terminate the element early with exit code 0, which is the exact failure class this task
exists to remove. A `if "</style>" in body: raise` guard matches the module's fail-loudly
design. For the final fix wave. BASE for Task 9 = 5efa1c8 Task 9: dispatched (implementer,
model=sonnet; render and print chain, plus the Step 4 stylesheet judgement) Task 9:
implemented (commit 4fc759e, 3 new and 62 suite passing, DONE; confirmed the KaTeX display
symptom and added .katex-display to both selector lists at lines 672 and 793, and rewrote the
stylesheet header with accurate provenance and British spelling) Task 9: review dispatched
(model=sonnet; told to check the Step 4 stylesheet change is justified by an observation
rather than by my suggestion) Task 9: complete (commits 5efa1c8..4fc759e, review clean, spec
compliant, Approved) Task 9: the reviewer verified the four-edits constraint by diffing both
scripts against the sibling repo's originals itself, and confirmed the watchdog and %%EOF
check byte-identical. It also confirmed the Step 4 stylesheet change rests on a real
measurement rather than on my suggestion: the implementer recorded that `.math.display`
computes to `display: inline` with scrollWidth and clientWidth both 0, so `overflow-x: auto`
never engages on it, while `.katex-display` is the real block box at scrollWidth 231 against
clientWidth 172.

### 28.

the Important finding gets a real test, in Task 11 rather than by reopening Task 9.
`test_the_pdf_is_complete` checks size and the %%EOF trailer, neither of which can see a PDF
whose maths snapshot fired before KaTeX finished: such a file is complete, correctly trailed
and A4 while showing raw \frac{}{}. That is the exact failure the chain exists to remove, and
the sibling repo's own CLAUDE.md concedes it cannot be checked without a PDF text extractor.
Task 11 now adds `pypdf==5.1.0` and a test extracting the printed exemplar's text, asserting
no backslash command survived and that extraction worked at all. Task 11 is the right home
because it prints the first lecture with figures, which is when a 5-second BUDGET could fire
early; Task 9's probe was equation-only and was verified by a human read. Cost if wrong: one
small pure-Python dependency. Task 9: minor (deferred): both carried-over scripts' `Usage:`
blocks still show `credit_lectures/*.qmd` examples from the sibling repo, contradicting the
rewritten header that says "One directory goes through here, `lectures/`". Outside the four
authorised edits, so correctly left. For the final fix wave. BASE for Task 10 = 13b151b Task
10: dispatched (implementer, model=sonnet; KaTeX sweep over the seventeen sibling lectures)
Task 10: implemented (commit e2ce340, 4 new and 66 suite passing, DONE_WITH_CONCERNS) Task 10
RESULT, the most useful de-risking in the plan: 1,760 maths spans across every source lecture,
ZERO unsupported by KaTeX. That confirms the preliminary grep's prediction against the real
parser and means Phase 4 inherits no MathJax-to-KaTeX migration debt.

### 29.

my "seventeen credit lectures" count is stale, and the implementer was right to flag it. The
sweep found eighteen `.qmd` files, because the sibling repo is under active development and
five lectures landed in it during this session. Rather than chase the number, both the plan
and the spec now carry a caveat saying the count is a moving target and is not load-bearing,
since every script and sweep globs the directory rather than counting it. Cost if wrong: none.
Task 10: minor (no action) on the two discrimination gaps the implementer found by mutation.
`test_fenced_code_is_not_scanned`'s first assertion is dead weight on its fixture while the
second does catch a broken fence-blank, so the property IS covered. And no test catches a
broken display-before-inline blanking order because, as it worked out, `$$` pairs are
structurally immune to the INLINE regex: its lookarounds plus its no-newline constraint mean a
`$$` on its own line cannot match. So my brief's claim that the ordering is load-bearing was
wrong; it is belt-and-braces against a future relaxation of that regex, which is worth keeping
and not worth a test for a property that cannot currently be broken.

### 30.

(final fix wave) the implementer found a latent false positive worth a docstring line. A line
carrying two currency amounts, "between $1 & $2", extracts "1 & " as a maths span, and `&`
outside an array is a KaTeX error, so the sweep would fail spuriously. None exists in today's
corpus. The corpus convention should be to write currency with the unit word rather than a
bare dollar sign, and the sweep's docstring should say so. Queued rather than reopening. Task
10: review dispatched (model=sonnet; told the headline result's credibility rests entirely on
throwOnError: true) Controller verification of Task 10, independent of both the implementer
and the reviewer, and the strongest evidence in the plan so far. Confirmed `throwOnError:
true` and `strict: "warn"` in scripts/katex_check.mjs, re-ran the sweep over one lecture (87
spans, 0 unsupported, consistent with 1,760 over eighteen files), then built a NEGATIVE
CONTROL in the scratchpad: a .qmd carrying one good span, one undefined control sequence in a
display block, and one bare `&` inline. The sweep reported both bad spans and neither good
one, named the display span at line 9 and the inline at line 13, both exactly right against
the source, and exited 1. That proves three things at once: the parser really throws, `_blank`
really preserves line numbers, and frontmatter really is skipped. The headline "zero
unsupported" is therefore a real result rather than a sweep that extracted nothing. Note: the
same control incidentally confirms the deferred currency false positive is a genuine failure
mode, since the bare `&` span did fail. The deferral stands because no such line exists in the
corpus, but the risk is demonstrated rather than theoretical. Task 10: review returned spec
compliant and Approved, with one Important finding, plan-mandated.

### 31.

fix it. The reviewer verified directly that `subprocess.CalledProcessError.__str__()` omits
the captured stderr, printing only the exit status, so a Phase 4 user whose Node harness
crashes gets a traceback with no cause while `exc.stderr` holds the real diagnostic. This is
the SAME failure class I already fixed for the missing `dot` binary in Task 7's `build()`, and
leaving one handled while the other is not would make the codebase inconsistent in exactly the
way that gets noticed later and copied wrongly. Also adding a `FileNotFoundError` branch for a
missing `node`, for the same symmetry, plus a monkeypatched test, since the sweep is the tool
Phase 4 leans on hardest and an untested error path is how a message rots. Cost if wrong: one
more error branch than strictly needed. Task 10: minor (deferred): `main()` recomputes
`extract_spans` per file to print the total, so every file is read and parsed twice. Harmless
at eighteen files, worth having `sweep()` return the count if revisited for Phase 4's larger
corpus. For final-review triage. Task 10: fix round 1/5 dispatched (original implementer
resumed; FIX_BASE e2ce340) Task 10: fix round 1/5 (commits e2ce340..1b4c738, 5 file tests and
67 suite passing, sweep result unchanged at 1,760/18/0, mutation verified against a genuine
broken require path); scoped re-review dispatched Checked myself, since I raised the ordering
question in the re-review brief: `CalledProcessError` derives from `SubprocessError` and
`FileNotFoundError` from `OSError`, and neither is a subclass of the other, so the catch
ordering in `sweep()` genuinely does not matter. Worth recording the contrast with Task 3,
where ordering DID matter because `KeyError` IS a subclass of `LookupError`. The lesson is the
class relationship rather than a general rule about ordering except clauses, and mis-
generalising from Task 3 would have produced a pointless constraint here. Task 10: complete
(commits 13b151b..1b4c738, 1 fix round, all findings ADDRESSED, no new breakage). The re-
reviewer independently confirmed the disjoint exception classes, that the success-path return
sits outside the try block, that monkeypatch is function-scoped so cannot leak, and that the
new fix matches the house shape already used for the missing `dot` binary. BASE for Task 11 =
1b4c738 Task 11: dispatched (implementer, model=sonnet; first real content, and the live test
of rulings R1 and the builds_on closure)

### 32.

the Task 11 implementer flagged a defect in my brief before committing to an interpretation,
and it was right. My step said to keep "the Bondora functions and the Eurostat fetcher" from
`convert_credit_data.py`, but that file contains no Eurostat content at all; the fetcher is a
separate sibling script, `fetch_macro_eurostat.py`, which the copy command never named.
Verified myself: zero Eurostat references in the file to be copied, the fetcher exists
separately, and the exemplar lecture's only two matches for eurostat/macro are the prose words
"macroeconomic factors" and "the macroeconomic block", not data reads. So S1 needs no macro
series, and the lectures that do (R1, R2) are outside Phase 0. Confirmed its reading: Bondora
functions only, `--datasets` dropped since one dataset remains, no Eurostat. Plan corrected.
Cost if wrong: a later task copies one more small script.

### 33.

the Task 11 implementer flagged a second defect in my brief, again before acting, and again it
was right. The exemplar lecture reads TWO parquet files, not one: the survival table at line
82 and `bondora_pd.parquet` at line 686, where it compares the cumulative-incidence estimate
against lecture 1's observed 12-month default rate. My brief named only the survival file in
both the data step and the verified-facts section, so Step 6's render would have failed
outright at that cell. Verified myself: both reads exist at those lines, both files are
present next door at 8.2 MB and 6.5 MB, and both are outputs of the same converter being
trimmed into `fetch_credit_data.py`. Confirmed its decision to copy both. Cost if wrong: 6.5
MB in a gitignored directory. Note on the pattern: two brief defects in one task, both caught
by the implementer reading the source before acting rather than after failing. That is the
standing instruction working on something other than tests. Both were mine and both came from
reading the lecture's header and first data read without reading the whole file.

### 34.

third Task 11 brief defect, and the subtlest. My Step 7 PDF test failed on a FALSE positive:
the lecture renders with `echo: true`, so Quarto prints every Python cell's source, and one
cell builds a matplotlib axis label `"$\mathrm{PD}_k$ (%)"` at line 613 whose mathtext shares
a command name with the watchlist. The match sat in echoed source, not in prose KaTeX was ever
asked to typeset. The implementer diagnosed it by pulling per-run font names through pypdf's
visitor_text rather than guessing: code sets in the mono face, prose in AvenirNext. Approved
its font-filter fix over the alternatives, and the reason is stronger than it knew: `\mathrm`
ALSO appears three times in the lecture's genuine display mathematics at lines 244, 472 and
639, setting PD, logit and CIF upright, so it is one of the best sentinels available and
narrowing the regex would have gutted the check. Refinement I added: the stylesheet's mono
stack is 'SF Mono', ui-monospace, Menlo, Consolas, 'Liberation Mono', so which face wins is
machine-dependent, and a filter keyed to Menlo alone would silently stop filtering elsewhere.
The test now matches a tuple of mono faces AND asserts at least one monospaced run was found,
printing the faces actually seen on failure. That converts a silent fragility into a
diagnosable one. Cost if wrong: one extra assertion. Note: three brief defects in one task,
all three found by the implementer reading the source before acting. All three were mine. Two
came from reading only the lecture's header and first data read; the third from specifying a
test against a PDF I had never extracted text from. Task 11: implemented (commit 8c902f1, 71
suite passing, check.py ok on all seven rules with 3 nodes and 2 paths, which I confirmed
myself). Both earlier rulings are now validated against real content: check 1's object-
identity collision map lets `survival-function` spend `obj.survival` in stats, life and credit
where it renders as S(t) in two of them, and check 4's transitive closure lets `survival-
braid` omit `conditional-probability` while inheriting it.

### 35.

added TASK 13 to the plan, so Phase 0 is thirteen tasks rather than twelve. I inspected the
generated node page myself and found two defects, both in Task 7's `site.py` and both
invisible until a page had mathematics in it. First, `render_node_page` links the stylesheet
and no KaTeX, so a reader sees `P(A \mid B) = \frac{P(A \cap B)}{P(B)}` as literal text; Phase
3 writes roughly 500 such pages. Second, and worse, CommonMark reads `\,` as an escaped comma
and eats the backslash, so the page already shows `,P(B)` where the source has `\,P(B)`: the
TeX is corrupted BEFORE any typesetter could see it, so adding KaTeX alone would typeset
broken input. Task 13 fixes both with `mdit-py-plugins`' dollarmath (which tokenises maths
ahead of escape handling) plus the vendored auto-render extension, and closes the deferred
`html=True` finding in the same function. Cost if wrong: one more task before the gate.

### 36.

node pages REFERENCE the vendored KaTeX relatively rather than inlining it, unlike lectures. A
lecture is inlined because people email and print it and 630 kB is the price; a node page is a
page in a published tree, and inlining would cost 630 kB times five hundred nodes in Phase 3.
Both remain free of any network dependency. Task 12's Pages allow-list gains `vendor/katex/`
accordingly. Cost if wrong: node pages are not single files.

### 37.

added criterion 3a to the definition of done, that the exemplar's generated page must typeset
its mathematics and open with the network disabled. Criterion 3 as written ("reads as a page
you would put in front of somebody") was already failed by a page showing raw TeX, but
implicitly, and an implicit criterion is one that gets argued about at the gate. Task 11:
complete (commits 1b4c738..8c902f1, review clean, spec compliant, Approved, no Critical or
Important findings) Settled the reviewer's ⚠️ myself, which it correctly said only a diff
against the sibling checkout could settle: `diff` shows exactly three hunks in the 802-line
lecture, all authorised, being the provenance comment, the stylesheet path and the `html-math-
method` block with its trailing slash. Nothing else moved. Note that only three of the four
authorised edits were needed, because `../data/` was already correct: the copy sits at the
same relative depth as the original.

### 38.

my "three times" count for `\mathrm` was wrong. It appears four times in genuine mathematics
at lines 253, 481, 648 and 745 of the copy, plus once in echoed code at 622. I had counted
from the original's line numbers and missed the fourth. Corrected in the plan, and the
correction folded into Task 13 as a step so the shipped docstring is fixed by an implementer
under review rather than by me. Cost if wrong: none, the filter is by typeface not by count.

### 39.

sharpened the tier-1 page template after the reviewer noticed `hazard-rate`'s closing sentence
names `discrete-time-hazard`, a node that does not exist. For that node it was the only honest
option, since it is terminal in both paths. But nothing validates a forward reference in
prose, so at Phase 3 scale an invented node id reads as fine writing and quietly promises a
page that will never be there, five hundred times over. The template now says to name a node
only where it exists in the graph, and otherwise to name the consequence. Declined to add a
checker rule, which would fight Phase 1's incremental landing of nodes. Cost if wrong: some
nodes end on a consequence where a node id would have been available. Task 11: minor
(deferred): the implementer verified `_prose_runs` both ways with a synthetic two-page
PdfReader fixture but did not ship it, so nothing in the suite proves the font filter leaves
genuine prose alone. The reviewer independently confirmed the underlying CSS fact, that
`.katex-display` carries no font-family rule and so inherits the body sans face, which makes
the property hold structurally. For final-review triage. BASE for Task 12 = 7934631 Task 12:
dispatched (implementer, model=sonnet; conventions, hook, pages workflow, pyright config)

### 40.

added TASK 14, so Phase 0 is fourteen tasks. Task 12's implementer dry-ran the Pages assemble
step and link-checked the tree, finding two defects, both mine, neither visible until a site
existed to check. I verified both. (1) `render_index` emits `href="paths/<id>.html"` while
`build()` writes to `site/paths/<id>.html`, so every index-to-path link is a 404, and check 7
guards only symbols.md so the committed index matches the buggy output with no drift reported.
(2) `lectures/*.html` is gitignored, so the published site has no lecture HTML and the path
page's link to it 404s; the PDF and figures publish because both are committed.

### 41. **DECISION FOR YOU.**

Ruling on defect 2, with the trade-off stated because it is a genuine one: commit the rendered
HTML, reversing Task 1's gitignore line. The alternative is adding Quarto, the modelling stack
and a data-fetch step to CI, which is slower, needs credentials, and still cannot reproduce a
gitignored extract. The cost is real: an inlined lecture is 767 kB against the sibling repo's
111 kB, because ours carries KaTeX and the stylesheet inside it, so each revision commits
about 656 kB of duplicated vendor bytes. At one lecture that is nothing; at Phase 4's sixty it
is worth revisiting, and the revisit has a clear answer available, namely stop inlining the
PUBLISHED html and have it reference vendor/katex/ relatively as node pages do, keeping
inline_assets.py for the standalone case the PDF largely already serves. Explicitly NOT doing
that now: it reverses two reviewed tasks and a spec promise on one lecture's numbers, and
Phase 4 will have sixty lectures' worth to decide on. Cost if wrong: git carries a few MB it
need not.

### 42.

Task 14's first step is a LINK-RESOLUTION TEST rather than the two point fixes, because both
defects are the same class and fixing the instances leaves the class open. It walks every href
and src a generator emits, resolves each RELATIVE TO THE PAGE THAT EMITTED IT (which is the
mistake defect 1 encodes), and asserts the page list is non-empty first so a build that wrote
nothing cannot pass. Added as criterion 1a to the definition of done.

### 43.

leaving commit 06289be as it stands. Task 12's `git add -A` swept my in-progress Task 14 plan
edit into its commit, so ~134 lines of plan text sit under a `chore:` message rather than a
`docs(plans):` one. Content is intact and nothing is lost. Not rewriting history: the branch
has no remote to reconcile through, I was actively committing while the implementer worked,
and the final whole-branch review reads the diff rather than the commit attribution. Cost if
wrong: one commit in a solo pre-PR branch is misattributed.

### 44.

this was MY process defect, not the implementer's. Every task's commit step in my own plan
says `git add -A`, while I have been committing plan corrections to the same branch
throughout, so the collision was designed in. The two remaining tasks' commit steps now name
explicit paths, and I have said why in the plan text so it is not restored. Declined the
alternative of holding my own commits while an implementer is live, since ruling promptly and
keeping the plan current is what the implementers actually read. Cost if wrong: an implementer
forgets a path and has to amend. Note for the final review: Task 12's review diff will carry
that plan text as noise. Flag it as mine, as I have for every other doc commit in a task
range. Task 12: implemented (commit 06289be, 74 suite passing, check.py ok on all seven,
Pyright clean on tests/, DONE). It also found the two published-site defects that became Task
14, and a twelfth non-discriminating test, which it reported rather than patching under the
brief's "do not add tests" instruction.

### 45.

moved that hook-test fix into Task 14 rather than reopening Task 12.
`test_the_hook_passes_on_the_current_tree` asserts only that the hook exits zero, so a hook
whose whole body was `exit 0` would pass it. Task 14 now adds a test asserting the checker's
own output appears in the hook's stdout, and requires verifying the contrast by replacing the
hook body with `exit 0` and confirming the new test fails while the old one still passes. It
belongs in Task 14 because it is the same defect as the link test there: something apparently
verified rather than actually verified. Cost if wrong: one test in a task whose theme it fits.
Task 12: review dispatched (model=sonnet; told the plan hunk in the diff is mine, not the
implementer's) BASE for Task 13 = 4392b99 Task 12: complete (commits 7934631..06289be, review
clean, spec compliant, Approved, no Critical or Important findings). The reviewer verified
claims against the repo rather than the diff text, independently re-running pyright against
`tests/test_model.py` (the file that actually imports the two broken names, where
`tests/test_hook.py` imports only stdlib and would have passed regardless) and parsing the
workflow YAML live.

### 46.

folded Task 12's two Minor findings into Task 14 rather than reopening. The hook's `cd "$(git
rev-parse --show-toplevel)"` gains `|| exit 1`. And CLAUDE.md's "71 tests pass" is DROPPED
rather than corrected to 74: the count was invalidated by the very commit that added it, has
drifted in every task of this plan, and will keep drifting through Phase 1, so a sentence
saying the suite passes is durable where a number is a hostage. Cost if wrong: the document
says less than it could. BASE for Task 13 = e19b86a Task 13: dispatched (implementer,
model=sonnet; node page mathematics, told to stop and report if dollarmath does not preserve
backslashes rather than improvising a regex approach) Task 13: implemented (commit a39ebe2, 78
suite passing, check.py ok on all seven; the implementer confirmed both prior-buggy states
actually fail by stashing and re-running all four new tests, and verified the rendered page
over loopback with zero outbound requests, seeing the fraction, the italics, the \qquad gap
and the \, thin space intact)

### 47.

the implementer's reported gap gets fixed before review rather than deferred, because it lands
on the exemplar itself. `dollarmath` emits `<span class="math inline">\(A\)</span>` and auto-
render is configured for `\(...\)`, but the alias table emits bare `<td>$\mu_x$</td>`, so on
hazard-rate.html the four symbols the whole notation contract exists to display show as raw
TeX. That fails criterion 3a of the definition of done directly. Fixed by reusing dollarmath's
own wrapper rather than adding `$...$` to the delimiter list, which needs no new delimiter and
cannot mistake a currency amount in prose for mathematics, a false-positive class that has
already bitten the KaTeX sweep. Cost if wrong: one more markup shape to keep in step.

### 48.

`alias.symbol` stays UN-escaped in that cell while `spend.domain` and `alias.name` are
escaped. It is TeX destined for a renderer, and escaping would hand KaTeX `&#x5C;mu_x`. It
comes from notation/objects.yaml, repo content under review rather than arbitrary author
input, and check 1 already constrains what a node may spend. Told the implementer to record
that reasoning so a later reader does not "fix" it into escaping. Cost if wrong: a symbol
containing markup could reach a page, which check 1 and review already gate. Task 13: alias
table fix landed (commit dc37ec0, 79 suite passing). Verified myself: grep for a literal
dollar returns 0 on all three node pages, the exemplar's table emits the wrapped `<span
class="math inline">\(...\)</span>` form, and index.html now reads "3 nodes," and "2 paths."
so the pluralisation is fixed. Task 13: review dispatched (model=sonnet; told the un-escaped
alias.symbol is authorised and not to report it, but to check the reasoning was recorded) Task
13: complete (commits e19b86a..dc37ec0, review clean, spec compliant, Approved, no Critical or
Important findings) Task 13, the finding worth recording: the implementer discovered at Step 3
that `dollarmath`'s own default renderer leaves NO delimiter characters in its output at all,
so a plain `renderMathInElement` call would have typeset nothing while every test about assets
and wrappers still passed. It supplied a custom `renderer` callback re-wrapping in `\(...\)`
and `\[...\]`, which the reviewer confirmed is the documented extension point with a matching
signature. That is exactly what Step 3 existed to surface, and it is the second time in this
plan that establishing a library's real output before asserting against it prevented a silent
failure. The reviewer also verified the delimiter match at BYTE level, reconstructing what the
Python string concatenation produces against what the renderer emits. Task 13: three minors,
all no action. NODE_HEAD duplicates the shared HEAD by design (my brief's instruction, small
enough that drift risk is low); the two KaTeX script tags load on every node page whether or
not it carries maths (a fixed per-page cost that does not scale with corpus size); and the
browser check used loopback rather than `file://` because the tool refused the latter, which
the reviewer judged still establishes the property Step 7 cared about, since the network log
shows zero non-loopback requests. BASE for Task 14 = dc37ec0 Task 14: dispatched (implementer,
model=sonnet; the last task. Link-resolution test first, then the two dangling links, then the
hook-contrast verification) Task 14: implemented (commit bc6ebe0, 81 suite passing with no
skips, check.py ok on all seven, no dangling links remaining, and the hook ran the real checks
on its own commit). It also self-caught an over-render: it had additionally re-run
html_to_pdf.sh, producing a same-size different-byte PDF with no requested change, and
reverted to the committed PDF under "touch only what's asked". Right call. Verified myself:
index.html now emits `href="site/paths/..."` for both paths, the lecture HTML is tracked, and
the link test passes in isolation.

### 49.

built a lecture-excluded review package, as I did for the vendored KaTeX in Task 8. The full
range is 796 kB of which 767 kB is one generated inlined HTML file; excluded it is 9.6 kB.
Verified the excluded file myself instead: a precise grep for `<link>` and `<script>` tags
carrying href or src returns NOTHING, so zero external asset dependencies, and both
`katex.render` and the stylesheet's own tokens are present so both are genuinely inlined.
Note, and it is the same lesson as the \mathrm false positive: my first grep for external
references used a loose pattern and returned 2 matches, which looked alarming. Both were
benign: one is `href="https://www.bondora.com/en/public-reports"`, a citation link in the
lecture's prose pointing at the public data source, which is content rather than an asset
dependency; the other two were the letters "cdn" occurring by chance inside base64 font data.
A loose check produced a false alarm exactly as a loose regex did in Task 11. Task 14: review
dispatched (model=sonnet, lecture-excluded diff) Task 14: review returned Needs fixes on one
Important finding, which is MINE and is the sharpest catch of the whole plan. The reviewer
proved that `cd ""` returns exit status 0 in bash and leaves the working directory unchanged,
so the `|| exit 1` guard I prescribed for the hook never fires on the very failure mode I
named. I verified it: from outside a repository the old form prints REACHED and exits 0, while
the capture-then-check form exits 1. My own prescription was the exact "looks fixed, is not"
pattern this plan has been hunting for fourteen tasks.

### 50.

fix it properly, with `toplevel="$(...)" || exit 1` then a `[[ -n "$toplevel" ]]` check then
the `cd`. And the test has to assert the guard's own MESSAGE, not the exit code, because the
old form also exits non-zero from outside a repo for the wrong reason: `check.py` is simply
not found relative to the unchanged directory. An exit-code assertion would have passed
against the broken guard, which would have been the thirteenth such test in this plan. Cost if
wrong: a hook edge case that only fires outside a git repository. Settled the reviewer's ⚠️
myself with the fresh-clone test it asked for. It noted that defect 2's dangling link was
never actually reproduced, because a leftover gitignored copy of the lecture HTML sat in the
implementer's working tree from Task 13. A clean clone of the branch carries the lecture HTML,
the PDF, the stylesheet, all three KaTeX assets, index.html, symbols.md and the three figures,
so nothing referenced is untracked and criterion 1a's concern is closed. Task 14: minor
(folded into the fix round): `.github/workflows/pages.yml` carries a comment saying
`lectures/*.html` is gitignored and absent unless a future task commits it. This task is that
future task. A stale comment beside a correct allow-list is how somebody later removes the
right entry. Task 14: fix round 1/5 dispatched (FIX_BASE bc6ebe0)

### 51.

approved the implementer's hook form over my own, which was wrong a SECOND time on the same
three lines. It found, and I verified, that an assignment propagates its command
substitution's exit status (`x="$(false)" || echo caught` prints), so my `toplevel="$(...)" ||
exit 1` exits on the ordinary not-in-a-repo case before the `[[ -n ]]` check runs, leaving
git's own `fatal:` on stderr rather than the guard's message. My own test therefore failed
against my own hook. Its form uses `|| true` plus `2>/dev/null` so one check covers both the
real failure and the hypothetical empty-success and emits one clear message. Recorded all
three measurements in the plan beside the code, plus the accepted cost of losing git's
diagnostic. Cost if wrong: a hook that says "not in a repository" for a corrupted repo too,
which still points the reader the right way. Note worth keeping: three rounds on eight lines
of shell, every round caught by somebody RUNNING the thing rather than reading it, and two of
the three errors were mine. Reading this guard convinced me twice that it was correct. That is
the clearest single argument in this whole plan for the standing instruction, and it is an
argument against my own judgement rather than anyone else's. Task 14: fix round 1/5 (commits
bc6ebe0..08c34fa, 82 suite passing, check.py ok on all seven). The implementer verified the
contrast by mutation and reported a detail that matters: under the OLD form the new test fails
on the stderr assertion while still exiting non-zero, but for the wrong reason, because the
directory stayed put so `.venv/bin/python` was not found there. That is exactly why the test
had to assert the message rather than the exit code. Verified the shipped hook myself in both
directions: from outside a repository it prints the guard's own message and exits 1, and
inside it has fired on several of my own commits running all seven checks green. Task 14:
scoped re-review dispatched (model=sonnet), and it is the last review before the whole-branch
review. Task 14: complete (commits dc37ec0..08c34fa, 1 fix round, all findings ADDRESSED, no
new Critical or Important breakage). The re-reviewer reconstructed the pre-fix hook in scratch
space and confirmed it fails the new test's stderr assertion while still exiting non-zero for
an unrelated reason, which is exactly why the test asserts the message. Task 14: minor (queued
for the final wave): the hook comment's causal narrative is inaccurate. It says `|| true`
prevents an abort on git's own fatal message, but with `2>/dev/null` on the same line,
removing `|| true` gives a SILENT abort under set -e, exit 128 with no stderr at all. The re-
reviewer verified this. That comment exists specifically to stop the next person breaking a
guard got wrong three times, so its precision matters more than a comment's usually would. It
is the fourth error in those eight lines and it is mine.

### 52.

one fix wave covering sections A to E of fix-wave.md, dispatched on OPUS given two Criticals
and roughly twenty items of judgement. Sections F and G record what NOT to touch.

### 53.

accepted scope growth of two new rules, checks 8 and 9, `taught_in` resolves and ledger
`needed_by` resolves. The reviewer ranked them first and second among missing rules and showed
both certain to bite: nothing checks `taught_in`, and Phase 4 lands lectures one at a time
against nodes already written, while a single mistyped ledger id disables check 6 for that
node silently and permanently. Ten lines each while the machinery is fresh. Cost if wrong: two
rules Phase 1 would have added anyway.

### 54. **DECISION FOR YOU.**

B7, the \lambda_{\mathrm{reg}} contradiction with spec section 4.2, is NOT resolved by me. The
spec says neither \lambda nor v can be renamed; objects.yaml renames it in ml and stats; check
2 did not force it. The spec is being amended to record it as an OPEN DECISION FOR MARIO at
gate 1, with my recommendation to keep the subscript, because once Phase 1 gives obj.hazard an
`ml` alias a node spending both objects in `ml` fails check 1 with no remedy. Resolving a
notation-policy question about his corpus silently, either way, would be wrong.

### 55.

two Phase 1 items deferred deliberately and recorded as the first entries of Phase 1's plan:
no KaTeX sweep covers node bodies (the sweep takes .qmd only, so an unsupported construct in a
node body renders as red error text while every script exits zero), and per-domain graphs are
unreadable at scale (measured: 600 nodes, 599 edges, 31 kB, and credit is the trunk). Fix
wave: applied (14 commits 08c34fa..HEAD, 66 files, 769 insertions, 183 deletions). 98 tests
passing with no warnings, up from 82. check.py ok on all NINE rules. With
ALCHEMIST_VAULT=/nonexistent, eight report ok and only check 5 skips, which confirms finding
B4's correction that my documentation wrongly claimed two rules skip. All three truncated
notes now parse whole, verified by parsing rather than reading. The 40 woff and ttf are gone
and the 20 woff2 remain. Fix wave: three residual concerns self-reported by the implementer,
all three verified by me. (1) graphviz is STILL a hard dependency of the unit suite: with
`dot` off PATH the link test FAILS with FileNotFoundError from site.py:297 rather than
skipping, so E1's third clause is not closed and definition-of-done criterion 1 is not met.
(2) check 1 accepts a duplicated (object, domain) spend, measured, which is a consequence of
my own earlier ruling that the collision map keys on object identity. (3) rule 8 checks the
.qmd while pages link the .html.

### 56.

(provisional, pending the re-review's view) park all three and surface them to Mario rather
than running a second fix wave. The skill is explicit that there is no second wave and that
residual load-bearing findings surface at the finish, and the value of that rule is precisely
that it stops the reasoning "but these are only one-liners", which is the reasoning I was
having. Asked the re-reviewer for its view on that inclination rather than assuming it. Cost
if wrong: Mario applies three one-line fixes himself, knowing exactly what they are. Scoped
re-review dispatched on OPUS, with the plan and spec INCLUDED in the package unusually,
because several findings were spec and plan corrections that need judging. Scoped re-review of
the fix wave: both Criticals ADDRESSED including A2's blocking detection half; 24 of 26 items
ADDRESSED, verified by running the bug in a scratch copy for 21 of them; B3 partially
addressed (one stale "six checks" left at spec line 345); E1 partially addressed (tmp_path
build and drift-repair closed, graphviz clause open).

### 57.

Ruling REVERSED, on the re-reviewer's argument, which was better than mine: I had been
inclined to park the graphviz dependency and surface it. It pointed out that parking it means
the branch cannot claim definition-of-done criterion 1, which promises no skip other than
Quarto or Chrome, because a contributor without graphviz gets a FAILURE; and that taking one
line is cheaper than writing that exception down. Accepted. Dispatched three closing edits:
the skipif, the stale spec count, and a docstring sentence making the rule-8 division a stated
decision rather than a silent one.

### 58.

no further review seat for those three, deliberately rather than as a shortcut. Each is
verifiable by RUNNING it rather than by reading it, which is the opposite of the case where a
reviewer adds value, and I verify all three myself. PARKED with rulings, to surface at the
finish: - Duplicated (object, domain) spend accepted by check 1. Follows from my own
collision-map ruling; no corpus node triggers it. The re-reviewer added the note that matters:
plan line 2651 now promises Phase 3 a trigger and row count the code does not implement, so
whoever changes `len(spends) > 1` must edit that sentence in the same commit. - Rule 9, and
identically check 6, crash rather than record a failure on a malformed ledger entry: a missing
`id` raises KeyError, a non-mapping raises AttributeError, and a scalar `needed_by` iterates
its characters and reports bogus failures. Same class as the C1 fix applied to check 5 in this
very wave. Non-blocking because check 6 would hit it first and no such entry exists, but Phase
1 seeds this ledger, so one isinstance guard whenever either rule is next touched. - Plan
criterion 2 still reads "ok on all seven rules"; covered by the historical-count marker at
plan line 13. Mario's call whether the marker suffices.

**Closed by Phase 1 Task 3.** The two ledger checks crashed rather than recording a failure
on a malformed entry. Three shapes were measured on 4 September 2026: a bare string in the
list and a mapping where the list belongs both raised `AttributeError` in either check, and an
entry with no `id` whose `needed_by` named an unknown node raised `KeyError` in rule 9 alone,
because check 6 never reaches `entry['id']` unless it has already found a reviewed node. Both
now share `_ledger_entries`, which reports a failure for each shape: a non-mapping entry or a
missing `id` names the entry's position, a non-list ledger names the file itself, and a
malformed `needed_by` names the entry's own id.

The hardening itself then introduced a fourth crash. An entry carrying `id` and `status` but
no `needed_by` key raised `KeyError: 'needed_by'` in both checks, because the original code's
`entry.get("needed_by") or []` had tolerated the missing key silently while the hardened check
bodies subscripted `entry["needed_by"]` unconditionally. `_ledger_entries` now resolves an
absent or an explicit null `needed_by` to an empty list on a copy of the entry, with no
complaint, since a gap naming no nodes is under-specified rather than malformed.
