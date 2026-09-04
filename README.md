# Sales Performance Analytics Dashboard

A complete beginner-friendly Data Analyst portfolio project using:

- Python
- Pandas
- NumPy
- SQL / MySQL
- Excel-compatible CSV files
- Statistics
- Power BI

## Project objective

Analyze company sales data and answer business questions such as:

- Which region generates the highest sales?
- Which products generate the most profit?
- How are sales changing month by month?
- Which customer segment performs best?
- What is the impact of discount on profit?
- Who are the top customers?

## Folder structure

```text
sales-performance-analytics/
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv          # created after cleaning
├── python/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── analysis.py
│   └── load_mysql.py
├── sql/
│   ├── create_database.sql
│   └── analysis_queries.sql
├── outputs/
│   └── analysis CSV files              # created after analysis
├── dashboard/
│   └── POWER_BI_STEPS.md
├── requirements.txt
└── README.md
```

# Step-by-step execution on Windows PowerShell

## 1. Extract the project

Extract the ZIP file and open the project folder.

Example:

```powershell
cd "C:\Users\YourName\Downloads\sales-performance-analytics"
```

## 2. Check Python

```powershell
python --version
```

Recommended: Python 3.10 or newer.

## 3. Create virtual environment

```powershell
python -m venv venv
```

## 4. Activate virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 5. Install libraries

```powershell
pip install -r requirements.txt
```

## 6. Optional: regenerate raw dataset

A sample `sales_data.csv` is already included.

To create it again:

```powershell
python .\python\generate_data.py
```

## 7. Clean the data

```powershell
python .\python\clean_data.py
```

This creates:

```text
data/cleaned_sales_data.csv
```

## 8. Run Python analysis

```powershell
python .\python\analysis.py
```

This creates:

```text
outputs/kpi_summary.csv
outputs/sales_by_region.csv
outputs/category_performance.csv
outputs/monthly_trend.csv
outputs/top_10_products.csv
outputs/top_10_customers.csv
outputs/discount_analysis.csv
```

# MySQL setup

## 9. Install MySQL

Install MySQL Server and MySQL Workbench if not already installed.

## 10. Create database

Open MySQL Workbench and run:

```sql
CREATE DATABASE IF NOT EXISTS sales_analytics;
USE sales_analytics;
```

You can also run the included:

```text
sql/create_database.sql
```

## 11. Update MySQL password

Open:

```text
python/load_mysql.py
```

Change:

```python
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_mysql_password"
```

Use your actual MySQL credentials.

## 12. Load cleaned data into MySQL

```powershell
python .\python\load_mysql.py
```

You should see something like:

```text
Loaded 1500 rows into sales_analytics.sales
```

## 13. Run SQL business analysis

Open:

```text
sql/analysis_queries.sql
```

Run the queries in MySQL Workbench.

# Power BI dashboard

Open:

```text
dashboard/POWER_BI_STEPS.md
```

Follow the instructions to import:

```text
data/cleaned_sales_data.csv
```

and create the dashboard.

# Statistics used

The Python analysis includes:

- Mean
- Median
- Standard deviation
- Correlation between discount and profit
- Aggregation by region/category/month/product/customer

# Interview explanation

You can say:

> I developed a Sales Performance Analytics project using Python, SQL, Excel-compatible datasets, statistics, and Power BI. I cleaned and transformed raw sales data using Pandas, handled missing values and duplicate records, and created additional features such as year, month, and profit margin. I used SQL to analyze regional sales, product performance, customers, monthly trends, and discount impact. Finally, I created an interactive Power BI dashboard with KPIs such as total sales, profit, orders, customers, and profit margin.

# Resume bullets

**Sales Performance Analytics Dashboard — Python, SQL, Excel, Power BI**

- Analyzed sales data to identify revenue trends, profitable products, regional performance, and customer purchasing patterns.
- Cleaned and transformed raw data using Python and Pandas, handling missing values, duplicates, and date formatting.
- Used SQL queries for aggregation, KPI calculation, product analysis, customer analysis, and monthly sales trends.
- Performed statistical analysis using mean, median, standard deviation, and correlation to evaluate sales and profit behavior.
- Built an interactive Power BI dashboard to visualize sales, profit, regional performance, customer segments, and top products.
