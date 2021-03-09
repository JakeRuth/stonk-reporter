from . import base_api


# Why is this stupidly called "Best" api? Cause it actually has all the fucking data, so yea it's the best!
# https://eodhistoricaldata.com/
# Documentation isn't that great but here's the docs page for this endpoint: https://eodhistoricaldata.com/financial-apis/stock-etfs-fundamental-data-feeds/#Stocks_Supported_Data
class BestApi(base_api.BaseStonkApiWrapper):
    def __init__(self, stonk_ticker, api_key, developer_mode):
        super().__init__(stonk_ticker, api_key, 'BEST', developer_mode)

        # This api has one endpoint to get a ton of data, so make sure we don't re-fetch to get data for companies we already called
        # This is just a little in memory cache, the base api has deeper caching to avoid hitting the api if memory cache isn't available
        self._dumb_cache = None

    def _get_json(self):
        if self._dumb_cache:
            print('Best api already called using cache to get data')
            return self._dumb_cache

        url = 'https://eodhistoricaldata.com/api/fundamentals/{}.US?api_token={}'.format(
            self.stonk_ticker,
            self.api_key,
        )
        response_json = self.get_json(url, 'fundamentals')
        self._dumb_cache = response_json
        return response_json

    def get_income_statements(self):
        res = self._get_json()
        income_statements = res['Financials']['Income_Statement']['quarterly']

        # json here is k -> v pairs of report date -> data, turn this into an array
        return list(income_statements.values())[:20]

    def get_cashflows(self):
        res = self._get_json()
        cashflows = res['Financials']['Cash_Flow']['quarterly']

        # json here is k -> v pairs of report date -> data, turn this into an array
        return list(cashflows.values())[:20]

    def get_balance_sheets(self):
        res = self._get_json()
        balance_sheets = res['Financials']['Balance_Sheet']['quarterly']

        # json here is k -> v pairs of report date -> data, turn this into an array
        return list(balance_sheets.values())[:20]

    def get_company_overview(self):
        res = self._get_json()
        all_data_we_want = res['Highlights']
        all_data_we_want.update(res['Valuation'])
        return all_data_we_want


class BalanceSheetDataKeys:
    cash = 'cash'
    currency = 'currency_symbol'
    current_assets = 'totalCurrentAssets'
    current_liabilities = 'totalCurrentLiabilities'
    current_long_term_debt = 'shortLongTermDebt'
    fiscal_date_ending = 'date'
    goodwill = 'goodWill'
    intangible_assets = 'intangibleAssets'
    inventory = 'inventory'
    long_term_debt = 'longTermDebt'
    tangible_book_value = 'netTangibleAssets'
    total_assets = 'totalAssets'
    total_liabilities = 'totalLiab'


class CashflowDataKeys:
    capex = 'capitalExpenditures'
    change_in_cash = 'changeInCash'
    currency = 'currency_symbol'
    financing = 'totalCashFromFinancingActivities'
    fiscal_date_ending = 'date'
    investing = 'totalCashflowsFromInvestingActivities'
    operations = 'totalCashFromOperatingActivities'


class IncomeStatementDataKeys:
    cost_of_revenue = 'costOfRevenue'
    currency = 'currency_symbol'
    fiscal_date_ending = 'date'
    gross_profit = 'grossProfit'
    net_income = 'netIncome'
    operating_income = 'operatingIncome'
    revenue = 'totalRevenue'


class CompanyOverviewDataKeys:
    eps = 'DilutedEpsTTM'
    market_cap = 'MarketCapitalization'
    pb_ratio = 'PriceBookMRQ'
    pe_ratio = 'PERatio'
    ps_ratio = 'PriceSalesTTM'
