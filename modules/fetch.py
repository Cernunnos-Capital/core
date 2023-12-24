"""Module fetches stock details"""
import itertools
import time
import requests
from bs4 import BeautifulSoup


def str_perc(metric):
    """Convert data to operatable ratios"""
    metric = str(metric)

    if metric != '-':
        metric = metric.replace('%', '')
        metric = float(metric)
    else:
        metric = 0.0

    return metric


def fetch_scrapper(endpoint):
    """Scrapes finviz"""
    endpoint_request = requests.get(endpoint, headers={'User-Agent': 'My User Agent 1.0'},
                                    timeout=10)

    # check status code
    if endpoint_request.status_code == 200:
        # Parsing the HTML
        html_parser = BeautifulSoup(endpoint_request.content, 'html.parser')
        return html_parser

    return None


def fetch_fundamentals(stock):
    """Returns ticker fundamentals"""
    trial = 1
    while trial < 4:
        try:
            raw_data = fetch_scrapper(
                f'https://finviz.com/quote.ashx?t={stock}')
            print(f'{stock} fetched')
            break
        except AttributeError:
            print(f'<------------- {stock} not fetched ------------->')
            time.sleep(trial)

        trial += 1

    names = raw_data.findAll('td', class_='snapshot-td2-cp')
    values = raw_data.findAll('td', class_='snapshot-td2')

    data = {}
    for (name, value) in itertools.zip_longest(names, values):
        data[name.text] = value.text
    return data
