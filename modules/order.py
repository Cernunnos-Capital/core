"""Module submits buy order using Alpaca API"""
import os
from credentials import trading_client
from screen import tickers

# cancel all pending orders
trading_client.cancel_all_orders()

# account info
account = trading_client.get_account()

# captial available per stock
cost_basis = float(os.environ['BUYING_POWER']) / float(len(tickers))

# create watchlists
watchlists = ['Long']
for w in watchlists:
    try:
        trading_client.create_watchlist(w)
    except:  # pylint: disable=bare-except
        pass


def submit_order_and_watchlist(watchlist_name):
    """Submit buy order and add to watchlist"""
    for sym in tickers:
        trading_client.submit_order(
            symbol=sym,
            side='buy',
            notional=cost_basis,
        )
        print('Bought', sym)

        watchlist_id = trading_client.get_watchlist_by_name(watchlist_name).id
        try:
            trading_client.add_to_watchlist(watchlist_id, sym)
        except:  # pylint: disable=bare-except
            pass


submit_order_and_watchlist('Long')
