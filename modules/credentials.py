"""Module connects Alpaca API"""
import os
# import sys
from alpaca.trading.client import TradingClient

# credentials
BASE_URL = os.environ['ENDPOINT']
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

# alpaca API
if 'paper' in BASE_URL:
    trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
else:
    trading_client = TradingClient(API_KEY, SECRET_KEY, paper=False)

# # check market hours
# if not trading_client.get_clock().is_open:
#     print('Market is Closed!')
#     sys.exit()
