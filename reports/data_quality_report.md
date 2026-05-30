# Task 1 - Data Immersion & Wrangling

## Objective
Produce a sales transaction data set for analysis by cleaning up the raw data, identifying quality issues, and fixing them, creating a dataset for analysis.

## Dataset Overview
- Raw rows received: 1,260
- Final cleaned rows: 1,250
- Date range after cleaning: 2025-01-01 to 2026-03-26
- Business grain: one row per order

## Data Quality Issues Found
| Issue | What I found | Treatment |
|---|---:|---|
| Duplicate orders | 10 rows | Removed by keeping the first record for each `transaction_id`. |
| Mixed date formats | Multiple formats such as yyyy-mm-dd, dd/mm/yyyy, and mm-dd-yyyy | Parsed and standardized to ISO date format. |
| Inconsistent text casing | Category and channel values appeared in mixed cases | Trimmed whitespace and converted to title case. |
| Missing payment method | 4 rows | Replaced blanks with `Unknown` to preserve the transaction. |
| Missing quantities and prices | 3-5% of rows | Filled with median values to avoid losing useful sales records. |
| Revenue outliers | 2% of records | Capped extreme values at 95th percentile to reduce impact of outliers. |

## New Fields Created
- `revenue`: calculated from unit_price × quantity × (1 - discount_percent/100).
- `month`: reporting month in YYYY-MM format for time-based analysis.
- Additional derived fields ready for EDA and dashboarding.

## Data Cleaning Pipeline Features

### 1. **Flexible Output Location**
The cleaning script now includes an interactive menu allowing users to save the cleaned and generate dataset to:
- ✅ **Project Folder** (default): `data/cleaned_analytics_dataset.csv`
- 🖥️ **Desktop** 
- ⬇️ **Downloads** 
- 🔧 **Custom Path** 

### 2. **Automated Directory Creation**
The script automatically creates parent directories if they don't exist, ensuring seamless file saving.

### 3. **Enhanced Error Handling**
- Try-except blocks to catch and report file I/O errors
- User-friendly error messages with troubleshooting suggestions

### 4. **Improved Output Summary**
After successful cleaning and generate, the script displays:
- ✅ Absolute file path (full path to saved file)
- 📁 Save location name (Project Folder, Desktop, Downloads, or Custom)
- 📊 Final dataset dimensions (rows × columns)

## Final Output
The cleaned file can be saved to a user-selected location:
- **Default**: `data/cleaned_analytics_dataset.csv`
- **Alternative locations**: Desktop, Downloads, or custom path of choice

## How to Run

```bash
# 1. Generate sample data with quality issues
python scripts/generate_sample_data.py

# 2. Clean the data (interactive save location prompt will appear)
python scripts/clean_sales_data.py
```

## Processing Steps

1. ✅ Load raw transactions data
2. ✅ Remove duplicate records by `transaction_id`
3. ✅ Parse and standardize mixed date formats
4. ✅ Standardize categorical columns (trim, title case)
5. ✅ Convert numeric columns (handle coercion errors)
6. ✅ Impute missing values using median strategy
7. ✅ Calculate revenue from base fields
8. ✅ Handle outliers (cap at 95th percentile)
9. ✅ Create derived columns (`month`)
10. ✅ **Interactive save location selection** ← NEW FEATURE
11. ✅ Export to selected location with full path confirmation
