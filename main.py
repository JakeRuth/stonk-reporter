import json

import stock_api
import stock_api_incomestatement_wrapper


api_key = input('Enter your ALPHA Vantage API key: ')
stock_api_wrapper = stock_api.StockApiWrapper(api_key)
income_statement_json = stock_api_wrapper.get_income_statement_json('APHA')

# Uncomment for local dev
# income_statement_json = None
# with open('static_json_data/apha_income.json') as json_file:
#         income_statement_json = json.load(json_file)

income_statement = stock_api_incomestatement_wrapper.IncomeStatementWrapper(income_statement_json, 'APHA')
income_statement.generate_excel_file()
income_statement.open_excel_sheet()
