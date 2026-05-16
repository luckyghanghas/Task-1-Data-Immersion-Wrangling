# Data Dictionary

| Column | Type | Description | Business Relevance |
|---|---|---|---|
| order_id | Text | Unique identifier for each order. | Used to track transactions and remove duplicates. |
| order_date | Date | Date when the order was placed. | Supports trend, seasonality, and monthly performance analysis. |
| order_month | Text | Year-month derived from order_date. | Useful for monthly KPI reporting. |
| customer_id | Text | Unique identifier for a customer. | Enables customer-level behavior and retention analysis. |
| customer_name | Text | Customer name. | Helpful for record inspection, not usually used for aggregate analysis. |
| customer_dob | Date | Customer date of birth. | Used to calculate customer age. |
| customer_age | Numeric | Customer age as of the analysis reference date. | Enables age-group segmentation. |
| customer_segment | Text | Customer category such as Student, Professional, Small Business, or Enterprise. | Supports segment-level performance analysis. |
| region | Text | Customer or sales region. | Supports geographic performance comparison. |
| sales_channel | Text | Channel where the sale occurred: Online, Retail, or Partner. | Helps compare channel effectiveness. |
| product | Text | Product purchased. | Used for product-level revenue and demand analysis. |
| quantity | Integer | Number of units purchased. | Required for volume and revenue calculations. |
| unit_price | Numeric | Price per unit before discount. | Required for revenue calculations and price analysis. |
| discount_rate | Numeric | Discount applied to the order. | Helps evaluate discounting impact on revenue. |
| gross_revenue | Numeric | quantity multiplied by unit_price. | Measures revenue before discounts. |
| net_revenue | Numeric | Gross revenue after discount. | Measures realized sales revenue. |
| payment_mode | Text | Payment method used by the customer. | Useful for operational and payment preference analysis. |
| order_status | Text | Completed, Returned, or Cancelled. | Supports fulfillment and return/cancellation analysis. |
