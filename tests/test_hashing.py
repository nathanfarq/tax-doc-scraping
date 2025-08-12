"""Tests for hashing utilities."""
from __future__ import annotations

import hashlib

from taxscraper.utils.hashing import hash_content


def test_hash_content() -> None:
    data = "abc"
    expected = hashlib.sha256(data.encode("utf-8")).hexdigest()
    assert hash_content(data) == expected
