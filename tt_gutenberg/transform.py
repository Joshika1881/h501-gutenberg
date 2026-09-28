import pandas as pd

from tt_gutenberg import DATA


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors = pd.read_csv(DATA + "gutenberg_authors.csv")
    metadata = pd.read_csv(DATA + "gutenberg_metadata.csv")

    return pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )