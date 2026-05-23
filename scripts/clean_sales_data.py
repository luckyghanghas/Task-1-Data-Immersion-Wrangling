"""
clean_sales_data.py
Comprehensive data cleaning and transformation pipeline for sales transactions.
Handles missing values, duplicates, formatting, and feature engineering.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class SalesDataCleaner:
    """Pipeline for cleaning and transforming sales transaction data."""
    
    def __init__(self, raw_data_path='data/sales_transactions_raw.csv'):
        """Initialize cleaner with raw data."""
        self.raw_data_path = raw_data_path
        self.df = None
        self.cleaning_log = []
        self.quality_metrics = {}
        
    def load_data(self):
        """Load raw data from CSV."""
        print("📂 Loading raw data...")
        self.df = pd.read_csv(self.raw_data_path)
        self.quality_metrics['initial_shape'] = self.df.shape
        print(f"✅ Loaded {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        return self
    
    def profile_data(self):
        """Generate initial data quality report."""
        print("\n📊 Profiling data quality issues...")
        
        missing_summary = self.df.isnull().sum()
        for col, count in missing_summary[missing_summary > 0].items():
            pct = (count / len(self.df)) * 100
            msg = f"   • {col}: {count} missing ({pct:.2f}%)"
            print(msg)
            self.cleaning_log.append(msg)
        
        duplicates = self.df.duplicated().sum()
        if duplicates > 0:
            msg = f"   • Duplicate rows: {duplicates}"
            print(msg)
            self.cleaning_log.append(msg)
        
        self.quality_metrics['initial_duplicates'] = duplicates
        self.quality_metrics['initial_missing'] = missing_summary
        return self
    
    def remove_duplicates(self):
        """Remove duplicate rows."""
        print("\n🔄 Removing duplicates...")
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates(subset=['transaction_id', 'date', 'product_name', 'quantity', 'unit_price'], keep='first')
        removed = initial_count - len(self.df)
        msg = f"   ✅ Removed {removed} duplicate rows"
        print(msg)
        self.cleaning_log.append(msg)
        self.quality_metrics['duplicates_removed'] = removed
        return self
    
    def standardize_text_columns(self):
        """Standardize text column formatting."""
        print("\n✏️ Standardizing text columns...")
        
        self.df['product_category'] = self.df['product_category'].str.strip().str.title()
        self.df['sales_channel'] = self.df['sales_channel'].str.strip().str.title()
        self.df['customer_segment'] = self.df['customer_segment'].str.strip().str.title()
        self.df['payment_mode'] = self.df['payment_mode'].str.strip().str.title()
        self.df['order_status'] = self.df['order_status'].str.strip().str.title()
        
        msg = f"   ✅ Standardized all text columns"
        print(msg)
        self.cleaning_log.append(msg)
        return self
    
    def clean_dates(self):
        """Convert and standardize date formats."""
        print("\n📅 Cleaning date fields...")
        
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        
        if self.df['date'].isnull().any():
            median_date = self.df['date'].median()
            self.df['date'].fillna(median_date, inplace=True)
        
        self.df['date_of_birth'] = pd.to_datetime(self.df['date_of_birth'], errors='coerce')
        
        msg = f"   ✅ Standardized date formats to YYYY-MM-DD"
        print(msg)
        self.cleaning_log.append(msg)
        return self
    
    def clean_numeric_fields(self):
        """Handle invalid and outlier values in numeric columns."""
        print("\n🔢 Cleaning numeric fields...")
        
        # Clean quantity
        self.df['quantity'].fillna(1, inplace=True)
        self.df.loc[self.df['quantity'] <= 0, 'quantity'] = 1
        self.df.loc[self.df['quantity'] > 100, 'quantity'] = 100
        
        # Clean unit_price
        median_price = self.df['unit_price'][self.df['unit_price'] > 0].median()
        self.df['unit_price'].fillna(median_price, inplace=True)
        self.df.loc[self.df['unit_price'] <= 0, 'unit_price'] = median_price
        
        # Clean discount_percent
        self.df['discount_percent'].fillna(0, inplace=True)
        self.df.loc[self.df['discount_percent'] < 0, 'discount_percent'] = 0
        self.df.loc[self.df['discount_percent'] > 100, 'discount_percent'] = 100
        
        msg = f"   ✅ Cleaned all numeric fields (quantity, price, discount)"
        print(msg)
        self.cleaning_log.append(msg)
        return self
    
    def engineer_features(self):
        """Create derived features for analysis."""
        print("\n⚙️ Engineering features...")
        
        # Customer age from date_of_birth
        today = pd.Timestamp.now()
        self.df['customer_age'] = (today - self.df['date_of_birth']).dt.days // 365
        self.df['customer_age'].fillna(self.df['customer_age'].median(), inplace=True)
        self.df.loc[self.df['customer_age'] < 18, 'customer_age'] = 18
        self.df.loc[self.df['customer_age'] > 100, 'customer_age'] = 100
        
        # Gross revenue
        self.df['gross_revenue'] = self.df['quantity'] * self.df['unit_price']
        
        # Net revenue (after discount)
        self.df['net_revenue'] = self.df['gross_revenue'] * (1 - self.df['discount_percent'] / 100)
        
        # Order month
        self.df['order_month'] = self.df['date'].dt.strftime('%Y-%m')
        
        msg = f"   ✅ Created derived features: customer_age, gross_revenue, net_revenue, order_month"
        print(msg)
        self.cleaning_log.append(msg)
        return self
    
    def drop_unnecessary_columns(self):
        """Drop columns no longer needed."""
        print("\n🗑️ Removing unnecessary columns...")
        self.df = self.df.drop(columns=['date_of_birth'])
        msg = f"   ✅ Dropped date_of_birth column"
        print(msg)
        self.cleaning_log.append(msg)
        return self
    
    def validate_and_export(self):
        """Validate cleaned data and export."""
        print("\n✅ Validating cleaned data...")
        
        missing = self.df.isnull().sum().sum()
        msg = f"   • Missing values: {missing}"
        print(msg)
        self.cleaning_log.append(msg)
        
        msg = f"   • Final shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns"
        print(msg)
        self.cleaning_log.append(msg)
        
        output_path = 'data/sales_transactions_cleaned.csv'
        self.df.to_csv(output_path, index=False)
        msg = f"   ✅ Exported cleaned data to {output_path}"
        print(msg)
        self.cleaning_log.append(msg)
        
        self.quality_metrics['final_shape'] = self.df.shape
        return self
    
    def run_pipeline(self):
        """Execute the complete cleaning pipeline."""
        print("\n" + "="*60)
        print("🚀 TASK-1: Data Immersion & Wrangling Pipeline")
        print("="*60)
        
        self.load_data()\
            .profile_data()\
            .remove_duplicates()\
            .standardize_text_columns()\
            .clean_dates()\
            .clean_numeric_fields()\
            .engineer_features()\
            .drop_unnecessary_columns()\
            .validate_and_export()
        
        print("\n" + "="*60)
        print("✅ Pipeline Completed Successfully!")
        print("="*60)
        print(f"📊 Records processed: {self.quality_metrics['initial_shape'][0]}")
        print(f"📈 Final dataset shape: {self.quality_metrics['final_shape']}")
        print(f"💾 Output: data/sales_transactions_cleaned.csv")

def main():
    """Run the data cleaning pipeline."""
    cleaner = SalesDataCleaner()
    cleaner.run_pipeline()

if __name__ == '__main__':
    main()
