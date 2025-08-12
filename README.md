# Tax Scraper

Pipeline for crawling, extracting, chunking and indexing tax guidance from the Canadian Revenue Agency (CRA) website.

## Features
- Scrapy based crawler respecting robots and scope restrictions
- Markdown extraction via trafilatura and lxml
- Embedding with sentence-transformers (bge-m3) into Qdrant
- CLI and FastAPI search stubs

## Development
```bash
make install  # install dependencies
make lint     # run pre-commit on all files
make test     # run pytest
```
