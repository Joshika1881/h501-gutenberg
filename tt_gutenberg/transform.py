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
}


def get_data():
    """Load and merge the Gutenberg authors and metadata datasets."""
    datasets = [read_csv(source) for source in DATA.values()]

    authors = next(
        data for data in datasets
        if "alias" in data.columns
    )
    metadata = next(
        data for data in datasets
        if "title" in data.columns
    )

    return merge(
        authors,
        metadata,
        on="gutenberg_author_id",
    )

