from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "sales_transactions_raw.csv"
CLEAN_PATH = ROOT / "data" / "sales_transactions_cleaned.csv"
PROFILE_PATH = ROOT / "reports" / "data_quality_report.md"


def parse_mixed_dates(series: pd.Series) -> pd.Series:
    parsed = pd.to_datetime(series, errors="coerce", dayfirst=False, format="mixed")
    missing = parsed.isna()
    if missing.any():
        parsed.loc[missing] = pd.to_datetime(series.loc[missing], errors="coerce", dayfirst=True, format="mixed")
    return parsed


def main() -> None:
    df = pd.read_csv(RAW_PATH)
    original_rows = len(df)
    original_columns = len(df.columns)

    duplicate_rows = int(df.duplicated().sum())
    missing_before = df.isna().sum().to_dict()

    df = df.drop_duplicates().copy()

    df.columns = [col.strip().lower() for col in df.columns]
    text_columns = [
        "customer_name",
        "customer_segment",
        "region",
        "sales_channel",
        "product",
        "payment_mode",
        "order_status",
    ]
    for col in text_columns:
        df[col] = df[col].astype("string").str.strip().str.title()

    df["product"] = df["product"].replace(
        {
            "Smart Phone": "Smartphone",
            "Head Phones": "Headphones",
        }
    )
    df["sales_channel"] = df["sales_channel"].replace({"Web": "Online"})

    df["order_date"] = parse_mixed_dates(df["order_date"])
    df["customer_dob"] = parse_mixed_dates(df["customer_dob"])
    rows_without_required_dates = int(df[["order_date", "customer_dob"]].isna().any(axis=1).sum())
    df = df.dropna(subset=["order_date", "customer_dob"]).copy()

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["discount_rate"] = pd.to_numeric(df["discount_rate"], errors="coerce")

    df.loc[df["quantity"] <= 0, "quantity"] = np.nan
    df.loc[(df["discount_rate"] < 0) | (df["discount_rate"] > 0.8), "discount_rate"] = np.nan

    price_cap = df["unit_price"].quantile(0.99)
    df.loc[df["unit_price"] > price_cap, "unit_price"] = np.nan

    df["region"] = df["region"].fillna("Unknown")
    df["discount_rate"] = df["discount_rate"].fillna(0)
    df["quantity"] = df["quantity"].fillna(df["quantity"].median()).astype(int)
    df["unit_price"] = df.groupby("product")["unit_price"].transform(lambda s: s.fillna(s.median()))

    reference_date = pd.Timestamp("2026-01-01")
    df["customer_age"] = ((reference_date - df["customer_dob"]).dt.days / 365.25).round()
    df["gross_revenue"] = (df["quantity"] * df["unit_price"]).round(2)
    df["net_revenue"] = (df["gross_revenue"] * (1 - df["discount_rate"])).round(2)
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    final_columns = [
        "order_id",
        "order_date",
        "order_month",
        "customer_id",
        "customer_name",
        "customer_dob",
        "customer_age",
        "customer_segment",
        "region",
        "sales_channel",
        "product",
        "quantity",
        "unit_price",
        "discount_rate",
        "gross_revenue",
        "net_revenue",
        "payment_mode",
        "order_status",
    ]
    df = df[final_columns].sort_values(["order_date", "order_id"])

    CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)

    missing_after = df.isna().sum().to_dict()
    report = [
        "# Data Quality Report",
        "",
        "## Dataset Profile",
        f"- Raw rows: {original_rows}",
        f"- Raw columns: {original_columns}",
        f"- Duplicate rows removed: {duplicate_rows}",
        f"- Rows removed due to missing required dates: {rows_without_required_dates}",
        f"- Cleaned rows: {len(df)}",
        f"- Cleaned columns: {len(df.columns)}",
        "",
        "## Issues Found",
        "- Missing values in region, unit_price, and customer_dob.",
        "- Duplicate transaction rows.",
        "- Mixed date formats in order_date and customer_dob.",
        "- Inconsistent category labels such as smart phone, Head Phones, and web.",
        "- Invalid quantity, discount, and outlier price values.",
        "",
        "## Cleaning Actions",
        "- Removed duplicate rows.",
        "- Standardized column names and text categories.",
        "- Parsed dates into a consistent ISO-style format.",
        "- Replaced invalid quantity and price values with product-aware or dataset median values.",
        "- Filled unknown regions and missing discount rates.",
        "- Added customer_age, gross_revenue, net_revenue, and order_month for analysis.",
        "",
        "## Missing Values Before Cleaning",
        *[f"- {key}: {value}" for key, value in missing_before.items() if value],
        "",
        "## Missing Values After Cleaning",
        *[f"- {key}: {value}" for key, value in missing_after.items() if value],
    ]
    if all(value == 0 for value in missing_after.values()):
        report.append("- No missing values remain in the cleaned dataset.")

    PROFILE_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Wrote {CLEAN_PATH}")
    print(f"Wrote {PROFILE_PATH}")


if __name__ == "__main__":
    main()
