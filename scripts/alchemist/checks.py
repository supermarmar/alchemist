"""The seven rules. Each returns a Result, so the runner reports every failure in
one pass rather than stopping at the first.

Nothing here parses a node body. Matching an alias string against TeX is not
reliable: \\lambda occurs inside \\lambda(t), v inside \\varphi, and every short
alias inside something longer. Declaring what a node spends is exact instead, and
whether the body honours the declaration is a review responsibility.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .model import Corpus, Objects


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
