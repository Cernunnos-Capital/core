"""Module submits sell order using Alpaca API"""
import time
import finviz
from credentials import trading_client

# high valuation
COUNT = 0
SOLD = False
get_watchlist = trading_client.get_watchlist_by_name('Long')
for p in get_watchlist.assets:
    p_fundamentals = finviz.get_stock(p['symbol'])
    COUNT += 1

    if COUNT % 5 == 0:
        time.sleep(1)

    if ((p_fundamentals['PEG'] != '-') and (p_fundamentals['P/E'] != '-')
            and (p_fundamentals['P/S'] != '-') and (p_fundamentals['P/B'] != '-')):

        if ((float(p_fundamentals['PEG']) > 2) and (float(p_fundamentals['P/E']) > 30)
                and (float(p_fundamentals['P/S']) > 10) and (float(p_fundamentals['P/B']) > 5)):
            trading_client.submit_order(
                symbol=p['symbol'],
                side='sell',
                qty=p.qty
            )
            SOLD = True
            print('Sold', p['symbol'])
            trading_client.delete_from_watchlist(get_watchlist.id, p['symbol'])

if not SOLD:
    print('All positions are healthy!')
