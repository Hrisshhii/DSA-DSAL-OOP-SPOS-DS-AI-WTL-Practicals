# Algorithms Used

### Content-Based Filtering (Main Algorithm)
Recommends movies based on similarity of features
Uses:
- Genres
- Keywords
- Overview
Idea:
- If two movies have similar content → recommend them

### TF-IDF Vectorization
Converts text → numerical vectors
Highlights important words
Used on:
- genres + keywords + overview
- Purpose:
Convert movie content into machine-understandable format

### Cosine Similarity
Formula used:
cosine similarity=A.B/∥A∥∥B∥
- Measures similarity between two movie vectors
Output:
- Value between 0 and 1
- Higher = more similar

### Sorting Algorithms (Data Processing)
Used internally:
- Sort by popularity → Trending
- Sort by release_date → Recent
- Sort by vote_average → Highest Rated

# Libraries Used (Backend - Python)

### Core Libraries

## 4. Sorting Techniques (Data Processing)

Used to generate different movie sections:

- Sort by **popularity** → Trending  
- Sort by **release_date** → Recent Movies  
- Sort by **vote_average** → Highest Rated  

---

# 🧰 Libraries Used

## 🔙 Backend (Python)

### Core Libraries

```bash
pip install pandas
pip install scikit-learn
pip install numpy
```
Purpose:
pandas
→ Data loading and manipulation (CSV handling)
scikit-learn
→ TF-IDF Vectorization (TfidfVectorizer)
→ Cosine Similarity
numpy
→ Numerical computations (used internally)

### Web Backend
```bash
pip install flask
pip install flask-cors
```

Purpose:
Flask
→ Backend API development
Flask-CORS
→ Enables communication between frontend and backend

## 🌐 Frontend (React + Tailwind)
```bash
npm create vite@latest
npm install
npm install tailwindcss @tailwindcss/vite
```

Technologies Used:
React
→ UI development
Tailwind CSS
→ Modern styling
Vite
→ Fast development environment

# 📌 Summary

This project uses a Content-Based Recommendation System where movie features such as genres, keywords, and overview are converted into numerical vectors using TF-IDF vectorization.
Cosine similarity is then used to find similar movies and generate recommendations.
The backend is built using Flask, and the frontend is developed using React with Tailwind CSS.
