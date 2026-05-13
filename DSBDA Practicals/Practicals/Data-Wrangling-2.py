import pandas as pd
import numpy as np

# Create Dataset
data = {
    'Name': ['Amit', 'Sonal', 'Raj', 'Priya', 'Karan', 'Neha'],
    'Math': [85, 90, np.nan, 95, 40, 500],
    'Science': [78, 88, 84, np.nan, 35, 92],
    'English': [80, 85, 82, 88, 30, 95],
    'Attendance': [90, 95, 85, 80, np.nan, 100]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Check Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Fill Missing Values
df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())

# Check Inconsistency
print("\nInconsistent Values")
print(df[df['Math'] > 100])

# Replace inconsistent values
median_value = df['Math'].median()
df.loc[df['Math'] > 100, 'Math'] = median_value

# Detect Outliers using IQR
Q1 = df['Math'].quantile(0.25)
Q3 = df['Math'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nLower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Remove Outliers
df = df[(df['Math'] >= lower_limit) & (df['Math'] <= upper_limit)]

# Normalize Attendance
df['Attendance'] = (df['Attendance'] - df['Attendance'].min()) / \
                   (df['Attendance'].max() - df['Attendance'].min())

print("\nProcessed Dataset")
print(df)
