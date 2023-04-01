import datetime
import os
import time

import requests
from lxml import etree, html


def get_table(page_html: requests.Response, headers, rows=None, **kwargs):
    """ Private function used to return table data inside a list of dictionaries. """
    if isinstance(page_html, str):
        page_parsed = html.fromstring(page_html)
    else:
        page_parsed = html.fromstring(page_html.text)
    # When we call this method from Portfolio we don't fill the rows argument.
    # Conversely, we always fill the rows argument when we call this method from Screener.
    # Also, in the portfolio page, we don't need the last row - it's redundant.
    if rows is None:
        # We'll increment it later (-1) and use it to cut the last row
        rows = -2

    data_sets = []
    # Select the HTML of the rows and append each column text to a list
    all_rows = [
        column.xpath("td//text()")
        for column in page_parsed.cssselect('tr[valign="top"]')
    ]

    # If rows is different from -2, this function is called from Screener
    if rows != -2:
        for row_number, row_data in enumerate(all_rows, 1):
            data_sets.append(dict(zip(headers, row_data)))
            if row_number == rows:  # If we have reached the required end
                break
    else:
        # Zip each row values to the headers and append them to data_sets
        [data_sets.append(dict(zip(headers, row))) for row in all_rows]

    return data_sets


def get_total_rows(page_content):
    """ Returns the total number of rows(results). """

    total_element = page_content.cssselect('td[width="128"]')
    total_number = (
        etree.tostring(total_element[0]).decode(
            "utf-8").split("</b>")[1].split()[0]
    )

    try:
        return int(total_number)
    except ValueError:
        return 0


def get_page_urls(page_content, rows, url):
    """ Returns a list containing all of the page URL addresses. """

    total_pages = int(
        [i.text.split("/")[1]
         for i in page_content.cssselect('option[value="1"]')][0]
    )
    urls = []

    for page_number in range(1, total_pages + 1):
        sequence = 1 + (page_number - 1) * 20

        if sequence - 20 <= rows < sequence:
            break
        urls.append(url + f"&r={str(sequence)}")

    return urls
