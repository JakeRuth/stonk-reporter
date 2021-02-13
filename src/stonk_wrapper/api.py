import json
import requests

class StonkApiException(Exception):
    pass

class AlphaVantageStonkApiWrapper:
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
    def get_income_statements(self):
        res = self._get_json('INCOME_STATEMENT')
        income_statements = res.get('quarterlyReports')
        if not income_statements:
            raise StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return income_statements

    # https://www.alphavantage.co/documentation/#cash-flow
    def get_cashflows(self):
        res = self._get_json('CASH_FLOW')
        cashflows = res.get('quarterlyReports')
        if not cashflows:
            raise StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return cashflows

    # https://www.alphavantage.co/documentation/#balance-sheet
    def get_balance_sheets(self):
        res = self._get_json('BALANCE_SHEET')
        balance_sheets = res.get('quarterlyReports')
        if not balance_sheets:
            raise StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return balance_sheets

    # https://www.alphavantage.co/documentation/#company-overview
    def get_company_overview(self):
        res = self._get_json('OVERVIEW')
        if len(res.keys()) == 0:
            raise StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return res
