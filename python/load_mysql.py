from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "cleaned_sales_data.csv"

# CHANGE THESE VALUES
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_mysql_password"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DATABASE = "sales_analytics"

password = quote_plus(MYSQL_PASSWORD)
engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{password}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

df = pd.read_csv(DATA)

# Convert date before loading
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df.to_sql(
    "sales",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    method="multi"
)

print(f"Loaded {len(df)} rows into {MYSQL_DATABASE}.sales")
