from json2html import *

class IncomeStatementWrapper:
    def __init__(self, income_statement_json):
        self.income_statement = income_statement_json

    @property
    def get_quarterly_revenue_growth_html_table(self):
        quarterly_reports = self.income_statement['quarterlyReports']
        return self._create_reports_table(quarterly_reports, 'Quarterly Revenue')

    @property
    def get_yearly_revenue_growth_html_table(self):
        annual_reports = self.income_statement['annualReports']
        return self._create_reports_table(annual_reports, 'Yearly Revenue')

    def _create_reports_table(self, reports, table_name):
        data = []
        previous_revenue = None

        # API returns in order from latest date until oldest, reverse this so q/q calculations are computed properly
        reports.reverse()
        for report in reports:
            revenue = float(report['totalRevenue'])
            revenue_change = 'n/a'
            percent_growth_b2b = 'n/a'
            if previous_revenue:
                revenue_change = round(revenue - previous_revenue, 2)
                percent_growth_b2b = round((revenue_change / previous_revenue) * 100, 2)

            data.append(
                {
                    'date': report['fiscalDateEnding'],
                    'revenue': round(revenue, 2),
                    'change': revenue_change,
                    '% change': percent_growth_b2b,
                }
            )
            previous_revenue = revenue

        total_change = 0.0
        total_revenue = 0.0
        for i in data[1:]:  # first element is the string 'n/a'
            total_revenue = total_revenue + i['change']
            total_change = total_change + i['% change']

        data.append(
            {
                'date': '~avg data~',
                'revenue': '~avg data~',
                'change': 'avg: {}'.format(round(total_revenue / len(data), 2)),
                '% change': 'avg: {}'.format(round(total_change / len(data), 2)),
            },
        )

        # Ordered was switched above to facilitate q/q calculations, reverse back so newest date is first
        data.reverse()
        return json2html.convert(
            json={table_name: data},
        )
