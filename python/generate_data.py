from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data"
DATA_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(42)
n = 1500
start = datetime(2024, 1, 1)

categories = {
    "Technology": ["Laptop", "Monitor", "Keyboard", "Mouse", "Headphones", "Webcam"],
    "Furniture": ["Office Chair", "Desk", "Bookshelf", "Cabinet", "Table"],
    "Office Supplies": ["Notebook", "Pen Set", "Printer Paper", "Stapler", "Folders"]
}
regions = ["North", "South", "East", "West"]
segments = ["Consumer", "Corporate", "Home Office"]

base_price = {
    "Laptop": 65000, "Monitor": 18000, "Keyboard": 2500, "Mouse": 1200, "Headphones": 3500, "Webcam": 3000,
    "Office Chair": 9000, "Desk": 15000, "Bookshelf": 8000, "Cabinet": 12000, "Table": 14000,
    "Notebook": 250, "Pen Set": 180, "Printer Paper": 450, "Stapler": 300, "Folders": 220
}

rows = []
for i in range(1, n + 1):
    category = rng.choice(list(categories.keys()))
    product = rng.choice(categories[category])
    region = rng.choice(regions)
    segment = rng.choice(segments, p=[0.5, 0.3, 0.2])
    order_date = start + timedelta(days=int(rng.integers(0, 730)))
    quantity = int(rng.integers(1, 8))
    discount = float(rng.choice([0, .05, .10, .15, .20, .25], p=[.18,.18,.20,.17,.17,.10]))

    gross = base_price[product] * quantity * rng.uniform(.9, 1.1)
    sales = gross * (1 - discount)

    margin = {"Technology": .22, "Furniture": .18, "Office Supplies": .28}[category]
    cost = gross * (1 - margin) * rng.uniform(.96, 1.04)
    profit = sales - cost

    rows.append({
        "Order_ID": f"ORD-{i:05d}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Customer_Name": f"Customer_{int(rng.integers(1, 301)):03d}",
        "Segment": segment,
        "Product_Name": product,
        "Category": category,
        "Region": region,
        "Quantity": quantity,
        "Discount": round(discount, 2),
        "Sales": round(sales, 2),
        "Profit": round(profit, 2)
    })

df = pd.DataFrame(rows)

# Add a few intentional issues for cleaning practice
df.loc[5, "Customer_Name"] = None
df.loc[33, "Region"] = None
df.loc[70, "Discount"] = None
df = pd.concat([df, df.iloc[[10, 20]]], ignore_index=True)

output = DATA_DIR / "sales_data.csv"
df.to_csv(output, index=False)
print(f"Created: {output}")
print(f"Rows: {len(df)}")
