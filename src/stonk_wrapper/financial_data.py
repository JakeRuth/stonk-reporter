from . import api
from . import balance_sheet
from . import cashflow
from . import income_statement

class FinancialData:
    def __init__(self, stonk_ticker):
        api_wrapper = api.StonkApiWrapper(stonk_ticker, 'jkjk')
        self._income_statement = income_statement.IncomeStatement(api_wrapper.income_statement)

    @property
    def income_statement(self):
        return self._income_statement
