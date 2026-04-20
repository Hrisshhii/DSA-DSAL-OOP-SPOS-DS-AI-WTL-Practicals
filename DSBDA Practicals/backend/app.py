from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend,movies

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Movie Recommender API running 🎬"

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    movie = request.args.get('movie')

    if not movie:
        return jsonify({"error": "Please provide a movie name"}), 400

    results = recommend(movie)

    return jsonify({
        "movie": movie,
        "recommendations": results
    })

@app.route('/trending', methods=['GET'])
def trending():
    top_movies = movies.sort_values(by='popularity', ascending=False).head(10)

    results = []
    for _, row in top_movies.iterrows():
        results.append({
            "title": row['title'],
            "poster": row['poster_path'],
            "overview": row['overview']
        })

    return jsonify(results)

@app.route('/recent', methods=['GET'])
def recent():
    recent_movies = movies.sort_values(by='release_date', ascending=False).head(10)

    results = []
    for _, row in recent_movies.iterrows():
        results.append({
            "title": row['title'],
            "poster": row['poster_path'],
            "overview": row['overview'],
            "rating": row['vote_average'],
            "year": str(row['release_date'])[:4]
        })

    return jsonify(results)

@app.route('/top-rated', methods=['GET'])
def top_rated():
    top_movies = movies.sort_values(by='vote_average', ascending=False).head(10)

    results = []
    for _, row in top_movies.iterrows():
        results.append({
            "title": row['title'],
            "poster": row['poster_path'],
            "overview": row['overview'],
            "rating": row['vote_average'],
            "year": str(row['release_date'])[:4]
        })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

