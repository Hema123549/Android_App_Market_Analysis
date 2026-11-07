# Android App Market Analysis

## Project Overview

This project analyzes Google Play Store application data to understand app market trends, user preferences, application ratings, installation patterns, pricing, and user review sentiment.

The analysis uses Python for data cleaning, exploratory data analysis (EDA), and sentiment analysis.

## Dataset

The project uses two datasets:

1. `googleplaystore.csv` – Google Play Store application information.
2. `googleplaystore_user_reviews.csv` – User reviews and sentiment information.

The datasets contain information about app categories, ratings, reviews, installations, prices, sizes, content ratings, and user sentiment.

**Note:** These datasets represent an older snapshot of Google Play Store data, not current live statistics.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- TextBlob
- WordCloud
- Scikit-learn

## Project Structure

```text
Android_App_Market_Analysis/
│
├── dataset/
│   ├── googleplaystore.csv
│   └── googleplaystore_user_reviews.csv
│
├── src/
│   ├── data_analysis.py
│   ├── data_cleaning.py
│   └── eda.py
│
├── outputs/
│   ├── cleaned_apps.csv
│   ├── cleaned_reviews.csv
│   └── visualization files
│
├── README.md
└── requirements.txt
```

## Data Cleaning

The following preprocessing operations were performed:

- Removed duplicate app records.
- Converted reviews into numeric values.
- Cleaned installation counts by removing commas and plus signs.
- Converted app prices into numeric values.
- Standardized app sizes into MB.
- Removed invalid ratings outside the 1–5 range.
- Handled missing values using appropriate imputation methods.
- Removed incomplete user reviews.
- Removed duplicate review records.

### Cleaned Dataset

| Dataset | Original Records | Cleaned Records |
|---|---:|---:|
| Apps | 10,841 | 10,357 |
| Reviews | 64,295 | 29,692 |

No missing values remained in the cleaned datasets.

## Exploratory Data Analysis

The following analyses were performed:

1. Top 10 app categories.
2. Distribution of app ratings.
3. Average ratings by category.
4. Most installed applications.
5. Free versus paid applications.
6. Paid application price distribution.
7. App size distribution.
8. Content rating distribution.
9. User review sentiment distribution.
10. Sentiment polarity distribution.
11. Word cloud of user reviews.

## Key Findings

### 1. App Categories
- FAMILY is the largest category with 1,943 apps.
- GAME is the second-largest category with 1,121 apps.
- TOOLS contains 843 apps.

### 2. Application Ratings
- The overall average app rating is approximately 4.2.
- EVENTS has the highest average rating at approximately 4.40.
- EDUCATION follows with approximately 4.38.

### 3. Installation Trends
Several popular applications, including Google Drive, Facebook, Instagram, and Subway Surfers, have approximately one billion installs in this dataset.

### 4. Free vs Paid Apps
- Free apps: 9,592.
- Paid apps: 765.
- Approximately 92.6% of applications are free.

### 5. Pricing
The average price of paid applications is approximately $13.96.

### 6. Application Size
The average application size is approximately 20.07 MB.

### 7. User Sentiment
- Positive reviews: 19,015.
- Negative reviews: 6,321.
- Neutral reviews: 4,356.
- Average sentiment polarity: 0.189.

Positive reviews dominate the dataset, indicating an overall positive user sentiment.

## Conclusion

The analysis reveals that the Google Play Store dataset is dominated by free applications, with FAMILY and GAME being major app categories.

Applications generally receive positive ratings, and popular apps demonstrate substantial installation counts.

Sentiment analysis also indicates that positive user reviews outnumber negative and neutral reviews.

These findings can help developers understand application market trends, user preferences, and opportunities for improving app quality and user satisfaction.

## Author

Oasis Infobyte Data Science Internship Project.