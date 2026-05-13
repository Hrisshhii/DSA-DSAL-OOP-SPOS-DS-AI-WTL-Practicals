import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print(df.head())

# Dimensions of dataset
print(df.shape)

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Statistical summary
print(df.describe())

# Datatypes
print(df.dtypes)

# Fill missing Age values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Convert datatype
df['Survived'] = df['Survived'].astype('category')

# Normalize Age column
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

# Convert categorical to numerical
df['Sex'] = df['Sex'].map({'male':0, 'female':1})

# Display updated dataset
print(df.head())
