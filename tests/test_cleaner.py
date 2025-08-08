import pandas as pd
from src.cleaner import clean_articles


def test_bad_source_removal():
    data = {
        "source.name": ["CrooksAndLiars.com", "BBC"],
        "author": ["John Doe", "Jane Smith"]
    }
    df = pd.DataFrame(data)
    result = clean_articles(df)
    assert "CrooksAndLiars.com" not in result["source.name"].values