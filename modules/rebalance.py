"""Module rebalances the portfolio by buying underwater equities"""
import math
from orders import buy
from credentials import trading_client

for p in trading_client.get_all_positions():
    loss = float(p.unrealized_plpc)

    if 0 > loss > -0.75:
        cost_basis = math.ceil(abs(float(p.unrealized_pl)) / 10) * 40
        buy(p.symbol, cost_basis)
