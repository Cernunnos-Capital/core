import os
import alpaca_trade_api as TradingClient
from finviz_screener import tickers

BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

trading_client = TradingClient.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# cancel pending order
trading_client.cancel_all_orders()

# account info
account = trading_client.get_account()

cost_basis = float(account.buying_power) / float(len(tickers))

for t in tickers:
    trading_client.submit_order(
        symbol = t[0],
        side = 'buy',
        notional = cost_basis,
        type = 'market',
        time_in_force = 'day'
    )
    print("Bought using env secrets", t[0])
