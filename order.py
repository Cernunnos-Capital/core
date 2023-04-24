"""Module submits buy order using Alpaca API"""
import calendar
from datetime import date
from credentials import trading_client
from screen import tickers

# account info
account = trading_client.get_account()

# pro-rated capital
today = date.today()
last_day = f'{today.year}-{today.month}-{calendar.monthrange(today.year, today.month)[1]}'

TRADING_DAYS = 0
for i in trading_client.get_calendar(start=today, end=last_day):
    TRADING_DAYS += 1

# captial available per stock
cost_basis = float(trading_client.get_account().cash) / \
    (TRADING_DAYS * float(len(tickers)))

# submit buy order
for sym in tickers:
    trading_client.submit_order(
        symbol=sym,
        side='buy',
        notional=cost_basis,
    )
    print('Bought', sym)
