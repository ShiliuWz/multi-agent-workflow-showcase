#!/usr/bin/env python3
"""Sanitized analyzer example.

The private version can call an LLM to create grouped summaries.
The public version keeps only deterministic local summarization logic.
"""

from collections import defaultdict
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "sample_articles.json"


def generate_summary(data: dict) -> str:
    by_account = defaultdict(list)
    for article in data.get("articles", []):
        by_account[article["account"]].append(article["title"])

    lines = [f"# Daily Digest · {data['date']}", ""]
    lines.append(f"Total new articles: {data['total_new']}")
    lines.append("")
    for account, titles in sorted(by_account.items()):
        lines.append(f"## {account}")
        for title in titles:
            lines.append(f"- {title}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    data = json.loads(SAMPLE.read_text(encoding="utf-8"))
    print(generate_summary(data))


if __name__ == "__main__":
    main()
