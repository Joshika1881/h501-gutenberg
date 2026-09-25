from tt_gutenberg.transform import get_data


def list_authors(by_languages=False, alias=False):
    """Return authors, optionally sorted by translation count."""
    data = get_data()

    name_column = "alias" if alias else "author_author"

    if alias:
        data = data.dropna(subset=["alias"])
        data = data[data["alias"].str.strip() != ""]

    if by_languages:
        authors = (
            data.groupby(name_column)["language"]
            .nunique()
            .sort_values(ascending=False)
        )
        return authors.index.tolist()

    return data[name_column].drop_duplicates().tolist()
