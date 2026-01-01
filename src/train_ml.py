import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def eval_model(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, pred, squared=False)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    return {"model": name, "RMSE": rmse, "MAE": mae, "R2": r2}

def main():
    df = pd.read_csv("data/movies_clean.csv")

    target = "popularity"
    y = df[target].astype(float)

    # Features: numeric + one-hot genres
    numeric = ["budget", "revenue", "runtime", "vote_average", "vote_count"]
    genre_cols = [c for c in df.columns if c.startswith("Genre_")]
    features = numeric + genre_cols
    X = df[features]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Preprocess numeric columns: impute + scale
    pre = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler()),
            ]), numeric),
            ("genre", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
            ]), genre_cols),
        ],
        remainder="drop"
    )

    models = [
        ("Ridge (baseline)", Ridge(alpha=1.0, random_state=42)),
        ("RandomForest", RandomForestRegressor(
            n_estimators=400, random_state=42, n_jobs=-1,
            max_depth=None, min_samples_leaf=2
        )),
        ("GradientBoosting", GradientBoostingRegressor(random_state=42))
    ]

    results = []
    for name, reg in models:
        pipe = Pipeline([("pre", pre), ("reg", reg)])
        results.append(eval_model(name, pipe, X_train, X_test, y_train, y_test))

    res = pd.DataFrame(results).sort_values("RMSE")
    print(res.to_string(index=False))

if __name__ == "__main__":
    main()

