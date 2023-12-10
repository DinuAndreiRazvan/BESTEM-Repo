from sys import exit
from prophet import Prophet
import pandas as pd
import numpy as np
import matplotlib as mp
import logging


def main():
    # read the Excel file

    logger = logging.getLogger('cmdstanpy')
    logger.addHandler(logging.NullHandler())
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)

    df = pd.read_excel("sales_and_eodStocks.xlsx", sheet_name="Sheet1")
    df = df.reset_index()

    models = {}
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
                data.rename(columns={'Date': 'ds', 'Sales': 'y'}, inplace=True)
                data['ds'] = pd.to_datetime(data['ds'])

                m = Prophet(yearly_seasonality=True, changepoint_range=0.8, changepoint_prior_scale=0.05)
                m.add_seasonality(name='monthly', period=30.5, fourier_order=5)
                m.fit(data)
                future = m.make_future_dataframe(periods=24, freq='MS')

                models[id] = m
                forecasts[id] = m.predict(future)

            id = str(row["Product_ID"])

    fig = models.get('15036').plot(forecasts.get('15036'), uncertainty=False, plot_cap=False, include_legend=True)
    fig.show()
    fig = models.get('15036').plot_components(forecasts.get('15036'))
    fig.show()


# Fisierul asta trebuie rulat din terminal pentru a rula programul
if __name__ == "__main__":
    exit(main())