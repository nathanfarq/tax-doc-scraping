"""Item pipelines for storing raw HTML."""
from __future__ import annotations

from datetime import datetime
import json

from taxscraper.config import RAW_HTML_DIR
from taxscraper.utils.hashing import hash_content
from taxscraper_crawler.items import PageItem


class HTMLStorePipeline:
    """Persist fetched HTML and metadata."""

    def open_spider(self, spider):  # type: ignore[override]
        RAW_HTML_DIR.mkdir(parents=True, exist_ok=True)
        self.index_path = RAW_HTML_DIR / "index.jsonl"
        self.index_file = self.index_path.open("a", encoding="utf-8")

    def close_spider(self, spider):  # type: ignore[override]
        self.index_file.close()

    def process_item(self, item: PageItem, spider):  # type: ignore[override]
        content_hash = hash_content(item.body)
        html_file = RAW_HTML_DIR / f"{content_hash}.html"
        html_file.write_text(item.body, encoding="utf-8")
        record = {
            "url": item.url,
            "status": item.status,
            "etag": item.etag,
            "last_modified": item.last_modified,
            "fetched_at": datetime.utcnow().isoformat(),
            "content_hash": content_hash,
            "path": html_file.name,
        }
        self.index_file.write(json.dumps(record) + "\n")
        return item
