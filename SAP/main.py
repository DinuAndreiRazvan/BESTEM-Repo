import datetime
from dataclasses import dataclass
from sys import exit
import pandas as pd
import numpy as np
import matplotlib as mp

from stock import *


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


def main():
    # read the Excel file
    df = pd.read_excel("sales_and_eodStocks.xlsx", sheet_name="Sheet1")

    # create a list of stocks
    stocks = []
    for _, row in df.iterrows():
        stocks.append(
            Stock(row["Date"], row["Product_ID"], row["Sales"], row["EndOfDayStock"])
        )

    stock_check(stocks)

    # read the Excel file
    # df = pd.read_excel("transactions.xlsx", sheet_name="Sheet1")

    # create a list of transactions
    # transactions = []
    # for _, row in df.iterrows():
    #     transactions.append(
    #         Transaction(row["Invoice"], row["Product_ID"], row["Description"],
    #                     row["Quantity"], row["Date"], row["Price"],
    #                     row["Customer ID"], row["Country"], ))


# Fisierul asta trebuie rulat din terminal pentru a rula programul
if __name__ == "__main__":
    exit(main())

