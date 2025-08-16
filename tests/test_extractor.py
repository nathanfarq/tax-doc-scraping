"""Tests for extraction and metadata utilities."""
from __future__ import annotations

from extractor.extract import extract_metadata, html_to_markdown
from taxscraper.utils.hashing import hash_content


def sample_html() -> str:
    return (
        "<html lang='en'>"
        "<head><title>Sample</title><meta name='dcterms.issued' content='2024-01-01'/></head>"
        "<body><h1>Heading</h1><p>Paragraph</p></body>"
        "</html>"
    )


def test_html_to_markdown_and_metadata() -> None:
    html = sample_html()
    md = html_to_markdown(html)
    assert "\nHeading\n" in md
    meta = extract_metadata(html, "https://www.canada.ca/en/revenue-agency.html")
    assert meta["title"] == "Heading"
    assert meta["language"] == "en"
    assert meta["published_date"] == "2024-01-01"
    version_hash = hash_content(md)
    assert len(version_hash) == 64
