from pandas import read_csv, merge

from tt_gutenberg.transform import DATA, get_data


def list_authors(by_languages=False, alias=False):
    """Return authors, optionally sorted by translation count."""
    data = get_data()
    name_column = "alias" if alias else "author_x"

    if alias:
        data = data.dropna(subset=["alias"])
        data = data[data["alias"].str.strip() != ""]

    if by_languages:
        languages = read_csv(DATA["gutenberg_languages.csv"])

        data = merge(
            data,
            languages,
            on="gutenberg_id",
        )

        authors = (
            data.groupby(name_column)["total_languages"]
            .count()
            .sort_values(ascending=False)
        )

        return authors.index.tolist()

    return data[name_column].drop_duplicates().tolist()
