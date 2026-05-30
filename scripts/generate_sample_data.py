"""
generate_sample_data.py
Generates a sample sales transactions dataset with realistic data quality issues.
This raw dataset is used as input for the data cleaning pipeline.

Features:
- Generate synthetic data with quality issues
- Save to project folder, Desktop, Downloads, or custom path
- Interactive menu for choosing save location
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
from pathlib import Path

np.random.seed(42)
random.seed(42)

def generate_sample_data(n_records=5000):
    """Generate synthetic sales transactions data with intentional data quality issues."""
    
    product_categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
    sales_channels = ['Online', 'Retail', 'Wholesale', 'direct sales', 'ONLINE', 'online']
    customer_segments = ['Premium', 'Standard', 'Basic', 'premium', 'BASIC', 'standard']
    payment_modes = ['Credit Card', 'Debit Card', 'Cash', 'Digital Wallet', 'credit card', 'CASH']
    order_statuses = ['Completed', 'Pending', 'Cancelled', 'Returned', 'completed', 'pending ']
    
    product_names = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smart Watch'],
        'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Shoes'],
        'Home & Garden': ['Sofa', 'Table', 'Plant Pot', 'Lamp', 'Rug'],
        'Sports': ['Running Shoes', 'Yoga Mat', 'Dumbbell', 'Tennis Racket', 'Bicycle'],
        'Books': ['Fiction Novel', 'Self-Help Book', 'Cookbook', 'Mystery', 'Biography']
    }
    
    data = {
        'transaction_id': [f'TXN_{str(i).zfill(6)}' for i in range(1, n_records + 1)],
        'date': [],
        'product_category': [],
        'product_name': [],
        'quantity': [],
        'unit_price': [],
        'discount_percent': [],
        'sales_channel': [],
        'customer_segment': [],
        'date_of_birth': [],
        'payment_mode': [],
        'order_status': []
    }
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = (end_date - start_date).days
    
    for _ in range(n_records):
        random_days = random.randint(0, date_range)
        transaction_date = start_date + timedelta(days=random_days)
        data['date'].append(transaction_date.strftime('%Y-%m-%d'))
    
    for _ in range(n_records):
        category = random.choice(product_categories)
        data['product_category'].append(category)
        data['product_name'].append(random.choice(product_names[category]))
    
    for _ in range(n_records):
        if random.random() < 0.05:
            data['quantity'].append(np.nan if random.random() < 0.5 else random.choice([-1, 0, 100]))
        else:
            data['quantity'].append(random.randint(1, 10))
    
    for _ in range(n_records):
        if random.random() < 0.03:
            data['unit_price'].append(np.nan if random.random() < 0.5 else random.choice([-50, 0]))
        else:
            data['unit_price'].append(round(random.uniform(10, 500), 2))
    
    for _ in range(n_records):
        if random.random() < 0.08:
            data['discount_percent'].append(np.nan if random.random() < 0.5 else random.choice([-10, 150]))
        else:
            data['discount_percent'].append(round(random.uniform(0, 50), 2))
    
    data['sales_channel'] = [random.choice(sales_channels) for _ in range(n_records)]
    data['customer_segment'] = [random.choice(customer_segments) for _ in range(n_records)]
    
    for _ in range(n_records):
        if random.random() < 0.10:
            data['date_of_birth'].append(np.nan)
        else:
            age = random.randint(18, 80)
            dob = datetime.now() - timedelta(days=age*365)
            data['date_of_birth'].append(dob.strftime('%Y-%m-%d'))
    
    data['payment_mode'] = [random.choice(payment_modes) for _ in range(n_records)]
    data['order_status'] = [random.choice(order_statuses) for _ in range(n_records)]
    
    df = pd.DataFrame(data)
    
    n_duplicates = int(n_records * 0.02)
    if n_duplicates > 0:
        duplicate_indices = np.random.choice(df.index, n_duplicates, replace=False)
        duplicates = df.loc[duplicate_indices].copy()
        duplicates['transaction_id'] = [f'TXN_{str(n_records + i).zfill(6)}' for i in range(n_duplicates)]
        df = pd.concat([df, duplicates], ignore_index=True)
    
    return df

def get_user_home():
    """Get the user's home directory."""
    return str(Path.home())

def get_save_location():
    """Interactive menu to select save location."""
    print("\n" + "="*60)
    print("📁 WHERE WOULD YOU LIKE TO SAVE THE FILE?")
    print("="*60)
    print("1️⃣  Project Folder (data/)")
    print("2️⃣  Desktop")
    print("3️⃣  Downloads")
    print("4️⃣  Custom Path")
    print("="*60)
    
    choice = input("Enter your choice (1-4): ").strip()
    
    home = get_user_home()
    
    if choice == '1':
        output_path = 'data/sales_transactions_raw.csv'
        location_name = "Project Folder"
    elif choice == '2':
        desktop_path = os.path.join(home, 'Desktop')
        output_path = os.path.join(desktop_path, 'sales_transactions_raw.csv')
        location_name = "Desktop"
    elif choice == '3':
        downloads_path = os.path.join(home, 'Downloads')
        output_path = os.path.join(downloads_path, 'sales_transactions_raw.csv')
        location_name = "Downloads"
    elif choice == '4':
        custom_path = input("Enter full path (or just filename for current directory): ").strip()
        if not custom_path.endswith('.csv'):
            custom_path += '.csv'
        output_path = custom_path
        location_name = "Custom Path"
    else:
        print("❌ Invalid choice! Defaulting to Project Folder...")
        output_path = 'data/sales_transactions_raw.csv'
        location_name = "Project Folder (Default)"
    
    return output_path, location_name

def main():
    """Generate and save sample data to selected location."""
    print("\n🔄 Generating sample sales transactions data...")
    df = generate_sample_data(n_records=5000)
    
    # Get save location from user
    output_path, location_name = get_save_location()
    
    # Create directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:  # Only create if there's a directory component
        os.makedirs(output_dir, exist_ok=True)
    
    # Save the file
    try:
        df.to_csv(output_path, index=False)
        
        print("\n" + "="*60)
        print("✅ SUCCESS! Sample data generated and saved!")
        print("="*60)
        print(f"📊 Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"📁 Location: {location_name}")
        print(f"💾 Full path: {os.path.abspath(output_path)}")
        print("="*60 + "\n")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        print("Please check the path and try again.")

if __name__ == '__main__':
    main()
