import json
import os

import openpyxl as pyxl

from excel import openpyxl_helper
from stonks import base_api, financial_data


def run(stock_ticker, developer_mode=False):
    try:
        data = financial_data.FinancialData(stock_ticker, developer_mode)
    except base_api.StonkApiException as exc:
        print(str(exc))
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps({
                'error': str(exc),
            }),
        }
    income_statement = data.income_statement
    company_overview = data.company_overview
    balance_sheet = data.balance_sheet
    cashflow = data.cashflow

    workbook = pyxl.Workbook()
    _add_income_sheet(workbook, income_statement, company_overview, cashflow)
    _add_balance_sheet(workbook, balance_sheet)
    _add_cashflow_sheet(workbook, cashflow)

    return workbook

def _add_cashflow_sheet(workbook, cashflow):
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='Cashflow',
        tab_color='92D050',
        index=2,
    )

    top_left_cell_label = '{} #s in 1000s'.format(cashflow.currency)
    all_report_dates_heading_row = [top_left_cell_label] + cashflow.report_dates
    operations_row = ['Operations'] + cashflow.operations
    financing_row = ['Financing'] + cashflow.financing
    investing_row = ['Investing'] + cashflow.investing

    cashflow_data = [
        all_report_dates_heading_row,
        operations_row,
        financing_row,
        investing_row,
    ]
    for row in cashflow_data:
        worksheet.append(row)

    num_table_rows = len(cashflow_data)
    num_table_columns = len(cashflow_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Cashflows',
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='blue',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Cashflows',
        y_axis_label=cashflow.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        chart_type='line',
    )

    for i in range(15):
        worksheet.append([''])

    free_cash_flow = ['Free Cash Flow'] + cashflow.free_cash_flow

    free_cash_flow_data = [
        all_report_dates_heading_row,
        free_cash_flow,
    ]
    for row in free_cash_flow_data:
        worksheet.append(row)

    num_table_rows = len(free_cash_flow_data)
    num_table_columns = len(free_cash_flow_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='FCF',
        row_offset=20,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='purp',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='FCF',
        y_axis_label=cashflow.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=20,
        chart_type='area',
    )

def _add_balance_sheet(workbook, balance_sheet):
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='Balance',
        tab_color='FFFF00',
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

    for i in range(15):
        worksheet.append([''])

    goodwill = ['Goodwill'] + balance_sheet.goodwill
    intangible_assets = ['Intangible Assets'] + balance_sheet.intangible_assets
    total_intangible_assets = ['Total Intangible Assets'] + balance_sheet.total_intangible_assets

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
        style='purp',
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

    for i in range(15):
        worksheet.append([''])

    current_assets = ['Curr Assets'] + balance_sheet.current_assets
    current_liabilities = ['Curr Liabilities'] + balance_sheet.current_liabilities

    # Create quarterly income table with graph
    current_data = [
        all_report_dates_heading_row,
        current_assets,
        current_liabilities,
    ]
    for row in current_data:
        worksheet.append(row)

    num_table_rows = len(current_data)
    num_table_columns = len(current_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Current',
        row_offset=41,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='red',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Current',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=41,
        chart_type='bar',
    )

    for i in range(15):
        worksheet.append([''])

    non_current_assets = ['Non Curr Assets'] + balance_sheet.non_current_assets
    non_current_liabilities = ['Non Curr Liabilities'] + balance_sheet.non_current_liabilities

    non_current_data = [
        all_report_dates_heading_row,
        non_current_assets,
        non_current_liabilities,
    ]
    for row in non_current_data:
        worksheet.append(row)

    num_table_rows = len(non_current_data)
    num_table_columns = len(non_current_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='NonCurrent',
        row_offset=59,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='red',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='NonCurrent',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=59,
        chart_type='bar',
    )

    for i in range(15):
        worksheet.append([''])

    non_current_debt = ['Curr Debt'] + balance_sheet.current_debt
    long_term_debt = ['Long Term Debt'] + balance_sheet.long_term_debt

    debt_data = [
        all_report_dates_heading_row,
        non_current_debt,
        long_term_debt,
    ]
    for row in debt_data:
        worksheet.append(row)

    num_table_rows = len(debt_data)
    num_table_columns = len(debt_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Debt',
        row_offset=77,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='teal',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Debt',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=77,
        chart_type='bar',
    )

    for i in range(15):
        worksheet.append([''])

    cash = ['Cash'] + balance_sheet.cash

    cash_data = [
        all_report_dates_heading_row,
        cash,
    ]
    for row in cash_data:
        worksheet.append(row)

    num_table_rows = len(cash_data)
    num_table_columns = len(cash_data[0])
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Cash',
        row_offset=95,
        num_rows=num_table_rows,
        num_columns=num_table_columns,
        style='green',
    )
    openpyxl_helper.add_graph(
        worksheet=worksheet,
        title='Cash',
        y_axis_label=balance_sheet.currency,
        num_columns=num_table_columns,
        num_rows=num_table_rows,
        row_offset=95,
        chart_type='area',
    )

def _add_income_sheet(workbook, income_statement, company_overview, cashflow):
    worksheet = openpyxl_helper.add_sheet(
        workbook=workbook,
        name='Income',
        tab_color='ff9191',
        index=0,
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
        chart_type='line',
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

    openpyxl_helper.add_cell(worksheet, 'G8', 'Fun Stats')
    openpyxl_helper.add_cell(worksheet, 'H8', 'Values')
    openpyxl_helper.add_cell(worksheet, 'G9', 'P/E Current')
    openpyxl_helper.add_cell(worksheet, 'H9', company_overview.pe_ratio)
    openpyxl_helper.add_cell(worksheet, 'G10', 'P/S TTM')
    openpyxl_helper.add_cell(worksheet, 'H10', company_overview.price_to_sales_ttm)
    openpyxl_helper.add_cell(worksheet, 'G11', 'P/B')
    openpyxl_helper.add_cell(worksheet, 'H11', company_overview.price_to_book)
    openpyxl_helper.add_cell(worksheet, 'G12', 'P/FCF')
    openpyxl_helper.add_cell(worksheet, 'H12', company_overview.price_to_fcf)
    openpyxl_helper.add_cell(worksheet, 'G13', 'EPS')
    openpyxl_helper.add_cell(worksheet, 'H13', company_overview.earnings_per_share)
    openpyxl_helper.add_cell(worksheet, 'G14', 'Mcap 1000s')
    openpyxl_helper.add_cell(worksheet, 'H14', company_overview.market_cap)
    openpyxl_helper.add_cell(worksheet, 'G15', 'FCF TTM 1000s')
    openpyxl_helper.add_cell(worksheet, 'H15', cashflow.free_cash_flow_ttm)
    openpyxl_helper.add_table(
        worksheet=worksheet,
        name='Ratios',
        row_offset=8,
        column_offset=7,
        num_rows=8,
        num_columns=2,
        style='black',
        showRowStripes=False,
    )

def run_local():
    stonk_ticker = 'APHA'
    workbook = run(stonk_ticker, True)
    filename = '{}_overview_v1.xlsx'.format(stonk_ticker)
    workbook.save(filename)
    os.startfile(filename)
run_local()
