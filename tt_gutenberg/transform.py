import pandas as pd

from tt_gutenberg import DATA


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    if isinstance(DATA, dict):
        sources = list(DATA.values())
        authors = pd.read_csv(sources[0])
        metadata = pd.read_csv(sources[1])
    else:
        authors = pd.read_csv(DATA + "gutenberg_authors.csv")
        metadata = pd.read_csv(DATA + "gutenberg_metadata.csv")

    return pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )


def get_languages():
    """Load the Gutenberg languages dataset."""
    if isinstance(DATA, dict):
        sources = list(DATA.values())
        return pd.read_csv(sources[2])

    return pd.read_csv(DATA + "gutenberg_languages.csv")
