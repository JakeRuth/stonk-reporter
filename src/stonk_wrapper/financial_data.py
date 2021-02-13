from . import api
from . import balance_sheet
from . import cashflow
from . import company_overview
from . import income_statement

class FinancialData:
    def __init__(self, stonk_ticker):
        api_wrapper = api.AlphaVantageStonkApiWrapper(stonk_ticker, 'jkjk')

        self._income_statement = income_statement.IncomeStatement(
            api_wrapper.get_income_statements()
        )
        self._balance_sheet = balance_sheet.BalanceSheet(
            api_wrapper.get_balance_sheets()
        )
        self._cashflow = cashflow.Cashflow(
            api_wrapper.get_cashflows()
        )
        self._company_overview = company_overview.CompanyOverview(
            api_wrapper.get_company_overview()
        )

    @property
    def income_statement(self):
        return self._income_statement

    @property
    def balance_sheet(self):
        return self._balance_sheet

    @property
    def company_overview(self):
        return self._company_overview

    @property
    def cashflow(self):
        return self._cashflow
