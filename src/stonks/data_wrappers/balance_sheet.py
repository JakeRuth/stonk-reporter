from stonks import math_helper

class BalanceSheet:
    def __init__(self, data):
        self._data = data
        self._report_dates = []
        self._total_assets = []
        self._total_liabilities = []
        self._intangible_assets = []
        self._total_tangible_assets = []
        self._goodwill = []
        self._total_intangible_assets = []
        self._share_holder_equity = []
        self._cash = []
        self._current_liabilities = []
        self._non_current_liabilities = []
        self._current_debt = []
        self._current_assets = []
        self._current_ratios = []
        self._non_current_assets = []
        self._tangible_book_value = []
        self._long_term_debt = []
        self._all_inventory = []

        for idx, report in enumerate(data):
            self._report_dates.append(report['fiscalDateEnding'])
            total_assets = math_helper.format_number(report['totalAssets'])
            self._total_assets.append(total_assets)

            total_liabilities = math_helper.format_number(report['totalLiabilities'])
            self._total_liabilities.append(total_liabilities)

            intangible_assets = math_helper.format_number(report['intangibleAssets'])
            self._intangible_assets.append(intangible_assets)

            goodwill = math_helper.format_number(report['goodwill'])
            self._goodwill.append(goodwill)

            total_intanglible_assets = intangible_assets + goodwill
            self._total_intangible_assets.append(total_intanglible_assets)

            total_tangible_assets = total_assets - total_intanglible_assets
            self._total_tangible_assets.append(total_tangible_assets)

            share_holder_equity = total_assets - total_liabilities
            self._share_holder_equity.append(share_holder_equity)

            cash = math_helper.format_number(report['cash'])
            self._cash.append(cash)

            current_liabilities = math_helper.format_number(report['totalCurrentLiabilities'])
            self._current_liabilities.append(current_liabilities)

            non_current_liabilities = math_helper.format_number(report['totalNonCurrentLiabilities'])
            self._non_current_liabilities.append(non_current_liabilities)

            current_long_term_debt = math_helper.format_number(report['currentLongTermDebt'])
            self._current_debt.append(current_long_term_debt)

            current_assets = math_helper.format_number(report['totalCurrentAssets'])
            self._current_assets.append(current_assets)
            self._current_ratios.append(math_helper.simple_ratio(current_assets, current_liabilities))

            non_current_assets = math_helper.format_number(report['totalNonCurrentAssets'])
            self._non_current_assets.append(non_current_assets)

            tangible_book_value = math_helper.format_number(report['netTangibleAssets'])
            self._tangible_book_value.append(tangible_book_value)

            long_term_debt = math_helper.format_number(report['longTermDebt'])
            self._long_term_debt.append(long_term_debt)

            inventory = math_helper.format_number(report['inventory'])
            self._all_inventory.append(inventory)

    @property
    def currency(self):
        return self._data[0]['reportedCurrency']

    @property
    def report_dates(self):
        return self._report_dates

    @property
    def total_assets(self):
        return self._total_assets

    @property
    def total_liabilities(self):
        return self._total_liabilities

    @property
    def intangible_assets(self):
        return self._intangible_assets

    @property
    def total_tangible_assets(self):
        return self._total_tangible_assets

    @property
    def goodwill(self):
        return self._goodwill

    @property
    def total_intangible_assets(self):
        return self._total_intangible_assets

    @property
    def share_holder_equity(self):
        return self._share_holder_equity

    @property
    def cash(self):
        return self._cash

    @property
    def current_liabilities(self):
        return self._current_liabilities

    @property
    def non_current_liabilities(self):
        return self._non_current_liabilities

    @property
    def current_debt(self):
        return self._current_debt

    @property
    def current_assets(self):
        return self._current_assets

    @property
    def current_assets(self):
        return self._current_assets

    @property
    def current_ratios(self):
        return self._current_ratios

    @property
    def current_assets(self):
        return self._current_assets

    @property
    def non_current_assets(self):
        return self._non_current_assets

    @property
    def tangible_book_value(self):
        return self._tangible_book_value

    @property
    def long_term_debt(self):
        return self._long_term_debt

    @property
    def all_inventory(self):
        return self._all_inventory
