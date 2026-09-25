from pandas import read_csv, merge


DATA = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
    "main/data/2025/2025-06-03/"
)


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors = read_csv(DATA + "gutenberg_authors.csv")
    metadata = read_csv(DATA + "gutenberg_metadata.csv")

    data = merge(
        authors,
        metadata,
        on="gutenberg_author_id",
        suffixes=("_author", "_metadata"),
    )

    return data
