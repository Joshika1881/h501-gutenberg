from pandas import read_csv, merge


DATA = {
    "gutenberg_authors.csv": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    ),
    "gutenberg_metadata.csv": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    ),
    "gutenberg_languages.csv": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_languages.csv"
    ),
}


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    authors = read_csv(DATA["gutenberg_authors.csv"])
    metadata = read_csv(DATA["gutenberg_metadata.csv"])

    return merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )

