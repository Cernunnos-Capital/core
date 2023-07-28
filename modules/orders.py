"""Module submits various orders using Alpaca API"""
from alpaca.trading.requests import MarketOrderRequest, TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from credentials import trading_client


def final(order_data):
    """Submits order using prepared data"""
    trading_client.submit_order(
        order_data=order_data
    )


def buy(sym, cost_basis):
    """Preparing market buy orders"""
    market_buy_order_data = MarketOrderRequest(
        symbol=sym,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY,
        notional=cost_basis
    )

    final(market_buy_order_data)
    print('Bought', sym)


def trailing_sell(sym, quantity):
    """Preparing trailing sell orders"""
    trailing_stop_order_data = TrailingStopOrderRequest(
        symbol=sym,
        qty=quantity,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC,
        trail_percent='5'
    )

    final(trailing_stop_order_data)


def sell(sym, quantity):
    """Preparing market sell orders"""
    market_sell_order_data = MarketOrderRequest(
        symbol=sym,
        side=OrderSide.SELL,
        qty=quantity
    )

    final(market_sell_order_data)
