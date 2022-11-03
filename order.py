"""Module submits buy order using Alpaca API"""
from credentials import trading_client
from screen import tickers

# cancel pending order
trading_client.cancel_all_orders()

# account info
account = trading_client.get_account()

# captial available per stock
# cost_basis = float(account.buying_power) / float(len(tickers))
cost_basis = 125 / float(len(tickers))  # test with 125$

# submit order
for t in tickers:
    trading_client.submit_order(
        symbol = t,
        side = 'buy',
        notional = cost_basis,
        type = 'market',
        time_in_force = 'day'
    )
    print("Bought", t)
