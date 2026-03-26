"""
Sanitized sample structure for a digest workflow.
This file is for portfolio demonstration only.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Post:
    author: str
    text: str
    ts: str


def collect_posts(accounts: List[str]) -> List[Post]:
    # Replace with real collectors in private/internal environments.
    return [Post(author=a, text=f"Sample update from {a}", ts="2026-03-26T09:30:00+08:00") for a in accounts]


def render_digest(posts: List[Post]) -> str:
    lines = ["# Daily Digest", ""]
    for p in posts:
        lines.append(f"- {p.author}: {p.text}")
    return "\n".join(lines)


if __name__ == "__main__":
    sample_accounts = ["example_project", "example_founder"]
    digest = render_digest(collect_posts(sample_accounts))
    print(digest)
