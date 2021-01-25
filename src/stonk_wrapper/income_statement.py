from . import math_helper

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
            revenue = math_helper.format_number(report['totalRevenue'])
            self._all_revenue.append(revenue)
            gross_profit = math_helper.format_number(report['grossProfit'])
            self._all_gross.append(gross_profit)
            operating_income = math_helper.format_number(report['operatingIncome'])
            self._all_operating_income.append(operating_income)
            net_income = math_helper.format_number(report['netIncome'])
            self._all_net_income.append(net_income)

            revenue_growth = 0
            gross_growth = 0
            operating_income_growth = 0
            net_income_growth = 0
            if idx < len(self._data) - 1:
                previous_revenue = math_helper.format_number(self._data[idx + 1]['totalRevenue'])
                revenue_growth = math_helper.calc_percent_increase(revenue, previous_revenue)

                previous_gross = math_helper.format_number(self._data[idx + 1]['grossProfit'])
                gross_growth = math_helper.calc_percent_increase(gross_profit, previous_gross)

                previous_operating_income = math_helper.format_number(self._data[idx + 1]['operatingIncome'])
                operating_income_growth = math_helper.calc_percent_increase(operating_income, previous_operating_income)

                previous_net_income = math_helper.format_number(self._data[idx + 1]['netIncome'])
                net_income_growth = math_helper.calc_percent_increase(net_income, previous_net_income)

            self._revenue_growth.append(revenue_growth)
            self._gross_growth.append(gross_growth)
            self._operating_income_growth.append(operating_income_growth)
            self._net_income_growth.append(net_income_growth)

            # Only add every 4th report, since we want yearly results, and this is a quarterly iteration
            if idx % 4 == 0 and idx < len(self._data) - 4:
                previous_revenue = math_helper.format_number(self._data[idx + 4]['totalRevenue'])
                revenue_growth_yoy = math_helper.calc_percent_increase(revenue, previous_revenue)
                self._revenue_growth_yoy.append(revenue_growth_yoy)

                previous_gross = math_helper.format_number(self._data[idx + 4]['grossProfit'])
                gross_growth_yoy = math_helper.calc_percent_increase(gross_profit, previous_gross)
                self._gross_growth_yoy.append(gross_growth_yoy)

                previous_operating_income = math_helper.format_number(self._data[idx + 4]['operatingIncome'])
                operating_income_growth_yoy = math_helper.calc_percent_increase(operating_income, previous_operating_income)
                self._operating_income_growth_yoy.append(operating_income_growth_yoy)

                previous_net_income = math_helper.format_number(self._data[idx + 4]['netIncome'])
                net_income_growth_yoy = math_helper.calc_percent_increase(net_income, previous_net_income)
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
