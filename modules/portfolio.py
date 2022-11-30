"""Module generates portfolio information"""
import finviz
import pygal
from credentials import trading_client
from pygal.style import DefaultStyle

TOTAL_COST_BASIS = 0.0
TOTAL_MARKET_VALUE = 0.0
UNREALIZED_INTRADAY_PL = 0.0
TOTAL_PL_PC = 0.0
INTRADAY_PL = 0.0
TOP_10_HOLDINGS = ''
STOCK_NEWS = ''
CHART = ''
CASH_FLOW = 0.0


def get_holdings(TOTAL_COST_BASIS, TOTAL_MARKET_VALUE,
                 UNREALIZED_INTRADAY_PL, TOTAL_PL_PC, INTRADAY_PL, CASH_FLOW):
    holdings = []
    dividend_activity = []
    for position in trading_client.list_positions():
        TOTAL_COST_BASIS += float(position.cost_basis)
        TOTAL_MARKET_VALUE += float(position.market_value)
        UNREALIZED_INTRADAY_PL += float(position.unrealized_intraday_pl)

        holdings.append(
            [trading_client.get_asset(position.symbol).name, float(position.market_value),
             round(float(position.current_price), 2),
             round(float(position.avg_entry_price), 2),
             str(round(float(position.unrealized_intraday_plpc) * 100, 2)) + '%',
             str(round(float(position.unrealized_plpc) * 100, 2)) + '%', position.symbol])
        dividend_activity.append(position.symbol)

    for s in trading_client.get_activities(activity_types='DIV'):
        if s.symbol in dividend_activity:
            CASH_FLOW += float(s.net_amount)

    TOTAL_PL_PC = ((TOTAL_MARKET_VALUE - TOTAL_COST_BASIS) /
                   TOTAL_COST_BASIS) * 100

    TOTAL_PL_PC = str(round(TOTAL_PL_PC, 2)) + '%'
    TOTAL_COST_BASIS = round(TOTAL_COST_BASIS, 2)

    TOTAL_MARKET_VALUE += CASH_FLOW
    TOTAL_MARKET_VALUE = round(TOTAL_MARKET_VALUE, 2)

    INTRADAY_PL = (UNREALIZED_INTRADAY_PL / TOTAL_MARKET_VALUE) * 100
    INTRADAY_PL = str(round(INTRADAY_PL, 2)) + '%'

    return {'HOLDINGS': holdings,
            'TOTAL_COST_BASIS': TOTAL_COST_BASIS, 'TOTAL_MARKET_VALUE': TOTAL_MARKET_VALUE,
            'UNREALIZED_INTRADAY_PL': UNREALIZED_INTRADAY_PL, 'TOTAL_PL_PC': TOTAL_PL_PC,
            'INTRADAY_PL': INTRADAY_PL, 'CASH_FLOW': CASH_FLOW}


def sort_by(market_value):
    """Sorts by market value"""
    return market_value[1]


def populate_table(stocks, weight):
    return f"""<tr>
                    <th scope="row" class="text-start" style="color: #272643;">{ stocks[0] }</th>
                    <td>{ str(weight) + '%' }</td>
                    <td class="text-muted">${ stocks[3] }</td>
                    <td style="color: #2c698d;">{ stocks[4] }</td>
                    <td style="color: #2b0080;">{ stocks[5] }</td>
                </tr>"""


def display_news(stocks, n):
    return f"""<div class="col-md-6">
                    <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                        <div class="col p-4 d-flex flex-column position-static">
                            <strong class="d-inline-block mb-2" style="color: #2b0080;">{ n.source }</strong>
                            <h5 class="mb-0">{ n.headline }</h5>
                            <div class="mb-1 text-muted">{ stocks[6] }</div>
                            <a href="{ n.url }" target="_blank" class="stretched-link"></a>
                        </div>
                        <div class="col-auto d-none d-lg-block">
                            <img src="{ n.images[1]['url'] }" width="200" height="180">
                        </div>
                    </div>
                </div>"""


def get_portfolio_attributes(holdings, TOP_10_HOLDINGS, STOCK_NEWS):
    """Portfolio meta data"""
    sectors = {}
    COUNT = 0
    for stocks in sorted(holdings, key=sort_by, reverse=True):
        stock_data = finviz.get_stock(stocks[6])
        STOCK_SECTOR = str(stock_data['Sector'])
        weight = float(round((stocks[1] / TOTAL_MARKET_VALUE) * 100, 2))
        chart_data = {'value': weight, 'label': stocks[0]}

        if STOCK_SECTOR not in sectors:
            sectors[STOCK_SECTOR] = [chart_data]
        else:
            sectors[STOCK_SECTOR].append(chart_data)

        if COUNT < 10:
            TOP_10_HOLDINGS += populate_table(stocks, weight)

            for n in trading_client.get_news(stocks[6], limit=1):
                if len(n.images) > 0:
                    STOCK_NEWS += display_news(stocks, n)

        COUNT += 1

    return {'SECTORS': sectors, 'TOP_10_HOLDINGS': TOP_10_HOLDINGS, 'STOCK_NEWS': STOCK_NEWS}


def create_pie_chart(sectors):
    """Renders pie chart using pygal"""
    DefaultStyle.background = 'transparent'
    pie_chart = pygal.Pie(truncate_legend=25,
                          style=DefaultStyle, legend_at_bottom=True, legend_box_size=20)

    for s in sectors:
        pie_chart.add(s, sectors[s])
    return pie_chart.render_data_uri()


"""Execution"""
PORTFOLIO = get_holdings(TOTAL_COST_BASIS, TOTAL_MARKET_VALUE,
                         UNREALIZED_INTRADAY_PL, TOTAL_PL_PC, INTRADAY_PL, CASH_FLOW)

TOTAL_MARKET_VALUE = PORTFOLIO['TOTAL_MARKET_VALUE']
DISPLAY_PORTFOLIO_DATA = get_portfolio_attributes(
    PORTFOLIO['HOLDINGS'], TOP_10_HOLDINGS, STOCK_NEWS)

CHART = create_pie_chart(DISPLAY_PORTFOLIO_DATA['SECTORS'])

# TOTAL_COST_BASIS = PORTFOLIO['TOTAL_COST_BASIS']
UNREALIZED_INTRADAY_PL = PORTFOLIO['UNREALIZED_INTRADAY_PL']
TOTAL_PL_PC = PORTFOLIO['TOTAL_PL_PC']
INTRADAY_PL = PORTFOLIO['INTRADAY_PL']
CASH_FLOW = PORTFOLIO['CASH_FLOW']
TOP_10_HOLDINGS = DISPLAY_PORTFOLIO_DATA['TOP_10_HOLDINGS']
STOCK_NEWS = DISPLAY_PORTFOLIO_DATA['STOCK_NEWS']
