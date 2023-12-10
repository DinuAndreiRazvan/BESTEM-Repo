from sys import exit
from prophet import Prophet
from operator import itemgetter
import pandas as pd
import numpy as np
import matplotlib as mp
import logging
import json


def main():
    # read the Excel file

    logger = logging.getLogger('cmdstanpy')
    logger.addHandler(logging.NullHandler())
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)

    df = pd.read_excel("sales_and_eodStocks.xlsx", sheet_name="Sheet1")
    df = df.reset_index()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Product_ID'] = df['Product_ID'].astype(str)
    df = df.groupby(['Product_ID'])

    models = {}
    forecasts = {}
    for id, data in df:
        print(f"Product_ID: {id}")
        if data.shape[0] > 1:
            data.rename(columns={'Date': 'ds', 'Sales': 'y'}, inplace=True)

            m = Prophet(yearly_seasonality=True, n_changepoints=25, seasonality_prior_scale=0.1,
                        holidays_prior_scale=0.1, uncertainty_samples=0,
                        changepoint_prior_scale=0.05)
            # m.add_seasonality(name='monthly', period=30.5, fourier_order=5)
            m.fit(data)
            future = m.make_future_dataframe(periods=12, freq='MS')

            models[str(id)] = m
            forecasts[str(id)] = m.predict(future)

    min = {}
    for key in forecasts:
        min[key] = round(forecasts.get(key)['yhat'].mean() - df.get_group(key)['EndOfDayStock'].iloc[-1])

    res = dict(sorted(min.items(), key=itemgetter(1), reverse=False)[:10])

    for key, values in res.items():
        print(key, round(values))
        print('\n')

    with open("./frontend/src/table_recommendation.json", "w") as outfile:
        json.dump(min, outfile)

    fig = models.get(next(iter(min))).plot(forecasts.get(next(iter(min))), uncertainty=False, plot_cap=False,
                                           include_legend=True)
    fig.show()
    fig.savefig("./frontend/src/prediction.svg", format="png")

    fig = models.get(next(iter(min))).plot_components(forecasts.get(next(iter(min))))
    fig.show()
    fig.savefig("./frontend/src/periodic_progress.svg", format="png")


# Fisierul asta trebuie rulat din terminal pentru a rula programul
if __name__ == "__main__":
    exit(main())