import pandas as pd


def load_data():
    """Load the Gutenberg datasets needed for the analysis."""
    authors_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_authors.csv"
    )
    metadata_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )
    languages_url = (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "main/data/2025/2025-06-03/gutenberg_languages.csv"
    )

    authors = pd.read_csv(authors_url)
    metadata = pd.read_csv(metadata_url)
    languages = pd.read_csv(languages_url)

    return authors, metadata, languages


def clean_aliases(data):
    """Remove missing and empty alias values."""
    aliases = data.dropna(subset=["alias"]).copy()
    aliases = aliases[aliases["alias"].str.strip() != ""]
    return aliases