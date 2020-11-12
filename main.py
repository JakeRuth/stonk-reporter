import json
import os
import time

import stock_api
import stock_api_incomestatement_wrapper

from selenium import webdriver
from webdriver_manager import chrome

income_statement_json = stock_api.get_income_statement_json('APHA')
income_statement = stock_api_incomestatement_wrapper.IncomeStatementWrapper(income_statement_json)
quarterly_revenue_table = income_statement.get_quarterly_revenue_growth_html_table
yearly_revenue_table = income_statement.get_yearly_revenue_growth_html_table

html = '<div>{quarterly_revenue_table}{yearly_revenue_table}</div>'.format(
    quarterly_revenue_table=quarterly_revenue_table,
    yearly_revenue_table=yearly_revenue_table,
)

driver = webdriver.Chrome(chrome.ChromeDriverManager().install())
driver.execute_script("document.write('{}')".format(html))
