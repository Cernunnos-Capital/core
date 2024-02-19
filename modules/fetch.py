"""Module fetches stock details"""
import sys
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
    raw_data = fetch_scrapper(
        f'https://finviz.com/quote.ashx?t={stock}')
    print(f'{stock} fetched')

    names = raw_data.findAll('td', class_='snapshot-td2 cursor-pointer w-[7%]')
    values = raw_data.findAll('td', class_='snapshot-td2 w-[8%]')

    data = {}
    for (name, value) in itertools.zip_longest(names, values):
        data[name.text] = value.text
    return data
