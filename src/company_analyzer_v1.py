import os

import openpyxl as pyxl

from excel import openpyxl_helper
from stonk_wrapper import financial_data


def main():
    stock_ticker = 'APHA'
    data = financial_data.FinancialData(stock_ticker)
    income_statement = data.income_statement_quarterly
    company_overview = data.company_overview
    balance_sheet = data.balance_sheet_quarterly

    workbook = pyxl.Workbook()
    _add_income_sheet(workbook, income_statement, company_overview)
    _add_balance_sheet(workbook, balance_sheet, company_overview)
    filename = '{}_overview_v1.xlsx'.format(stock_ticker)
    workbook.save(filename)
    os.startfile(filename)

def _add_balance_sheet(workbook, balance_sheet, company_overview):
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='Balance',
        tab_color='0dff4d',
        index=1,
    )

    top_left_cell_label = '{} #s in 1000s'.format(balance_sheet.currency)
    all_report_dates_heading_row = [top_left_cell_label] + balance_sheet.report_dates
    total_assets_row = ['Total Assets'] + balance_sheet.total_assets
    total_tan_assets_row = ['Total Tang Assets'] + balance_sheet.total_tangible_assets
    total_liabilities_row = ['Total Liabilities'] + balance_sheet.total_liabilities
    share_holder_equity_row = ['Book Value'] + balance_sheet.share_holder_equity
    tangible_book_value_row = ['Tan Book Value'] + balance_sheet.tangible_book_value

    # Create quarterly balance sheet table with graph
    balance_table_data = [
        all_report_dates_heading_row,
        total_assets_row,
        total_tan_assets_row,
        total_liabilities_row,
        share_holder_equity_row,
        tangible_book_value_row,
    ]
    for row in balance_table_data:
        worksheet.append(row)

    num_table_rows = len(balance_table_data)
    num_table_columns = len(balance_table_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='QuarterlyBalance',
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='blue',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Quarterly Balance',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        chart_type='bar',
    )

    # this is dumb but it's the easiest way I've found to add rows deeper down a sheet
    # instead of adding it with .append and then manually moving the range
    for i in range(15):
        worksheet.append([''])

    goodwill = ['Goodwill'] + balance_sheet.goodwill
    intangible_assets = ['Intangile Assets'] + balance_sheet.intangible_assets
    total_intangible_assets = ['Total Intangile Assets'] + balance_sheet.total_intangible_assets

    # Create quarterly income table with graph
    intangible_assets_data = [
        all_report_dates_heading_row,
        total_intangible_assets,
        goodwill,
        intangible_assets,
    ]
    for row in intangible_assets_data:
        worksheet.append(row)

    num_table_rows = len(intangible_assets_data)
    num_table_columns = len(intangible_assets_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='IntangibleAssets',
        row_offset=22,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='red',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Intangible Assets',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=22,
        chart_type='bar',
    )

    # this is dumb but it's the easiest way I've found to add rows deeper down a sheet
    # instead of adding it with .append and then manually moving the range
    for i in range(15):
        worksheet.append([''])

    current_liabilities = ['Curr Liabilities'] + balance_sheet.current_liabilities
    non_current_liabilities = ['Non Curr Liabilities'] + balance_sheet.non_current_liabilities

    # Create quarterly income table with graph
    liabilities_data = [
        all_report_dates_heading_row,
        current_liabilities,
        non_current_liabilities,
    ]
    for row in liabilities_data:
        worksheet.append(row)

    num_table_rows = len(liabilities_data)
    num_table_columns = len(liabilities_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Liabilities',
        row_offset=41,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='red',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Liabilities',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=41,
        chart_type='bar',
    )

def _add_income_sheet(workbook, income_statement, company_overview):
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='Income',
        tab_color='ff9191',
    )

    top_left_cell_label = '{} #s in 1000s'.format(income_statement.currency)
    all_report_dates_heading_row = [top_left_cell_label] + income_statement.all_report_dates
    all_revenue_row = ['Revenue'] + income_statement.all_revenue
    all_gross_row = ['Gross'] + income_statement.all_gross
    all_operating_income_row = ['Op Income'] + income_statement.all_operating_income
    all_net_income_row = ['Net'] + income_statement.all_net_income

    # Create quarterly income table with graph
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
        title='Quarterly',
        y_axis_label=income_statement.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
    )

    # this is dumb but it's the easiest way I've found to add rows deeper down a sheet
    # instead of adding it with .append and then manually moving the range
    for i in range(15):
        worksheet.append([''])

    # Create quarterly income growth table
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
        row_offset=21,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='red',
    )

    # Create yearly income growth table
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
        row_offset=26,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='purp',
    )

    # Add some random last remaining stats to round off a killer sheet >:)
    openpyxl_helper.add_cell(worksheet, 'G8', 'Fun Stats')
    openpyxl_helper.add_cell(worksheet, 'H8', 'Values')
    openpyxl_helper.add_cell(worksheet, 'G9', 'P/E Current')
    openpyxl_helper.add_cell(worksheet, 'H9', company_overview.pe_ratio)
    openpyxl_helper.add_cell(worksheet, 'G10', 'P/S TTM')
    openpyxl_helper.add_cell(worksheet, 'H10', company_overview.price_to_sales_ttm)
    openpyxl_helper.add_cell(worksheet, 'G11', 'P/B')
    openpyxl_helper.add_cell(worksheet, 'H11', company_overview.price_to_book)
    openpyxl_helper.add_cell(worksheet, 'G12', 'EPS')
    openpyxl_helper.add_cell(worksheet, 'H12', company_overview.earnings_per_share)
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Ratios',
        row_offset=8,
        column_offset=7,
        num_rows=5,
        num_columns=2,
        style='black',
        showRowStripes=False,
    )

main()
