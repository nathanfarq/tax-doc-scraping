"""Spider for CRA pages."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import scrapy
import yaml
from taxscraper_crawler.items import PageItem

from taxscraper.config import url_in_scope

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SEED_PATH = PROJECT_ROOT / "seeds" / "cra.yaml"
with SEED_PATH.open("r", encoding="utf-8") as f:
    CFG = yaml.safe_load(f)


class CraSpider(scrapy.Spider):
    name = "cra"
    allowed_domains = CFG["allow_domains"]
    custom_settings = {
        "DEPTH_LIMIT": CFG.get("max_depth", 2),
        "DOWNLOAD_DELAY": CFG.get("rate_limit", {}).get("download_delay", 0.5),
        "CONCURRENT_REQUESTS": CFG.get("rate_limit", {}).get("concurrent_requests", 2),
    }

    def start_requests(self) -> Iterable[scrapy.Request]:  # type: ignore[override]
        for url in CFG["start_urls"]:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response: scrapy.http.Response, **kwargs):  # type: ignore[override]
        item = PageItem(
            url=response.url,
            status=response.status,
            body=response.text,
            etag=response.headers.get("ETag"),
            last_modified=response.headers.get("Last-Modified"),
        )
        yield item
        for href in response.css("a::attr(href)").getall():
            url = response.urljoin(href)
            if not url_in_scope(url):
                continue
            if any(
                url.startswith(f"https://{self.allowed_domains[0]}{p}")
                for p in CFG.get("deny_paths", [])
            ):
                continue
            yield scrapy.Request(url, callback=self.parse)
