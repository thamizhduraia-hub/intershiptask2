import pandas as pd

# CSV file-ஐ load செய்க
df = pd.read_csv("/Users/thamizh/Desktop/sales_data-selected-columns.csv")

# முதல் 5 rows-ஐ பார்க்க
print("First 5 Rows:")
print(df.head())

# Dataset தகவல்களை பார்க்க
print("\nDataset Information:")
print(df.info())

# Null values இருக்கிறதா பார்க்க
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows இருக்கிறதா பார்க்க
print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Column names-ஐ clean பண்ண
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nColumn Names:")
print(df.columns)

# Date format மாற்ற
df["sale_date"] = pd.to_datetime(df["sale_date"])

print(df.dtypes)

# Cleaned dataset save
df.to_csv("/Users/thamizh/Desktop/cleaned_sales_data.csv", index=False)

print("Cleaned dataset saved successfully!")