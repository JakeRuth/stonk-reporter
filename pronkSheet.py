import json
import os

import openpyxl as xl
from openpyxl.worksheet import table as xltable
from openpyxl import chart as xlchart
from openpyxl import utils as xlutils

from shared import excel_helpers
from shared import stock_api

# define data shape
stock_data = {
    'Revenue': [],
    'Cost of Revenue': [],
    'Gross Profit': [],
    'Gross Margin': [],
    'Operating Expense': [],
    'Operating Income': [],
    'Operating Margin': [],
    'Revenue Growth y/y': [],
    'Total Cash': [],
    'Current Assets': [],
    'Current Liabilities Total': [],
    'Current Ratio': [],
    'Total Assets': [],
    'Total Liabilities': [],
    'Stock Holder Equity': [],
    'Stock Holder Growth q/q': [],
    'Goodwill': [],
    'Intangile Assets': [],
    'Tangible Assets': [],
    'Total Liabilities': [],
    'Tangible Book Value': [],
    'Free Cash Flow': [],
    'Free Cash Flow (TTM)': [],
    'Valuation': [],
    'P/FCF Ratio': [],
    'P/E Ratio': [],
    'P/S Ratio': [],
}

# Get input from user
api_key = input('Enter your ALPHA Vantage API key: ')
stock_tickers = input('Enter stock tickers (comma separated, no spaces): ')

# Uncomment for local dev
income_statement_json = None
with open('static_json_data/apha_income.json') as json_file:
    income_statement_json = json.load(json_file)

stock_api_wrapper = stock_api.StockApiWrapper(api_key)
heading_row = ['']  # intentially leave first cell blank
for ticker in stock_tickers:
    heading_row.append(ticker)
    income_quarterly_reports = stock_api_wrapper.get_income_statement_json(ticker)['quarterlyReports']
    cashflow = stock_api_wrapper.get_cashflow_json(ticker)
    company_overview = stock_api_wrapper.get_company_overview_json(ticker)

    revenue_ttm = 0
    cost_of_revenue_ttm = 0
    gross_profit_ttm = 0
    for qr in income_quarterly_reports[:4]:
        revenue_ttm = revenue_ttm + excel_helpers.string_to_float(qr['totalRevenue'])
        cost_of_revenue_ttm = cost_of_revenue_ttm + excel_helpers.string_to_float(qr['costOfRevenue'])
        gross_profit_ttm = gross_profit_ttm + excel_helpers.string_to_float(qr['grossProfit'])

    stock_data['Revenue'].append(revenue_ttm / 1000)
    stock_data['Cost of Revenue'].append(cost_of_revenue_ttm / 1000)
    stock_data['Gross Profit'].append(gross_profit_ttm / 1000)

    # Take the gross profit, divide by the total revenue (sales)
    stock_data['Gross Margin'].append(round(gross_profit_ttm / revenue_ttm, 3))

workbook = xl.Workbook()
worksheet = workbook.create_sheet('Overview', 0)
worksheet.append(heading_row)
for key in stock_data.keys():
    row_data = [key] + stock_data[key]
    worksheet.append(row_data)

worksheet.add_table(xltable.Table(
    displayName='Overview',
    # If this isn't specified the program will crash in a cryptic way
    ref='A1:{}{}'.format(
        xlutils.get_column_letter(len(stock_tickers) + 1),
        len(stock_data.keys()) + 1,
    ),
    tableStyleInfo=xltable.TableStyleInfo(
        name='TableStyleMedium9',
        showFirstColumn=True,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False,
    )
))

# 100 is a dumb value to just set all the column widths to be LORGE
for i in range(100):
    worksheet.column_dimensions[xlutils.get_column_letter(i + 1)].width = 25

workbook.save('pronkSheet.xlsx')
os.startfile('pronkSheet.xlsx')
