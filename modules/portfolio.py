from credentials import trading_client
from datetime import date

total_cost_basis = 0.0
total_market_value = 0.0
unrealized_intraday_pl = 0.0
stocks = []
for p in trading_client.list_positions():
    stocks.append(trading_client.get_asset(p.symbol).name)
    total_cost_basis += float(p.cost_basis)
    total_market_value += float(p.market_value)
    unrealized_intraday_pl += float(p.unrealized_intraday_pl)

total_pl = ((total_market_value - total_cost_basis) /
            total_cost_basis) * 100
total_pl = str(round(total_pl, 2)) + '%'
total_cost_basis = round(total_cost_basis, 2)
total_market_value = round(total_market_value, 2)

intraday_pl = (unrealized_intraday_pl / total_market_value) * 100
intraday_pl = round(intraday_pl, 2)

with open('README.md', 'w', newline='', encoding='utf8') as f:
    f.write('# autoinvest\n')
    f.write('Automated Investing with Dynamic Rebalancing\n')

    f.write('## Portfolio\n')
    f.write('```\n')
    f.write('Cost Basis:         $' + str(total_cost_basis) + '\n')
    f.write('Market Value:       $' + str(total_cost_basis) + '\n')
    f.write('Unrealized gain:    ' + str(total_pl) + '\n')
    f.write('```\n')

    f.write('>*last updated ' + date.today().strftime("%B %d, %Y") + '*\n')

    f.write('## Current Holdings\n')
    for s in stocks:
        f.write('- ' + s + '\n')

    f.close()
