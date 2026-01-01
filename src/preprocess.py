import pandas as pd
import numpy as np
import os

def main():
    df = pd.read_csv("data/raw_movies.csv")

    # Parse dates
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    # Ensure numeric
    for c in ["budget", "revenue", "runtime", "vote_average", "vote_count", "popularity"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Financial filtering (as in your README)
    df = df[(df["budget"] >= 1000) & (df["revenue"] >= 1000)]

    # Drop rows without target
    df = df.dropna(subset=["popularity"])

    # Genres column is stored as a string in CSV; convert safely
    # raw format may look like "['Action', 'Drama']"
    df["genres"] = df["genres"].fillna("[]").apply(lambda x: eval(x) if isinstance(x, str) else x)

    # One-hot encode multi-label genres
    all_genres = sorted({g for lst in df["genres"] for g in (lst or [])})
    for g in all_genres:
        df[f"Genre_{g.replace(' ', '')}"] = df["genres"].apply(lambda lst: 1 if g in (lst or []) else 0)

    # Optional: basic runtime filter (keeps realism)
    df = df[(df["runtime"].isna()) | ((df["runtime"] >= 40) & (df["runtime"] <= 240))]

    # Keep modeling columns
    keep = ["movie_id", "title", "release_date", "budget", "revenue", "runtime",
            "vote_average", "vote_count", "popularity"] + [c for c in df.columns if c.startswith("Genre_")]
    df = df[keep].dropna(subset=["budget", "revenue", "runtime", "vote_average"])

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/movies_clean.csv", index=False)
    print("Saved: data/movies_clean.csv", df.shape)

if __name__ == "__main__":
    main()

