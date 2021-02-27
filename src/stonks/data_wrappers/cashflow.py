from stonks import math_helper

class Cashflow:
    def __init__(self, data, data_keys):
        self._data = data
        self._data_keys = data_keys

        self._report_dates = []
        self._operations = []
        self._investing = []
        self._financing = []
        self._capex = []
        self._free_cash_flow = []
        self._dividend_payout = []
        self._stock_sale_and_purchase = []
        self._change_in_cash = []

        for idx, report in enumerate(data):
            self._report_dates.append(report[data_keys.fiscal_date_ending])
            operations = math_helper.format_number(report[data_keys.operations])
            self._operations.append(operations)

            investing = math_helper.format_number(report[data_keys.investing])
            self._investing.append(investing)

            financing = math_helper.format_number(report[data_keys.financing])
            self._financing.append(financing)

            capex = math_helper.format_number(report[data_keys.capex])
            self._capex.append(capex)

            free_cash_flow = operations - capex
            self._free_cash_flow.append(free_cash_flow)

            change_in_cash = math_helper.format_number(report[data_keys.change_in_cash])
            self._change_in_cash.append(change_in_cash)

    @property
    def currency(self):
        return self._data[0][self._data_keys.fiscal_date_ending]

    @property
    def report_dates(self):
        return self._report_dates

    @property
    def operations(self):
        return self._operations

    @property
    def investing(self):
        return self._investing

    @property
    def financing(self):
        return self._financing

    @property
    def capex(self):
        return self._capex

    @property
    def free_cash_flow(self):
        return self._free_cash_flow

    @property
    def free_cash_flow_ttm(self):
        return math_helper.get_ttm_or_error(self._free_cash_flow)

    @property
    def change_in_cash(self):
        return self._change_in_cash
