import requests


def do_search(bookstore_url, params):
    return requests.get(bookstore_url, params)
