import os

import openpyxl as pyxl
from openpyxl import utils as pyxl_utils

from excel import openpyxl_helper
from stonk_wrapper import financial_data


stock_ticker = 'APHA'
data = financial_data.FinancialData(stock_ticker)
income_statement = data.income_statement

top_left_cell_label = '{} #s in 1000s'.format(income_statement.currency)
all_report_dates_heading_row = [top_left_cell_label] + income_statement.all_quarterly_report_dates
all_revenue_row = ['Revenue'] + income_statement.all_quarterly_revenue
all_gross_row = ['Gross'] + income_statement.all_quarterly_gross
all_operating_income_row = ['Op Income'] + income_statement.all_quarterly_operating_income
all_net_income_row = ['Net'] + income_statement.all_quarterly_net_income

workbook = pyxl.Workbook()
worksheet = workbook.create_sheet('Income', 0)
worksheet.sheet_properties.tabColor = 'ff9191'  # colors are cool... why not?
# 100 is a dumb value to just set all the column widths to be LORGE
for i in range(100):
    worksheet.column_dimensions[pyxl_utils.get_column_letter(i + 1)].width = 15

quarterly_income_table_data = [
    all_report_dates_heading_row,
    all_revenue_row,
    all_gross_row,
    all_operating_income_row,
    all_net_income_row,
]
for row in quarterly_income_table_data:
    worksheet.append(row)

num_table_rows = len(quarterly_income_table_data)
num_table_columns = len(quarterly_income_table_data[0])
openpyxl_helper.add_table(
    worksheet=worksheet,
    name='Quarterly',
    start_cell='A1',
    num_rows=num_table_rows,
    num_columns=num_table_columns,
)
openpyxl_helper.add_graph(
    worksheet=worksheet,
    start_cell='A{}'.format(num_table_rows + 1),
    title='Quarterly',
    y_axis_label=income_statement.currency,
    chart_length=num_table_columns,
)

filename = '{}_overview_v1.xlsx'.format(stock_ticker)
workbook.save(filename)
os.startfile(filename)
