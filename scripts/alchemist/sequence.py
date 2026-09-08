"""The mechanical order of a path: topological tier, then id.

Task 12 sequenced the domain paths this way and the braids by hand. A node's tier
is the longest chain of prerequisites behind it inside the same path, so tier 0
holds what the path can open with, and inside a tier the ids sort alphabetically,
which is deterministic and says nothing about pedagogy. D1 (a) replaces this order
on the credit trunk by hand and leaves it on every other path until its pages
exist, so anything that edits `requires` re-runs this over the mechanical paths.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from .model import Corpus, TeachingPath

NODES_BLOCK = re.compile(r"^nodes:\n(?:- .*\n?)*", re.M)


def mechanical_order(path: TeachingPath, corpus: Corpus) -> tuple[str, ...]:
    members = set(path.nodes)
    depth: dict[str, int] = {}

    def tier(node_id: str) -> int:
        if node_id in depth:
            return depth[node_id]
        inside = [r for r in corpus.nodes[node_id].requires if r in members]
        depth[node_id] = 0 if not inside else 1 + max(tier(r) for r in inside)
        return depth[node_id]

    for node_id in path.nodes:
        tier(node_id)
    return tuple(sorted(path.nodes, key=lambda n: (depth[n], n)))


def rewrite_nodes(text: str, order: Iterable[str]) -> str:
    """Replace the nodes block and nothing else, so a preamble's wrapping survives.

    The block must be the last thing in the file and hold only `- id` lines. A
    comment or an indented item inside it would otherwise match as an empty
    block and the ids would be written twice, so anything else is refused."""
    match = NODES_BLOCK.search(text)
    if match is None or match.end() != len(text):
        raise ValueError("the nodes block must be the last block of the file and hold only '- id' lines")
    block = "nodes:\n" + "".join(f"- {n}\n" for n in order)
    return text[: match.start()] + block
