"""The eleven rules. Each returns a Result, so the runner reports every failure in
one pass rather than stopping at the first.

Nothing here parses a node body. Matching an alias string against TeX is not
reliable: \\lambda occurs inside \\lambda(t), v inside \\varphi, and every short
alias inside something longer. Declaring what a node spends is exact instead, and
whether the body honours the declaration is a review responsibility.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .model import FRONTMATTER, REPO, Corpus, Objects
from .site import render_symbols
from .vault import attachment_complaint


@dataclass
class Result:
    rule: str
    failures: list[str] = field(default_factory=list)
    skipped: str | None = None

    @property
    def ok(self) -> bool:
        return not self.failures


def check_declared_symbols_resolve(corpus: Corpus, objects: Objects) -> Result:
    result = Result("1. declared symbols resolve")
    for node in corpus.nodes.values():
        seen: dict[str, str] = {}
        for spend in node.spends:
            if spend.object not in objects.by_id:
                result.failures.append(
                    f"{node.id}: spends unknown object {spend.object!r}"
                )
                continue
            if spend.domain not in node.domains:
                result.failures.append(
                    f"{node.id}: spends {spend.object} in domain {spend.domain!r}, "
                    f"which is not among its own domains {list(node.domains)}"
                )
                continue
            try:
                symbol = objects.rendering(spend)
            except LookupError as exc:
                result.failures.append(f"{node.id}: {exc}")
                continue
            if symbol in seen and seen[symbol] != spend.object:
                result.failures.append(
                    f"{node.id}: {seen[symbol]} and {spend.object} both render "
                    f"as {symbol!r} in domain {spend.domain!r}"
                )
            seen[symbol] = spend.object
    return result


def check_symbol_uniqueness_within_domain(objects: Objects) -> Result:
    result = Result("2. one symbol per object within a domain")
    claims: dict[tuple[str, str], list[str]] = defaultdict(list)
    for obj in objects.by_id.values():
        for alias in obj.aliases:
            claims[(alias.domain, alias.symbol)].append(obj.id)
    for (domain, symbol), owners in sorted(claims.items()):
        if len(owners) > 1:
            result.failures.append(
                f"domain {domain!r}: {symbol!r} is claimed by {sorted(owners)}"
            )
    return result


def check_requires_resolve_and_acyclic(corpus: Corpus) -> Result:
    result = Result("3. prerequisites resolve and the graph is acyclic")
    for node in corpus.nodes.values():
        for required in node.requires:
            if required not in corpus.nodes:
                result.failures.append(
                    f"{node.id}: requires unknown node {required!r}"
                )

    WHITE, GREY, BLACK = 0, 1, 2
    colour = dict.fromkeys(corpus.nodes, WHITE)

    def visit(node_id: str, trail: list[str]) -> None:
        if colour[node_id] == GREY:
            cycle = trail[trail.index(node_id):] + [node_id]
            result.failures.append("cycle: " + " -> ".join(cycle))
            return
        if colour[node_id] == BLACK:
            return
        colour[node_id] = GREY
        for required in corpus.nodes[node_id].requires:
            if required in colour:
                visit(required, trail + [node_id])
        colour[node_id] = BLACK

    for node_id in sorted(corpus.nodes):
        if colour[node_id] == WHITE:
            visit(node_id, [])
    return result


def check_path_teachability(corpus: Corpus) -> Result:
    """A node's prerequisites appear earlier in its own path, or anywhere in a
    path reachable through builds_on. Without the second clause every domain
    path would fail, since a life path does not restate the maths it assumes.
    """
    result = Result("4. every path is teachable in order")

    def inherited(path_id: str) -> set[str] | None:
        """Nodes supplied by the builds_on closure. None where that closure cycles."""
        seen: set[str] = set()
        frontier = list(corpus.paths[path_id].builds_on)
        while frontier:
            nxt = frontier.pop()
            if nxt == path_id:
                return None
            if nxt in seen or nxt not in corpus.paths:
                continue
            seen.add(nxt)
            frontier.extend(corpus.paths[nxt].builds_on)
        return {n for pid in seen for n in corpus.paths[pid].nodes}

    for path in sorted(corpus.paths.values(), key=lambda p: p.id):
        for referenced in path.builds_on:
            if referenced not in corpus.paths:
                result.failures.append(
                    f"{path.id}: builds_on unknown path {referenced!r}"
                )
        supplied = inherited(path.id)
        if supplied is None:
            result.failures.append(
                f"{path.id}: builds_on cycle reaches back to itself"
            )
            continue
        available = set(supplied)
        for node_id in path.nodes:
            node = corpus.nodes.get(node_id)
            if node is None:
                result.failures.append(f"{path.id}: unknown node {node_id!r}")
                continue
            for required in node.requires:
                if required not in available:
                    result.failures.append(
                        f"{path.id}: {node_id} needs {required!r} before it, and "
                        f"neither the path nor its builds_on closure supplies it"
                    )
            available.add(node_id)
    return result


PUBLISHABLE = {"public-free"}


def vault_root() -> Path:
    """The vault is a separate private repo, so its location is configurable."""
    return Path(
        os.environ.get("ALCHEMIST_VAULT", Path.home() / "Documents" / "Repos" / "vault")
    ).expanduser()


def _register_path(vault: Path, source_id: str) -> Path:
    return vault / "wiki" / "_meta" / "sources" / f"{source_id}.md"


def _register_entry(path: Path) -> dict | None:
    """The parsed frontmatter of a register entry, or None where there is none.

    Check 5 is the rule that keeps purchased material off a public site, so it
    has to fail closed. Two shapes used to defeat it. A file whose frontmatter
    does not parse returned None, which the caller reported as "is not in the
    vault register", untrue of a file sitting right there. And `yaml.safe_load`
    on scalar or list frontmatter returns a non-dict, so `entry.get(...)` raised
    AttributeError rather than failing. Both now come back as None from here and
    the caller distinguishes them from an absent file by looking first.
    """
    match = FRONTMATTER.match(path.read_text())
    if match is None:
        return None
    entry = yaml.safe_load(match.group(1))
    return entry if isinstance(entry, dict) else None


def check_publishable_citations(corpus: Corpus, vault: Path) -> Result:
    """This repo is public, so a quoted source has to be publishable.

    Purchased material can still inform a node through vault_articles, since
    the article lives in the private vault and the node's own prose is original.
    What it can never do is appear in vault_sources, which means the node quotes
    the primary text.
    """
    result = Result("5. quoted sources are publishable")
    if not (vault / "wiki" / "_meta" / "sources").is_dir():
        result.skipped = f"no vault register at {vault}"
        return result
    for node in corpus.nodes.values():
        for source_id in node.vault_sources:
            path = _register_path(vault, source_id)
            if not path.is_file():
                result.failures.append(
                    f"{node.id}: {source_id!r} is not in the vault register"
                )
                continue
            entry = _register_entry(path)
            if entry is None:
                result.failures.append(
                    f"{node.id}: {source_id!r} is in the register at {path}, but "
                    f"its frontmatter is absent or does not parse to a mapping, "
                    f"so its confidentiality cannot be read"
                )
                continue
            confidentiality = entry.get("confidentiality")
            if confidentiality in PUBLISHABLE:
                continue
            if confidentiality == "public-paid" and entry.get("publication_waiver"):
                continue
            result.failures.append(
                f"{node.id}: quotes {source_id!r}, which is {confidentiality!r} "
                f"with no publication waiver, and this repo is public"
            )
    return result


def _ledger_entries(ledger: Path) -> tuple[list[dict], list[str]]:
    """Read the ledger defensively and return (usable entries, complaints).

    A malformed entry has to become a recorded failure rather than a stack
    trace, because Phase 1 seeds this ledger and a trace mid-run costs more to
    diagnose than the guard costs to write. The shapes that used to crash were
    measured rather than guessed: a bare string in the list, a mapping where a
    list belongs, and a missing `id` reached only through rule 9's failure path.

    A returned entry always carries a `needed_by` list. An absent key or an
    explicit null normalises to an empty list, because an entry naming no
    nodes is under-specified rather than malformed, so neither is a
    complaint; anything else that is not a list, `{}` and `''` and `0` and
    `false` included, is. The test is presence and type rather than
    truthiness, because a falsy-but-wrong shape such as `{}` must still
    complain. Resolving `needed_by` here rather than at each call site means
    both check bodies can subscript `entry["needed_by"]` unconditionally
    without either of them re-crashing on a hand-typed entry that simply
    omits the key. The returned entry is a shallow copy, so this function
    reads the ledger rather than mutating it.
    """
    raw = yaml.safe_load(ledger.read_text())
    if raw is None:
        return [], []
    if not isinstance(raw, list):
        return [], [
            f"{ledger.name}: malformed, the file is a "
            f"{type(raw).__name__} where a list of entries belongs"
        ]
    entries, complaints = [], []
    for position, entry in enumerate(raw, start=1):
        if not isinstance(entry, dict):
            complaints.append(
                f"{ledger.name}: malformed entry {position}, a "
                f"{type(entry).__name__} where a mapping belongs"
            )
            continue
        if "id" not in entry:
            complaints.append(f"{ledger.name}: malformed entry {position}, no id")
            continue
        needed = entry.get("needed_by")
        if needed is None:
            needed = []
        elif not isinstance(needed, list):
            complaints.append(
                f"{entry['id']}: malformed needed_by, a "
                f"{type(needed).__name__} where a list of node ids belongs"
            )
            continue
        entries.append({**entry, "needed_by": needed})
    return entries, complaints


def check_gap_closure(corpus: Corpus, root: Path = REPO) -> Result:
    result = Result("6. no reviewed node carries an open source gap")
    ledger = root / "sources" / "wanted.yaml"
    if not ledger.is_file():
        result.skipped = f"no ledger at {ledger}"
        return result
    entries, complaints = _ledger_entries(ledger)
    result.failures.extend(complaints)
    for entry in entries:
        if entry.get("status") == "ingested":
            continue
        for node_id in entry["needed_by"]:
            node = corpus.nodes.get(node_id)
            if node is not None and node.status == "reviewed":
                result.failures.append(
                    f"{node_id}: reviewed, but gap {entry['id']!r} is still "
                    f"{entry.get('status')!r}"
                )
    return result


def check_generated_current(objects: Objects, root: Path = REPO) -> Result:
    """A committed build artefact drifts unless something checks it."""
    result = Result("7. generated artefacts are current")
    target = root / "notation" / "symbols.md"
    if not target.is_file():
        result.failures.append(f"{target} is missing; run build_site.py")
        return result
    if target.read_text() != render_symbols(objects):
        result.failures.append(
            f"{target} has drifted from objects.yaml; run build_site.py"
        )
    return result


def check_taught_in_resolves(corpus: Corpus, root: Path = REPO) -> Result:
    """A node marked taught before its lecture renders publishes a dead link.

    Phase 4 lands lectures one at a time against nodes already written, so the
    window between a node claiming `taught_in` and the file existing is the
    normal state of the corpus rather than an oddity.

    This rule resolves the Quarto **source**, `lectures/<value>.qmd`, and stops
    there. A node page and a path page both link the rendered
    `lectures/<value>.html`, and that artefact is covered instead by the
    link-resolution test in `tests/test_cli.py`, which walks every reference the
    generators emit. The division is deliberate, because CI cannot render a
    lecture: rebuilding one needs Quarto, the modelling stack and gitignored
    parquet extracts, so the HTML is a committed artefact rather than something
    a check could regenerate and verify.

    Skips where `lectures/` is absent, matching checks 5 and 6. In practice that
    means it runs on every checkout, since the directory is tracked. The guard
    is there so that a corpus rooted somewhere without one reports a missing
    input rather than failing every taught node in it.
    """
    result = Result("8. every taught_in names a lecture")
    lectures = root / "lectures"
    if not lectures.is_dir():
        result.skipped = f"no lecture directory at {lectures}"
        return result
    for node in corpus.nodes.values():
        if node.taught_in is None:
            continue
        source = lectures / f"{node.taught_in}.qmd"
        if not source.is_file():
            result.failures.append(
                f"{node.id}: taught_in names {node.taught_in!r}, and "
                f"{source} does not exist"
            )
    return result


def check_ledger_references_resolve(corpus: Corpus, root: Path = REPO) -> Result:
    """A mistyped id in `needed_by` disables check 6 for that node, silently.

    Check 6 looks each id up with `corpus.nodes.get` and moves on where it finds
    nothing, which is correct for its own rule and useless as a guard. So the
    only thing standing between one typo and a permanently unenforced gap is
    this rule.
    """
    result = Result("9. every ledger reference resolves")
    ledger = root / "sources" / "wanted.yaml"
    if not ledger.is_file():
        result.skipped = f"no ledger at {ledger}"
        return result
    entries, complaints = _ledger_entries(ledger)
    result.failures.extend(complaints)
    for entry in entries:
        for node_id in entry["needed_by"]:
            if node_id not in corpus.nodes:
                result.failures.append(
                    f"{entry['id']}: needed_by names unknown node {node_id!r}, "
                    f"so check 6 can never enforce this gap"
                )
    return result


# Single words that are proper names in their own right, wherever they appear.
PROPER_NAMES = frozenset({
    "American", "Basel", "Bayes", "Black", "Bolzano", "Borel", "Brace",
    "Brownian", "Euclidean", "Gatarek", "Greeks", "Heine", "Laplace", "Lloyd",
    "Markov", "Musiela", "Pareto", "Poisson", "Scholes", "Tier", "Weierstrass",
})

# Defined terms of more than one word. Each of these used to cost the word list
# an entry per word, and every such entry licensed that word across all 1,560
# titles: "Capital" was admitted everywhere so that "Capital Requirements
# Regulation" would pass. A phrase containing another has to mask before the
# shorter one can match inside it; `_mask_phrases` enforces that by sorting on
# length at the point of use, so this tuple need not be kept longest first by hand.
PROPER_PHRASES = (
    "Capital Requirements Regulation",
    "Business Indicator Component",
    "Internal Loss Multiplier",
    "World Trade Organization",
    "Great Depression",
    "Basel Accord",
    "Monte Carlo",
)
ROMAN = re.compile(r"^(?:I|II|III|IV|V|VI|VII|VIII|IX|X)$")


def _mask_phrases(title: str) -> str:
    """Lower-case every known phrase in place, leaving the word count alone.

    Masking rather than deleting is load-bearing. `_capitalised_off_list` skips
    `title.split()[1:]`, so removing a phrase that opens a title would promote
    the phrase's second word to first and skip it for the wrong reason.

    Each phrase is matched on a word boundary, because a plain substring match
    also fires inside a longer word: "Great Depression" would otherwise lower-case
    the "Depression" inside "Depressionism", leaving a word whose initial is no
    longer a capital, so `_capitalised_off_list` skips a genuine offender.
    """
    masked = title
    for phrase in sorted(PROPER_PHRASES, key=len, reverse=True):
        masked = re.sub(rf"\b{re.escape(phrase)}\b", phrase.lower(), masked)
    return masked


def _capitalised_off_list(title: str) -> list[str]:
    """Words after the first that carry a capital the rule does not allow."""
    offenders: list[str] = []
    for word in _mask_phrases(title).split()[1:]:
        for part in word.split("-"):
            core = part.strip("(),:;\"'").removesuffix("'s")
            if not core or not core[0].isupper():
                continue
            if len(core) == 1 or sum(ch.isupper() for ch in core) >= 2:
                continue
            if ROMAN.match(core) or core in PROPER_NAMES:
                continue
            offenders.append(part)
    return offenders


def check_titles_sentence_case(corpus: Corpus) -> Result:
    """Sentence case, ruled at gate 2 (D4, 8 September 2026). A title in the source's
    own casing reads as a different concept from the same title in sentence case,
    and twenty transcribers produced fourteen such disagreements. Proper names,
    acronyms, Roman numerals, single letters and possessives of names pass; a
    single-word name goes on PROPER_NAMES, and a body's defined term of several
    words goes on PROPER_PHRASES instead, which is why Business Indicator
    Component and Capital Requirements Regulation pass.
    """
    result = Result("10. titles are sentence case")
    for node in sorted(corpus.nodes.values(), key=lambda n: n.id):
        offenders = _capitalised_off_list(node.title)
        if offenders:
            result.failures.append(
                f"{node.id}: title {node.title!r} capitalises {', '.join(offenders)}, "
                f"which is off the proper-name list"
            )
    return result


def check_attached_articles(corpus: Corpus, vault: Path) -> Result:
    """An attached slug has to name a real, classified wiki article.

    Phase 2 attaches through agents, and an agent can produce a plausible slug
    for an article that does not exist. Resolution is the mechanical answer:
    a fabricated slug fails here rather than waiting for a Phase 3 writer to
    open nothing.

    `attachment_complaint` in `.vault` is the one place that resolves and
    classifies a slug; this check calls it and only decides how to word each
    of its three outcomes. The three arms report differently on purpose. A
    slug naming no file is a fabrication or a stale rename, a slug whose
    article carries no confidentiality field is one reclassified in the vault
    after it was attached, and a slug whose article is neither public-free
    nor public-paid names a value this public repo cannot carry.
    """
    result = Result("11. attached vault articles resolve and are publishable")
    if not (vault / "wiki").is_dir():
        result.skipped = f"no vault wiki at {vault}"
        return result
    for node in sorted(corpus.nodes.values(), key=lambda n: n.id):
        for slug in node.vault_articles:
            problem = attachment_complaint(vault, slug)
            if problem is None:
                continue
            if problem.kind == "missing":
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, which does not resolve; "
                    f"looked for {problem.path}"
                )
            elif problem.kind == "unclassified":
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, whose article at {problem.path} "
                    f"carries no confidentiality field, so it cannot be read"
                )
            elif problem.kind == "not-publishable":
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, which is "
                    f"{problem.confidentiality!r} rather than public-free or "
                    f"public-paid, and this repo is public"
                )
            else:
                raise NotImplementedError(
                    f"unhandled attachment problem kind {problem.kind!r}"
                )
    return result


def run_all(corpus: Corpus, objects: Objects, root: Path, vault: Path) -> list[Result]:
    return [
        check_declared_symbols_resolve(corpus, objects),
        check_symbol_uniqueness_within_domain(objects),
        check_requires_resolve_and_acyclic(corpus),
        check_path_teachability(corpus),
        check_publishable_citations(corpus, vault),
        check_gap_closure(corpus, root),
        check_generated_current(objects, root),
        check_taught_in_resolves(corpus, root),
        check_ledger_references_resolve(corpus, root),
        check_titles_sentence_case(corpus),
        check_attached_articles(corpus, vault),
    ]
