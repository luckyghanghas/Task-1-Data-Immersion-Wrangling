# Data Quality Report

## Dataset Profile
- Raw rows: 256
- Raw columns: 14
- Duplicate rows removed: 6
- Rows removed due to missing required dates: 2
- Cleaned rows: 248
- Cleaned columns: 18

## Issues Found
- Missing values in region, unit_price, and customer_dob.
- Duplicate transaction rows.
- Mixed date formats in order_date and customer_dob.
- Inconsistent category labels such as smart phone, Head Phones, and web.
- Invalid quantity, discount, and outlier price values.

## Cleaning Actions
- Removed duplicate rows.
- Standardized column names and text categories.
- Parsed dates into a consistent ISO-style format.
- Replaced invalid quantity and price values with product-aware or dataset median values.
- Filled unknown regions and missing discount rates.
- Added customer_age, gross_revenue, net_revenue, and order_month for analysis.

## Missing Values Before Cleaning
- customer_dob: 2
- region: 3
- unit_price: 2

## Missing Values After Cleaning
- No missing values remain in the cleaned dataset.
