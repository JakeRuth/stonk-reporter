import json
import os

import openpyxl as pyxl

from excel import openpyxl_helper
from stonk_wrapper import api, financial_data


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
    'P/S': ['P/S'],
}

def main():
    stonk_tickers = ['GOOG', 'AMZN', 'AAPL', 'FB', 'SNAP', 'APHA', 'TLRY']
    income_statement = None  # Used outside for loop to get currency
    for ticker in stonk_tickers:
        print(ticker)
        try:
            data = financial_data.FinancialData(ticker)
        except api.StonkApiException as exc:
            print(str(exc))
            for idx, stonk_row_key in enumerate(stonk_rows.keys()):
                if idx == 0:
                    stonk_rows[stonk_row_key].append(str(exc))
                else:
                    stonk_rows[stonk_row_key].append('>.>')
            continue

        income_statement = data.income_statement
        company_overview = data.company_overview
        balance_sheet = data.balance_sheet
        cashflow = data.cashflow

        stonk_rows['Revenue (TTM)'].append(income_statement.revenue_ttm)
        stonk_rows['Cost of Revenue'].append(income_statement.cost_of_revenue_ttm)
        stonk_rows['Gross Profit'].append(income_statement.gross_ttm)
        stonk_rows['Gross Margin'].append(income_statement.gross_margin_ttm)
        stonk_rows['Operating Expense'].append('')
        stonk_rows['Operating Income'].append('')
        stonk_rows['Operating Margin'].append('')
        stonk_rows['blank1'].append('')
        stonk_rows['Total Cash'].append('')
        stonk_rows['Inventory'].append('')
        stonk_rows['Total Current Assets'].append('')
        stonk_rows['Total Current Liabilities'].append('')
        stonk_rows['Current Ratio'].append('')
        stonk_rows['Total Assets'].append('')
        stonk_rows['Total Liabilities'].append('')
        stonk_rows['Stock Holder Equity (B/V)'].append('')
        stonk_rows['Goodwill'].append('')
        stonk_rows['Intangible Assets'].append('')
        stonk_rows['Total Tangible Assets'].append('')
        stonk_rows['Total Liabilities 2'].append('')
        stonk_rows['Tangible Book Value'].append('')
        stonk_rows['blank2'].append('')
        stonk_rows['Free Cash Flow (last q)'].append('')
        stonk_rows['Free Cash Flow TTM'].append('')
        stonk_rows['blank3'].append('')
        stonk_rows['Valuation'].append('')
        stonk_rows['P/FCF'].append('')
        stonk_rows['P/E'].append('')
        stonk_rows['P/S'].append('')

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
    filename = '_multiple_stonks.xlsx'
    workbook.save(filename)
    os.startfile(filename)

main()
