#!/usr/bin/env python3
"""Sanitized schema example for the public workflow package."""

SCHEMA = {
    "kb_snapshots": ["snapshot_date", "account_name", "month_folder", "kb_path", "title", "file_hash"],
    "articles": ["account_name", "title", "kb_url", "pub_date", "content_text", "discovered_date"],
    "daily_reports": ["report_date", "article_count", "account_count", "report_markdown"],
    "delivery_log": ["report_date", "channel", "target", "status", "message_id"],
}


if __name__ == "__main__":
    for table, fields in SCHEMA.items():
        print(f"{table}: {', '.join(fields)}")
