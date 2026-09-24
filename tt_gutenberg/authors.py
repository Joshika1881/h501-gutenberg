import pandas as pd

from tt_gutenberg.utils import clean_aliases, load_data


def list_authors(by_languages=False, alias=False):
    """Return authors, optionally ordered by language count."""
    authors, metadata, languages = load_data()

    if alias:
        authors = clean_aliases(authors)

    author_data = authors.merge(
        metadata[["gutenberg_author_id", "gutenberg_id"]],
        on="gutenberg_author_id",
    )

    author_data = author_data.merge(
        languages[["gutenberg_id", "language"]],
        on="gutenberg_id",
    )

    name_column = "alias" if alias else "author"

    if by_languages:
        author_data = (
            author_data.groupby(name_column)["language"]
            .nunique()
            .sort_values(ascending=False)
        )
        return author_data.index.tolist()

    return author_data[name_column].drop_duplicates().tolist()