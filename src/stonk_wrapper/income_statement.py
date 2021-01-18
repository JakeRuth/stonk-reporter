# Consider putting this in a different spot
def string_to_float(string_float):
    if (string_float == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 0

    return round(float(string_float), 2) / 1000

class IncomeStatement:
    def __init__(self, raw_json):
        self._quarterly_reports = raw_json['quarterlyReports']

        self._all_quarterly_revenue = []
        self._all_quarterly_gross = []
        self._all_quarterly_operating_income = []
        self._all_quarterly_net_income = []
        self._all_quarterly_report_dates = []

        for qr in self._quarterly_reports:
            self._all_quarterly_revenue.append(string_to_float(qr['totalRevenue']))
            self._all_quarterly_gross.append(string_to_float(qr['grossProfit']))
            self._all_quarterly_operating_income.append(string_to_float(qr['operatingIncome']))
            self._all_quarterly_net_income.append(string_to_float(qr['netIncome']))
            self._all_quarterly_report_dates.append(qr['fiscalDateEnding'])

    @property
    def currency(self):
        return self._quarterly_reports[0]['reportedCurrency']

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
