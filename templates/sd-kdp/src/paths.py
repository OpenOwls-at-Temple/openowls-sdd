"""Shared paths for the SD-KDP pipeline.

All scripts import from here so folder locations live in one place.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

AI_SPECS = ROOT / "ai_specs"
KDB = ROOT / "kdb"          # collected raw documents (gitignored contents)
WIKI = ROOT / "wiki"        # distilled output (gitignored contents)
INDEX = ROOT / ".index"     # retrieval index
STATE = ROOT / ".state"     # manifest + run logs
BACKUPS = ROOT / "backups"  # local backups of kdb/ and wiki/

# kdb subfolders
KDB_PDFS = KDB / "pdfs"
KDB_LINKS = KDB / "links"
KDB_FETCHED = KDB / "fetched"

# wiki subfolders
WIKI_ARTICLES = WIKI / "articles"
WIKI_FAQ = WIKI / "faq"
WIKI_INDEX = WIKI / "index.md"

MANIFEST = STATE / "manifest.json"


def ensure_dirs() -> None:
    for p in (KDB_PDFS, KDB_LINKS, KDB_FETCHED, WIKI_ARTICLES, WIKI_FAQ,
              INDEX, STATE, STATE / "runs", BACKUPS):
        p.mkdir(parents=True, exist_ok=True)
