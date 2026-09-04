"""The nine rules. Each returns a Result, so the runner reports every failure in
one pass rather than stopping at the first.

Nothing here parses a node body. Matching an alias string against TeX is not
reliable: \\lambda occurs inside \\lambda(t), v inside \\varphi, and every short
alias inside something longer. Declaring what a node spends is exact instead, and
whether the body honours the declaration is a review responsibility.
"""

from __future__ import annotations

import os
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .model import FRONTMATTER, REPO, Corpus, Objects
from .site import render_symbols


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
        needed = entry.get("needed_by") or []
        if not isinstance(needed, list):
            complaints.append(
                f"{entry['id']}: malformed needed_by, a "
                f"{type(needed).__name__} where a list of node ids belongs"
            )
            continue
        entries.append(entry)
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
        for node_id in entry["needed_by"] or []:
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
        for node_id in entry["needed_by"] or []:
            if node_id not in corpus.nodes:
                result.failures.append(
                    f"{entry['id']}: needed_by names unknown node {node_id!r}, "
                    f"so check 6 can never enforce this gap"
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
    ]
