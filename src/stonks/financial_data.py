from . import alpha_vantage_api
from . import iex_cloud_api
from . import math_helper

from stonks.data_wrappers import balance_sheet
from stonks.data_wrappers import cashflow
from stonks.data_wrappers import company_overview
from stonks.data_wrappers import iex_company_overview
from stonks.data_wrappers import income_statement


class FinancialData:
    def __init__(self, stonk_ticker, developer_mode=False):
        use_av = False
        api = None
        if use_av:
            api = alpha_vantage_api
            api_wrapper = alpha_vantage_api.AlphaVantageApi(
                stonk_ticker,
                'jkjk',
                developer_mode=developer_mode,
            )
        else:
            api = iex_cloud_api
            api_wrapper = iex_cloud_api.IexCloudApi(
                stonk_ticker,
                'poop',
                developer_mode=developer_mode,
            )

        self._income_statement = income_statement.IncomeStatement(
            api_wrapper.get_income_statements(),
            api.IncomeStatementDataKeys,
        )
        self._balance_sheet = balance_sheet.BalanceSheet(
            api_wrapper.get_balance_sheets(),
            api.BalanceSheetDataKeys,
        )
        self._cashflow = cashflow.Cashflow(
            api_wrapper.get_cashflows(),
            api.CashflowDataKeys,
        )

        if use_av:
            self._company_overview = company_overview.CompanyOverview(
                api_wrapper.get_company_overview(),
                alpha_vantage_api.CompanyOverviewDataKeys
            )
        else:
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
