import pandas as pd
import numpy as np
from scipy import stats

def mann_whitney(a, b):
    a = a.dropna()
    b = b.dropna()
    return stats.mannwhitneyu(a, b, alternative="two-sided")

def spearman(x, y):
    df = pd.concat([x, y], axis=1).dropna()
    r, p = stats.spearmanr(df.iloc[:,0], df.iloc[:,1])
    return r, p, len(df)

def main():
    df = pd.read_csv("data/movies_clean.csv")
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    # 1) Spearman: popularity vs budget
    r, p, n = spearman(df["popularity"], df["budget"])
    print(f"[TEST 1] Spearman(popularity, budget): r={r:.4f}, p={p:.4g}, n={n}")

    # 2) Spearman: popularity vs vote_average
    r, p, n = spearman(df["popularity"], df["vote_average"])
    print(f"[TEST 2] Spearman(popularity, vote_average): r={r:.4f}, p={p:.4g}, n={n}")

    # 3) Action vs non-Action
    if "Genre_Action" in df.columns:
        action = df[df["Genre_Action"] == 1]["popularity"]
        non_action = df[df["Genre_Action"] == 0]["popularity"]
        u, p = mann_whitney(action, non_action)
        print(f"[TEST 3] Mann-Whitney(Action vs Non-Action): U={u:.1f}, p={p:.4g}")
    else:
        print("[TEST 3] Genre_Action column not found.")

    # 4) Pre-2010 vs 2010+
    pre = df[df["release_date"] < "2010-01-01"]["popularity"]
    post = df[df["release_date"] >= "2010-01-01"]["popularity"]
    u, p = mann_whitney(pre, post)
    print(f"[TEST 4] Mann-Whitney(Pre-2010 vs 2010+): U={u:.1f}, p={p:.4g}")

if __name__ == "__main__":
    main()
