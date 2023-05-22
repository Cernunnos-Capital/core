"""Module submits sell order using Alpaca API"""
from credentials import trading_client
from fetch import fetch_fundamentals, str_perc
from orders import trailing_sell, sell

# high valuation
SOLD = False
for p in trading_client.get_all_positions():
    data = fetch_fundamentals(p.symbol)
    if data is None:
        continue

    # PE_RATIO = str_perc(data['P/E'])
    FWD_PE_RATIO = str_perc(data['Forward P/E'])
    PEG_RATIO = str_perc(data['PEG'])
    PS_RATIO = str_perc(data['P/S'])
    PB_RATIO = str_perc(data['P/B'])
    INSIDER_TRANS = str_perc(data['Insider Trans'])
    TARGET_PRICE = str_perc(data['Target Price'])
    CURRENT_PRICE = str_perc(data['Price'])
    RSI = str_perc(data['RSI (14)'])

    STRIKE = 0
    if PEG_RATIO > 2:
        STRIKE += 1
    if PS_RATIO > 10:
        STRIKE += 1
    if PB_RATIO > 5:
        STRIKE += 1
    if INSIDER_TRANS < -20:
        STRIKE += 1

    if (FWD_PE_RATIO > PE_RATIO) and (STRIKE > 1) and (RSI > 60) and (CURRENT_PRICE > TARGET_PRICE):
        SOLD = True
        QTY = float(p.qty)
        TRAILING_SELL_QTY = int(QTY)

        try:
            if TRAILING_SELL_QTY > 0:
                trailing_sell(p.symbol, TRAILING_SELL_QTY)

            LIQUIDATION_SELL_QTY = QTY - TRAILING_SELL_QTY

            sell(p.symbol, LIQUIDATION_SELL_QTY)
            print('Sold', p.symbol)
        except:  # pylint: disable=bare-except
            print(p.symbol, ': Sell order already placed!')


if not SOLD:
    print('All positions are healthy!')
