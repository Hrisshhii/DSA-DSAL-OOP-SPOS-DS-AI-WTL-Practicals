1. Import libraries and load dataset
```python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

df=pd.read_csv("uber.csv")
print(df.head())
print(df.info())
print("Dataset shape:", df.shape)
```
2. Preprocess the dataset
```python3
# Remove unnecessary columns
df.drop(columns=["Unnamed: 0", "key"], errors="ignore", inplace=True)

# Convert pickup_datetime to datetime
df["pickup_datetime"] = pd.to_datetime(
    df["pickup_datetime"], errors="coerce", utc=True
)

# Remove missing values and duplicate rows
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Remove invalid fares, coordinates and passenger counts
df = df[
    (df["fare_amount"] > 0) &
    (df["pickup_longitude"].between(-180, 180)) &
    (df["dropoff_longitude"].between(-180, 180)) &
    (df["pickup_latitude"].between(-90, 90)) &
    (df["dropoff_latitude"].between(-90, 90)) &
    (df["passenger_count"] > 0)
].copy()

# Remove geographically implausible coordinates outside NYC region
df = df[
    df["pickup_longitude"].between(-75, -72) &
    df["dropoff_longitude"].between(-75, -72) &
    df["pickup_latitude"].between(40, 42) &
    df["dropoff_latitude"].between(40, 42)
].copy()

# Extract time features
df["pickup_hour"] = df["pickup_datetime"].dt.hour
df["pickup_day"] = df["pickup_datetime"].dt.day
df["pickup_month"] = df["pickup_datetime"].dt.month
df["pickup_weekday"] = df["pickup_datetime"].dt.dayofweek

# Calculate geographical distance using Haversine formula
lat1 = np.radians(df["pickup_latitude"])
lat2 = np.radians(df["dropoff_latitude"])
lon1 = np.radians(df["pickup_longitude"])
lon2 = np.radians(df["dropoff_longitude"])

a = (
    np.sin((lat2 - lat1) / 2) ** 2
    + np.cos(lat1) * np.cos(lat2)
    * np.sin((lon2 - lon1) / 2) ** 2
)

df["distance_km"] = 6371 * 2 * np.arcsin(np.sqrt(a))

# Remove zero-distance and unusually long trips
df = df[
    (df["distance_km"] > 0) &
    (df["distance_km"] < 100) &
    (df["fare_amount"] < 200)
].copy()

print("Cleaned dataset shape:", df.shape)
print(df.head())
```
3. Identify outliers
```python3
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.boxplot(y=df["fare_amount"])
plt.title("Fare Amount Outliers")

plt.subplot(1, 2, 2)
sns.boxplot(y=df["distance_km"])
plt.title("Distance Outliers")

plt.tight_layout()
plt.show()

# IQR method
for col in ["fare_amount", "distance_km"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[df[col].between(lower, upper)].copy()

print("Shape after outlier removal:", df.shape)
```

4. Check correlation
```python3
features = [
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude",
    "passenger_count",
    "pickup_hour",
    "pickup_day",
    "pickup_month",
    "pickup_weekday",
    "distance_km"
]

correlation = df[features + ["fare_amount"]].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("Correlation with fare amount:")
print(correlation["fare_amount"].sort_values(ascending=False))
```

5. Implement Linear Regression and Random Forest Regression
```python3
X = df[features]
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
```

6. Evaluate and compare models
```python3
def evaluate_model(name, actual, predicted):
    r2 = r2_score(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)

    return {
        "Model": name,
        "R2 Score": round(r2, 4),
        "RMSE": round(rmse, 4),
        "MAE": round(mae, 4)
    }

results = pd.DataFrame([
    evaluate_model("Linear Regression", y_test, lr_pred),
    evaluate_model("Random Forest", y_test, rf_pred)
])

print(results)
```

7. Predict a fare
```python3
new_ride = pd.DataFrame([{
    "pickup_longitude": -73.985,
    "pickup_latitude": 40.748,
    "dropoff_longitude": -73.977,
    "dropoff_latitude": 40.752,
    "passenger_count": 1,
    "pickup_hour": 14,
    "pickup_day": 15,
    "pickup_month": 6,
    "pickup_weekday": 0,
    "distance_km": 1.0
}])

print("Linear Regression Fare:", lr.predict(new_ride)[0])
print("Random Forest Fare:", rf.predict(new_ride)[0])
```

```text

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 2. Load dataset
df = pd.read_csv("uber.csv")

print(df.head())
print(df.info())

# 3. Preprocessing
df = df.dropna()

df = df.drop(['Unnamed: 0', 'key'], axis=1, errors='ignore')

df['pickup_datetime'] = pd.to_datetime(
    df['pickup_datetime'], errors='coerce', utc=True
)

df = df.dropna(subset=['pickup_datetime'])

# Extract time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month

df = df.drop('pickup_datetime', axis=1)

# 4. Calculate distance
def distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(
        np.radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2

    c = 2 * np.arcsin(np.sqrt(a))

    return 6371 * c

df['distance'] = distance(
    df['pickup_latitude'], df['pickup_longitude'],
    df['dropoff_latitude'], df['dropoff_longitude']
)

# 5. Remove invalid values
df = df[
    (df['pickup_latitude'].between(-90, 90)) &
    (df['dropoff_latitude'].between(-90, 90)) &
    (df['pickup_longitude'].between(-180, 180)) &
    (df['dropoff_longitude'].between(-180, 180)) &
    (df['distance'] > 0) &
    (df['distance'] < 100) &
    (df['fare_amount'] > 0) &
    (df['fare_amount'] < 100) &
    (df['passenger_count'] > 0)
]

# 6. Remove outliers using IQR
Q1 = df['fare_amount'].quantile(0.25)
Q3 = df['fare_amount'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[
    (df['fare_amount'] >= lower) &
    (df['fare_amount'] <= upper)
]

print("Shape after preprocessing:", df.shape)

# 7. Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 8. Select input and output
X = df.drop('fare_amount', axis=1)
y = df['fare_amount']

# 9. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 10. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred1 = lr.predict(X_test)

# 11. Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=100, max_depth=15, random_state=42, n_jobs=-1
)

rf.fit(X_train, y_train)

y_pred2 = rf.predict(X_test)

# 12. Evaluate models
print("\nLINEAR REGRESSION")
print("R2 Score:", r2_score(y_test, y_pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred1)))
print("MAE:", mean_absolute_error(y_test, y_pred1))

print("\nRANDOM FOREST")
print("R2 Score:", r2_score(y_test, y_pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred2)))
print("MAE:", mean_absolute_error(y_test, y_pred2))

```
