from finviz.screener import Screener

# screening attributes 
STOCK_SCREENER = ['cap_midover', 'fa_debteq_low', 'fa_eps5years_pos', 'fa_estltgrowth_pos', 'fa_ltdebteq_u0.5',
                    'fa_opermargin_pos', 'fa_pe_u25', 'fa_pfcf_u20', 'fa_roa_pos', 'fa_roe_pos', 'fa_roi_o10', 
                    'fa_sales5years_pos', 'sh_instown_o60', 'ta_sma200_pb']

try:
    stock_list = Screener(filters=STOCK_SCREENER)
except:
  print("Better luck next time!")
  exit()

tickers = []
for stock in stock_list:
    tickers.append([stock['Ticker'], stock['Price']])