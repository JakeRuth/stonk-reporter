from . import api
from . import balance_sheet
from . import cashflow
from . import income_statement

class FinancialData:
    def __init__(self, stonk_ticker):
        api_wrapper = api.StonkApiWrapper(stonk_ticker, 'jkjk')

        income_statement_json = api_wrapper.income_statement
        self._income_statement_quarterly = income_statement.IncomeStatement(
            income_statement_json['quarterlyReports']
        )

    @property
    def income_statement_quarterly(self):
        return self._income_statement_quarterly
