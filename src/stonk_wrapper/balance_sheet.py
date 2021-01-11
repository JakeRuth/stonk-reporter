class BalanceSheet:
    def __init__(self, raw_json):
        self.quarterly_reports = raw_json['quarterlyReports']
        self.annual_reports = raw_json['annualReports']
