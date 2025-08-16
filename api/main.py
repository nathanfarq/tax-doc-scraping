"""FastAPI application stub."""
from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Tax Scraper API")


@app.get("/search")
def search(q: str):
    """Stub search endpoint."""
    return {"query": q, "results": []}
