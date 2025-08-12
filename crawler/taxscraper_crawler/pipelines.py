"""Item pipelines."""
from __future__ import annotations


class NoopPipeline:
    """Placeholder pipeline."""

    def process_item(self, item, spider):  # type: ignore[override]
        return item
