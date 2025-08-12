"""Embedding utilities using sentence-transformers."""
from __future__ import annotations

from typing import List

from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-m3"
_model: SentenceTransformer | None = None


def get_model() -> SentenceTransformer:
    """Load and cache the embedding model."""
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Embed a list of texts using the configured model."""
    model = get_model()
    vectors = model.encode(texts, normalize_embeddings=True)
    return [vec.tolist() for vec in vectors]
