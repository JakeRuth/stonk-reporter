import json
import requests


class StonkApiException(Exception):
    pass

# Little local file/caching utility for local devlopment to save $ on api calls
def get_cached_api_filename(stonk_ticker, api_call, api_name):
    return 'stonks/cached_api_calls/{}_{}_{}.json'.format(stonk_ticker, api_call, api_name).lower()

def save_api_response(stonk_ticker, api_call, api_name, res_json):
    filename = get_cached_api_filename(stonk_ticker, api_call, api_name)
    file = open(filename, 'w+')
    file.write(json.dumps(res_json))
    file.close()

def query_api_cache(stonk_ticker, api_call, api_name):
    filename = get_cached_api_filename(stonk_ticker, api_call, api_name)
    print('Looking in cache for {}'.format(filename))
    try:
        with open(filename) as json_file:
            print('Cache HIT for {}'.format(filename))
            return json.load(json_file)
    except FileNotFoundError:
        print('No cache found for {}'.format(filename))

class BaseStonkApiWrapper:
    def __init__(self, stonk_ticker, api_key, api_name):
        self.stonk_ticker = stonk_ticker
        self.api_key = api_key
        self.api_name = api_name

    def get_json(self, url, api_function):
        # Check cache for file first
        cached_response = query_api_cache(self.stonk_ticker, api_function, self.api_name)
        if cached_response:
            return cached_response

        response = requests.get(url).json()
        save_api_response(self.stonk_ticker, api_function, self.api_name, response)
        return response

    def get_income_statements(self):
        raise NotImplementedError()

    def get_cashflows(self):
        raise NotImplementedError()

    def get_balance_sheets(self):
        raise NotImplementedError()

    def get_company_overview(self):
        raise NotImplementedError()
