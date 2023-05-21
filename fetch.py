"""Module fetches stock details from autoviz"""
import requests
import bs4 as BeautifulSoup
import itertools

ratios = {'Basic Materials': [5, 22.5],
          'Communication Services': [22.5, 35],
          'Consumer Cyclical': [22.5, 35],
          'Consumer Defensive': [22.5, 35],
          'Energy': [7, 8.5],
          'Healthcare': [25, 30],
          'Industrials': [20, 30],
          'Real Estate': [25, 35],
          'Technology': [30, 40],
          'Utilities': [5, 15],
          'Financial': [15, 10]
          }


def fetch_fundamentals(stock):
    """Returns ticker fundamentals"""
    BASE_URL = f'https://finviz.com/quote.ashx?t={stock}'

    r = requests.get(BASE_URL, headers={'User-Agent': 'My User Agent 1.0'})

    data = {}
    # check status code
    if r.status_code == 200:
        # Parsing the HTML
        html_parser = BeautifulSoup(r.content, 'html.parser')
        key = html_parser.findAll('td', class_='snapshot-td2-cp')
        value = html_parser.findAll('td', class_='snapshot-td2')

        for (d, v) in itertools.zip_longest(key, value):
            data[d.text] = v.text
    return data


def str_perc(metric):
    """Convert data to operatable ratios"""
    metric = str(metric)

    if metric != '-':
        metric = metric.replace('%', '')
        metric = float(metric)
    else:
        metric = 0.0

    return metric
