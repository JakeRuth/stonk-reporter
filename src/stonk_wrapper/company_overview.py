from . import math_helper

class CompanyOverview:
    def __init__(self, overview_json):
        self._pe_ratio = math_helper.string_to_float(overview_json['PERatio'])
        self._price_to_sales_ttm = math_helper.string_to_float(overview_json['PriceToSalesRatioTTM'])
        self._price_to_book = math_helper.string_to_float(overview_json['PriceToBookRatio'])
        self._earnings_per_share = math_helper.string_to_float(overview_json['EPS'])
        self._market_cap = math_helper.format_number(overview_json['MarketCapitalization'])

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
