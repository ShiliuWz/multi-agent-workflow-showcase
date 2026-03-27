#!/usr/bin/env python3
"""Sanitized sync runner example.

Private implementation details for authenticated sync are omitted.
This public file documents the workflow boundary and expected stages.
"""

SYNC_STEPS = [
    "load auth from local private config",
    "request account/article metadata from content source",
    "compare against existing local state",
    "submit fetch jobs for newly discovered items",
    "store normalized metadata for downstream digest generation",
]


if __name__ == "__main__":
    for idx, step in enumerate(SYNC_STEPS, start=1):
        print(f"{idx}. {step}")
