# Task 1: Data Immersion & Wrangling

This data repository is part of a full data immersion and data wrangling process developed while taking part in Task 1 of the 60-Day Data Analytics Internship Program. We are using Python and Pandas for transforming the raw retail sales transactions data to a clean, structured, and analysis-ready dataset for the project.

## Objective

Create a raw sales transactions dataset which can be analyzed with confidence by finding and fixing data quality problems using Python/Pandas and generating an analysis-ready dataset.

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

The data includes retail sales transactions for products, geographies, channels of distribution, customer groups, product campaigns, payment methods, delivery timings, ratings, and returns. It contains realistic DQ problems like duplicate orders, dated format mix-ups, text case inconsistencies, missing values, revenue outliers, and so on.

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

These are all actions performed by the cleaning script:

1. Loads the original transaction data.
2. Finds the profile's missing values & duplicates.
3. Removes duplicates.
4. Cleans up column names and text categories.
5. Converts mixed date formats to date values.
6. Manages invalid quantities, discounts, and price outliers.
7. Fill in missing numbers and data in logical ways.
8. Generates analysis-ready fields such as gross profit, gross margin, month, age group and returned flag.
9. Cleanses the dataset and exports it for working with it in other applications for EDA or dashboarding.


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
This task will provide hands-on experience in applying data wrangling techniques: understanding basic principles behind data profiling; recording the structure 
of a dataset; implementing repeatable data cleaning; and preparing the dataset for subsequent EDA and business intelligence tasks.
