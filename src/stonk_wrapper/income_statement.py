# Consider putting this in a different spot
def string_to_float(string_float):
    if (string_float == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 0

    return round(float(string_float), 2) / 1000

class IncomeStatement:
    def __init__(self, data):
        self._data = data

        self._all_revenue = []
        self._revenue_growth_yoy = []
        self._all_gross = []
        self._all_operating_income = []
        self._all_net_income = []
        self._all_report_dates = []

        for report in self._data:
            self._all_revenue.append(string_to_float(report['totalRevenue']))
            self._all_gross.append(string_to_float(report['grossProfit']))
            self._all_operating_income.append(string_to_float(report['operatingIncome']))
            self._all_net_income.append(string_to_float(report['netIncome']))
            self._all_report_dates.append(report['fiscalDateEnding'])

    @property
    def currency(self):
        return self._data[0]['reportedCurrency']

    @property
    def all_revenue(self):
        return self._all_revenue

    @property
    def all_gross(self):
        return self._all_gross

    @property
    def all_operating_income(self):
        return self._all_operating_income

    @property
    def all_net_income(self):
        return self._all_net_income

    @property
    def all_report_dates(self):
        return self._all_report_dates
