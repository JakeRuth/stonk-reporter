class CompanyOverview:
    def __init__(self, overview_json):
        self._pe_ratio = float(overview_json['PERatio'])
        self._price_to_sales_ttm = float(overview_json['PriceToSalesRatioTTM'])
        self._price_to_book = float(overview_json['PriceToBookRatio'])
        self._earnings_per_share = float(overview_json['EPS'])

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
