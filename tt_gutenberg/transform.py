from pandas import read_csv, merge


DATA = {
    "authors": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "metadata": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
}


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors = read_csv(DATA["authors"])
    metadata = read_csv(DATA["metadata"])

    data = merge(
        authors,
        metadata,
        on="gutenberg_author_id",
        suffixes=("_author", "_metadata"),
    )

    return data
