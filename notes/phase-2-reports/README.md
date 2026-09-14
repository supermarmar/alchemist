# Phase 2 attach reports

One report per batch, thirty-nine of them, written by the agents that worked batches 1 to 39
across three waves between 11 and 14 September 2026. Each names every candidate considered for
every node in its batch, the sentence or section that earned an attachment, why each rejected
candidate lost, and the reasoning behind each uncovered node.

They are here because `sources/wanted.yaml` records what the corpus is missing without
recording why, and the gate decides acquisition off that file. Where you want to know why a
node was left uncovered, or why one article beat another, the answer is in the report for the
batch that owns the node; `.staging/phase-2/manifest.yaml` maps a node id to its batch.

The brief these were written to is `notes/phase-2-attach-brief.md`.
