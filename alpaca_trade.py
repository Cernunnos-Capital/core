from finviz_screener import tickers
import alpaca_trade_api as TradingClient

BASE_URL = 'https://paper-api.alpaca.markets'
API_KEY = 'PKB9Y7E4C0J8LQHJGXOG'
SECRET_KEY = 'VsTkYNA2T6cWh1VKvHAPQnxkGGgqf516uLobEOSM'

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
    print("Bought", t[0])
