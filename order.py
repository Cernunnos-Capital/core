"""Module submits buy order using Alpaca API"""
import calendar
import numpy as np
from datetime import datetime
from credentials import trading_client, BASE_URL
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from screen import tickers

# account info
account = trading_client.get_account()

# pro-rated capital
today = datetime.now()
last_day = f"{np.datetime64(today, 'M')}-{calendar.monthrange(today.year, today.month)[1]}"
today = np.datetime64(today, 'D')
last_day = np.datetime64(last_day)

TRADING_DAYS = np.busday_count(today, last_day)

# captial available per stock
if 'paper' in BASE_URL:
    cost_basis = 100 / float(len(tickers))
else:
    cost_basis = float(trading_client.get_account().cash) / \
        (TRADING_DAYS * float(len(tickers)))

for sym in tickers:
    # preparing orders
    market_order_data = MarketOrderRequest(
        symbol=sym,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
        notional=cost_basis
    )

    # submit buy order
    trading_client.submit_order(
        order_data=market_order_data
    )

    print('Bought', sym)
