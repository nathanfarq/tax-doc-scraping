"""Scrapy middlewares placeholders."""
from __future__ import annotations

from scrapy import signals


class TaxscraperSpiderMiddleware:
    """Placeholder spider middleware."""

    @classmethod
    def from_crawler(cls, crawler):  # type: ignore[override]
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):  # type: ignore[override]
        spider.logger.info("Spider opened: %s", spider.name)


class TaxscraperDownloaderMiddleware:
    """Placeholder downloader middleware."""

    def process_request(self, request, spider):  # type: ignore[override]
        return None
