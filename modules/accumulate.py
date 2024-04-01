"""Module allocates pro-rated capital"""
import os
import calendar
from datetime import datetime
import sys
import numpy as np
from credentials import trading_client, BASE_URL
from screen import tickers
from orders import buy

# account info - cash in hand
cash_in_account = float(trading_client.get_account().cash)

# trading days within a month
today = datetime.now()
last_day = f"{np.datetime64(today, 'M')}-{calendar.monthrange(today.year, today.month)[1]}"
today = np.datetime64(today, 'D')
last_day = np.datetime64(last_day)

# inclusive
TRADING_DAYS = 1 + np.busday_count(today, last_day)

# captial available per stock
if 'paper' in BASE_URL:
    cost_basis = 100 / float(len(tickers))
else:
    cost_basis = cash_in_account / (TRADING_DAYS * float(len(tickers)))

cost_basis = round(cost_basis, 2)

if cash_in_account < os.environ['MAGIC_NUMBER']:
    print('Insufficient funds.')
    sys.exit()

for sym in tickers:
    buy(sym, cost_basis)
