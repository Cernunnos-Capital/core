"""Module fetches stock details"""
import itertools
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


def fetch_fundamentals(stock):
    """Returns ticker fundamentals"""
    endpoint = f'https://finviz.com/quote.ashx?t={stock}'

    endpoint_request = requests.get(endpoint, headers={'User-Agent': 'My User Agent 1.0'},
                                    timeout=10)

    data = {}
    # check status code
    if endpoint_request.status_code == 200:
        # Parsing the HTML
        html_parser = BeautifulSoup(endpoint_request.content, 'html.parser')
        names = html_parser.findAll('td', class_='snapshot-td2-cp')
        values = html_parser.findAll('td', class_='snapshot-td2')

        for (name, value) in itertools.zip_longest(names, values):
            data[name.text] = value.text
    return data
