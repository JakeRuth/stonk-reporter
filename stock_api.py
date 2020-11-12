import requests

def _get_api_url(function, ticker):
    return 'https://www.alphavantage.co/query?function={}&symbol={}&apikey=LD4DVO1UE512YL6K'.format(
        function,
        ticker,
    )

def get_income_statement_json(ticker):
    url = _get_api_url('INCOME_STATEMENT', ticker)
    return requests.get(url).json()
