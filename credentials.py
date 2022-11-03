import os
import alpaca_trade_api as TradingClient

# credentials
BASE_URL = os.environ['ENDPOINT']
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

# alpaca API
trading_client = TradingClient.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# cancel all pending orders
trading_client.cancel_all_orders()