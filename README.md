 KAAN KAPLAN 31946 SECTION D

# Cinematic Signatures: An Analysis of Movie Metadata and its Correlation with Popularity

#### INTRODUCTION

In the modern film industry, data aggregators like **The Movie Database (TMDb)** are a dominant force. These platforms not only catalog films but also meticulously categorize them, assigning every title a rich set of metadata (like genre, release date, runtime, and user scores). This creates a unique opportunity to study films with objective data. However, the relationship between this metadata and a movie's actual commercial success or popular reception remains a complex and interesting question.

This project intends to investigate the measurable properties of movies on TMDb to determine if there are significant correlations between a film's metadata and its performance metrics (like popularity score and user ratings).

#### OBJECTIVES

- To quantify and analyze the distributions of core metadata (e.g., genre, runtime, release_date) for movies appearing on major TMDb lists.

- To evaluate the statistical relationship between these metadata features and a movie's popularity score and vote_average.

- To compare the genre distribution and average runtime of different movie lists (e.g., "Popular" vs. "Top Rated") to identify distinct characteristics.

- To offer data-driven insights into the metadata combinations (e.g., genre + runtime) that are most common in high-performing films.

#### DATA SOURCES

Data will be sourced exclusively and programmatically from **The Movie Database (TMDb) API**.

- **List Endpoints:** To retrieve the complete list of movie IDs from curated lists, specifically the "/movie/popular" and "/movie/top_rated" charts.

- **Movie Details Endpoint:** To gather movie-specific metadata, including title, genres, runtime, release_date, popularity, and vote_average.

#### METHODOLOGY

**1. Data Collection:**

- An automated Python script will be developed using the "requests" library.
- The script will authenticate with the TMDb API using a simple API key.
- It will fetch all movies from the target lists, extract their unique IDs, and then query the API for the corresponding detailed metadata.
- The consolidated data (movie info, popularity, genres, runtime, release date) will be compiled into a single Pandas DataFrame and saved as tmdb_movie_data.csv to ensure the analysis is reproducible.

**2. Data Processing:**

- The raw data will be cleaned. The runtime is already in minutes and suitable for direct analysis.
- popularity and vote_average will be used as the primary proxies for success.
- The genres list (an array of objects) will be processed to extract the primary and secondary genres for analysis.

**3. Descriptive Statistics:**

- Mean, median, and standard deviation will be calculated for runtime, popularity, and vote_average.
- Frequency distributions for genres will be calculated and visualized (e.g., bar chart).

**4. Correlation Analysis:**

- A correlation heatmap will be generated to measure the relationship between numerical features like runtime, release_date, popularity, and vote_average.

**5. Hypothesis Testing:**

- A **Chi-square test** will be used to see if the genre distribution on one list (e.g., 'Popular') is significantly different from another (e.g., 'Top Rated').
- **Null Hypothesis:** There is no statistically significant difference in the mean runtime between movies with a high vote_average (e.g., > 8.0) and movies with a moderate vote_average (e.g., 5.0-7.0).
- **Alternative Hypothesis:** A statistically significant difference exists in the mean runtime based on user rating.

**6. Interpretation and Perspectives:**

- The results will be interpreted to determine which metadata features, if any, are most strongly associated with high popularity or user ratings.
- The analysis will explore whether 'hit' movies have an 'optimal' runtime or are dominated by specific genres.

#### EXPECTED OUTCOMES

- A high-quality, clean dataset of popular movies from TMDb and their metadata, ready for analysis.
- Statistically-backed findings on the genres that are most correlated with high user ratings.
- A clear, comparative analysis defining the "typical" metadata profile of a successful movie on TMDb.
- A final report and/or Jupyter Notebook with visualizations (bar charts, histograms, scatter plots) that communicate the project's findings.
