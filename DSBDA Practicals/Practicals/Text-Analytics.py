import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer

# Download resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample Text
text = """
Data Science is an interdisciplinary field.
It uses scientific methods and algorithms to extract knowledge from data.
"""

# Tokenization
tokens = word_tokenize(text)

print("Tokens")
print(tokens)

# POS Tagging
pos = pos_tag(tokens)

print("\nPOS Tags")
print(pos)

# Stop Word Removal
stop_words = set(stopwords.words('english'))

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("\nFiltered Words")
print(filtered_words)

# Stemming
ps = PorterStemmer()

stemmed_words = []

for word in filtered_words:
    stemmed_words.append(ps.stem(word))

print("\nStemmed Words")
print(stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in filtered_words:
    lemmatized_words.append(lemmatizer.lemmatize(word))

print("\nLemmatized Words")
print(lemmatized_words)

# TF-IDF
documents = [text]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)

print("\nFeature Names")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix")
print(tfidf.toarray())
