"""Measure grain across the bodies. Emit numbers rather than judgements.

Spec section 4.1a states that inconsistent grain is invisible in a node list
read once and surfaces only in Phase 3, when some pages come out at two
paragraphs and others are lectures in disguise. So nothing here decides whether
a body is wrong. It reports that CS2 produced 1.08 nodes per syllabus item and
SP7 produced 0.33, and a reader draws the conclusion.

The band is 0.5 to 1.5, which is the brief's own instruction to the agents, so
a body outside it is a body that departed from what it was told and owes an
explanation rather than a correction.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

BAND = (0.5, 1.5)
FUSED = re.compile(r"\band\b|,")


@dataclass(frozen=True)
class BodyGrain:
    body: str
    items: int
    nodes: int
    ratio: float | None


@dataclass
class GrainReport:
    per_body: dict[str, BodyGrain] = field(default_factory=dict)
    outliers: list[str] = field(default_factory=list)
    unmeasurable: list[str] = field(default_factory=list)


def audit(manifests: list[dict]) -> GrainReport:
    report = GrainReport()
    for manifest in manifests:
        body = manifest["body"]
        items = int(manifest.get("items_in_document") or 0)
        nodes = int(manifest.get("nodes_emitted") or 0)
        if items == 0:
            report.per_body[body] = BodyGrain(body, items, nodes, None)
            report.unmeasurable.append(body)
            continue
        ratio = nodes / items
        report.per_body[body] = BodyGrain(body, items, nodes, ratio)
        if not BAND[0] <= ratio <= BAND[1]:
            report.outliers.append(body)
    return report


def requires_distribution(requires: list[tuple[str, ...]]) -> dict[int, int]:
    """How many nodes carry zero prerequisites, how many carry one, and so on.

    A long tail is the second grain signal after the ratio: a node needing eight
    prerequisites is usually three nodes rather than one rich one.
    """
    counts: dict[int, int] = {}
    for entry in requires:
        counts[len(entry)] = counts.get(len(entry), 0) + 1
    return dict(sorted(counts.items()))


def fused_titles(titles: list[str]) -> list[str]:
    """Every distinct title carrying "and" or a comma, sorted.

    The cheapest available tell for two examinable things fused into one node,
    because a syllabus item reading "estimation and forecasting" is two nodes and
    an agent under time pressure emits one. Many flags are false positives:
    "Profit and loss attribution" is one thing. It is a list to read rather than a list
    to act on. Two nodes sharing the exact same title text collapse to one entry here,
    since the report flags the title itself rather than a count of the nodes that carry it.
    """
    return sorted({t for t in titles if FUSED.search(t)})
