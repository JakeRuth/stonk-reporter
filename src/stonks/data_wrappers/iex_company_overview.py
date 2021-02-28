from stonks import math_helper

# This is super ugly to make this custom, but since I'm confident we will stick with just this
# api I am going to impl this quick in hopes I can delete the alpha vantage api code/other company overview wrapper
class IexCompanyOverview:
    def __init__(self, company_overview, income_statement, balance_sheet, cashflow):
        market_cap = company_overview['marketcap']
        self._market_cap = market_cap
        self._pe_ratio = company_overview['peRatio']
        self._price_to_sales_ttm = math_helper.simple_ratio(market_cap, income_statement.revenue_ttm)

        self._price_to_book = math_helper.simple_ratio(market_cap, balance_sheet.share_holder_equity[0])
        self._earnings_per_share = company_overview['ttmEPS']
        self._price_to_fcf = math_helper.simple_ratio(market_cap, cashflow.free_cash_flow_ttm)

    @property
    def pe_ratio(self):
        return self._pe_ratio

    @property
    def price_to_sales_ttm(self):
        return self._price_to_sales_ttm

    @property
    def price_to_book(self):
        return self._price_to_book

    @property
    def earnings_per_share(self):
        return self._earnings_per_share

    @property
    def market_cap(self):
        return self._market_cap

    @property
    def price_to_fcf(self):
        return
