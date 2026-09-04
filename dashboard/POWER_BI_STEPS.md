# Power BI Dashboard Steps

1. Open **Power BI Desktop**.
2. Click **Get Data > Text/CSV**.
3. Select `data/cleaned_sales_data.csv`.
4. Click **Load**.

## Create these measures

```DAX
Total Sales = SUM(cleaned_sales_data[Sales])

Total Profit = SUM(cleaned_sales_data[Profit])

Total Orders = DISTINCTCOUNT(cleaned_sales_data[Order_ID])

Total Customers = DISTINCTCOUNT(cleaned_sales_data[Customer_Name])

Average Order Value = AVERAGE(cleaned_sales_data[Sales])

Profit Margin % =
DIVIDE(
    [Total Profit],
    [Total Sales],
    0
) * 100
```

## Dashboard layout

### KPI cards
- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Profit Margin %

### Charts
1. Line chart
   - X axis: Year_Month
   - Y axis: Total Sales

2. Clustered bar chart
   - Y axis: Region
   - X axis: Total Sales

3. Clustered column chart
   - X axis: Category
   - Y axis: Total Profit

4. Bar chart
   - Y axis: Product_Name
   - X axis: Total Sales
   - Visual filter: Top N = 10 by Total Sales

5. Scatter chart
   - X axis: Discount
   - Y axis: Profit
   - Size: Sales
   - Legend: Category

6. Donut chart
   - Legend: Segment
   - Values: Total Sales

### Slicers
- Year
- Region
- Category
- Segment

## Suggested title
Sales Performance Analytics Dashboard
