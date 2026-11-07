import pandas as pd
import os

# Load datasets
apps = pd.read_csv("dataset/googleplaystore.csv")
reviews = pd.read_csv("dataset/googleplaystore_user_reviews.csv")

print("INITIAL APP DATASET:", apps.shape)
print("INITIAL REVIEWS DATASET:", reviews.shape)

# ==================================
# 1. CLEAN APP DATASET
# ==================================

# Remove duplicate records
apps = apps.drop_duplicates()

# Convert Reviews column to numeric
apps["Reviews"] = pd.to_numeric(
    apps["Reviews"], errors="coerce"
)

# Clean Installs column
apps["Installs"] = (
    apps["Installs"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
)

apps["Installs"] = pd.to_numeric(
    apps["Installs"], errors="coerce"
)

# Clean Price column
apps["Price"] = (
    apps["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
)

apps["Price"] = pd.to_numeric(
    apps["Price"], errors="coerce"
)

# Clean Size column and convert everything to MB
def convert_size(value):

    value = str(value)

    if value == "nan" or value == "Varies with device":
        return None

    if value.endswith("M"):
        return float(value.replace("M", ""))

    elif value.endswith("k"):
        return float(value.replace("k", "")) / 1024

    return None


apps["Size"] = apps["Size"].apply(convert_size)

# Remove invalid ratings
apps.loc[
    (apps["Rating"] < 1) | (apps["Rating"] > 5),
    "Rating"
] = None

# Fill missing values
apps["Rating"] = apps["Rating"].fillna(
    apps["Rating"].median()
)

apps["Size"] = apps["Size"].fillna(
    apps["Size"].median()
)

apps["Type"] = apps["Type"].fillna(
    apps["Type"].mode()[0]
)

apps["Content Rating"] = apps["Content Rating"].fillna(
    apps["Content Rating"].mode()[0]
)

apps["Current Ver"] = apps["Current Ver"].fillna(
    apps["Current Ver"].mode()[0]
)

apps["Android Ver"] = apps["Android Ver"].fillna(
    apps["Android Ver"].mode()[0]
)

# Remove rows with missing essential values
apps = apps.dropna(
    subset=["App", "Category", "Reviews", "Installs", "Price"]
)

# ==================================
# 2. CLEAN REVIEWS DATASET
# ==================================

# Remove duplicate review records
reviews = reviews.drop_duplicates()

# Remove rows without review text
reviews = reviews.dropna(
    subset=["Translated_Review"]
)

# Remove rows with invalid sentiment
reviews = reviews.dropna(
    subset=["Sentiment"]
)

# ==================================
# 3. SAVE CLEANED DATASETS
# ==================================

os.makedirs("outputs", exist_ok=True)

apps.to_csv(
    "outputs/cleaned_apps.csv",
    index=False
)

reviews.to_csv(
    "outputs/cleaned_reviews.csv",
    index=False
)

# ==================================
# 4. DISPLAY RESULTS
# ==================================

print("\nCLEANED APP DATASET:", apps.shape)
print("CLEANED REVIEWS DATASET:", reviews.shape)

print("\nAPP MISSING VALUES:")
print(apps.isnull().sum())

print("\nREVIEW MISSING VALUES:")
print(reviews.isnull().sum())

print("\nAPP SIZE UNIT: MB")

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")