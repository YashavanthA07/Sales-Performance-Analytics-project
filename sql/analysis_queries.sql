USE sales_analytics;

-- 1. Overall KPIs
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_Name) AS Unique_Customers,
    ROUND(AVG(Sales), 2) AS Average_Order_Value
FROM sales;

-- 2. Sales and profit by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 3. Category performance
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG(Profit_Margin_Pct), 2) AS Avg_Profit_Margin_Pct
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 4. Monthly sales trend
SELECT
    Year_Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales,
    ROUND(SUM(Profit), 2) AS Monthly_Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales
GROUP BY Year_Month
ORDER BY Year_Month;

-- 5. Top 10 products by sales
SELECT
    Product_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    SUM(Quantity) AS Units_Sold
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 6. Top 10 customers
SELECT
    Customer_Name,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 7. Discount impact
SELECT
    Discount,
    ROUND(AVG(Sales), 2) AS Avg_Sales,
    ROUND(AVG(Profit), 2) AS Avg_Profit,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Discount
ORDER BY Discount;

-- 8. Most profitable products
SELECT
    Product_Name,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;

-- 9. Loss-making products
SELECT
    Product_Name,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales
GROUP BY Product_Name
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC;

-- 10. Segment performance
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Orders
FROM sales
GROUP BY Segment
ORDER BY Total_Sales DESC;
