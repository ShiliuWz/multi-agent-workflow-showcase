#!/usr/bin/env python3
"""Sanitized KB scanner example.

Demonstrates the structure of a scan -> snapshot -> diff workflow without
shipping private monitored account lists.
"""

from dataclasses import dataclass


@dataclass
class SnapshotItem:
    account_name: str
    title: str
    month_folder: str
    kb_path: str


EXAMPLE_ITEMS = [
    SnapshotItem("Example Creator A", "Workflow note", "2026-03", "/kb/example/workflow-note.md"),
    SnapshotItem("Example Creator B", "AI product memo", "2026-03", "/kb/example/ai-product-memo.md"),
]


if __name__ == "__main__":
    for item in EXAMPLE_ITEMS:
        print(item)
