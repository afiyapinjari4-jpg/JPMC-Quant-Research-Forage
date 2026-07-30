import pandas as pd

# Load dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Keep only required columns
df = df[['fico_score', 'default']]

# Number of buckets
num_buckets = 10

# Create equal-frequency buckets
df['rating'] = pd.qcut(
    df['fico_score'],
    q=num_buckets,
    labels=False,
    duplicates='drop'
)

# Lower rating = Better credit score
df['rating'] = df['rating'].max() - df['rating'] + 1

# Rating summary
summary = (
    df.groupby('rating')
      .agg(
          Min_FICO=('fico_score', 'min'),
          Max_FICO=('fico_score', 'max'),
          Customers=('fico_score', 'count'),
          Defaults=('default', 'sum'),
          PD=('default', 'mean')
      )
      .sort_index()
)

print("\n===== FICO Rating Map =====")
print(summary)

summary.to_csv("fico_rating_map.csv")
df.to_csv("fico_bucketed_data.csv", index=False)

print("\nFiles saved successfully!")