#!/usr/bin/env python3
"""Sanitized webhook delivery example.

This public version only builds a preview payload and prints it locally.
No real webhook is included in the repository.
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "sample_articles.json"


def build_card(data: dict) -> dict:
    return {
        "header": {"title": "Daily Content Intelligence Digest"},
        "summary": {
            "date": data["date"],
            "total_new": data["total_new"],
            "updated_accounts": len(data.get("accounts", {})),
        },
        "highlights": [
            {"account": article["account"], "title": article["title"]}
            for article in data.get("articles", [])[:5]
        ],
    }


def main() -> None:
    data = json.loads(SAMPLE.read_text(encoding="utf-8"))
    print(json.dumps(build_card(data), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
