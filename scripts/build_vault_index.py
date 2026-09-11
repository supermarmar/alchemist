"""Write the vault wiki index the Phase 2 attach agents read once each.

    .venv/bin/python scripts/build_vault_index.py

The output is `data/vault-index.yaml`, which is gitignored along with the rest
of `data/`. It is never committed: the slugs reach this public repo anyway
through node frontmatter, whereas 477 vault article titles and topic lists
describe the shape of a private research base and buy nothing here. Rebuild it
rather than storing it; it takes seconds.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.checks import vault_root
from scripts.alchemist.vault import read_wiki

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vault", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=REPO / "data" / "vault-index.yaml")
    args = parser.parse_args()

    vault = args.vault or vault_root()
    if not (vault / "wiki").is_dir():
        print(f"no vault wiki at {vault}", file=sys.stderr)
        return 2

    articles, skipped = read_wiki(vault)
    payload = {
        "built": date.today().isoformat(),
        "vault": str(vault),
        "articles": [
            {"slug": a.slug, "title": a.title, "type": a.type,
             "topics": list(a.topics), "confidentiality": a.confidentiality}
            for a in articles
        ],
        "skipped": skipped,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))
    print(f"{len(articles)} articles indexed, {len(skipped)} skipped -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
