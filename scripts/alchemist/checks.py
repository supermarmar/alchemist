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
