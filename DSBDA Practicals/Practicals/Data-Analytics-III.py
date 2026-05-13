import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score
)

# Load Dataset
df = pd.read_csv("Iris.csv")

print(df.head())

# Features and Target
X = df.iloc[:, 1:5]

y = df.iloc[:, 5]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42
)

# Create Model
model = GaussianNB()

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nPredicted Values")
print(y_pred)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Error Rate
error_rate = 1 - accuracy

print("Error Rate:", error_rate)

# Precision
precision = precision_score(y_test, y_pred, average='macro')

print("Precision:", precision)

# Recall
recall = recall_score(y_test, y_pred, average='macro')

print("Recall:", recall)
