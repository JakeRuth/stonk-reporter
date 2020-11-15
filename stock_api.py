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

    def get_income_statement_json(self, ticker):
        url = self._get_api_url('INCOME_STATEMENT', ticker)
        return requests.get(url).json()
