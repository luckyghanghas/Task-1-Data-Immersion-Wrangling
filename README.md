# Task 1: Data Immersion & Wrangling

This data repository is part of a full data immersion and data wrangling process developed while taking part in Task 1 of the 60-Day Data Analytics Internship 
Program. For the project, we are using Python and Pandas to manipulate the raw sales transactions data and to update it into a structured, cleaned and analysed 
data for analysis.

## Objective

Build a raw dataset of sales transactions that can be analyzed with confidence by reporting and rectifying data quality issues with Python and Pandas and transform the data into an analytics-ready dataset.

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

Retail sales transaction data covers products sold, geographies served, distribution channels, customer groups, product campaigns sold, payment methods, delivery time, and ratings as well as returns. Includes realistic problem of DQ (Data Quality), such as duplicate orders, wrong dated format, text case, missing value, revenue outlier, etc.

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

All those are operations carried out by the cleaning script:

Loads the original data set from transactions.
2. Finds the profile's missing values & duplicates.
3. Dedupes based on 'transaction_id'.
5. Makes corrections to cleaned-up data.
6. Performs string to date conversions.
6. Deals with quantities and discounts that are not valid and with price outliers.
7. Complete the number and information to make sense out of it.
8. Creates analysis-ready fields (revenue, month, etc.).
9. Interactive Save Route Selection - Save destination of cleaned and generated data:
   - 📁 Project Folder (default)
   - 🖥️ Desktop
   - ⬇️ Downloads
   - 🔧 Custom Path
10. Washes up the data set and writes it to the selected location to be used in other applications for EDA or dashboarding.

## How to Run

```bash
pip install -r requirements.txt
python scripts/generate_sample_data.py  # Follow the interactive menu to select save location
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
When you run `clean_sales_data.py`,`generate_sample_data.py`, you'll be prompted to choose where to save the cleaned and generate dataset:
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
After cleaning and generate, get a comprehensive summary showing:
- ✅ Full absolute path to saved file
- 📁 Save location used
- 📊 Final dataset dimensions

## Key Learning
This task will give practical experience in implementing data wrangling techniques: learning basic principles of data profiling; capturing the structure and quality of the data profile; and implementing the data profile by applying data wrangling techniques. 
Defining what constitutes a good amount and the application of repeatable data cleansing; and the preparation of the data for the next step in EDA and business intelligence.
