from tt_gutenberg.transform import get_data, get_languages


def list_authors(by_languages=False, alias=False):
    """Return authors or aliases, optionally sorted by translation count."""
    data = get_data()
    name_column = "alias" if alias else "author_x"

    if alias:
        data = data.dropna(subset=["alias"])
        data = data[data["alias"].str.strip() != ""]

    if by_languages:
        languages = get_languages()

        data = data.drop(
            columns=["language"],
            errors="ignore",
        ).merge(
            languages[["gutenberg_id", "language"]],
            on="gutenberg_id",
        )

        counts = (
            data.groupby(name_column)["language"]
            .count()
            .sort_values(ascending=False)
        )

        return counts.index.tolist()

    return data[name_column].drop_duplicates().tolist()
