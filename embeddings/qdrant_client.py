"""Qdrant client helpers."""
from __future__ import annotations

from qdrant_client import QdrantClient


def get_qdrant_client(url: str = "http://localhost:6333") -> QdrantClient:
    """Return a Qdrant client instance."""
    return QdrantClient(url=url)
