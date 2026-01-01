# 🎬 Cinematic Signatures: AI-Powered Movie Success Predictor

**Student:** Kaan Kaplan  
**ID:** 31946  
**Section:** D  

A comprehensive data science pipeline that leverages Machine Learning (Random Forest) to predict **movie popularity** based on **pre-release metadata** collected from TMDb.

---

## 📌 Table of Contents

1. [Project Overview](#project-overview)  
2. [Data Description](#data-description)  
3. [Methodology](#methodology)  
   - [Phase 1: Data Collection (ETL)](#phase-1-data-collection-etl)  
   - [Phase 2: Data Preprocessing & Cleaning](#phase-2-data-preprocessing--cleaning)  
   - [Phase 3: Exploratory Data Analysis (EDA)](#phase-3-exploratory-data-analysis-eda)  
   - [Phase 4: Machine Learning (Regression)](#phase-4-machine-learning-regression)  
4. [Model Evaluation](#model-evaluation)  
5. [Key Insights](#key-insights)  
6. [Sample Dataset Table](#sample-dataset-table)  
7. [Future Work](#future-work)

---

## 🚀 Project Overview

In the modern film industry, data aggregators like **The Movie Database (TMDb)** act as central hubs for movie information. They store rich metadata for each film, such as:

- Genre  
- Release date  
- Runtime  
- User ratings  
- Popularity scores  

This project investigates how such **pre-release metadata** correlates with a film’s **commercial success and popularity**.

The core goal is to formulate a **regression problem** that predicts a movie’s **TMDb popularity score** based purely on features that are realistically available **before release** (e.g., budget, runtime, genres).

---

## 📊 Data Description

**Source:** Programmatically collected from the **TMDb API**.

We use and merge data from:

- `/movie/popular`  
- `/movie/top_rated`  

This ensures a balanced dataset of both **commercial hits** and **critically acclaimed** movies.

**Approximate Dataset Size (after cleaning):**

- ~1,000–1,500 movies

### ✨ Key Features

| Feature       | Type       | Description                                                                 |
|--------------|------------|-----------------------------------------------------------------------------|
| `budget`     | Numerical  | Production budget in USD (critical predictor).                               |
| `revenue`    | Numerical  | Box office revenue in USD.                                                   |
| `runtime`    | Numerical  | Duration in minutes.                                                         |
| `genres`     | Categorical| Multi-label list (e.g. `["Action", "Sci-Fi"]`), later one-hot encoded.       |
| `vote_average` | Numerical | Average user rating (0–10).                                                 |
| `popularity` | Numerical  | **Target** – TMDb proprietary engagement score (continuous).                 |

---

## 🧠 Methodology

The project follows a **structured data science pipeline** implemented in Python, starting from raw API responses and ending with a trained regression model.

### Phase 1: Data Collection (ETL)

- **API Client:** Custom Python script using `requests`  
- **Endpoints:**
  - `/movie/popular`
  - `/movie/top_rated`
  - `/movie/{id}` (to fetch full metadata including budget/revenue)
- **Granularity:**  
  These list endpoints **do not** provide financial data, so each movie receives a second detailed query.
- **Volume:**  
  - ~2,000+ movies collected  
  - Valid entries reduced after filtering unrealistic values

> Objective: Build a **statistically meaningful dataset** with clean metadata + financials.

---

### Phase 2: Data Preprocessing & Cleaning

1. **Financial Filtering**
   - Remove unrealistic movies where:
     - `budget < 1000` OR  
     - `revenue < 1000`  
   - Prevents the model from learning noise.

2. **Date Parsing**
   - Convert `release_date` → `datetime`.

3. **Encoding Genres**
   - Multi-label genre lists transformed via **One-Hot Encoding**.
   - Example columns:  
     - `Genre_Action`, `Genre_Drama`, `Genre_SciFi`, etc.

---

### Phase 3: Exploratory Data Analysis (EDA)

- **Correlation Heatmap:**  
  Shows relationships among budget, revenue, runtime, and popularity.
- **Distribution Analysis:**  
  Detects outliers and skewness in popularity scores.

---

### Phase 4: Machine Learning (Regression)

- **Algorithm:** Random Forest Regressor  
- **Train/Test Split:** 80% / 20%  
- **Metrics:**
  - RMSE  
  - R² Score  

Random Forest handles non-linearity and feature interactions extremely well.

---

## 📏 Model Evaluation

- **RMSE** evaluates prediction error magnitude.  
- **R²** explains how much variance in popularity is captured.  

Higher budget and certain genres produce notably higher predictive power.

---

## 💡 Key Insights

1. **Budget is the strongest predictor** of popularity.  
2. Genres like **Action**, **Adventure**, **Sci-Fi** significantly enhance performance.  
3. Very long movies (>180 minutes) often show diminishing popularity unless paired with huge budgets.  
4. Ratings matter but financials matter more.

---

## 📁 Sample Dataset Table

A realistic example of how the cleaned dataset looks after preprocessing:

| movie_id | title              | budget      | revenue      | runtime | Genre_Action | Genre_Drama | Genre_SciFi | vote_average | popularity |
|----------|--------------------|-------------|--------------|---------|--------------|--------------|--------------|---------------|------------|
| 19995    | Avatar             | 237000000   | 2847246203   | 162     | 1            | 0            | 1            | 7.5           | 150.437     |
| 155      | The Dark Knight    | 185000000   | 1004558444   | 152     | 1            | 1            | 0            | 8.5           | 98.312      |
| 24428    | The Avengers       | 220000000   | 1518812988   | 143     | 1            | 0            | 1            | 7.7           | 125.874     |
| 597      | Titanic            | 200000000   | 2187463944   | 195     | 0            | 1            | 0            | 7.9           | 80.123      |
| 1124     | The Matrix         | 63000000    | 466364845    | 136     | 1            | 0            | 1            | 8.2           | 70.548      |
| 157336   | Interstellar       | 165000000   | 701729206    | 169     | 0            | 1            | 1            | 8.6           | 85.921      |
| 424      | Schindler's List   | 22000000    | 322161245    | 195     | 0            | 1            | 0            | 8.9           | 45.317      |
| 102899   | Ant-Man            | 130000000   | 519311965    | 117     | 1            | 0            | 1            | 7.0           | 72.661      |

> 🎯 This sample reflects the exact format the model receives post-cleaning and encoding.
>
 ## 🔮 Future Work

- **Add NLP processing for movie descriptions**  
  Incorporate textual features using TF-IDF, word embeddings, or transformer-based encoders (BERT, DistilBERT) to improve prediction accuracy.

- **Explore XGBoost / LightGBM**  
  Benchmark tree-boosting models against Random Forest to evaluate improvements in R² and RMSE.

- **Build a Streamlit prediction dashboard**  
  Develop an interactive web app where users can input metadata (budget, runtime, genres) and receive a predicted popularity score.

- **Add seasonality-based features**  
  Integrate temporal variables such as month, quarter, and holiday release periods to capture release-timing effects.