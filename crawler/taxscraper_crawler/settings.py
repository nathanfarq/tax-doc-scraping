"""Scrapy settings for taxscraper project."""
from __future__ import annotations

BOT_NAME = "taxscraper_crawler"

SPIDER_MODULES = ["taxscraper_crawler.spiders"]
NEWSPIDER_MODULE = "taxscraper_crawler.spiders"

ROBOTSTXT_OBEY = True
USER_AGENT = "taxscraper (+https://github.com/example/taxscraper; contact@example.com)"
CONCURRENT_REQUESTS = 2
DOWNLOAD_DELAY = 0.5
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.5
AUTOTHROTTLE_MAX_DELAY = 60
DEPTH_LIMIT = 2

ITEM_PIPELINES = {
    "taxscraper_crawler.pipelines.HTMLStorePipeline": 300,
}
