import pandas as pd
import os


# Read the raw JSON file
df = pd.read_json("data/raw/repositories.json")


# Select only the important columns
df = df[
    [
        "name",
        "full_name",
        "stargazers_count",
        "forks_count",
        "language",
        "open_issues_count",
        "created_at"
    ]
]


# Rename columns to simpler names
df = df.rename(
    columns={
        "stargazers_count": "stars",
        "forks_count": "forks",
        "open_issues_count": "open_issues"
    }
)


# Remove duplicate repositories
df = df.drop_duplicates()


# Replace missing programming languages
df["language"] = df["language"].fillna("Unknown")


# Convert creation date into datetime format
df["created_at"] = pd.to_datetime(df["created_at"])


# Check missing values
print("Missing values:")
print(df.isnull().sum())


# Create processed folder if it does not exist
os.makedirs("data/processed", exist_ok=True)


# Save cleaned data as a Parquet file
df.to_parquet(
    "data/processed/repositories.parquet",
    index=False
)


print("\nData transformed successfully!")
print("Total repositories:", len(df))

print("\nFirst 5 rows:")
print(df.head())