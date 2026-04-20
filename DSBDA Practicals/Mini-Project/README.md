### Algorithms Used

# Content-Based Filtering (Main Algorithm)
Recommends movies based on similarity of features
Uses:
- Genres
- Keywords
- Overview
Idea:
- If two movies have similar content → recommend them

# TF-IDF Vectorization
Converts text → numerical vectors
Highlights important words
Used on:
- genres + keywords + overview
- Purpose:
Convert movie content into machine-understandable format

# Cosine Similarity
Formula used:
cosine similarity=A.B/∥A∥∥B∥
- Measures similarity between two movie vectors
Output:
- Value between 0 and 1
- Higher = more similar

# Sorting Algorithms (Data Processing)
Used internally:
- Sort by popularity → Trending
- Sort by release_date → Recent
- Sort by vote_average → Highest Rated
