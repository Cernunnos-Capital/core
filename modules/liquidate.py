"""Module submits sell order using Alpaca API"""
from credentials import trading_client
from fetch import fetch_fundamentals

# high valuation
SOLD = False
get_watchlist = trading_client.get_watchlist_by_name('Long')
for p in get_watchlist.assets:
    data = fetch_fundamentals(p)
    if data is None:
        continue

    PEG_RATIO = data['PEG']
    PS_RATIO = data['P/S']
    PB_RATIO = data['P/B']

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
