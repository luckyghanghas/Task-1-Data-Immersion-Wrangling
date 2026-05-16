# LinkedIn Video Script: Task 1 Walkthrough

## Opening

Hello everyone, this is my Task 1 submission for the Data Analytics internship: Data Immersion and Wrangling. In this task, I worked with a sales transactions dataset and prepared it for analysis using Python and Pandas.

## Dataset Overview

The dataset contains order details such as order date, customer information, customer segment, region, sales channel, product, quantity, unit price, discount, payment mode, and order status. I also created a data dictionary to document every column, its meaning, data type, and business relevance.

## Data Quality Issues

During profiling, I found several common data quality issues:

- Missing values in fields such as region, unit price, and customer date of birth.
- Duplicate transaction rows.
- Mixed date formats.
- Inconsistent category names, such as different spellings for the same product or sales channel.
- Invalid numeric values, including negative quantities, unrealistic discounts, and an extreme price outlier.

## Cleaning Process

I wrote a reproducible Python cleaning script. The script removes duplicate rows, standardizes column names and text values, converts mixed date formats, handles invalid numeric values, fills missing values, and creates new analysis-ready columns.

The new columns include customer age, gross revenue, net revenue, and order month. These fields will be useful in the next task for exploratory data analysis and business intelligence.

## Final Output

The final output is a cleaned CSV dataset, a data dictionary, and a data quality report. The cleaned dataset is now consistent, structured, and ready for analysis.

## Closing

This task helped me understand how important data preparation is before analysis. Clean data improves the reliability of insights, dashboards, and business decisions. Thank you.
