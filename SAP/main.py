import datetime
from dataclasses import dataclass
from sys import exit
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analysis import *


@dataclass
class Stock:
    date: datetime.date
    product_ID: str
    sales: int
    endOfDayStock: int


@dataclass
class Product:
    dates: List[datetime.date]
    sales: List[int]
    stocks: List[int]


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


def main():
    # read the Excel file
    stock_file = pd.read_excel("sales_and_eodStocks.xlsx", sheet_name="Sheet1")

    # create a list of stocks
    stocks = []
    for _, row in stock_file.iterrows():
        stocks.append(
            Stock(row["Date"], row["Product_ID"], row["Sales"], row["EndOfDayStock"])
        )

    # Create a dictionary of Product objects with product IDs as keys
    unique_ids = set(stock.product_ID for stock in stocks)
    products_dict = {product_id: Product([], [], []) for product_id in unique_ids}

    # Populate the Product objects with data from the stocks array
    for stock in stocks:
        products_dict[stock.product_ID].dates.append(stock.date)
        products_dict[stock.product_ID].sales.append(stock.sales)
        products_dict[stock.product_ID].stocks.append(stock.endOfDayStock)

    # read the Excel file
    transaction_file = pd.read_excel("transactions.xlsx", sheet_name="Sheet1")
    # create a list of transactions
    transactions = []
    for _, row in transaction_file.iterrows():
        transactions.append(
            Transaction(
                row["Invoice"],
                row["Product_ID"],
                row["Description"],
                row["Quantity"],
                row["Date"],
                row["Price"],
                row["Customer ID"],
                row["Country"],
            )
        )


if __name__ == "__main__":
    exit(main())
