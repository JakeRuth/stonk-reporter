from . import api
from . import balance_sheet
from . import cashflow
from . import company_overview
from . import income_statement

class FinancialData:
    def __init__(self, stonk_ticker):
        api_wrapper = api.StonkApiWrapper(stonk_ticker, 'jkjk')

        income_statement_json = api_wrapper.income_statement
        self._income_statement_quarterly = income_statement.IncomeStatement(
            income_statement_json['quarterlyReports']
        )

        balance_sheet_json = api_wrapper.balance_sheet
        self._balance_sheet_quarterly = balance_sheet.BalanceSheet(
            balance_sheet_json['quarterlyReports']
        )

        company_overview_json = api_wrapper.company_overview
        self._company_overview = company_overview.CompanyOverview(company_overview_json)

    @property
    def income_statement_quarterly(self):
        return self._income_statement_quarterly

    @property
    def balance_sheet_quarterly(self):
        return self._balance_sheet_quarterly

    @property
    def company_overview(self):
        return self._company_overview
