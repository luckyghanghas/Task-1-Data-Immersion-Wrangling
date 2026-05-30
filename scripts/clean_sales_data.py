from datetime import datetime

import pandas as pd

raw_path = "data/sales_transactions_raw.csv"
cleaned_path = "data/sales_transactions_cleaned.csv"

df = pd.read_csv(raw_path)
df = df.drop_duplicates(subset=["transaction_id"], keep="first")

def parse_order_date(value):
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return pd.NaT

df["date"] = df["date"].apply(parse_order_date)
df = df.dropna(subset=["date"])

df["product_category"] = df["product_category"].astype(str).str.strip().str.title()
df["sales_channel"] = df["sales_channel"].astype(str).str.strip().str.title()
df["payment_mode"] = df["payment_mode"].fillna("Unknown").replace("", "Unknown")

numeric_cols = ["quantity", "unit_price", "discount_percent"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing/invalid data
df["quantity"] = df["quantity"].fillna(df["quantity"].median()).astype(int)
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].median())
df["discount_percent"] = df["discount_percent"].fillna(0)

# Calculate revenue
df["revenue"] = (df["unit_price"] * df["quantity"] * (1 - df["discount_percent"] / 100)).round(2)

# Standardize categorical columns
df["customer_segment"] = df["customer_segment"].astype(str).str.strip().str.title()
df["order_status"] = df["order_status"].astype(str).str.strip().str.title()

# Create derived columns
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M").astype(str)

df.to_csv(cleaned_path, index=False)
print(f"Cleaned rows: {len(df):,}")
