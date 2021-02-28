from . import base_api


class AlphaVantageApi(base_api.BaseStonkApiWrapper):
    def __init__(self, stonk_ticker, api_key, developer_mode):
        super().__init__(stonk_ticker, api_key, 'AV', developer_mode)

    def _get_json(self, api_function):
        url = 'https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(
            api_function,
            self.stonk_ticker,
            self.api_key,
        )
        response = self.get_json(url, api_function)
        # api responds with a single "note" if you go over the usage limit for their api
        # their free tier is 5 requests per minute and 500 a day (ref: https://www.alphavantage.co/premium/)
        over_api_request_throttle_limit = response.get('Note')
        if bool(over_api_request_throttle_limit):
            print(response)
            raise base_api.StonkApiException('Api request limit reached :( we are allowed 5 requests per minutes, and 500 daily')

        return response

    def should_cache_api_response(self, response):
        return not bool(response.get('Note'))

    # https://www.alphavantage.co/documentation/#income-statement
    def get_income_statements(self):
        res = self._get_json('INCOME_STATEMENT')
        income_statements = res.get('quarterlyReports')
        if not income_statements:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return income_statements

    # https://www.alphavantage.co/documentation/#cash-flow
    def get_cashflows(self):
        res = self._get_json('CASH_FLOW')
        cashflows = res.get('quarterlyReports')
        if not cashflows:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return cashflows

    # https://www.alphavantage.co/documentation/#balance-sheet
    def get_balance_sheets(self):
        res = self._get_json('BALANCE_SHEET')
        balance_sheets = res.get('quarterlyReports')
        if not balance_sheets:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return balance_sheets

    # https://www.alphavantage.co/documentation/#company-overview
    def get_company_overview(self):
        res = self._get_json('OVERVIEW')
        if len(res.keys()) == 0:
            raise base_api.StonkApiException('This stonk does not exist in the stonk data api we are using :(')
        return res


class BalanceSheetDataKeys:
    cash = 'cash'
    currency = 'reportedCurrency'
    current_assets = 'totalCurrentAssets'
    current_liabilities = 'totalCurrentLiabilities'
    current_long_term_debt = 'currentLongTermDebt'
    fiscal_date_ending = 'fiscalDateEnding'
    goodwill = 'goodwill'
    intangible_assets = 'intangibleAssets'
    inventory = 'inventory'
    long_term_debt = 'longTermDebt'
    tangible_book_value = 'netTangibleAssets'
    total_assets = 'totalAssets'
    total_liabilities = 'totalLiabilities'


class CashflowDataKeys:
    capex = 'capitalExpenditures'
    change_in_cash = 'changeInCash'
    currency = 'reportedCurrency'
    financing = 'cashflowFromFinancing'
    fiscal_date_ending = 'fiscalDateEnding'
    investing = 'cashflowFromInvestment'
    operations = 'operatingCashflow'


class IncomeStatementDataKeys:
    cost_of_revenue = 'costOfRevenue'
    currency = 'reportedCurrency'
    fiscal_date_ending = 'fiscalDateEnding'
    gross_profit = 'grossProfit'
    net_income = 'netIncome'
    operating_income = 'operatingIncome'
    revenue = 'totalRevenue'


class CompanyOverviewDataKeys:
    eps = 'EPS'
    market_cap = 'MarketCapitalization'
    pb_ratio = 'PriceToBookRatio'
    pe_ratio = 'PERatio'
    ps_ratio = 'PriceToSalesRatioTTM'
