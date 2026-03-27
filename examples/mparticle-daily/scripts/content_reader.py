#!/usr/bin/env python3
"""Sanitized content reader example.

The original workflow reads article pages, extracts metadata, and saves
normalized text for digest generation.
"""

from dataclasses import dataclass


@dataclass
class ArticleContent:
    title: str
    pub_date: str
    content_text: str


def normalize_article(title: str, pub_date: str, content_text: str) -> ArticleContent:
    return ArticleContent(
        title=title.strip(),
        pub_date=pub_date.strip(),
        content_text=" ".join(content_text.split()),
    )


if __name__ == "__main__":
    sample = normalize_article(
        "Sample Article",
        "2026-03-26 08:15",
        "This   is   normalized   content   for   public   demonstration.",
    )
    print(sample)
