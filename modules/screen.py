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
            print(f'Trying {TIME} sec.')

    eps_growth = str(p_fundamentals['EPS next 5Y'])
    if stock['Industry'] == 'Banks - Regional':
        if eps_growth == '-':
            continue

        eps_growth = eps_growth.replace('%', '')
        eps_growth = float(eps_growth)

        if eps_growth < 10:
            continue

    if stock['Sector'] == 'Energy':
        if eps_growth == '-':
            continue

        eps_growth = eps_growth.replace('%', '')
        eps_growth = float(eps_growth)

        if eps_growth < -1:
            continue

    insider_trans = str(p_fundamentals['Insider Trans'])

    if insider_trans != '-':
        insider_trans = insider_trans.replace('%', '')
        insider_trans = float(insider_trans)

    if insider_trans == '-' or insider_trans > -20.00:
        tickers.append(stock['Ticker'])

# restrict to 10 stocks
if len(tickers) > 10:
    tickers = random.sample(tickers, k=10)
