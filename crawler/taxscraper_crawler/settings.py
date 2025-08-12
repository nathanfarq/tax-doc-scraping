"""Scrapy settings for taxscraper project."""
from __future__ import annotations

BOT_NAME = "taxscraper_crawler"

SPIDER_MODULES = ["taxscraper_crawler.spiders"]
NEWSPIDER_MODULE = "taxscraper_crawler.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "taxscraper_crawler.pipelines.NoopPipeline": 300,
}
