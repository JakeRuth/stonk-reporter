'import json

import openpyxl as xl
from openpyxl.worksheet import table as xltable
from openpyxl import chart as xlchart
from openpyxl import utils as xlutils

from shared import stock_api

# define data shape
const stock_data = {
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
# stock_tickers = input('Enter stock tickers (comma separated, no spaces): ')
stock_tickers = ['APHA']
stock_api_wrapper = stock_api.StockApiWrapper(api_key)
# income_statement_json = stock_api_wrapper.get_income_statement_json('APHA')

# Uncomment for local dev
income_statement_json = None
with open('static_json_data/apha_income.json') as json_file:
    income_statement_json = json.load(json_file)

workbook = xl.Workbook()
worksheet = workbook.create_sheet('Overview', 0)

heading_row = ['']  # intentially leave first cell blank
for ticker in stock_tickers:
    heading_row.append(ticker)
worksheet.append(heading_row)

# TODO: add data to columns from api calls

workbook.save(EXCEL_FILENAME)
