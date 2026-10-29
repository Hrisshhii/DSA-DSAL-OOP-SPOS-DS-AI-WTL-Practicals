# Practical 6 - (K-Means Clustering)

### 1. Load dataset
```python3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("sales_data_sample.csv", encoding="ISO-8859-1")
print(df.head())
```

### 2. Select numerical columns
```python3
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]]
```
### 3. Scale the data
```python3
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
### 4. Find the optimal number of clusters using Elbow Method
```python3
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
```
### 5. Plot the Elbow graph
```python3
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()
```
### 6. Apply K-Means with the chosen number of clusters
```python3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nClustered Data:")
print(df[["QUANTITYORDERED", "PRICEEACH", "SALES", "Cluster"]].head())

print("\nNumber of records in each cluster:")
print(df["Cluster"].value_counts())
```
