import pandas as pd

from tt_gutenberg import DATA


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    if isinstance(DATA, dict):
        datasets = [pd.read_csv(source) for source in DATA.values()]

        authors = next(
            data for data in datasets
            if "alias" in data.columns
        )

        metadata = next(
            data for data in datasets
            if "gutenberg_id" in data.columns
            and "title" in data.columns
        )
    else:
        authors = pd.read_csv(DATA + "gutenberg_authors.csv")
        metadata = pd.read_csv(DATA + "gutenberg_metadata.csv")

    return pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )
