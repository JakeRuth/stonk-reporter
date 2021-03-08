from . import alpha_vantage_api
from . import best_api
from . import iex_cloud_api
from . import math_helper

from stonks.data_wrappers import balance_sheet
from stonks.data_wrappers import cashflow
from stonks.data_wrappers import company_overview
from stonks.data_wrappers import income_statement


class FinancialData:
    # TODO: Add reusable code to switch which api to use, right now you need to edit code here to do that
    def __init__(self, stonk_ticker, developer_mode=False):
        api_wrapper = best_api.BestApi(
            stonk_ticker,
            'poop',
            developer_mode=developer_mode,
        )

        self._income_statement = income_statement.IncomeStatement(
            api_wrapper.get_income_statements(),
            best_api.IncomeStatementDataKeys,
        )
        self._balance_sheet = balance_sheet.BalanceSheet(
            api_wrapper.get_balance_sheets(),
            best_api.BalanceSheetDataKeys,
        )
        self._cashflow = cashflow.Cashflow(
            api_wrapper.get_cashflows(),
            best_api.CashflowDataKeys,
        )
        self._company_overview = company_overview.CompanyOverview(
            api_wrapper.get_company_overview(),
            best_api.CompanyOverviewDataKeys,
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
