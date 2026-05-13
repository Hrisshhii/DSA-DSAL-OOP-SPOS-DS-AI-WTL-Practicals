import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("BostonHousing.csv")

print(df.head())

# Dataset Info
print(df.info())

# Missing Values
print(df.isnull().sum())

# Features and Target
X = df.drop('medv', axis=1)

y = df['medv']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Model
model = LinearRegression()

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nPredicted Values")
print(y_pred)

# Evaluation
mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)
