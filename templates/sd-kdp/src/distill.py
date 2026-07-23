"""Stage 2 — Distill.

Turns raw documents in kdb/ into distilled output in wiki/, following:
  - ai_specs/oracle.md                 (voice + intended bias)
  - ai_specs/domain_knowledge.md       (terms, rules, pitfalls)
  - ai_specs/distillation_techniques.md (how to summarize)
  - ai_specs/output_format.md          (exact output shape — the contract)

Flow (see specs for details):
  1. Load the four specs above as the system context.
  2. For each new/changed source (hash-based), extract text.
  3. Prompt the distillation model to produce output that EXACTLY follows
     output_format.md, in the Oracle's voice.
  4. Merge/dedup by topic; run the faithfulness + voice quality checks.
  5. Write wiki/articles/<slug>.md and wiki/faq/<slug>.md; regenerate wiki/index.md.

This is a STUB. Fill in the TODOs.
"""
from __future__ import annotations

from paths import AI_SPECS, KDB, WIKI_ARTICLES, WIKI_FAQ, WIKI_INDEX, ensure_dirs

SPEC_FILES = [
    "oracle.md",
    "domain_knowledge.md",
    "distillation_techniques.md",
    "output_format.md",
]


def load_specs() -> dict[str, str]:
    """Read the specs that guide distillation."""
    return {name: (AI_SPECS / name).read_text() for name in SPEC_FILES}


def extract_text(path) -> str:
    """Extract text from a PDF or a fetched .md source."""
    # TODO: PDF text extraction (+ OCR for scans); read .md directly.
    raise NotImplementedError


def distill_source(text: str, specs: dict[str, str]) -> dict:
    """Call the model to produce {article, faq} following output_format.md."""
    # TODO: build the prompt from specs + text; call the distillation model;
    #       parse the response into article + FAQ.
    raise NotImplementedError


def merge_and_write(results: list[dict]) -> None:
    """Merge per-topic, dedup, run quality checks, write wiki/ files + index."""
    # TODO: aggregation, dedup, faithfulness/voice checks, write files,
    #       regenerate WIKI_INDEX.
    raise NotImplementedError


def distill() -> dict:
    ensure_dirs()
    specs = load_specs()
    stats = {"sources": 0, "articles": 0, "faqs": 0, "failed": 0}

    results: list[dict] = []
    for src in KDB.rglob("*"):
        if not src.is_file() or src.name == ".gitkeep":
            continue
        # TODO: skip unchanged sources via the manifest
        try:
            results.append(distill_source(extract_text(src), specs))
            stats["sources"] += 1
        except Exception:  # noqa: BLE001
            stats["failed"] += 1

    merge_and_write(results)
    return stats


if __name__ == "__main__":
    print(distill())
