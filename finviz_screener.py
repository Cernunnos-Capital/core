from finviz.screener import Screener
import random

# screening attributes 
STOCK_SCREENER = ['cap_midover', 'fa_debteq_u0.5', 'fa_eps5years_pos', 'fa_ltdebteq_u0.5', 
                    'fa_netmargin_pos', 'fa_opermargin_pos', 'fa_pe_low', 'fa_pfcf_u20', 
                    'fa_roa_pos', 'fa_roe_pos', 'fa_roi_o15', 'fa_sales5years_pos', 'sh_avgvol_o400', 
                    'sh_instown_o50', 'ta_rsi_nob60', 'ta_sma200_pb', 'targetprice_a20']

# error handling for no result
try:
    stock_list = Screener(filters=STOCK_SCREENER)
except:
    print("Better luck next time!")
    exit()

tickers = []
for stock in stock_list:
    tickers.append([stock['Ticker'], stock['Price']])

# restrict to 10 stocks 
if (len(tickers) > 10):
    tickers = random.sample(tickers, k=10)