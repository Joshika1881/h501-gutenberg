import pandas as pd


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    )
    metadata_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )

    authors = pd.read_csv(authors_url)
    metadata = pd.read_csv(metadata_url)

    data = authors.merge(
        metadata,
        on="gutenberg_author_id",
        suffixes=("_author", "_metadata"),
    )

    return data
