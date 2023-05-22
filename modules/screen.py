"""Module screens stocks from Finviz"""
import os
import random
from credentials import trading_client
from fetch import fetch_scrapper


SECTORS = [os.environ['URL_BM'], os.environ['URL_CS'], os.environ['URL_CC'], os.environ['URL_CD'],
           os.environ['URL_EN'], os.environ['URL_FN'], os.environ['URL_HL'], os.environ['URL_IN'],
           os.environ['URL_RE'], os.environ['URL_TC'], os.environ['URL_UT']]

tickers = []
for sec in SECTORS:
    links = fetch_scrapper(sec).findAll('a', class_='screener-link-primary')

    for a in links:
        stock_attr = trading_client.get_asset(a.text)
        if (stock_attr.tradable is True) and (stock_attr.fractionable is True):
            print(stock_attr.name)
            tickers.append(a.text)
        else:
            print(f'<---------- {a.text} not fractionable/tradable ---------->')

# buy existing underwater positions
if len(tickers) == 0:
    for p in trading_client.get_all_positions():
        loss = float(p.unrealized_plpc)

        if 0 > loss > -0.75:
            tickers.append(p.symbol)

# restrict to 10 stocks
if len(tickers) > 10:
    tickers = random.sample(tickers, k=10)
