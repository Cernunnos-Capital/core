import os
from finviz.screener import Screener
import random

# screening attributes 
STOCK_SCREENER = os.environ['STOCK_SCREENER']

# error handling for no result
try:
    stock_list = Screener(filters=STOCK_SCREENER)
except:
    print("Better luck next time!")
    exit()

tickers = []
for stock in stock_list:
    tickers.append([stock['Ticker'], stock['Price']])

# restrict to 10 stocks 
if (len(tickers) > 10):
    tickers = random.sample(tickers, k=10)