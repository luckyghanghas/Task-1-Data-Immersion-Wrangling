from datetime import datetime
import pandas as pd
import numpy as np

# File paths
transactions_raw_path = "data/sales_transactions_raw.csv"
cleaned_output_path = "data/cleaned_analytics_dataset.csv"

print("🚀 STARTING DATA WRANGLING PIPELINE...\n")

# ========== LOAD DATA ==========
print("📖 Reading raw files into memory...\n")
transactions_df = pd.read_csv(transactions_raw_path)

# ========== CLEAN TRANSACTIONS TABLE ==========
print("🧼 CLEANING TRANSACTIONS TABLE...")

# Remove duplicates by transaction_id
initial_rows = len(transactions_df)
transactions_df = transactions_df.drop_duplicates(subset=["transaction_id"], keep="first")
duplicates_removed = initial_rows - len(transactions_df)

# Parse dates - handle multiple formats
def parse_order_date(value):
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return pd.NaT

transactions_df["date"] = transactions_df["date"].apply(parse_order_date)
transactions_df = transactions_df.dropna(subset=["date"])
print(f"   -> Unified layout anomalies into YYYY-MM-DD format.")

# Standardize categorical columns
transactions_df["product_category"] = transactions_df["product_category"].astype(str).str.strip().str.title()
transactions_df["sales_channel"] = transactions_df["sales_channel"].astype(str).str.strip().str.title()
transactions_df["payment_mode"] = transactions_df["payment_mode"].fillna("Unknown").replace("", "Unknown")
transactions_df["customer_segment"] = transactions_df["customer_segment"].astype(str).str.strip().str.title()
transactions_df["order_status"] = transactions_df["order_status"].astype(str).str.strip().str.title()

# Convert numeric columns
numeric_cols = ["quantity", "unit_price", "discount_percent"]
for col in numeric_cols:
    if col in transactions_df.columns:
        transactions_df[col] = pd.to_numeric(transactions_df[col], errors="coerce")

# Impute missing values with median
median_unit_price = transactions_df["unit_price"].median()
transactions_df["quantity"] = transactions_df["quantity"].fillna(transactions_df["quantity"].median()).astype(int)
transactions_df["unit_price"] = transactions_df["unit_price"].fillna(median_unit_price)
transactions_df["discount_percent"] = transactions_df["discount_percent"].fillna(0)
print(f"   -> Replaced missing spend metrics with baseline median: ${median_unit_price:.2f}")

# Calculate revenue
transactions_df["revenue"] = (
    transactions_df["unit_price"] * 
    transactions_df["quantity"] * 
    (1 - transactions_df["discount_percent"] / 100)
).round(2)

# Handle outliers - cap extreme revenue values at 95th percentile
revenue_95th_percentile = transactions_df["revenue"].quantile(0.95)
outliers_count = (transactions_df["revenue"] > revenue_95th_percentile).sum()
transactions_df["revenue"] = transactions_df["revenue"].clip(upper=revenue_95th_percentile)
print(f"   -> Isolated and capped {outliers_count} extreme revenue outliers at: ${revenue_95th_percentile:.2f}")

# Create derived columns
transactions_df["month"] = pd.to_datetime(transactions_df["date"]).dt.to_period("M").astype(str)

print()

# ========== EXPORT DATA ==========
print("💾 Exporting production files...")

transactions_df.to_csv(cleaned_output_path, index=False)

# ========== FINAL SUMMARY ==========
final_rows = len(transactions_df)
final_cols = len(transactions_df.columns)

print()
print("🎉 SUCCESS: Data Wrangling pipeline finished successfully!")
print(f"📍 Final Output Created: {cleaned_output_path}")
print(f"📊 Final Dimensions Matrix: {final_rows:,} rows x {final_cols} columns")
print()
