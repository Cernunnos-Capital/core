"""Module gets stock data from finviz"""
from autoviz.helper_functions.request_functions import http_request_get

STOCK_URL = "https://finviz.com/quote.ashx"
NEWS_URL = "https://finviz.com/news.ashx"
CRYPTO_URL = "https://finviz.com/crypto_performance.ashx"
STOCK_PAGE = {}


def get_page(ticker):
    """Checks stock page"""
    global STOCK_PAGE

    if ticker not in STOCK_PAGE:
        STOCK_PAGE[ticker], _ = http_request_get(
            url=STOCK_URL, payload={"t": ticker}, parse=True
        )


def get_stock(ticker):
    """
    Returns a dictionary containing stock data.

    :param ticker: stock symbol
    :type ticker: str
    :return dict
    """

    get_page(ticker)
    page_parsed = STOCK_PAGE[ticker]

    title = page_parsed.cssselect('table[class="fullview-title"]')[0]
    keys = ["Company", "Sector", "Industry", "Country"]
    fields = [f.text_content() for f in title.cssselect('a[class="tab-link"]')]
    data = dict(zip(keys, fields))

    company_link = title.cssselect('a[class="tab-link"]')[0].attrib["href"]
    data["Website"] = company_link if company_link.startswith("http") else None

    all_rows = [
        row.xpath("td//text()")
        for row in page_parsed.cssselect('tr[class="table-dark-row"]')
    ]

    for row in all_rows:
        for column in range(0, 11, 2):
            if row[column] == "EPS next Y" and "EPS next Y" in data.keys():
                data["EPS growth next Y"] = row[column + 1]
                continue
            if row[column] == "Volatility":
                vols = row[column + 1].split()
                data["Volatility (Week)"] = vols[0]
                data["Volatility (Month)"] = vols[1]
                continue

            data[row[column]] = row[column + 1]

    return data
