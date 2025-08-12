"""Hashing utilities."""
from __future__ import annotations

import hashlib
from typing import Union


def hash_content(content: Union[str, bytes]) -> str:
    """Return SHA256 hex digest for the given content."""
    if isinstance(content, str):
        content = content.encode("utf-8")
    return hashlib.sha256(content).hexdigest()
