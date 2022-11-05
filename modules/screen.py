"""Module screens stocks from Finviz"""
import os
import sys
import random
from finviz.screener import Screener

# screening attributes
STOCK_SCREENER = os.environ['URL'].split(',')

# error handling for no result
try:
    stock_list = Screener(filters=STOCK_SCREENER)
except:  # pylint: disable=bare-except
    print("Better luck ")
    sys.exit()

tickers = []
for stock in stock_list:
    tickers.append(stock['Ticker'])

# restrict to 10 stocks
if len(tickers) > 10:
    tickers = random.sample(tickers, k=10)
