# Consider putting this in a different spot
def string_to_float(string_float):
    if (string_float == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 0

    return round(float(string_float), 2) / 1000

def calc_percent_increase(current, previous):
    if current <= 0 or previous <= 0:
        return 0
    increase = (current - previous) / previous
    return round(increase * 100, 2)

class IncomeStatement:
    def __init__(self, data):
        self._data = data

        self._all_revenue = []
        self._revenue_growth = []
        self._revenue_growth_yoy = []

        self._all_gross = []
        self._gross_growth = []
        self._gross_growth_yoy = []

        self._all_operating_income = []
        self._operating_income_growth = []
        self._operating_income_growth_yoy = []

        self._all_net_income = []
        self._net_income_growth = []
        self._net_income_growth_yoy = []

        self._all_report_dates = []

        for idx, report in enumerate(self._data):
            self._all_report_dates.append(report['fiscalDateEnding'])
            revenue = string_to_float(report['totalRevenue'])
            self._all_revenue.append(revenue)
            gross_profit = string_to_float(report['grossProfit'])
            self._all_gross.append(gross_profit)
            operating_income = string_to_float(report['operatingIncome'])
            self._all_operating_income.append(operating_income)
            net_income = string_to_float(report['netIncome'])
            self._all_net_income.append(net_income)

            revenue_growth = 0
            gross_growth = 0
            operating_income_growth = 0
            net_income_growth = 0
            if idx < len(self._data) - 1:
                previous_revenue = string_to_float(self._data[idx + 1]['totalRevenue'])
                revenue_growth = calc_percent_increase(revenue, previous_revenue)

                previous_gross = string_to_float(self._data[idx + 1]['grossProfit'])
                gross_growth = calc_percent_increase(gross_profit, previous_gross)

                previous_operating_income = string_to_float(self._data[idx + 1]['operatingIncome'])
                operating_income_growth = calc_percent_increase(operating_income, previous_operating_income)

                previous_net_income = string_to_float(self._data[idx + 1]['netIncome'])
                net_income_growth = calc_percent_increase(net_income, previous_net_income)

            self._revenue_growth.append(revenue_growth)
            self._gross_growth.append(gross_growth)
            self._operating_income_growth.append(operating_income_growth)
            self._net_income_growth.append(net_income_growth)

            # Only add every 4th report, since we want yearly results, and this is a quarterly iteration
            if idx % 4 == 0 and idx < len(self._data) - 4:
                previous_revenue = string_to_float(self._data[idx + 4]['totalRevenue'])
                revenue_growth_yoy = calc_percent_increase(revenue, previous_revenue)
                self._revenue_growth_yoy.append(revenue_growth_yoy)

                previous_gross = string_to_float(self._data[idx + 4]['grossProfit'])
                gross_growth_yoy = calc_percent_increase(gross_profit, previous_gross)
                self._gross_growth_yoy.append(gross_growth_yoy)

                previous_operating_income = string_to_float(self._data[idx + 4]['operatingIncome'])
                operating_income_growth_yoy = calc_percent_increase(operating_income, previous_operating_income)
                self._operating_income_growth_yoy.append(operating_income_growth_yoy)

                previous_net_income = string_to_float(self._data[idx + 4]['netIncome'])
                net_income_growth_yoy = calc_percent_increase(net_income, previous_net_income)
                self._net_income_growth_yoy.append(net_income_growth_yoy)


    @property
    def currency(self):
        return self._data[0]['reportedCurrency']

    @property
    def all_revenue(self):
        return self._all_revenue

    @property
    def revenue_growth(self):
        return self._revenue_growth

    @property
    def revenue_growth_yoy(self):
        return self._revenue_growth_yoy

    @property
    def all_gross(self):
        return self._all_gross

    @property
    def gross_growth(self):
        return self._gross_growth

    @property
    def gross_growth_yoy(self):
        return self._gross_growth_yoy

    @property
    def all_operating_income(self):
        return self._all_operating_income

    @property
    def operating_income_growth(self):
        return self._operating_income_growth

    @property
    def operating_income_growth_yoy(self):
        return self._operating_income_growth_yoy

    @property
    def all_net_income(self):
        return self._all_net_income

    @property
    def net_income_growth(self):
        return self._net_income_growth

    @property
    def net_income_growth_yoy(self):
        return self._net_income_growth_yoy

    @property
    def all_report_dates(self):
        return self._all_report_dates
