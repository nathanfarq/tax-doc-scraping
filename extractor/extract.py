"""HTML to Markdown extraction utilities."""
from __future__ import annotations

from trafilatura import extract


def html_to_markdown(html: str) -> str:
    """Convert raw HTML to Markdown using trafilatura."""
    text = extract(html, output_format="markdown", include_tables=True)
    return text or ""
