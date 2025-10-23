KAAN KAPLAN 31946 SECTION D

# Sonic Signatures: An Analysis of Apple Music's Audio Features and their Correlation with Chart Popularity

#### INTRODUCTION

In the modern music industry, streaming platforms like Apple Music are a dominant force. These platforms not only distribute music but also meticulously categorize it, assigning every track a rich set of metadata (like genre, release date, duration). This creates a unique opportunity to study music with objective data. However, the relationship between this metadata and a song's actual commercial success remains a complex and interesting question.

This project intends to investigate the measurable properties of music on Apple Music to determine if there are significant correlations between a song's metadata and its performance on Apple Music's influential charts.

#### OBJECTIVES

- To quantify and analyze the distributions of core metadata (e.g., genre, durationInMillis, releaseDate) for songs appearing on major Apple Music charts.

- To evaluate the statistical relationship between these metadata features and a song's position on the charts.

- To compare the genre distribution and average song duration of different chart types (e.g., "Top Songs: Global" vs. "Top Songs: USA") to identify distinct characteristics.

- To offer data-driven insights into the metadata combinations (e.g., genre + duration) that are most common in high-performing tracks.

#### DATA SOURCES

Data will be sourced exclusively and programmatically from the Apple Music API.

**Charts Endpoint:** To retrieve the complete list of track IDs from curated charts, specifically the "Top Songs: Global" chart.

**Catalog Endpoints:** To gather track-specific metadata, including artist, name, genreNames, durationInMillis, and releaseDate.

#### METHODOLOGY

**1-Data Collection:**

An automated Python script will be developed using libraries like requests and PyJWT.
The script will authenticate with the Apple Music API using a private key and developer token.
It will fetch all tracks from the target charts, extract their unique IDs, and then query the API for the corresponding catalog metadata.
The consolidated data (track info, chart position, genre, duration, release date) will be compiled into a single Pandas DataFrame and saved as apple_music_data.csv to ensure the analysis is reproducible.

**2-Data Processing:**

The raw data will be cleaned. durationInMillis will be converted to seconds.
A chart_position feature will be used as a proxy for popularity.
The genreNames array will be processed to analyze primary and secondary genres.

**3-Descriptive Statistics:**

Mean, median, and standard deviation will be calculated for durationInMillis.
Frequency distributions for genreNames will be calculated and visualized (e.g., bar chart).

**4-Correlation Analysis:**

A correlation analysis will be generated to measure the relationship between durationInMillis or releaseDate and chart_position.

**5-Hypothesis Testing:**

A Chi-square test could be used to see if the genre distribution on one chart (e.g., 'Global') is significantly different from another (e.g., 'USA').
**Null Hypothesis:** There is no statistically significant difference in the mean durationInMillis between songs in the Top 10 and songs in the 50-100 range.
**Alternative Hypothesis:** A statistically significant difference exists in the mean durationInMillis based on chart position.

**6-Interpretation and Perspectives:**

The results will be interpreted to determine which metadata features, if any, are most strongly associated with high chart performance.
The analysis will explore whether 'hit' songs have an 'optimal' duration or are dominated by specific genres.

#### EXPECTED OUTCOMES

A high-quality, clean dataset of popular songs from Apple Music and their metadata, ready for analysis.
Statistically-backed findings on the genres that are most correlated with chart success.
A clear, comparative analysis defining the "typical" metadata profile of a hit song on Apple Music.
A final report and/or Jupyter Notebook with visualizations (bar charts, histograms, scatter plots) that communicate the project's findings.


