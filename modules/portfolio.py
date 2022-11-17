from credentials import trading_client

holdings = []
total_cost_basis = 0.0
total_market_value = 0.0
unrealized_intraday_pl = 0.0
for position in trading_client.list_positions():
    total_cost_basis += float(position.cost_basis)
    total_market_value += float(position.market_value)
    unrealized_intraday_pl += float(position.unrealized_intraday_pl)

    holdings.append(
        [trading_client.get_asset(position.symbol).name,
         float(position.market_value),
         round(float(position.current_price), 2),
         round(float(position.avg_entry_price), 2),
         str(round(float(position.unrealized_intraday_plpc) * 100, 2)) + '%',
         str(round(float(position.unrealized_plpc) * 100, 2)) + '%'])

total_pl = ((total_market_value - total_cost_basis) / total_cost_basis) * 100

total_pl = str(round(total_pl, 2)) + '%'
total_cost_basis = round(total_cost_basis, 2)
total_market_value = round(total_market_value, 2)

intraday_pl = (unrealized_intraday_pl / total_market_value) * 100
intraday_pl = str(round(intraday_pl, 2)) + '%'


def sort_by_market_value(s):
    return s[1]


data = ""
count = 0
for stocks in sorted(holdings, key=sort_by_market_value, reverse=True):
    data += f"""<tr>
              <th scope="row" class="text-start" style="color: #272643;">{ stocks[0] }</th>
              <td>{ str(round((stocks[1] / total_market_value) * 100, 2)) + '%' }</td>
              <td class="text-muted">${ stocks[3] }</td>
              <td style="color: #2c698d;">{ stocks[4] }</td>
              <td style="color: #2b0080;">{ stocks[5] }</td>
            </tr>"""

    count += 1
    if count == 10:
        break
