"""Module fetches stock details from finviz"""
import time
import finviz
import requests


def fetch_fundamentals(stock):
    """Returns ticker details"""
    wait = 0
    get_fundamentals = True

    while get_fundamentals:
        try:
            try:
                data = finviz.get_stock(stock['Ticker'])
            except KeyError:
                data = finviz.get_stock(stock['symbol'])
            get_fundamentals = False
        except requests.exceptions.HTTPError:
            wait += 1
            time.sleep(wait)

        if wait > 5:
            data = None
            get_fundamentals = False

    return data
