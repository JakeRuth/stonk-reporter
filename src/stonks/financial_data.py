from . import alpha_vantage_api
from . import math_helper

from stonks.data_wrappers import balance_sheet
from stonks.data_wrappers import cashflow
from stonks.data_wrappers import company_overview
from stonks.data_wrappers import income_statement

class FinancialData:
    def __init__(self, stonk_ticker, developer_mode=False):
        api_wrapper = alpha_vantage_api.AlphaVantageApi(
            stonk_ticker,
            'jkjk',
            developer_mode=developer_mode,
        )

        self._income_statement = income_statement.IncomeStatement(
            api_wrapper.get_income_statements(),
            alpha_vantage_api.IncomeStatementDataKeys
        )
        self._balance_sheet = balance_sheet.BalanceSheet(
            api_wrapper.get_balance_sheets(),
            alpha_vantage_api.BalanceSheetDataKeys
        )
        self._cashflow = cashflow.Cashflow(
            api_wrapper.get_cashflows(),
            alpha_vantage_api.CashflowDataKeys
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

    @property
    def price_to_fcf(self):
        return math_helper.simple_ratio(
            self.company_overview.market_cap,
            self.cashflow.free_cash_flow_ttm,
        )
