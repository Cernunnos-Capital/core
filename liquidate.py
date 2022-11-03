"""Module submits sell order using Alpaca API"""
import finviz
from credentials import trading_client

# high valuation
for p in trading_client.list_positions():
    if ((finviz.get_stock(p.symbol)['PEG'] != '-') and
        (finviz.get_stock(p.symbol)['P/E'] != '-') and
        (finviz.get_stock(p.symbol)['P/S'] != '-') and
        (finviz.get_stock(p.symbol)['P/B'] != '-')):

        if ((float(finviz.get_stock(p.symbol)['PEG']) > 2) and
            (float(finviz.get_stock(p.symbol)['P/E']) > 30) and
            (float(finviz.get_stock(p.symbol)['P/S']) > 10) and
            (float(finviz.get_stock(p.symbol)['P/B']) > 5)):
            trading_client.submit_order(
                symbol = p.symbol,
                side = 'sell',
                qty = p.qty
            )
