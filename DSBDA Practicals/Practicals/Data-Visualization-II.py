import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic Dataset
df = sns.load_dataset('titanic')
print(df.head())

# Check Missing Values
print(df.isnull().sum())

# Remove Missing Age Values
df = df.dropna(subset=['age'])

# Boxplot
sns.boxplot(x='sex', y='age', hue='survived', data=df)
plt.title("Age Distribution by Gender and Survival")
plt.show()

# Swarmplot
sns.swarmplot(x='sex',y='age',hue='survived',data=df)
plt.title('Swarm Plot')
plt.show()

# Barplot
sns.barplot(x='sex',y='age',hue='survived',data=df)
plt.title("Bar Plot")
plt.show()

# Stripplot
sns.stripplot(x="sex",y="age",data=df)
plt.title("Strip Plot")
plt.show()
