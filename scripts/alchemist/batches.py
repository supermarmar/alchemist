"""Slicing the corpus into agent batches, and catching a write outside one.

The slice runs over sorted node ids, so a rerun reproduces the same batches.
The manifest then records the ids explicitly rather than the slice bounds: a
manifest read after the corpus has changed still describes the work that was
actually done, whereas bounds would silently re-point at different nodes.
"""

from __future__ import annotations

BATCH_SIZE = 40
PER_WAVE = 13


def slice_batches(node_ids: list[str], size: int = BATCH_SIZE) -> list[list[str]]:
    ordered = sorted(node_ids)
    return [ordered[i:i + size] for i in range(0, len(ordered), size)]


def wave_of(batch_number: int, per_wave: int = PER_WAVE) -> int:
    """One-based batch to one-based wave. Thirty-nine batches at thirteen a
    wave is three waves, which is what fits the fifteen-agent guideline."""
    return (batch_number - 1) // per_wave + 1


# `wave` and `nodes` are the contract between this writer and stray_writes's
# reader below: rename or nest either key differently here and only the
# round-trip test in test_batches.py stands between that change and every
# honest write being reported as a stray one.
def manifest_payload(node_ids: list[str], size: int = BATCH_SIZE, per_wave: int = PER_WAVE) -> dict:
    """The batches section of the manifest: number, wave and explicit ids.

    `build_manifest.py` and `stray_writes` both need to agree on this shape, so
    it lives here once rather than as two copies that could drift apart, one
    writing the manifest and the other reading it back.
    """
    batches = slice_batches(node_ids, size)
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
