import datetime

import pandas as pd
from dataclasses import dataclass


@dataclass
class Stocks:
    date: datetime.datetime
    product_ID: str
    sales: int
    endOfDayStock: int


# read the Excel file
df = pd.read_excel('sales_and_eodStocks.xlsx', sheet_name='Sheet1')

# create a list of student objects
stocks = []
for _, row in df.iterrows():
    stocks.append(Stocks(row['Date'], row['Product_ID'], row['Sales'], row['EndOfDayStock']))

print(stocks)