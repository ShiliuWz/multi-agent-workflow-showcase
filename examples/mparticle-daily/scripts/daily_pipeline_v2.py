#!/usr/bin/env python3
"""Sanitized daily pipeline example for a content intelligence workflow.

Public demo flow:
1. Read config templates / auth placeholders
2. Fetch article metadata from a content API
3. Detect new items against a local state store
4. Download normalized text content for recent items
5. Save structured output for digest generation
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def build_public_sample() -> dict:
    sample_path = DATA_DIR / "sample_articles.json"
    return json.loads(sample_path.read_text(encoding="utf-8"))


def main() -> None:
    payload = build_public_sample()
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
