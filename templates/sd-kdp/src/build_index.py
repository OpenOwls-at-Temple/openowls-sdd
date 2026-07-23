"""Stage 3 — Build the retrieval index.

Chunks everything in wiki/, embeds each chunk, and writes a vector index into
.index/ for the chatbot to query. Metadata per chunk: source file, topic, tags,
provenance (see ai_specs/output_format.md front-matter).

This is a STUB. Fill in the TODOs.
"""
from __future__ import annotations

from paths import WIKI, INDEX, ensure_dirs


def chunk(text: str, size: int = 700, overlap: int = 120) -> list[str]:
    """Split text into overlapping passages."""
    # TODO: token-aware chunking with overlap
    return [text]


def embed(chunks: list[str]) -> list[list[float]]:
    """Embed chunks with the configured embedding model."""
    # TODO: call the embedding model
    raise NotImplementedError


def build_index() -> dict:
    ensure_dirs()
    stats = {"files": 0, "chunks": 0}
    for md in WIKI.rglob("*.md"):
        # TODO: read front-matter + body, chunk, embed, upsert into the store in INDEX
        stats["files"] += 1
    _ = INDEX
    return stats


if __name__ == "__main__":
    print(build_index())
