"""Module screens stocks from Finviz"""
import os
import sys
import random
import time
import finviz
from finviz.screener import Screener

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
    """Convert data to operatable ratios"""
    metric = str(metric)

    if metric != '-':
        metric = metric.replace('%', '')
        metric = float(metric)
    else:
        metric = 0.0

    return metric


def trim(data, ins_trn, pe_ratio, pfcf, peg):
    """Trim data as per the sector"""
    if peg > 2 or ins_trn < -20:
        return
    if data['Sector'] == 'Basic Materials':
        if pe_ratio > 4.164 or pfcf > 20.60:
            return
    if data['Sector'] == 'Communication Services':
        if pe_ratio > 22.244 or pfcf > 34.14:
            return
    if data['Sector'] == 'Consumer Cyclical':
        if pe_ratio > 22.284 or pfcf > 40.41:
            return
    if data['Sector'] == 'Consumer Defensive':
        if pe_ratio > 23.264 or pfcf > 50:
            return
    if data['Sector'] == 'Energy':
        if pe_ratio > 6.214 or pfcf > 8.27:
            return
    if data['Industry'] == 'Banks - Regional':
        roe = str_perc(p_fundamentals['ROE'])
        if pe_ratio > 13.87 or roe < 20 or pfcf > 10.77:
            return
    if data['Sector'] == 'Healthcare':
        if pe_ratio > 25.09 or pfcf > 30.21:
            return
    if data['Sector'] == 'Industrials':
        if pe_ratio > 19.584 or pfcf > 29.18:
            return
    if data['Sector'] == 'Real Estate':
        if pe_ratio > 25.974 or pfcf > 40.34:
            return
    if data['Sector'] == 'Technology':
        if pe_ratio > 28.914 or pfcf > 37.95:
            return
    if data['Sector'] == 'Utilities':
        if pe_ratio > 3.494 or pfcf > 50:
            return

    tickers.append(data['Ticker'])


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
