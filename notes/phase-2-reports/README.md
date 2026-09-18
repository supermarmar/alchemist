# Phase 2 attach reports

One report per batch, thirty-nine of them, written by the agents that worked batches 1 to 39
across three waves between 11 and 14 September 2026. Each names every candidate considered for
every node in its batch, the sentence or section that earned an attachment, why each rejected
candidate lost, and the reasoning behind each uncovered node.

They are here because the gap ledger records what the corpus is missing without recording
why, and the gate decides acquisition off it. The ledger was one file when these were
written and became two on 14 September 2026, `sources/wanted.yaml` for the documents to
acquire and `sources/to-ingest.yaml` for those the vault holds already, so a report naming
the single file is describing the ledger as it stood that week. Where you want to know why a
node was left uncovered, or why one article beat another, the answer is in the report for the
batch that owns the node; `.staging/phase-2/manifest.yaml` maps a node id to its batch.

The brief these were written to is `notes/phase-2-attach-brief.md`.

## The fragments are spent, and re-merging them would undo work

`.staging/phase-2/` holds the thirty-nine `ledger-NN.yaml` fragments these reports were written
beside, along with the manifest. That directory is gitignored, so it exists only in the working
tree that ran Phase 2; a fresh clone has neither the fragments nor the manifest, and the reports
are the durable record.

Treat the fragments as consumed. Their content reached `sources/wanted.yaml` and
`sources/to-ingest.yaml` in the merge of 14 September 2026, and on 18 September every entry whose
claim had been outgrown was rewritten to describe the whole span of its need, with the accumulated
per-batch paragraphs collapsed into what the acquisition gate actually reads. The fragments still
carry the superseded claims and the old paragraphs, and `merge_ledger.py` accumulates notes on a
shared id rather than keeping the first, so running it against them restores the state that
rewrite removed. Measured on 18 September 2026, one run took `assa-f107-study-material-2026` from
a four-paragraph note back to thirty-two.

Consequently a merge is the right move only for a fragment written after that date. Where an
older fragment has to be re-merged for some other reason, check the claim and note of every id it
touches afterwards.
