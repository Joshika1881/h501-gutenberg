from tt_gutenberg.transform import get_data


def list_authors(by_languages=False, alias=False):
    """Return authors or aliases, optionally sorted by translation count."""
    data = get_data()
    name_column = "alias" if alias else "author_x"

    if alias:
        data = data.dropna(subset=["alias"])
        data = data[data["alias"].str.strip() != ""]

    if by_languages:
        data = data.dropna(subset=["language"]).copy()
        data["language"] = data["language"].str.split("/")
        data = data.explode("language")

        counts = (
            data.groupby(name_column)["language"]
            .count()
            .sort_values(ascending=False)
        )

        return counts.index.tolist()

    return data[name_column].drop_duplicates().tolist()
