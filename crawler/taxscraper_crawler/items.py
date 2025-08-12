"""Item definitions for crawler."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class PageItem:
    """Representation of a fetched page."""
    url: str
    status: int
    body: str
    etag: Optional[str] = None
    last_modified: Optional[str] = None
