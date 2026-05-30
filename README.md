# Task 1: Data Immersion & Wrangling

This data repository is part of a full data immersion and data wrangling process developed while taking part in Task 1 of the 60-Day Data Analytics Internship Program. We are using Python and Pandas for transforming the raw retail sales transactions data to a clean, structured, and analysis-ready dataset for the project.

## Objective

Create a raw sales transactions dataset which can be analyzed with confidence by finding and fixing data quality problems using Python/Pandas and generating an analysis-ready dataset.

## Repository Structure

```text
data/
  sales_transactions_raw.csv
  cleaned_analytics_dataset.csv
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
| Duplicate orders | Removed duplicate `transaction_id` records. |
| Mixed date formats | Converted all order dates into a consistent date format. |
| Inconsistent text casing | Standardized category and channel values. |
| Missing payment method | Replaced blanks with `Unknown`. |
| Missing quantities & prices | Filled using median values. |
| Revenue outliers | Capped extreme values at 95th percentile. |

## Cleaning Summary

These are all actions performed by the cleaning script:

1. Loads the original transaction data.
2. Finds the profile's missing values & duplicates.
3. Removes duplicates by `transaction_id`.
4. Cleans up column names and text categories.
5. Converts mixed date formats to date values.
6. Manages invalid quantities, discounts, and price outliers.
7. Fill in missing numbers and data in logical ways.
8. Generates analysis-ready fields such as revenue and month.
9. **Interactive save location selection** - Choose where to save cleaned and generate data:
   - 📁 Project Folder (default)
   - 🖥️ Desktop
   - ⬇️ Downloads
   - 🔧 Custom Path
10. Cleanses the dataset and exports it to selected location for working with it in other applications for EDA or dashboarding.

## How to Run

```bash
pip install -r requirements.txt
python scripts/generate_sample_data.py
python scripts/clean_sales_data.py  # Follow the interactive menu to select save location
```

## Deliverables

- Data dictionary: `reports/data_dictionary.md`
- Cleaning script: `scripts/clean_sales_data.py` (with interactive save location)
- Sample data generator: `scripts/generate_sample_data.py` (saved to user-selected location)
- Raw dataset: `data/sales_transactions_raw.csv`
- Cleaned dataset: `cleaned_analytics_dataset.csv` (saved to user-selected location)
- Data quality report: `reports/data_quality_report.md`

## Key Features

### 🎯 Interactive Save Location
When you run `clean_sales_data.py`,'generate_sample_data.py', you'll be prompted to choose where to save the cleaned dataset:
```
════════════════════════════════════════════════════════════
📁 WHERE WOULD YOU LIKE TO SAVE THE CLEANED FILE?
════════════════════════════════════════════════════════════
1️  Project Folder (data/)
2️  Desktop
3️  Downloads
4️  Custom Path
════════════════════════════════════════════════════════════
```

### 🔄 Automatic Directory Creation
Directories are automatically created if they don't exist, making it seamless to save files anywhere.

### ✅ Enhanced Error Handling
The script includes robust error handling with user-friendly messages for any file I/O issues.

### 📊 Detailed Summary Output
After cleaning, get a comprehensive summary showing:
- ✅ Full absolute path to saved file
- 📁 Save location used
- 📊 Final dataset dimensions

## Key Learning
This task will provide hands-on experience in applying data wrangling techniques: understanding basic principles behind data profiling; recording the structure of a dataset; implementing repeatable data cleaning; and preparing the dataset for subsequent EDA and business intelligence tasks.
