"""Simple text chunking."""
from __future__ import annotations

from typing import List


def simple_chunk(text: str, size: int = 1000, overlap: int = 100) -> List[str]:
    """Split text into overlapping chunks by characters."""
    chunks: List[str] = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + size, text_len)
        chunks.append(text[start:end])
        if end == text_len:
            break
        start = end - overlap
    return chunks
