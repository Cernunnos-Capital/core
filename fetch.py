"""Module fetches stock details from autoviz"""
import time
import requests
import autoviz

ratios = {'Basic Materials': [5, 22.5],
          'Communication Services': [22.5, 35],
          'Consumer Cyclical': [22.5, 35],
          'Consumer Defensive': [22.5, 35],
          'Energy': [7, 8.5],
          'Healthcare': [25, 30],
          'Industrials': [20, 30],
          'Real Estate': [25, 35],
          'Technology': [30, 40],
          'Utilities': [5, 15],
          'Financial': [15, 10]
          }


def fetch_fundamentals(stock):
    """Returns ticker details"""
    wait = 0
    get_fundamentals = True

    while get_fundamentals:
        try:
            try:
                data = autoviz.get_stock(stock['Ticker'])
            except TypeError:
                data = autoviz.get_stock(stock.symbol)
            get_fundamentals = False
        except requests.exceptions.HTTPError:
            wait += 1
            time.sleep(wait)

        if wait > 5:
            data = None
            get_fundamentals = False

    return data


def str_perc(metric):
    """Convert data to operatable ratios"""
    metric = str(metric)

    if metric != '-':
        metric = metric.replace('%', '')
        metric = float(metric)
    else:
        metric = 0.0

    return metric
