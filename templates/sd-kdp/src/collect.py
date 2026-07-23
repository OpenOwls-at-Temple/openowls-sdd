"""Stage 1 — Collect.

Downloads source documents into kdb/, following ai_specs/collection_techniques.md.

Responsibilities (see the spec for details):
  - Copy/download PDFs into kdb/pdfs/.
  - Parse .md files in kdb/links/, fetch each URL, extract readable text,
    and save cleaned text into kdb/fetched/.
  - Hash every document and skip unchanged sources (change detection).
  - Respect robots.txt / rate limits; skip sources the Oracle rejects.
  - Record provenance (source URL/path) for each collected item.

This is a STUB. Fill in the TODOs.
"""
from __future__ import annotations

import hashlib
import json

from paths import KDB_LINKS, KDB_FETCHED, MANIFEST, ensure_dirs


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {}


def save_manifest(manifest: dict) -> None:
    MANIFEST.write_text(json.dumps(manifest, indent=2))


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def iter_urls() -> list[str]:
    """Read every kdb/links/*.md and return the URLs found inside."""
    urls: list[str] = []
    for md in KDB_LINKS.glob("*.md"):
        # TODO: parse markdown, extract http(s) links
        _ = md
    return urls


def fetch_readable(url: str) -> str:
    """Fetch a URL and return cleaned article text."""
    # TODO: fetch (headless browser for JS-heavy pages), strip nav/ads/boilerplate.
    raise NotImplementedError


def collect() -> dict:
    """Run the collection stage. Returns run stats."""
    ensure_dirs()
    manifest = load_manifest()
    stats = {"new": 0, "changed": 0, "skipped": 0, "failed": 0}

    for url in iter_urls():
        try:
            text = fetch_readable(url)
            digest = sha256(text)
            if manifest.get(url, {}).get("hash") == digest:
                stats["skipped"] += 1
                continue
            # TODO: write text to kdb/fetched/<slug>.md with a provenance header
            manifest[url] = {"hash": digest}
            stats["new" if url not in manifest else "changed"] += 1
        except Exception:  # noqa: BLE001 — one bad source must not abort the run
            stats["failed"] += 1

    # TODO: also hash/track PDFs in kdb/pdfs/
    save_manifest(manifest)
    return stats


if __name__ == "__main__":
    print(collect())
