from pandas import read_csv, merge


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

    authors = read_csv(authors_url)
    metadata = read_csv(metadata_url)

    return merge(
        authors,
        metadata,
        on="gutenberg_author_id",
        suffixes=("_author", "_metadata"),
    )
