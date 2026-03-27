#!/usr/bin/env python3
"""Sanitized orchestrator example.

Documents the end-to-end shape of the daily content intelligence workflow.
"""

PIPELINE = [
    "scan monitored content sources",
    "detect new articles since last run",
    "extract normalized article text",
    "generate a grouped daily digest",
    "deliver digest to a chat destination",
]


if __name__ == "__main__":
    for stage in PIPELINE:
        print(f"- {stage}")
