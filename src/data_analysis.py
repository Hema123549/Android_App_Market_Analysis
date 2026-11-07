import pandas as pd

# Load datasets
apps = pd.read_csv("dataset/googleplaystore.csv")
reviews = pd.read_csv("dataset/googleplaystore_user_reviews.csv")

# 1. App Dataset Overview
print("=" * 50)
print("GOOGLE PLAY STORE APP DATASET")
print("=" * 50)

print("\nDataset Shape:")
print(apps.shape)

print("\nFirst Five Rows:")
print(apps.head())

print("\nDataset Information:")
apps.info()

print("\nColumn Names:")
print(apps.columns.tolist())

# 2. Missing Values
print("\nMissing Values in App Dataset:")
print(apps.isnull().sum())

# 3. Duplicate Records
print("\nDuplicate App Records:")
print(apps.duplicated().sum())

# 4. Category Distribution
print("\nTop 10 App Categories:")
print(apps["Category"].value_counts().head(10))

# 5. Ratings Overview
print("\nRating Statistics:")
print(apps["Rating"].describe())

# 6. Reviews Dataset Overview
print("\n" + "=" * 50)
print("GOOGLE PLAY STORE USER REVIEWS")
print("=" * 50)

print("\nReviews Dataset Shape:")
print(reviews.shape)

print("\nFirst Five Review Records:")
print(reviews.head())

print("\nReview Dataset Information:")
reviews.info()

print("\nMissing Values in Reviews:")
print(reviews.isnull().sum())

# 7. Sentiment Distribution
print("\nSentiment Distribution:")
print(reviews["Sentiment"].value_counts(dropna=False))

print("\nDATA ANALYSIS COMPLETED SUCCESSFULLY!")