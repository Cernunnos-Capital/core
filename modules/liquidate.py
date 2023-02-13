"""Module submits sell order using Alpaca API"""
import time
import finviz
from credentials import trading_client

# high valuation
SOLD = False
get_watchlist = trading_client.get_watchlist_by_name('Long')
for p in get_watchlist.assets:
    p_fundamentals = finviz.get_stock(p['symbol'])

    try:
        PEG_RATIO = p_fundamentals['PEG']
        PS_RATIO = p_fundamentals['P/S']
        PB_RATIO = p_fundamentals['P/B']
    except:
        time.sleep(1)
        PEG_RATIO = p_fundamentals['PEG']
        PS_RATIO = p_fundamentals['P/S']
        PB_RATIO = p_fundamentals['P/B']

    STRIKE = 0
    if ((PEG_RATIO != '-') and (PS_RATIO != '-') and (PB_RATIO != '-')):
        if float(PEG_RATIO) > 2:
            STRIKE += 1
        if float(PS_RATIO) > 10:
            STRIKE += 1
        if float(PB_RATIO) > 5:
            STRIKE += 1

        if STRIKE > 1:
            SOLD = True
            trading_client.delete_from_watchlist(get_watchlist.id, p['symbol'])
            print('Sold', p['symbol'])

if not SOLD:
    print('All positions are healthy!')
