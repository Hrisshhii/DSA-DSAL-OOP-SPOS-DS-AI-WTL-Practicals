import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = sns.load_dataset("iris")
print(df.head())

# Dataset Information
print(df.info())

# Datatypes
print(df.dtypes)

# Features
features=[
  'sepal_length',
  'sepal_width',
  'petal_length',
  'petal_width'
]

# Histograms
df.hist(figsize=(10, 10))
plt.show()

# Histograms:
for feat in features:
  sns.histplot(df[feat],bins=20)
  plt.title(f'{feat} Histograms')
  plt.show()

# Boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=df.iloc[:, 1:5])
plt.title("Boxplot of Iris Features")
plt.show()

for feat in features:
  sns.boxplot(df[feat])
  plt.title(f'{feat} Histograms')
  plt.show()

# KDE plot(Kernel Density Estimate)
sns.kdeplot(data=df,x='sepal_length',hue='species',fill=True)
plt.title('KDE plot')
plt.show()

# Scatterplot
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=df)
plt.title('Scatter Plot')
plt.show()
