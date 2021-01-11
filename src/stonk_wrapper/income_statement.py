class IncomeStatement:
    def __init__(self, raw_json):
        self._all_quarterly_revenue = []
        self._all_quarterly_gross = []
        self._all_quarterly_operating_income = []
        self._all_quarterly_net_income = []
        self._all_quarterly_report_dates = []

        for qr in raw_json['quarterlyReports']:
            self._all_quarterly_revenue.append(qr['totalRevenue'])
            self._all_quarterly_gross.append(qr['grossProfit'])
            self._all_quarterly_operating_income.append(qr['operatingIncome'])
            self._all_quarterly_net_income.append(qr['netIncome'])
            self._all_quarterly_report_dates.append(qr['fiscalDateEnding'])

    @property
    def all_quarterly_revenue(self):
        return self._all_quarterly_revenue

    @property
    def all_quarterly_gross(self):
        return self._all_quarterly_gross

    @property
    def all_quarterly_operating_income(self):
        return self._all_quarterly_operating_income

    @property
    def all_quarterly_net_income(self):
        return self._all_quarterly_net_income

    @property
    def all_quarterly_report_dates(self):
        return self._all_quarterly_report_dates
