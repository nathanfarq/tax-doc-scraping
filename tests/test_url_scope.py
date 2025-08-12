"""Tests for CRA URL scope logic."""
from __future__ import annotations

from taxscraper.config import url_in_scope


def test_url_in_scope() -> None:
    assert url_in_scope("https://www.canada.ca/en/revenue-agency.html")
    assert not url_in_scope("https://www.canada.ca/en/other-agency.html")
