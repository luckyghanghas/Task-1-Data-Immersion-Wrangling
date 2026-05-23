# Task 1: Data Immersion & Wrangling

This repository contains the Task 1 submission for the 60-day Data Analytics internship: acquiring, profiling, cleaning, transforming, and preparing a dataset for analysis.

## Objective

Prepare a raw sales transactions dataset for reliable analysis by identifying data quality issues, cleaning them with Python/Pandas, and producing an analysis-ready dataset.

## Repository Structure

```text
data/
  sales_transactions_raw.csv
  sales_transactions_cleaned.csv
reports/
  data_dictionary.md
  data_quality_report.md
 scripts/
  generate_sample_data.py
  clean_sales_data.py
requirements.txt
```

## Dataset

The dataset represents retail sales transactions across products, regions, sales channels, customer segments, payment modes, and order statuses. It includes intentionally realistic data quality issues such as missing values, duplicate rows, inconsistent categories, mixed date formats, invalid numeric values, and outliers.

## Cleaning Summary

The cleaning script performs these steps:

1. Loads the raw transaction dataset.
2. Profiles missing values and duplicate rows.
3. Removes duplicates.
4. Standardizes column names and text categories.
5. Converts mixed date formats into consistent date values.
6. Handles invalid quantities, discounts, and price outliers.
7. Fills missing values using sensible rules.
8. Creates analysis-ready fields: `customer_age`, `gross_revenue`, `net_revenue`, and `order_month`.
9. Exports the cleaned dataset and data quality report.

## How to Run

```bash
pip install -r requirements.txt
python scripts/generate_sample_data.py
python scripts/clean_sales_data.py
```

## Deliverables

- Data dictionary: `reports/data_dictionary.md`
- Cleaning script: `scripts/clean_sales_data.py`
- Cleaned dataset: `data/sales_transactions_cleaned.csv`
- Data quality report: `reports/data_quality_report.md`
  
## Key Learning

This task demonstrates practical data wrangling skills: profiling raw data, documenting dataset structure, applying reproducible cleaning logic, and preparing a dataset for later EDA and business intelligence work.
