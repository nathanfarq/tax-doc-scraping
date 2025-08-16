"""HTML to Markdown extraction and normalization pipeline."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict

from lxml import html as lxml_html
from markdownify import markdownify as md
from trafilatura.metadata import extract_metadata as tf_extract_metadata

from taxscraper.config import MD_DIR, RAW_HTML_DIR
from taxscraper.utils.hashing import hash_content


@dataclass(slots=True)
class DocumentRecord:
    """Metadata for an extracted Markdown document."""

    url: str
    source: str
    jurisdiction: str
    doc_type: str
    title: str | None
    published_date: str | None
    language: str | None
    content_hash: str
    version_hash: str
    md_path: str


def html_to_markdown(html: str) -> str:
    """Convert raw HTML to Markdown while preserving headings."""
    tree = lxml_html.fromstring(html)
    for bad in tree.xpath("//script|//style"):
        bad.drop_tree()
    cleaned_html = lxml_html.tostring(tree, encoding="unicode")
    return md(cleaned_html)


def extract_metadata(html: str, url: str) -> Dict[str, str | None]:
    """Extract metadata fields using trafilatura and lxml as fallback."""
    meta = tf_extract_metadata(html)
    tree = lxml_html.fromstring(html)
    lang = tree.xpath("//html/@lang")
    title = meta.title or (tree.xpath("//title/text()") or [url])[0]
    return {
        "title": title.strip() if isinstance(title, str) else title,
        "language": lang[0] if lang else None,
        "published_date": meta.date,
    }


def process_raw_index(index_path: Path | None = None) -> None:
    """Process raw HTML index and produce Markdown plus metadata records."""
    index_path = index_path or (RAW_HTML_DIR / "index.jsonl")
    MD_DIR.mkdir(parents=True, exist_ok=True)
    md_index_path = MD_DIR / "index.jsonl"

    with index_path.open("r", encoding="utf-8") as fin, md_index_path.open(
        "a", encoding="utf-8"
    ) as fout:
        for line in fin:
            record = json.loads(line)
            html_path = RAW_HTML_DIR / record["path"]
            html = html_path.read_text(encoding="utf-8")
            markdown = html_to_markdown(html)
            version_hash = hash_content(markdown)
            md_file = MD_DIR / f"{version_hash}.md"
            md_file.write_text(markdown, encoding="utf-8")
            meta = extract_metadata(html, record["url"])
            doc = DocumentRecord(
                url=record["url"],
                source="cra",
                jurisdiction="CA",
                doc_type="guidance",
                title=meta["title"],
                published_date=meta["published_date"],
                language=meta["language"],
                content_hash=record["content_hash"],
                version_hash=version_hash,
                md_path=md_file.name,
            )
            fout.write(json.dumps(asdict(doc)) + "\n")


def main() -> None:
    """Run extraction for all raw HTML snapshots."""
    process_raw_index()


if __name__ == "__main__":
    main()
