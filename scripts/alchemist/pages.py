"""Writing one tier-1 page, and the numbers the gate reads over all of them.

Thirty-nine Phase 3 agents write pages, and hand-edited frontmatter would give
thirty-nine styles and the occasional record `parse_node` rejects. `write_page`
re-renders the whole record through the same `render` the attach tool and the
staging merge use, so every write is identical in shape, and it refuses a body
the template rejects or a spend check 1 would reject, so the refusal happens
here with the author present rather than at the pre-commit hook after the agent
has moved on.

Check 1 is called on a one-node corpus rather than re-implemented, for the
reason `attach_articles.py` gives about `attachment_complaint`: a second copy of
a rule drifts from the first.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import replace
from pathlib import Path

from .checks import check_declared_symbols_resolve
from .model import Corpus, Node, Objects, Spend, parse_node
from .staging import render
from .template import DISPLAY, HEADINGS, RATHER_THAN, validate_body


class PageRefused(Exception):
    """The body or the spends would fail a check; the message names each reason."""


def parse_spend(text: str) -> Spend:
    """`obj.hazard:credit` -> Spend. The colon keeps a spend one shell word."""
    obj, sep, domain = text.partition(":")
    if not sep or not obj or not domain:
        raise ValueError(f"spend {text!r} is not of the form object:domain")
    return Spend(obj, domain)


def write_page(
    node_file: Path,
    body: str,
    spends: tuple[Spend, ...],
    objects: Objects,
    *,
    force: bool = False,
) -> Node:
    """Replace the body, declare the spends, set `drafted`, and re-render.

    Spends are sorted and deduplicated so a rerun with the same inputs is
    byte-identical. A `reviewed` node is refused without `force`, because
    `reviewed` is Mario's verdict after a gate and a rerun batch must not undo
    it silently; with `force` the page goes back to `drafted`, since a rewritten
    page needs reviewing again.
    """
    node = parse_node(node_file)
    if node.status == "reviewed" and not force:
        raise PageRefused(
            f"{node.id} is reviewed; pass --force to overwrite a reviewed page"
        )
    ordered = tuple(sorted(set(spends), key=lambda s: (s.object, s.domain)))
    updated = replace(node, status="drafted", spends=ordered, body=body.strip() + "\n")
    problems = validate_body(updated.body)
    one_node = Corpus({node.id: updated}, {})
    prefix = f"{node.id}: "
    problems += [
        failure.removeprefix(prefix)
        for failure in check_declared_symbols_resolve(one_node, objects).failures
    ]
    if problems:
        raise PageRefused("\n".join(problems))
    node_file.write_text(render(updated))
    return updated


def page_statistics(corpus: Corpus) -> dict:
    """The numbers a gate note reads over the written pages.

    Word counts split on whitespace and so count TeX tokens as words, which is
    the same measure across pages and is all a distribution needs. The
    forward-reference test looks for an unlock's title or id, lowercased, in the
    closing section, and it is approximate: a page naming its unlock by an
    inflection is listed, and the gate reads the list as candidates for a look
    rather than as failures.
    """
    written = [n for n in corpus.nodes.values() if n.status != "stub"]
    words = sorted(len(n.body.split()) for n in written)

    def quantile(p: float) -> int:
        return words[min(len(words) - 1, int(p * len(words)))] if words else 0

    unlocks: dict[str, list[Node]] = defaultdict(list)
    for n in corpus.nodes.values():
        for r in n.requires:
            unlocks[r].append(n)
    missing = []
    for n in written:
        if not unlocks[n.id]:
            continue
        # Whitespace is normalised because bodies are hard-wrapped, and a
        # title straddling a line break is still a title named.
        closing = " ".join(n.body.split(HEADINGS[2], 1)[-1].lower().split())
        if not any(u.title.lower() in closing or u.id in closing for u in unlocks[n.id]):
            missing.append(n.id)

    return {
        "by_status": dict(Counter(n.status for n in corpus.nodes.values())),
        "written_by_domain": dict(Counter(d for n in written for d in n.domains)),
        "display_blocks": dict(Counter(len(DISPLAY.findall(n.body)) for n in written)),
        "words": {
            "min": quantile(0), "q1": quantile(0.25), "median": quantile(0.5),
            "q3": quantile(0.75), "max": words[-1] if words else 0,
        },
        "rather_than": sum(len(RATHER_THAN.findall(n.body)) for n in written),
        "no_forward_reference": sorted(missing),
    }
