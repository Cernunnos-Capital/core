"""Module submits sell order using Alpaca API"""
import os
from credentials import trading_client
from fetch import fetch_fundamentals, str_perc
from orders import trailing_sell, sell

# high valuation
COUNT = 0

for p in trading_client.get_all_positions():
    try:
        data = fetch_fundamentals(p.symbol)
    except:  # pylint: disable=bare-except
        continue

    EPS_GROWTH = str_perc(data['EPS next 5Y'])

    if EPS_GROWTH < os.environ['MAGIC_NUMBER']:
        print(p.symbol)
        COUNT += 1
        QTY = float(p.qty)
        TRAILING_SELL_QTY = int(QTY)
        LIQUIDATION_SELL_QTY = QTY - TRAILING_SELL_QTY

        try:
            if TRAILING_SELL_QTY >= 1:
                trailing_sell(p.symbol, TRAILING_SELL_QTY)
                print(
                    f'Trailing stop-loss set for {TRAILING_SELL_QTY} shares.')

            if LIQUIDATION_SELL_QTY > 10 ** -9:
                sell(p.symbol, LIQUIDATION_SELL_QTY)
                print(f'Sold {LIQUIDATION_SELL_QTY} shares.')
        except:  # pylint: disable=bare-except
            print('*********** PENDING SALE ***********')
        print()

print(COUNT)
