import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ==========================================
# SETUP
# ==========================================

os.makedirs("outputs", exist_ok=True)

sns.set_style("whitegrid")

apps = pd.read_csv("outputs/cleaned_apps.csv")
reviews = pd.read_csv("outputs/cleaned_reviews.csv")

print("APPS DATASET SHAPE:", apps.shape)
print("REVIEWS DATASET SHAPE:", reviews.shape)

# ==========================================
# 1. TOP APP CATEGORIES
# ==========================================

category_counts = apps["Category"].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=category_counts.values, y=category_counts.index)
plt.title("Top 10 App Categories")
plt.xlabel("Number of Apps")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("outputs/top_app_categories.png")
plt.close()

# ==========================================
# 2. RATING DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))
sns.histplot(apps["Rating"], bins=20, kde=True)
plt.title("Distribution of App Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.savefig("outputs/rating_distribution.png")
plt.close()

# ==========================================
# 3. AVERAGE RATING BY CATEGORY
# ==========================================

category_ratings = (
    apps.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
sns.barplot(x=category_ratings.values, y=category_ratings.index)
plt.title("Top 10 Categories by Average Rating")
plt.xlabel("Average Rating")
plt.ylabel("Category")
plt.xlim(0, 5)
plt.tight_layout()
plt.savefig("outputs/category_average_ratings.png")
plt.close()

# ==========================================
# 4. TOP INSTALLED APPS
# ==========================================

top_apps = apps.sort_values(
    by="Installs", ascending=False
).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_apps, x="Installs", y="App")
plt.title("Top 10 Most Installed Apps")
plt.xlabel("Number of Installs")
plt.ylabel("App")
plt.tight_layout()
plt.savefig("outputs/top_installed_apps.png")
plt.close()

# ==========================================
# 5. FREE VS PAID APPS
# ==========================================

type_counts = apps["Type"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    type_counts.values,
    labels=type_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Free vs Paid Apps")
plt.tight_layout()
plt.savefig("outputs/free_vs_paid.png")
plt.close()

# ==========================================
# 6. PAID APP PRICE DISTRIBUTION
# ==========================================

paid_apps = apps[apps["Price"] > 0]

plt.figure(figsize=(10, 6))
sns.histplot(paid_apps["Price"], bins=30, kde=True)
plt.title("Price Distribution of Paid Apps")
plt.xlabel("Price ($)")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.savefig("outputs/price_distribution.png")
plt.close()

# ==========================================
# 7. APP SIZE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))
sns.histplot(apps["Size"], bins=30, kde=True)
plt.title("Distribution of App Sizes")
plt.xlabel("Size (MB)")
plt.ylabel("Number of Apps")
plt.tight_layout()
plt.savefig("outputs/app_size_distribution.png")
plt.close()

# ==========================================
# 8. CONTENT RATING
# ==========================================

content_counts = apps["Content Rating"].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=content_counts.values, y=content_counts.index)
plt.title("Apps by Content Rating")
plt.xlabel("Number of Apps")
plt.ylabel("Content Rating")
plt.tight_layout()
plt.savefig("outputs/content_rating_distribution.png")
plt.close()

# ==========================================
# 9. REVIEW SENTIMENT DISTRIBUTION
# ==========================================

sentiment_counts = reviews["Sentiment"].value_counts()

plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values)
plt.title("User Review Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("outputs/sentiment_distribution.png")
plt.close()

# ==========================================
# 10. SENTIMENT POLARITY
# ==========================================

plt.figure(figsize=(10, 6))
sns.histplot(reviews["Sentiment_Polarity"], bins=30, kde=True)
plt.title("Distribution of Sentiment Polarity")
plt.xlabel("Sentiment Polarity")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("outputs/sentiment_polarity.png")
plt.close()

# ==========================================
# 11. REVIEW WORD CLOUD
# ==========================================

review_text = " ".join(
    reviews["Translated_Review"].dropna().astype(str)
)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white",
    max_words=150
).generate(review_text)

plt.figure(figsize=(14, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in User Reviews")
plt.tight_layout()
plt.savefig("outputs/review_wordcloud.png")
plt.close()

# ==========================================
# 12. PRINT ANALYSIS RESULTS
# ==========================================

print("\n========== EDA INSIGHTS ==========")

print("\nTOP 10 APP CATEGORIES:")
print(category_counts)

print("\nTOP 10 MOST INSTALLED APPS:")
print(top_apps[["App", "Installs", "Rating"]])

print("\nTOP 10 CATEGORIES BY AVERAGE RATING:")
print(category_ratings)

print("\nFREE VS PAID APP COUNTS:")
print(type_counts)

print("\nAVERAGE APP RATING:")
print(round(apps["Rating"].mean(), 2))

print("\nAVERAGE APP SIZE (MB):")
print(round(apps["Size"].mean(), 2))

print("\nAVERAGE PAID APP PRICE:")
print(round(paid_apps["Price"].mean(), 2))

print("\nUSER SENTIMENT COUNTS:")
print(sentiment_counts)

print("\nAVERAGE SENTIMENT POLARITY:")
print(round(reviews["Sentiment_Polarity"].mean(), 3))

print("\nEDA COMPLETED SUCCESSFULLY!")