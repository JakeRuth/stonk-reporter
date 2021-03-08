from . import base_api


class IexCloudApi(base_api.BaseStonkApiWrapper):
    def __init__(self, stonk_ticker, api_key, developer_mode):
        super().__init__(stonk_ticker, api_key, 'IEX', developer_mode)

    def _get_json(self, api_function):
        url = 'https://cloud.iexapis.com/stable/stock/{}/{}?last=12&token={}'.format(
            self.stonk_ticker,
            api_function,
            self.api_key,
        )
        return self.get_json(url, api_function)

    def should_cache_api_response(self, response):
        return len(response.keys()) != 0

    # https://iexcloud.io/docs/api/#income-statement
    def get_income_statements(self):
        res = self._get_json('income')
        income_statements = res.get('income')
        if not income_statements:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return income_statements

    # https://iexcloud.io/docs/api/#cash-flow
    def get_cashflows(self):
        res = self._get_json('cash-flow')
        cashflows = res.get('cashflow')
        if not cashflows:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return cashflows

    # https://iexcloud.io/docs/api/#balance-sheet
    def get_balance_sheets(self):
        res = self._get_json('balance-sheet')
        balance_sheets = res.get('balancesheet')
        if not balance_sheets:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return balance_sheets

    # https://iexcloud.io/docs/api/#key-stats
    def get_company_overview(self):
        res = self._get_json('stats')
        if not res:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return res


class BalanceSheetDataKeys:
    cash = 'currentCash'
    currency = 'currency'
    current_assets = 'currentAssets'
    current_liabilities = 'totalCurrentLiabilities'
    current_long_term_debt = 'currentLongTermDebt'
    fiscal_date_ending = 'fiscalDate'
    goodwill = 'goodwill'
    intangible_assets = 'intangibleAssets'
    inventory = 'inventory'
    long_term_debt = 'longTermDebt'
    tangible_book_value = 'netTangibleAssets'
    total_assets = 'totalAssets'
    total_liabilities = 'totalLiabilities'


class CashflowDataKeys:
    capex = 'capitalExpenditures'
    change_in_cash = 'cashChange'
    currency = 'currency'
    financing = 'cashFlowFinancing'
    fiscal_date_ending = 'fiscalDate'
    investing = 'totalInvestingCashFlows'
    operations = 'cashFlow'


class IncomeStatementDataKeys:
    cost_of_revenue = 'costOfRevenue'
    currency = 'currency'
    fiscal_date_ending = 'fiscalDate'
    gross_profit = 'grossProfit'
    net_income = 'netIncome'
    operating_income = 'operatingIncome'
    revenue = 'totalRevenue'
