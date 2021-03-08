import json
import os

import openpyxl as pyxl

from excel import openpyxl_helper
from stonks import base_api, financial_data


def run(stonk_tickers, developer_mode=False):
    stonk_rows = {
        'Revenue (TTM)': ['Revenue (TTM)'],
        'Cost of Revenue': ['Cost of Revenue'],
        'Gross Profit': ['Gross Profit'],
        'Gross Margin': ['Gross Margin'],
        'Operating Expense': ['Operating Expense'],
        'Operating Income': ['Operating Income'],
        'Operating Margin': ['Operating Margin'],
        'blank1': [''],
        'Total Cash': ['Total Cash'],
        'Inventory': ['Inventory'],
        'Total Current Assets': ['Total Current Assets'],
        'Total Current Liabilities': ['Total Current Liabilities'],
        'Current Ratio': ['Current Ratio'],
        'Total Assets': ['Total Assets'],
        'Total Liabilities': ['Total Liabilities'],
        'Stock Holder Equity (B/V)': ['Stock Holder Equity (B/V)'],
        'Goodwill': ['Goodwill'],
        'Intangible Assets': ['Intangible Assets'],
        'Total Tangible Assets': ['Total Tangible Assets'],
        'Total Liabilities 2': ['Total Liabilities'],
        'Tangible Book Value': ['Tangible Book Value'],
        'blank2': [''],
        'Free Cash Flow (last q)': ['Free Cash Flow (last q)'],
        'Free Cash Flow TTM': ['Free Cash Flow TTM'],
        'blank3': [''],
        'Valuation': ['Valuation'],
        'P/FCF': ['P/FCF'],
        'P/E': ['P/E'],
        'EPS': ['EPS'],
        'P/B': ['P/B'],
        'P/S (TTM)': ['P/S'],
    }
    income_statement = None  # Used outside for loop to get currency
    for ticker in stonk_tickers:
        print(ticker)
        try:
            stonk_data = financial_data.FinancialData(ticker, developer_mode)
        except base_api.StonkApiException as exc:
            print(str(exc))
            for idx, stonk_row_key in enumerate(stonk_rows.keys()):
                if idx == 0:
                    stonk_rows[stonk_row_key].append(str(exc))
                else:
                    stonk_rows[stonk_row_key].append('>.>')
            continue

        income_statement = stonk_data.income_statement
        company_overview = stonk_data.company_overview
        balance_sheet = stonk_data.balance_sheet
        cashflow = stonk_data.cashflow

        stonk_rows['Revenue (TTM)'].append(income_statement.revenue_ttm)
        stonk_rows['Cost of Revenue'].append(income_statement.cost_of_revenue_ttm)
        stonk_rows['Gross Profit'].append(income_statement.gross_ttm)
        stonk_rows['Gross Margin'].append(income_statement.gross_margin_ttm)
        stonk_rows['Operating Expense'].append(income_statement.operating_expense_ttm)
        stonk_rows['Operating Income'].append(income_statement.operating_income_ttm)
        stonk_rows['Operating Margin'].append(income_statement.operating_margin_ttm)
        stonk_rows['blank1'].append('')
        stonk_rows['Total Cash'].append(balance_sheet.cash[0])
        stonk_rows['Inventory'].append(balance_sheet.all_inventory[0])
        stonk_rows['Total Current Assets'].append(balance_sheet.current_assets[0])
        stonk_rows['Total Current Liabilities'].append(balance_sheet.current_liabilities[0])
        stonk_rows['Current Ratio'].append(balance_sheet.current_ratios[0])
        stonk_rows['Total Assets'].append(balance_sheet.total_assets[0])
        stonk_rows['Total Liabilities'].append(balance_sheet.total_liabilities[0])
        stonk_rows['Stock Holder Equity (B/V)'].append(balance_sheet.share_holder_equity[0])
        stonk_rows['Goodwill'].append(balance_sheet.goodwill[0])
        stonk_rows['Intangible Assets'].append(balance_sheet.intangible_assets[0])
        stonk_rows['Total Tangible Assets'].append(balance_sheet.total_tangible_assets[0])
        stonk_rows['Total Liabilities 2'].append(balance_sheet.total_liabilities[0])
        stonk_rows['Tangible Book Value'].append(balance_sheet._tangible_book_value[0])
        stonk_rows['blank2'].append('')
        stonk_rows['Free Cash Flow (last q)'].append(cashflow.free_cash_flow[0])
        stonk_rows['Free Cash Flow TTM'].append(cashflow.free_cash_flow_ttm)
        stonk_rows['blank3'].append('')
        stonk_rows['Valuation'].append(company_overview.market_cap)
        stonk_rows['P/FCF'].append(company_overview.price_to_fcf)
        stonk_rows['P/E'].append(company_overview.pe_ratio)
        stonk_rows['EPS'].append(company_overview.earnings_per_share)
        stonk_rows['P/B'].append(company_overview.price_to_book)
        stonk_rows['P/S (TTM)'].append(company_overview.price_to_sales_ttm)

    workbook = pyxl.Workbook()
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='stonks',
        tab_color='ff9191',
        index=0,
    )

    heading_row = [
        "#'s in thousands ({})'".format(income_statement.currency)
    ] + stonk_tickers
    worksheet.append(heading_row)  # heading row
    for stonk_row_key in stonk_rows.keys():
        worksheet.append(stonk_rows[stonk_row_key])

    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='stonks',
        num_rows=len(stonk_rows.keys()) + 1,
        num_columns=len(stonk_tickers) + 1,
        style='blue',
    )
    return workbook

def run_local():
    workbook = run([
        'MSFT',
        'AAPL',
        'GOOGL'
    ], True)

    filename = '_multiple_stonks.xlsx'
    workbook.save(filename)
    os.startfile(filename)

if __name__ == '__main__':
    run_local()
