import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv('movies.csv')

# 🔥 LIMIT DATASET (VERY IMPORTANT)
movies = movies.head(10000)   # You can increase later

# Select useful columns
movies = movies[['title', 'genres', 'keywords', 'overview', 'poster_path', 'vote_average', 'release_date','popularity']]

# Handle missing values
movies.fillna('', inplace=True)

# Combine features
movies['features'] = movies['genres'] + " " + movies['keywords'] + " " + movies['overview']

# Vectorize
vectorizer = TfidfVectorizer(stop_words='english')
matrix = vectorizer.fit_transform(movies['features'])

# Recommendation function (optimized)
def recommend(movie_name):
    movie_name = movie_name.lower()
    matches = movies[movies['title'].str.lower() == movie_name]

    if matches.empty:
        return ["Movie not found"]

    idx = matches.index[0]

    scores = cosine_similarity(matrix[idx], matrix).flatten()
    similar_indices = scores.argsort()[::-1][1:9]

    results = []
    for i in similar_indices:
        results.append({
            "title": movies.iloc[i]['title'],
            "poster": movies.iloc[i]['poster_path'],
            "overview": movies.iloc[i]['overview'],
            "rating": movies.iloc[i]['vote_average'],
            "year": str(movies.iloc[i]['release_date'])[:4]
        })

    return results
