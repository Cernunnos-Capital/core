"""Module rebalances the portfolio by buying underwater equities"""
import math
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from credentials import trading_client

for p in trading_client.get_all_positions():
    loss = float(p.unrealized_plpc)

    if 0 > loss > -0.75:
        cost_basis = math.ceil(abs(float(p.unrealized_pl)) / 10) * 40

        # preparing orders
        market_order_data = MarketOrderRequest(
            symbol=p.symbol,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
            notional=cost_basis
        )

        # submit buy order
        trading_client.submit_order(
            order_data=market_order_data
        )

        print('Bought', p.symbol)
