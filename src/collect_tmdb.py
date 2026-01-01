import os
import time
import requests
import pandas as pd

BASE_URL = "https://api.themoviedb.org/3"

# We will use v3 API key (most reliable for beginners)
HEADERS = {
    "Content-Type": "application/json;charset=utf-8"
}

def fetch_json(url, params=None, timeout=30):
    if params is None:
        params = {}

    # Always add v3 api_key
    api_key = os.getenv("TMDB_API_KEY", "").strip()
    if api_key:
        params["api_key"] = api_key

    r = requests.get(url, headers=HEADERS, params=params, timeout=timeout)

    if r.status_code == 401:
        print("401 Unauthorized from TMDb.")
        print("TMDB_API_KEY present?", bool(api_key))
        print("Response snippet:", r.text[:200])

    r.raise_for_status()
    return r.json()

def list_movies(endpoint, pages=10):
    """
    Collect movie IDs from list endpoints such as:
    /movie/popular
    /movie/top_rated
    """
    ids = []
    for page in range(1, pages + 1):
        data = fetch_json(f"{BASE_URL}{endpoint}", params={"page": page})
        for movie in data.get("results", []):
            if "id" in movie:
                ids.append(movie["id"])
        time.sleep(0.3)  # be gentle with the API
    return ids

def movie_details(movie_id):
    """
    Fetch detailed movie metadata by ID
    """
    return fetch_json(f"{BASE_URL}/movie/{movie_id}")

def main():
    print("Collecting movie IDs...")

    popular_ids = set(list_movies("/movie/popular", pages=25))
    top_ids = set(list_movies("/movie/top_rated", pages=25))

    all_ids = sorted(popular_ids.union(top_ids))
    print(f"Total unique movies: {len(all_ids)}")

    rows = []

    for i, movie_id in enumerate(all_ids, start=1):
        try:
            d = movie_details(movie_id)
            rows.append({
                "movie_id": d.get("id"),
                "title": d.get("title"),
                "release_date": d.get("release_date"),
                "budget": d.get("budget"),
                "revenue": d.get("revenue"),
                "runtime": d.get("runtime"),
                "vote_average": d.get("vote_average"),
                "vote_count": d.get("vote_count"),
                "popularity": d.get("popularity"),
                "genres": [g.get("name") for g in (d.get("genres") or [])]
            })
        except Exception as e:
            print(f"[WARN] Failed movie_id={movie_id}: {e}")

        if i % 50 == 0:
            print(f"Fetched {i}/{len(all_ids)} movies")

        time.sleep(0.35)

    df = pd.DataFrame(rows)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_movies.csv", index=False)

    print("✅ Saved data/raw_movies.csv")
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()
