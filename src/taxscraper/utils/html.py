"""HTML helpers."""
from __future__ import annotations

from lxml import html


def extract_text(html_content: str) -> str:
    """Extract text from an HTML string using lxml."""
    tree = html.fromstring(html_content)
    return tree.text_content()
