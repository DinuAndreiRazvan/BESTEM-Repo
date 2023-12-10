from sys import exit
from prophet import Prophet
from operator import itemgetter
from collections import OrderedDict
import pandas as pd
import logging
import json
import itertools
from Send_Messages.send_message import *


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
    df['EndOfDayStock'] = df['EndOfDayStock'].astype(int)
    df = df.groupby(['Product_ID'])

    models = {}
    forecasts = {}
    for id, data in df:
        # print(f"Product_ID: {id}")

        if data.shape[0] > 90:
            data.rename(columns={'Date': 'ds', 'Sales': 'y'}, inplace=True)

            m = Prophet(yearly_seasonality=True, n_changepoints=25, seasonality_prior_scale=0.1,
                        holidays_prior_scale=0.1, uncertainty_samples=0,
                        changepoint_prior_scale=0.05)
            m.fit(data)
            future = m.make_future_dataframe(periods=12, freq='MS')

            models[str(id)] = m
            forecasts[str(id)] = m.predict(future)
            break

    overstocks = {}
    for id, data in df:
        upper_bound = (forecasts[str(id)]['yhat'] * 1.75).mean()
        lower_bound = (forecasts[str(id)]['yhat'] * 0.25).mean()

        for val in data['EndOfDayStock']:
            if val - lower_bound < 0:
                send_email('Send_Messages/contacts.txt', 'Send_Messages/inc_stocks.txt')
            elif val - upper_bound > 0:
                send_email('Send_Messages/contacts.txt', 'Send_Messages/dec_stocks.txt')
                if overstocks.get(str(id)) is not None:
                    if overstocks.get(str(id)) < val:
                        overstocks[str(id)] = val

    res_stock = OrderedDict(sorted(overstocks.items(), key=itemgetter(1), reverse=False)[:10])
    with open("./frontend/src/overstock.json", "w") as outfile:
        json.dump(OrderedDict(itertools.islice(res_stock.items(), 10)), outfile)

    min = {}
    for key in forecasts:
        min[key] = round(forecasts.get(key)['yhat'].mean() - df.get_group(key)['EndOfDayStock'].iloc[-1])

    res_min = OrderedDict(sorted(min.items(), key=itemgetter(1), reverse=False)[:10])
    with open("./frontend/src/table_recommendation.json", "w") as outfile:
        json.dump(OrderedDict(itertools.islice(res_min.items(), 10)), outfile)

    fig = models.get(next(iter(min))).plot(forecasts.get(next(iter(min))), uncertainty=False, plot_cap=False,
                                           include_legend=True)
    fig.savefig("./frontend/src/prediction.svg", format="png")

    fig = models.get(next(iter(min))).plot_components(forecasts.get(next(iter(min))))
    fig.show()
    fig.savefig("./frontend/src/periodic_progress.svg", format="png")


# Fisierul asta trebuie rulat din terminal pentru a rula programul
if __name__ == "__main__":
    exit(main())