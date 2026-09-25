"""Slicing the corpus into agent batches, and catching a write outside one.

The slice runs over sorted node ids, so a rerun reproduces the same batches.
The manifest then records the ids explicitly rather than the slice bounds: a
manifest read after the corpus has changed still describes the work that was
actually done, whereas bounds would silently re-point at different nodes.
"""

from __future__ import annotations

from collections.abc import Callable

from .model import Node

BATCH_SIZE = 40
PER_WAVE = 13


def slice_batches(
    node_ids: list[str], size: int = BATCH_SIZE, key: Callable[[str], object] | None = None
) -> list[list[str]]:
    ordered = sorted(node_ids, key=key)
    return [ordered[i:i + size] for i in range(0, len(ordered), size)]


def wave_of(batch_number: int, per_wave: int = PER_WAVE) -> int:
    """One-based batch to one-based wave. Thirty-nine batches at thirteen a
    wave is three waves, which is what fits the fifteen-agent guideline."""
    return (batch_number - 1) // per_wave + 1


def requires_depth(nodes: dict[str, Node]) -> dict[str, int]:
    """Longest prerequisite chain beneath each node, a root being 0. Check 3
    keeps the graph acyclic, so the recursion terminates; the deepest node in
    the corpus sits at 12."""
    depth: dict[str, int] = {}

    def visit(node_id: str) -> int:
        if node_id not in depth:
            requires = nodes[node_id].requires
            depth[node_id] = 0 if not requires else 1 + max(visit(r) for r in requires)
        return depth[node_id]

    for node_id in nodes:
        visit(node_id)
    return depth


def depth_key(nodes: dict[str, Node]) -> Callable[[str], tuple[int, str]]:
    """A sort key putting shallower nodes first and ids alphabetical within a
    depth. Phase 3 slices on it so that an agent writing a page's closing
    section reads a drafted prerequisite more often than a stub."""
    depth = requires_depth(nodes)
    return lambda node_id: (depth[node_id], node_id)


def phase_node_ids(nodes: dict[str, Node], phase: int) -> list[str]:
    """Phase 2 batched every node; Phase 3 batches the stubs, since a drafted
    node already carries its page and a rerun must not overwrite it."""
    if phase == 2:
        return list(nodes)
    return [n.id for n in nodes.values() if n.status == "stub"]


# `wave` and `nodes` are the contract between this writer and stray_writes's
# reader below: rename or nest either key differently here and only the
# round-trip test in test_batches.py stands between that change and every
# honest write being reported as a stray one.
def manifest_payload(
    node_ids: list[str],
    size: int = BATCH_SIZE,
    per_wave: int = PER_WAVE,
    key: Callable[[str], object] | None = None,
) -> dict:
    """The batches section of the manifest: number, wave and explicit ids.

    `build_manifest.py` and `stray_writes` both need to agree on this shape, so
    it lives here once rather than as two copies that could drift apart, one
    writing the manifest and the other reading it back.
    """
    batches = slice_batches(node_ids, size, key)
    return {
        "nodes": len(node_ids),
        "batches": {
            number: {"wave": wave_of(number, per_wave), "nodes": ids}
            for number, ids in enumerate(batches, start=1)
        },
    }


def stray_writes(manifest: dict, batch_number: int, changed: list[str]) -> list[str]:
    """Changed node ids the batch does not own, sorted.

    Batches are disjoint, which is the whole reason agents write node files
    directly. This is what verifies the assumption instead of trusting it.
    A batch number the manifest does not hold raises rather than reading as a
    clean, empty result, because a mistyped number must fail loudly and not
    look like a verified batch.
    """
    batches = manifest["batches"]
    if batch_number not in batches:
        numbers = sorted(batches)
        held = f"batches {numbers[0]} to {numbers[-1]}" if numbers else "no batches"
        raise KeyError(f"batch {batch_number} is not in the manifest, which holds {held}")
    owned = set(batches[batch_number]["nodes"])
    return sorted(set(changed) - owned)
