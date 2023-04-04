"""Module submits buy order using Alpaca API"""
import os
from credentials import trading_client
from screen import tickers

# account info
account = trading_client.get_account()

# captial available per stock
cost_basis = float(os.environ['BUYING_POWER']) / float(len(tickers))

# submit buy order
for sym in tickers:
    trading_client.submit_order(
        symbol=sym,
        side='buy',
        notional=cost_basis,
    )
    print('Bought', sym)
