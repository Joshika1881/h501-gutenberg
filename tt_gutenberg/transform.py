import pandas as pd


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    )

    metadata = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )

    return pd.merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )


def get_languages():
    """Load the Gutenberg languages dataset."""
    return pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_languages.csv"
    )
