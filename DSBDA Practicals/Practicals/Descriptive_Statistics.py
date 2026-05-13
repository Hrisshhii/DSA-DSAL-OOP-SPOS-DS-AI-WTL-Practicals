import pandas as pd
import numpy as np

# Create Dataset
data = {
    'Name': ['Amit', 'Sonal', 'Raj', 'Priya', 'Karan', 'Neha'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [20, 21, 19, 22, 20, 21],
    'Marks': [85, 90, 78, 92, 70, 88]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Group by Gender
grouped = df.groupby('Gender')['Marks']

print("\nMean")
print(grouped.mean())

print("\nMedian")
print(grouped.median())

print("\nMinimum")
print(grouped.min())

print("\nMaximum")
print(grouped.max())

print("\nStandard Deviation")
print(grouped.std())

# Lists
male_marks = df[df['Gender'] == 'Male']['Marks'].tolist()
female_marks = df[df['Gender'] == 'Female']['Marks'].tolist()

print("\nMale Marks:", male_marks)
print("Female Marks:", female_marks)

# Load Iris Dataset
#iris = pd.read_csv("Iris.csv")
import seaborn as sb
iris=sb.load_dataset("iris")
print("\nIris Dataset")
print(iris.head())

# Group by Species
grouped_species = iris.groupby('Species')

print("\nMean")
print(grouped_species.mean())

print("\nStandard Deviation")
print(grouped_species.std())

print("\nMinimum")
print(grouped_species.min())

print("\nMaximum")
print(grouped_species.max())

print("\nPercentiles")
print(grouped_species.quantile([0.25, 0.5, 0.75]))
