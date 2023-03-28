"""Module submits sell order using Alpaca API"""
from credentials import trading_client
from fetch import fetch_fundamentals, str_perc

# high valuation
SOLD = False
for p in trading_client.list_positions():
    data = fetch_fundamentals(p)
    if data is None:
        continue

    PEG_RATIO = str_perc(data['PEG'])
    PS_RATIO = str_perc(data['P/S'])
    PB_RATIO = str_perc(data['P/B'])
    INSIDER_TRANS = str_perc(data['Insider Trans'])
    RSI = str_perc(data['RSI (14)'])

    STRIKE = 0
    if float(PEG_RATIO) > 2:
        STRIKE += 1
    if float(PS_RATIO) > 10:
        STRIKE += 1
    if float(PB_RATIO) > 5:
        STRIKE += 1
    if INSIDER_TRANS < -20:
        STRIKE += 1

    if STRIKE > 1 and RSI > 60:
        SOLD = True
        QTY = float(trading_client.get_position(p.symbol).qty)
        TRAILING_SELL_QTY = int(QTY)

        if TRAILING_SELL_QTY > 0:
            trading_client.submit_order(
                side='sell',
                symbol=p.symbol,
                type='trailing_stop',
                trail_percent='5',
                time_in_force='gtc',
                qty=TRAILING_SELL_QTY,
            )

        LIQUIDATION_SELL_QTY = QTY - TRAILING_SELL_QTY

        trading_client.submit_order(
            side='sell',
            symbol=p.symbol,
            qty=LIQUIDATION_SELL_QTY,
        )

        print('Sold', p.symbol)

if not SOLD:
    print('All positions are healthy!')
