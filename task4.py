import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("bank.csv")

# Dataset information
print("Dataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_bank.csv", index=False)

print("\nData cleaned successfully!")
print("Cleaned dataset saved as cleaned_bank.csv")
# Job Distribution
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='job', order=df['job'].value_counts().index)
plt.xticks(rotation=45)
plt.title("Job Distribution")
plt.tight_layout()
plt.savefig("job_distribution.png")
plt.show()

# Deposit Pie Chart
plt.figure(figsize=(6,6))
df['deposit'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Deposit Distribution")
plt.savefig("deposit_distribution.png")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['age'], bins=20)
plt.title("Age Distribution")
plt.savefig("age_distribution.png")
plt.show()