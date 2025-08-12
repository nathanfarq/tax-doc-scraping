"""CLI utilities for querying Qdrant (stub)."""
from __future__ import annotations

import click


@click.command()
@click.argument("query")
def main(query: str) -> None:
    """Search Qdrant for the given query (placeholder)."""
    click.echo(f"Query: {query}")


if __name__ == "__main__":
    main()
