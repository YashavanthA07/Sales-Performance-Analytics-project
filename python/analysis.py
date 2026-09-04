from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "cleaned_sales_data.csv"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order_Date"])

# KPI summary
summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Unique Customers",
        "Average Order Value",
        "Average Profit",
        "Average Discount",
        "Median Sales",
        "Sales Std Dev",
        "Discount-Profit Correlation"
    ],
    "Value": [
        round(df["Sales"].sum(), 2),
        round(df["Profit"].sum(), 2),
        int(df["Order_ID"].nunique()),
        int(df["Customer_Name"].nunique()),
        round(df["Sales"].mean(), 2),
        round(df["Profit"].mean(), 2),
        round(df["Discount"].mean(), 4),
        round(df["Sales"].median(), 2),
        round(df["Sales"].std(), 2),
        round(df["Discount"].corr(df["Profit"]), 4)
    ]
})
summary.to_csv(OUT / "kpi_summary.csv", index=False)

# Regional performance
region = (
    df.groupby("Region", as_index=False)
      .agg(Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Orders=("Order_ID", "nunique"))
      .sort_values("Total_Sales", ascending=False)
)
region.to_csv(OUT / "sales_by_region.csv", index=False)

# Category performance
category = (
    df.groupby("Category", as_index=False)
      .agg(Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Avg_Profit_Margin=("Profit_Margin_Pct", "mean"))
      .sort_values("Total_Sales", ascending=False)
)
category.to_csv(OUT / "category_performance.csv", index=False)

# Monthly trend
monthly = (
    df.groupby("Year_Month", as_index=False)
      .agg(Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Orders=("Order_ID", "nunique"))
      .sort_values("Year_Month")
)
monthly.to_csv(OUT / "monthly_trend.csv", index=False)

# Top products
products = (
    df.groupby("Product_Name", as_index=False)
      .agg(Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Units_Sold=("Quantity", "sum"))
      .sort_values("Total_Sales", ascending=False)
      .head(10)
)
products.to_csv(OUT / "top_10_products.csv", index=False)

# Top customers
customers = (
    df.groupby("Customer_Name", as_index=False)
      .agg(Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Orders=("Order_ID", "nunique"))
      .sort_values("Total_Sales", ascending=False)
      .head(10)
)
customers.to_csv(OUT / "top_10_customers.csv", index=False)

# Discount analysis
discount = (
    df.groupby("Discount", as_index=False)
      .agg(Avg_Sales=("Sales", "mean"),
           Avg_Profit=("Profit", "mean"),
           Total_Sales=("Sales", "sum"),
           Total_Profit=("Profit", "sum"),
           Orders=("Order_ID", "nunique"))
      .sort_values("Discount")
)
discount.to_csv(OUT / "discount_analysis.csv", index=False)

print("\n=== KPI SUMMARY ===")
print(summary.to_string(index=False))

print("\n=== SALES BY REGION ===")
print(region.to_string(index=False))

print("\n=== TOP 10 PRODUCTS ===")
print(products.to_string(index=False))

print(f"\nAnalysis files saved to: {OUT}")
