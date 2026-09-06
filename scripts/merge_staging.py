"""Merge Phase 1's staging directories into nodes/ and report every merge."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import parse_node
from scripts.alchemist.staging import collect, merge, near_misses, write_merged

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging", type=Path, default=REPO / ".superpowers" / "phase-1")
    parser.add_argument("--target", type=Path, default=REPO / "nodes")
    parser.add_argument("--report", type=Path, default=REPO / "notes" / "merge-report-2026-09-04.md")
    args = parser.parse_args()

    grouped = collect(args.staging)
    existing = {n.id: n for n in (parse_node(p) for p in sorted(args.target.glob("*.md")))}
    merged, notes = {}, []
    for node_id, records in grouped.items():
        merged[node_id], node_notes = merge(records, existing.get(node_id))
        notes.extend(node_notes)

    written = write_merged(merged, args.target)
    shared = sum(1 for records in grouped.values() if len(records) > 1)
    protected = sum(1 for node_id in merged if node_id in existing)

    lines = [
        "# Merge report, Phase 1",
        "",
        f"- Staged records: {sum(len(r) for r in grouped.values())}",
        f"- Distinct nodes: {len(merged)}",
        f"- Nodes produced by more than one body: {shared}",
        f"- Records already in `{args.target.name}/` and protected: {protected}",
        f"- Written to `{args.target.name}/`: {len(written)}",
        "",
        "## Notes to adjudicate",
        "",
    ]
    lines.extend(f"- {note}" for note in sorted(notes))
    pairs = near_misses(merged)
    lines += ["", "## Near-miss ids for Task 11", "",
              "Distinct ids one token apart, which the exact-match reuse check could not see. "
              "Each is a merge, a parent-child pair, or a coincidence, and a human decides which.", ""]
    lines.extend(f"- `{a}` and `{b}`" for a, b in pairs)
    args.report.write_text("\n".join(lines) + "\n")

    print(f"{len(merged)} nodes written, {shared} shared across bodies, {len(pairs)} near-miss pairs")
    print(f"report: {args.report.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
