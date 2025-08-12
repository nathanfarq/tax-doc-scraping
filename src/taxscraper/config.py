"""Project level configuration and helpers."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

BASE_CRA_URL = "https://www.canada.ca/en/revenue-agency"
ALLOWED_DOMAIN = "www.canada.ca"
ALLOWED_PATH_PREFIX = "/en/revenue-agency"

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
RAW_HTML_DIR = DATA_DIR / "raw"
MD_DIR = DATA_DIR / "md"


def url_in_scope(url: str) -> bool:
    """Return True if the given URL is within the CRA scope."""
    parsed = urlparse(url)
    return (
        parsed.scheme in {"http", "https"}
        and parsed.netloc == ALLOWED_DOMAIN
        and parsed.path.startswith(ALLOWED_PATH_PREFIX)
    )
