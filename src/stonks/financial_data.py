from . import iex_cloud_api
from . import math_helper

from stonks.data_wrappers import balance_sheet
from stonks.data_wrappers import cashflow
from stonks.data_wrappers import iex_company_overview
from stonks.data_wrappers import income_statement

class FinancialData:
    def __init__(self, stonk_ticker, developer_mode=False):
        api_wrapper = iex_cloud_api.IexCloudApi(
            stonk_ticker,
            'nooo',
            developer_mode=developer_mode,
        )

        self._income_statement = income_statement.IncomeStatement(
            api_wrapper.get_income_statements(),
            iex_cloud_api.IncomeStatementDataKeys,
        )
        self._balance_sheet = balance_sheet.BalanceSheet(
            api_wrapper.get_balance_sheets(),
            iex_cloud_api.BalanceSheetDataKeys,
        )
        self._cashflow = cashflow.Cashflow(
            api_wrapper.get_cashflows(),
            iex_cloud_api.CashflowDataKeys,
        )
        self._company_overview = iex_company_overview.IexCompanyOverview(
            api_wrapper.get_company_overview(),
            self._income_statement,
            self._balance_sheet,
            self._cashflow
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
