"""Module rebalances the portfolio by buying underwater equities"""
import math
from credentials import trading_client

for p in trading_client.list_positions():
    loss = float(p.unrealized_plpc)

    if loss < 0 and loss > -0.75:
        cost_basis = math.ceil(abs(float(p.unrealized_pl)) / 10) * 40

        trading_client.submit_order(
            symbol=p.symbol,
            side='buy',
            notional=cost_basis,
        )
        print('Bought', p.symbol)
