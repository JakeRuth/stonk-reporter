import os

import openpyxl as pyxl
from openpyxl import utils as pyxl_utils

from excel import openpyxl_helper
from stonk_wrapper import financial_data


stock_ticker = 'APHA'
data = financial_data.FinancialData(stock_ticker)
income_statement = data.income_statement_quarterly

top_left_cell_label = '{} #s in 1000s'.format(income_statement.currency)
all_report_dates_heading_row = [top_left_cell_label] + income_statement.all_report_dates
all_revenue_row = ['Revenue'] + income_statement.all_revenue
all_gross_row = ['Gross'] + income_statement.all_gross
all_operating_income_row = ['Op Income'] + income_statement.all_operating_income
all_net_income_row = ['Net'] + income_statement.all_net_income

workbook = pyxl.Workbook()
worksheet = workbook.create_sheet('Income', 0)
worksheet.sheet_properties.tabColor = 'ff9191'  # colors are cool... why not?
# 100 is a dumb value to just set all the column widths to be LORGE
worksheet.column_dimensions[pyxl_utils.get_column_letter(1)].width = 20
for i in range(1, 100):
    worksheet.column_dimensions[pyxl_utils.get_column_letter(i + 1)].width = 15

income_table_data = [
    all_report_dates_heading_row,
    all_revenue_row,
    all_gross_row,
    all_operating_income_row,
    all_net_income_row,
]
for row in income_table_data:
    worksheet.append(row)

num_table_rows = len(income_table_data)
num_table_columns = len(income_table_data[0])
openpyxl_helper.add_table(
    worksheet=worksheet,
    name='Quarterly',
    num_rows=num_table_rows,
    num_columns=num_table_columns,
    style='blue',
)
openpyxl_helper.add_graph(
    worksheet=worksheet,
    start_cell='A{}'.format(num_table_rows + 1),
    title='Quarterly',
    y_axis_label=income_statement.currency,
    chart_length=num_table_columns,
)

# this is dumb but it's the easiest way I've found to add rows deeper down a sheet
# instead of adding it with .append and then manually moving the range
for i in range(15):
    worksheet.append([''])

income_growth_data = [
    ['% change quarterly'] + income_statement.all_report_dates,
    ['Revenue Growth q/q'] + income_statement.revenue_growth,
    ['Gross Growth q/q'] + income_statement.gross_growth,
    ['Op Inc Growth q/q'] + income_statement.operating_income_growth,
    ['Net Growth q/q'] + income_statement.net_income_growth,
]
for row in income_growth_data:
    worksheet.append(row)

num_table_rows = len(income_growth_data)
num_table_columns = len(income_growth_data[0])
openpyxl_helper.add_table(
    worksheet=worksheet,
    name='Growth',
    offset=21,
    num_rows=num_table_rows,
    num_columns=num_table_columns,
    style='red',
)

income_growth_data = [
    ['% change yearly'] + income_statement.all_report_dates[0::4],
    ['Revenue Growth y/y'] + income_statement.revenue_growth_yoy,
    ['Gross Growth y/y'] + income_statement.gross_growth_yoy,
    ['Op Inc Growth y/y'] + income_statement.operating_income_growth_yoy,
    ['Net Growth y/y'] + income_statement.net_income_growth_yoy,
]
for row in income_growth_data:
    worksheet.append(row)

num_table_rows = len(income_growth_data)
num_table_columns = len(income_growth_data[0])
openpyxl_helper.add_table(
    worksheet=worksheet,
    name='GrowthYear',
    offset=26,
    num_rows=num_table_rows,
    num_columns=num_table_columns,
    style='purp',
)

filename = '{}_overview_v1.xlsx'.format(stock_ticker)
workbook.save(filename)
os.startfile(filename)
