from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import random

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "sales_transactions_raw.csv"


random.seed(42)
np.random.seed(42)

products = {
    "Laptop": (55000, 90000),
    "Smartphone": (12000, 45000),
    "Headphones": (800, 5000),
    "Keyboard": (700, 3500),
    "Monitor": (7000, 24000),
    "Mouse": (400, 2500),
}
regions = ["North", "South", "East", "West", "Central"]
channels = ["Online", "Retail", "Partner"]
payment_modes = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]
customer_segments = ["Student", "Professional", "Small Business", "Enterprise"]
statuses = ["Completed", "Returned", "Cancelled"]

rows = []
start_date = datetime(2025, 1, 1)

for i in range(1, 251):
    product = random.choice(list(products))
    low, high = products[product]
    quantity = random.choices([1, 2, 3, 4, 5], weights=[50, 25, 12, 8, 5])[0]
    unit_price = round(random.uniform(low, high), 2)
    discount = random.choice([0, 0, 0.05, 0.1, 0.15, 0.2])
    status = random.choices(statuses, weights=[85, 10, 5])[0]
    order_date = start_date + timedelta(days=random.randint(0, 364))
    dob = datetime(random.randint(1975, 2005), random.randint(1, 12), random.randint(1, 28))

    rows.append(
        {
            "order_id": f"ORD-{1000+i}",
            "order_date": order_date.strftime(random.choice(["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"])),
            "customer_id": f"CUST-{random.randint(1, 90):03d}",
            "customer_name": random.choice(
                ["Aarav Sharma", "Priya Nair", "Rohan Mehta", "Sneha Rao", "Vikram Singh", "Neha Gupta"]
            ),
            "customer_dob": dob.strftime(random.choice(["%Y-%m-%d", "%d/%m/%Y"])),
            "customer_segment": random.choice(customer_segments),
            "region": random.choice(regions),
            "sales_channel": random.choice(channels),
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_rate": discount,
            "payment_mode": random.choice(payment_modes),
            "order_status": status,
        }
    )

df = pd.DataFrame(rows)

# Inject realistic data quality issues for the cleaning task.
df.loc[[8, 29, 61], "region"] = np.nan
df.loc[[14, 73], "unit_price"] = np.nan
df.loc[[35, 114], "customer_dob"] = np.nan
df.loc[19, "quantity"] = -2
df.loc[87, "discount_rate"] = 1.25
df.loc[123, "unit_price"] = 999999
df.loc[47, "product"] = "smart phone"
df.loc[68, "product"] = "Head Phones"
df.loc[91, "sales_channel"] = "web"

duplicates = df.sample(6, random_state=11)
df = pd.concat([df, duplicates], ignore_index=True)

RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(RAW_PATH, index=False)
print(f"Wrote {RAW_PATH} with {len(df)} rows")
