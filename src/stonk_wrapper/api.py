import json
import requests

class StonkApiException(Exception):
    pass

class StonkApiWrapper:
    def __init__(self, stonk_ticker, api_key):
        self.api_key = api_key
        self.stonk_ticker = stonk_ticker

    def _get_json(self, api_function):
        url = 'https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(
            api_function,
            self.stonk_ticker,
            self.api_key,
        )
        response = requests.get(url).json()
        # api responds with a single "note" if you go over the usage limit for their api
        # their free tier is 5 requests per minute and 500 a day (ref: https://www.alphavantage.co/premium/)
        over_api_request_throttle_limit = response.get('Note')
        if bool(over_api_request_throttle_limit):
            raise StonkApiException('Api request limit reached :( we are allowed 5 requests per minutes, and 500 daily')

        return response

    # https://www.alphavantage.co/documentation/#income-statement
    @property
    def income_statement(self):
        # if self.stonk_ticker == 'APHA':
        #     with open('stonk_wrapper/cached_api_calls/apha_income.json') as json_file:
        #         print('Getting static income statement for APHA from cache')
        #         return json.load(json_file)

        return self._get_json('INCOME_STATEMENT')

    # https://www.alphavantage.co/documentation/#cash-flow
    @property
    def cashflow(self):
        return self._get_json('CASH_FLOW')

    # https://www.alphavantage.co/documentation/#balance-sheet
    @property
    def balance_sheet(self):
        # if self.stonk_ticker == 'APHA':
        #     with open('stonk_wrapper/cached_api_calls/apha_balance_sheet.json') as json_file:
        #         print('Getting static income statement for APHA from cache')
        #         return json.load(json_file)

        return self._get_json('BALANCE_SHEET')

    # https://www.alphavantage.co/documentation/#company-overview
    @property
    def company_overview(self):
        # if self.stonk_ticker == 'APHA':
        #     with open('stonk_wrapper/cached_api_calls/apha_overview.json') as json_file:
        #         print('Getting static overview for APHA from cache')
        #         return json.load(json_file)

        return self._get_json('OVERVIEW')
