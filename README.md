# Task 1: Data Immersion & Wrangling

This repository presents a complete data immersion and wrangling workflow developed as part of Task 1 of the 60-Day Data Analytics Internship Program. The project transforms raw retail sales transaction data into a clean, structured, and analysis-ready dataset using Python and Pandas.

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

The dataset represents retail sales transactions across products, regions, sales channels, customer segments, campaigns, payment methods, delivery timelines, ratings, and returns. It includes realistic data quality issues such as duplicate orders, mixed date formats, inconsistent text casing, missing values, and revenue outliers.

## Data Quality Issues Handled

| Issue | Action Taken |
|---|---|
| Duplicate orders | Removed duplicate `order_id` records. |
| Mixed date formats | Converted all order dates into a consistent date format. |
| Inconsistent text casing | Standardized region and channel values. |
| Missing payment method | Replaced blanks with `Unknown`. |
| Missing customer age | Filled using the median customer age. |
| Revenue outliers | Corrected unit price scale errors and recalculated revenue. |

## Cleaning Summary

The cleaning script performs these steps:

1. Loads the raw transaction dataset.
2. Profiles missing values and duplicate rows.
3. Removes duplicates.
4. Standardizes column names and text categories.
5. Converts mixed date formats into consistent date values.
6. Handles invalid quantities, discounts, and price outliers.
7. Fills missing values using sensible rules.
8. Creates analysis-ready fields: `gross_profit`, `gross_margin`, `month`, `age_group`, and `returned_flag`.
9. Exports the cleaned dataset for later EDA and dashboarding.

## How to Run

```bash
pip install -r requirements.txt
python scripts/generate_sample_data.py
python scripts/clean_sales_data.py
```

## Deliverables

- Data dictionary: `reports/data_dictionary.md`
- Cleaning script: `scripts/clean_sales_data.py`
- Raw dataset: `data/sales_transactions_raw.csv`
- Cleaned dataset: `data/sales_transactions_cleaned.csv`
- Data quality report: `reports/data_quality_report.md`
  
## Key Learning

This task demonstrates practical data wrangling skills: profiling raw data, documenting dataset structure, applying reproducible cleaning logic, and preparing a dataset for later EDA and business intelligence work.
