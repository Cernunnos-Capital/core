from credentials import trading_client
import finviz
import time
import pygal

holdings = []
total_cost_basis = 0.0
total_market_value = 0.0
unrealized_intraday_pl = 0.0
COUNT = 0
for position in trading_client.list_positions():
    stock_data = finviz.get_stock(position.symbol)

    total_cost_basis += float(position.cost_basis)
    total_market_value += float(position.market_value)
    unrealized_intraday_pl += float(position.unrealized_intraday_pl)

    holdings.append(
        [stock_data['Company'], float(position.market_value),
         round(float(position.current_price), 2),
         round(float(position.avg_entry_price), 2),
         str(round(float(position.unrealized_intraday_plpc) * 100, 2)) + '%',
         str(round(float(position.unrealized_plpc) * 100, 2)) + '%', position.symbol])

    COUNT += 1

    if COUNT % 5 == 0:
        time.sleep(1)

total_pl_pc = ((total_market_value - total_cost_basis) /
               total_cost_basis) * 100

total_pl_pc = str(round(total_pl_pc, 2)) + '%'
total_cost_basis = round(total_cost_basis, 2)
total_market_value = round(total_market_value, 2)

intraday_pl = (unrealized_intraday_pl / total_market_value) * 100
intraday_pl = str(round(intraday_pl, 2)) + '%'


def sort_by_market_value(s):
    return s[1]


data = ""
count = 0
sectors = {}
for stocks in sorted(holdings, key=sort_by_market_value, reverse=True):
    stock_data = finviz.get_stock(stocks[6])
    stock_sector = str(stock_data['Sector'])
    stock_industry = str(stock_data['Industry'])
    weight = float(round((stocks[1] / total_market_value) * 100, 2))
    chart_data = {'value': weight, 'label': stocks[0]}

    if stock_sector not in sectors.keys():
        sectors[stock_sector] = [chart_data]
    else:
        sectors[stock_sector].append(chart_data)

    if count < 10:
        data += f"""<tr>
                <th scope="row" class="text-start" style="color: #272643;">{ stocks[0] }</th>
                <td>{ str(weight) + '%' }</td>
                <td class="text-muted">${ stocks[3] }</td>
                <td style="color: #2c698d;">{ stocks[4] }</td>
                <td style="color: #2b0080;">{ stocks[5] }</td>
                </tr>"""

    count += 1

pie_chart = pygal.Pie(truncate_legend=25)
pie_chart.title = 'Portfolio slices (in %)'

for s in sectors:
    pie_chart.add(s, sectors[s])

chart = pie_chart.render_data_uri()
