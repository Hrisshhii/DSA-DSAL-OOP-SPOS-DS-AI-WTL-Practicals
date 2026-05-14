import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic Dataset
df = sns.load_dataset('titanic')

print(df.head())

# Dataset Information
print(df.info())

# Survival Count
sns.countplot(x='survived', data=df)

plt.title("Survival Count")

plt.show()

# Gender vs Survival
sns.countplot(x='sex', hue='survived', data=df)

plt.title("Gender vs Survival")

plt.show()

# Passenger Class vs Survival
sns.countplot(x='pclass', hue='survived', data=df)

plt.title("Passenger Class vs Survival")

plt.show()

# Histogram of Fare
plt.hist(df['fare'], bins=30)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()

# Boxplot
sb.boxplot(df['fare'])
plt.title('Fare Boxplot')
plt.show()

# Scatterplot
sb.scatterplot(x="age",y="fare",hue="survived",data=df)
plt.title("Age vs fare")
plt.show()

# Volinplot
sb.violinplot(x="sex",y="age",hue="survived",data=df)
plt.title("Violin Plot")
plt.show()

# Heatmap
sb.heatmap(df.corr(numeric_only=True),annot=True)
plt.title('Correlation Heatmap')
plt.show()
