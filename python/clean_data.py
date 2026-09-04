from pathlib import Path
import pandas as pd
import numpy as np

BASE = Path(__file__).resolve().parents[1]
input_file = BASE / "data" / "sales_data.csv"
output_file = BASE / "data" / "cleaned_sales_data.csv"

df = pd.read_csv(input_file)

print("Original shape:", df.shape)

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Handle missing values
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown Customer")
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
df["Discount"] = df["Discount"].fillna(df["Discount"].median())

# Ensure numeric columns
for col in ["Quantity", "Discount", "Sales", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows missing essential numeric/date values
df = df.dropna(subset=["Order_Date", "Quantity", "Sales", "Profit"])

# Feature engineering
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%b")
df["Year_Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Profit_Margin_Pct"] = np.where(
    df["Sales"] != 0,
    (df["Profit"] / df["Sales"]) * 100,
    0
).round(2)

df["Sales_Band"] = pd.cut(
    df["Sales"],
    bins=[-float("inf"), 10000, 50000, 150000, float("inf")],
    labels=["Low", "Medium", "High", "Very High"]
)

# Reorder columns
columns = [
    "Order_ID","Order_Date","Year","Month","Month_Name","Year_Month",
    "Customer_Name","Segment","Product_Name","Category","Region",
    "Quantity","Discount","Sales","Profit","Profit_Margin_Pct","Sales_Band"
]
df = df[columns].sort_values("Order_Date")

df.to_csv(output_file, index=False)

print("Cleaned shape:", df.shape)
print(f"Saved cleaned data to: {output_file}")
