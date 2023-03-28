"""Module screens stocks from Finviz"""
import os
import sys
import random
import finviz
from finviz.screener import Screener
from fetch import fetch_fundamentals, str_perc
from credentials import trading_client

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


def trim(data, p_e, p_fcf):
    """Trim data as per the sector"""
    industry_pe = ratios[data['Sector']][0]
    industry_pfcf = ratios[data['Sector']][1]

    if p_e > industry_pe or p_fcf > industry_pfcf:
        return

    tickers.append(data['Ticker'])


tickers = []
for stock in stock_list:
    if trading_client.get_asset(stock['Ticker']).fractionable is True:
        stock_detail = fetch_fundamentals(stock)

        insider_trans = str_perc(stock_detail['Insider Trans'])
        price_to_earn_gwth = str_perc(stock_detail['PEG'])

        if price_to_earn_gwth > 2 or insider_trans < -20:
            continue

        return_on_equity = str_perc(stock_detail['ROE'])
        if stock_detail['Industry'] == 'Banks - Regional' and return_on_equity < 20:
            continue

        price_to_earnings = str_perc(stock_detail['P/E'])
        price_to_fcf = str_perc(stock_detail['P/FCF'])
        trim(stock, price_to_earnings, price_to_fcf)


# restrict to 10 stocks
if len(tickers) > 10:
    tickers = random.sample(tickers, k=10)
