import requests

class StockApiWrapper:
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_api_url(self, function, ticker):
        return 'https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(
            function,
            ticker,
            self.api_key,
        )

    # https://www.alphavantage.co/documentation/#income-statement
    def get_income_statement_json(self, ticker):
        url = self._get_api_url('INCOME_STATEMENT', ticker)
        return requests.get(url).json()

    # https://www.alphavantage.co/documentation/#cash-flow
    def get_cashflow_json(self, ticker):
        url = self._get_api_url('CASH_FLOW', ticker)
        return requests.get(url).json()

    # https://www.alphavantage.co/documentation/#cash-flow
    def get_balance_json(self, ticker):
        url = self._get_api_url('CASH_FLOW', ticker)
        return requests.get(url).json()

    # https://www.alphavantage.co/documentation/#company-overview
    def get_company_overview_json(self, ticker):
        url = self._get_api_url('OVERVIEW', ticker)
        return requests.get(url).json()
