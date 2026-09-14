"""Unioning the Phase 2 agents' ledger fragments into one gap ledger.

Thirty-nine agents each propose the documents their uncovered nodes need, and
many propose the same document. Unioning by document id is what turns roughly
a thousand uncovered nodes into a ledger Mario can read in one sitting.

A seeded entry wins every field it already carries, `note` excepted. Phase 1
wrote those four by hand with a considered claim and, in one case, a primary
alternative, and an agent's guess at the same document should extend the node
list rather than overwrite the reasoning. The disagreement is reported rather
than dropped.

`note` is the exception because it is the one field where each batch has
something different and true to say about the same document, naming the
chapters its own nodes need. Notes therefore accumulate, a blank line apart,
in the order they arrive.

THE FRAGMENT CONTRACT

A fragment is a YAML file, holding a list of mappings. Each mapping proposes
one ledger entry and carries:

    Required:  id, needed_by, claim, document, expected_tier, acquisition,
               status
    Optional:  url, note, primary_alternative

`acquisition` and `status` are closed vocabularies, copied from the header
comment of `sources/wanted.yaml` rather than invented here:

    acquisition: public-download | regulator | journal | purchased-personal
    status:      wanted | located | in-raw | ingested

`needed_by` is required in a well-formed entry, but an entry that omits it
is under-specified rather than malformed: it normalises to an empty list in
`union_entries`, the same tolerance `_ledger_entries` in `checks.py` applies
to the merged ledger. Only a `needed_by` present with the wrong type, a
value that is not a list, is structural, because that is the shape already
seen to crash a caller that expects to iterate it.

`read_fragments` refuses to guess at a fragment it cannot make sense of: a
file that does not parse, a file that is not a list, an entry that is not a
mapping, an entry with no id, an entry missing one of the other required
keys, or an entry whose `acquisition` or `status` falls outside its
vocabulary. Every one of those becomes a complaint naming the file, the
entry's position, its id where it has one, and precisely what is wrong, so a
wave agent can fix its own fragment without re-reading this module.
`merge_ledger.py` refuses to write the ledger at all while any complaint
stands, because a partial ledger reaching the gate wearing the appearance of
a complete one is worse than no ledger: acquisition is decided off it.

A disagreement between a seeded entry's field and a proposed one is a
different kind of problem. Both sides are well-formed; they simply differ.
The seeded entry's value stands, `union_entries` reports the disagreement
rather than blocking on it, and the write proceeds.
"""

from __future__ import annotations

from pathlib import Path

import yaml

REQUIRED_KEYS = frozenset({
    "id", "needed_by", "claim", "document", "expected_tier", "acquisition", "status",
})
OPTIONAL_KEYS = frozenset({"url", "note", "primary_alternative"})

# Ordered to match the header comment in sources/wanted.yaml, which is the
# source of truth; update both together if that comment ever changes.
ACQUISITION_VALUES = ("public-download", "regulator", "journal", "purchased-personal")
STATUS_VALUES = ("wanted", "located", "in-raw", "ingested")

_OTHER_REQUIRED_KEYS = sorted(REQUIRED_KEYS - {"id", "needed_by"})


def _normalise(entry: dict) -> dict:
    """A returned entry always carries a needed_by list, sorted and unique.

    Rule 9 reads needed_by on every entry, and rule 6 enforces gap closure
    through it, so an entry arriving without one would disable check 6 for its
    nodes silently and permanently.
    """
    needed_by = entry.get("needed_by")
    if not isinstance(needed_by, list):
        needed_by = []
    return {**entry, "needed_by": sorted({str(n) for n in needed_by})}


def _joined_note(held: str, arriving: str) -> str:
    """Both notes, a blank line apart, or the held one where they say the same.

    A shared ledger id collects one note per batch, each naming the chapters
    that batch's nodes need, and acquisition is decided off the merged ledger
    rather than off the thirty-nine reports. Keeping the first note and
    reporting the rest as a disagreement, which is what every other field
    does, put that reasoning somewhere nobody reads it at the gate.
    """
    if arriving.strip() in {part.strip() for part in held.split("\n\n")}:
        return held
    return f"{held.rstrip(chr(10))}\n\n{arriving}"


def read_fragments(staging: Path) -> tuple[list[dict], list[str]]:
    """Every usable proposed entry across the fragments, plus a complaint per
    entry the reader cannot make sense of.

    A complaint blocks the whole write in `merge_ledger.py`, so it is reserved
    for a fragment the reader genuinely cannot use: the wrong YAML shape, a
    missing id, a missing required field, or a value outside a closed
    vocabulary. A disagreement in an otherwise well-formed field is a
    different, non-blocking problem that `union_entries` reports instead.
    """
    entries: list[dict] = []
    complaints: list[str] = []
    for path in sorted(staging.glob("ledger-*.yaml")):
        try:
            loaded = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            complaints.append(f"{path.name}: does not parse ({exc.__class__.__name__})")
            continue
        if not isinstance(loaded, list):
            complaints.append(
                f"{path.name}: is a {type(loaded).__name__} where a list of entries belongs"
            )
            continue
        for position, entry in enumerate(loaded, start=1):
            if not isinstance(entry, dict):
                complaints.append(
                    f"{path.name}: entry {position} is a {type(entry).__name__} "
                    f"where a mapping belongs"
                )
                continue
            entry_id = entry.get("id")
            if not entry_id:
                complaints.append(f"{path.name}: entry {position} has no id")
                continue
            problems = []
            missing = [key for key in _OTHER_REQUIRED_KEYS if not entry.get(key)]
            if missing:
                problems.append(f"missing {', '.join(missing)}")
            needed_by = entry.get("needed_by")
            if needed_by is not None and not isinstance(needed_by, list):
                problems.append(
                    f"needed_by is a {type(needed_by).__name__} where a list belongs"
                )
            acquisition = entry.get("acquisition")
            if acquisition is not None and acquisition not in ACQUISITION_VALUES:
                problems.append(
                    f"acquisition {acquisition!r} is not one of {list(ACQUISITION_VALUES)}"
                )
            status = entry.get("status")
            if status is not None and status not in STATUS_VALUES:
                problems.append(f"status {status!r} is not one of {list(STATUS_VALUES)}")
            if problems:
                complaints.append(
                    f"{path.name}: entry {position} {entry_id!r} " + "; ".join(problems)
                )
                continue
            entries.append(entry)
    return entries, complaints


def union_entries(
    seeded: list[dict], proposed: list[dict]
) -> tuple[list[dict], list[str]]:
    """Merged entries sorted by id, plus a complaint per field disagreement."""
    merged: dict[str, dict] = {}
    complaints: list[str] = []
    for entry in [_normalise(e) for e in seeded]:
        merged[entry["id"]] = entry
    for entry in [_normalise(e) for e in proposed]:
        key = entry["id"]
        if key not in merged:
            merged[key] = entry
            continue
        held = merged[key]
        for field, value in entry.items():
            if field == "needed_by":
                continue
            if field == "note" and "note" in held:
                held["note"] = _joined_note(held["note"], value)
                continue
            if field in held and held[field] != value:
                complaints.append(
                    f"{key}: {field} differs; keeping {held[field]!r} over {value!r}"
                )
            elif field not in held:
                held[field] = value
        held["needed_by"] = sorted(set(held["needed_by"]) | set(entry["needed_by"]))
    return [merged[key] for key in sorted(merged)], complaints
