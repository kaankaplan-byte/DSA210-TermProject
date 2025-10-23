KAAN KAPLAN 31946 SECTION D

#TITLE

INTRODUCTION

In the modern music industry, streaming platforms like Spotify are the dominant force. These platforms not only distribute music but also quantify it, assigning every track a set of "audio features." This creates a unique opportunity to study music with objective data. However, the relationship between these quantitative features (like energy, danceability, valence) and a song's actual commercial success remains a complex and interesting question.

This project intends to investigate the measurable sonic properties of music to determine if there are significant correlations between a song's audio profile and its performance on Spotify's influential charts.

OBJECTIVES

-To quantify and analyze the distributions of core audio features (e.g., valence, energy, acousticness) for songs appearing on major Spotify playlists.

-To evaluate the statistical relationship between these audio features and Spotify's internal popularity metric.

-To compare the mean audio feature profiles of different chart types (e.g., "Global Top 50" vs. "Global Viral 50") to identify distinct sonic characteristics.

-To offer data-driven insights into the audio-feature combinations that are most common in high-performing tracks.

DATA SOURCES

Data will be sourced exclusively and programmatically from the Spotify Web API.

-Playlist Endpoints: To retrieve the complete list of track IDs from curated charts, specifically the "Global Top 50" (play-driven) and "Global Viral 50" (share-driven).

-Track Endpoints: To gather track-specific metadata, including artist, name, and the popularity metric.

-Audio Features Endpoint: To obtain the detailed quantitative audio feature data for each track ID.

METHODOLOGY

1:Data Collection:

An automated Python script will be developed using the spotipy library.

The script will authenticate with the Spotify API using Client Credentials.

It will fetch all tracks from the target playlists, extract their unique IDs, and then query the API for the corresponding audio features.

The consolidated data (track info, popularity, and features) will be compiled into a single Pandas DataFrame and saved as spotify_data.csv to ensure the analysis is reproducible.

2:Data Processing:

The raw data will be cleaned to handle any missing values or duplicates.

A 'playlist_source' (e.g., 'Top 50', 'Viral 50') feature will be created to label each track.

The distributions of key audio features will be examined.

3:Descriptive Statistics:

Mean, median, mode, and standard deviation will be calculated for all continuous audio features (e.g., danceability, energy) across the entire dataset and for each playlist sub-group.

4:Correlation Analysis:

A Pearson correlation matrix will be generated to measure the linear relationships between all continuous audio features and the popularity score. This will be visualized using a heatmap.

5:Hypothesis Testing:

An independent two-sample t-test will be used to compare the mean feature values of the two playlists.

Null Hypothesis (H0): There is no statistically significant difference in the mean valence (or other selected features) between songs on the 'Global Top 50' and songs on the 'Global Viral 50'.

Alternative Hypothesis (H1): A statistically significant difference exists in the mean valence (or other features) between the two chart types.

6:Interpretation and Perspectives:

The results will be interpreted to determine which sonic features, if any, are most strongly associated with popularity.

The analysis will explore whether different types of popularity (play-driven vs. share-driven) correspond to different "sonic signatures."

EXPECTED OUTCOMES

-A high-quality, clean dataset of popular songs and their audio features, ready for analysis.

-Statistically-backed findings on the audio features that are most (and least) correlated with a song's popularity score.

-A clear, comparative analysis defining the "typical" audio profile of songs on the 'Global Top 50' versus the 'Global Viral 50'.

-A final report and/or Jupyter Notebook with visualizations (histograms, boxplots, heatmaps) that communicate the project's findings.


