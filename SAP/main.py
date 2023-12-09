import datetime
from dataclasses import dataclass
from sys import exit
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from stock import *


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


def find_outliers(products_dict, unique_ids):
    for key, value in products_dict.items():
        if key == "17164B":
            df = pd.DataFrame(
                {
                    "dates": value.dates,
                    "sales": value.sales,
                }
            )
            # Calculate the interquartile range (IQR)
            Q1 = df["sales"].quantile(0.25)
            Q3 = df["sales"].quantile(0.75)
            IQR = Q3 - Q1

            # Define the lower and upper bounds for outliers
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Identify outliers based on the bounds
            outliers = df[(df["sales"] < lower_bound) | (df["sales"] > upper_bound)]

            # Print or further analyze the outliers
            print("Outliers:")
            print(outliers)
            plt.plot(outliers)
            plt.title("Sales Over Time")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.show()


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
    unique_ids = list(dict.fromkeys(stock.product_ID for stock in stocks))
    products_dict = {product_id: Product([], [], []) for product_id in unique_ids}
    stock_check(stocks)

    # Populate the Product objects with data from the stocks array
    for stock in stocks:
        products_dict[stock.product_ID].dates.append(stock.date)
        products_dict[stock.product_ID].sales.append(stock.sales)
        products_dict[stock.product_ID].stocks.append(stock.endOfDayStock)

    find_outliers(products_dict, unique_ids)

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

    # transactions = []
    # for _, row in df.iterrows():
    #     transactions.append(
    #         Transaction(row["Invoice"], row["Product_ID"], row["Description"],
    #                     row["Quantity"], row["Date"], row["Price"],
    #                     row["Customer ID"], row["Country"], ))


if __name__ == "__main__":
    exit(main())
