import datetime
import pandas as pd
from dataclasses import dataclass


@dataclass
class Stock:
    date: datetime.date
    product_ID: str
    sales: int
    endOfDayStock: int


@dataclass
class Transaction:
    invoice: int
    product_ID: str
    description: str
    quantity: int
    date: datetime.datetime
    price: float
    customer_ID: str
    country: str


# read the Stocks Excel file
df = pd.read_excel('sales_and_eodStocks.xlsx', sheet_name='Sheet1')

# create a list of Stock objects
stocks = []
for _, row in df.iterrows():
    stocks.append(Stock(row['Date'], row['Product_ID'], row['Sales'], row['EndOfDayStock']))

# read the Transactions Excel file
df = pd.read_excel('transactions.xlsx', sheet_name='Sheet1')

# create a list of Transaction objects
transactions = []
for _, row in df.iterrows():
    transactions.append(Transaction(row['Invoice'], row['Product_ID'], row['Description'],
                                    row['Quantity'], row['Date'], row['Price'],
                                    row['Customer ID'], row['Country']))