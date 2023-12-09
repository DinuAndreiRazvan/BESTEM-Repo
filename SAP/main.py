from sys import exit
from prophet import Prophet
import pandas as pd
import numpy as np
import matplotlib as mp
import logging


def prediction(data):
    data.rename(columns={'Date': 'ds', 'Sales': 'y'}, inplace=True)
    data['ds'] = pd.to_datetime(data['ds'])
    m = Prophet()
    m.fit(data)

    future = m.make_future_dataframe(periods=36, freq='MS')
    forecast = m.predict(future)
    return forecast


def main():
    # read the Excel file

    logger = logging.getLogger('cmdstanpy')
    logger.addHandler(logging.NullHandler())
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)

    df = pd.read_excel("sales_and_eodStocks.xlsx", sheet_name="Sheet1")
    df = df.reset_index()

    forecasts = {}
    row_list = []
    for index, row in df.iterrows():
        if len(row_list) == 0:
            row_list.append(row)
            id = str(row["Product_ID"])
        elif str(row["Product_ID"]) == id:
            row_list.append(row)
        else:
            data = pd.DataFrame(row_list)
            row_list.clear()
            row_list.append(row)
            if data.shape[0] > 1:
                forecasts[id] = prediction(data)


# Fisierul asta trebuie rulat din terminal pentru a rula programul
if __name__ == "__main__":
    exit(main())