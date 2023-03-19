"""Module screens stocks from Finviz"""
import os
import sys
import random
import finviz
from finviz.screener import Screener
import time

# screening attributes
STOCK_SCREENER = os.environ['URL'].split(',')
STOCK_SCREENER_FALLBACK = os.environ['URL_FALLBACK'].split(',')

# error handling for no result
try:
    stock_list = Screener(filters=STOCK_SCREENER)
except finviz.helper_functions.error_handling.NoResults:
    stock_list = Screener(filters=STOCK_SCREENER_FALLBACK)
except:  # pylint: disable=bare-except
    print("Market is Overvalued!")
    sys.exit()


def str_perc(metric):
    metric = str(metric)

    if metric != '-':
        metric = metric.replace('%', '')
        metric = float(metric)
    else:
        metric = 0.0

    return metric


def trim(stock, insider_trans, price_to_earnings, price_to_fcf, price_to_earn_gwth):
    if price_to_earn_gwth > 2 or insider_trans < -20:
        return
    elif stock['Sector'] == 'Basic Materials':
        if price_to_earnings > 4.164 or price_to_fcf > 20.60:
            return
    elif stock['Sector'] == 'Communication Services':
        if price_to_earnings > 22.244 or price_to_fcf > 34.14:
            return
    elif stock['Sector'] == 'Consumer Cyclical':
        if price_to_earnings > 22.284 or price_to_fcf > 40.41:
            return
    elif stock['Sector'] == 'Consumer Defensive':
        if price_to_earnings > 23.264 or price_to_fcf > 50:
            return
    elif stock['Sector'] == 'Energy':
        if price_to_earnings > 6.214 or price_to_fcf > 8.27:
            return
    elif stock['Industry'] == 'Banks - Regional':
        roe = str_perc(p_fundamentals['ROE'])
        if price_to_earnings > 13.87 or roe < 20 or price_to_fcf > 10.77:
            return
    elif stock['Sector'] == 'Healthcare':
        if price_to_earnings > 25.09 or price_to_fcf > 30.21:
            return
    elif stock['Sector'] == 'Industrials':
        if price_to_earnings > 19.584 or price_to_fcf > 29.18:
            return
    elif stock['Sector'] == 'Real Estate':
        if price_to_earnings > 25.974 or price_to_fcf > 40.34:
            return
    elif stock['Sector'] == 'Technology':
        if price_to_earnings > 28.914 or price_to_fcf > 37.95:
            return
    elif stock['Sector'] == 'Utilities':
        if price_to_earnings > 3.494 or price_to_fcf > 50:
            return

    tickers.append(stock['Ticker'])


tickers = []
for stock in stock_list:
    TIME = 0
    GET_FUNDAMENTALS = True

    while GET_FUNDAMENTALS:
        try:
            p_fundamentals = finviz.get_stock(stock['Ticker'])
            GET_FUNDAMENTALS = False
        except:  # pylint: disable=bare-except
            TIME += 1
            time.sleep(TIME)

    insider_trans = str_perc(p_fundamentals['Insider Trans'])
    price_to_earnings = str_perc(p_fundamentals['P/E'])
    price_to_fcf = str_perc(p_fundamentals['P/FCF'])
    price_to_earn_gwth = str_perc(p_fundamentals['PEG'])

    trim(stock, insider_trans, price_to_earnings,
         price_to_fcf, price_to_earn_gwth)


# restrict to 10 stocks
if len(tickers) > 10:
    tickers = random.sample(tickers, k=10)
