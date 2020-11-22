import os

import excel_helpers
import openpyxl as xl
from openpyxl.worksheet import table as xltable
from openpyxl import utils as xlutils


EXCEL_FILENAME = 'income_annual_apha.xlsx'

class IncomeStatementWrapper:
    def __init__(self, income_statement_json, ticker):
        self.income_statement = income_statement_json
        self.ticker = ticker
        self.workbook = xl.Workbook()

    def open_excel_sheet(self):
        os.startfile(EXCEL_FILENAME)

    def add_yearly_revenue_sheet(self):
        annual_reports = self.income_statement['annualReports']
        worksheet = self.workbook.create_sheet('Income Annual', 0)
        worksheet.sheet_properties.tabColor = 'ff9191'
        self._generate_excel_file(annual_reports, worksheet, 'Annual')

    def add_quarterly_revenue_sheet(self):
        quarterly_reports = self.income_statement['quarterlyReports']
        worksheet = self.workbook.create_sheet('Income Quarterly', 1)
        worksheet.sheet_properties.tabColor = '91ff91'
        self._generate_excel_file(quarterly_reports, worksheet, 'Quarterly')

    def _generate_excel_file(self, reports, worksheet, table_name):
        # top left most cell shows ticker + currency
        column_headings = ['{} ({})'.format(self.ticker, reports[0]['reportedCurrency'])]
        data = [
            ['Revenue'],
            ['Gross'],
            ['Op Inc'],
            ['EBIT'],
            ['Net'],
        ]
        for report in reports:
            column_headings.append(report['fiscalDateEnding'])
            data[0].append(excel_helpers.string_to_float(report['totalRevenue']))
            data[1].append(excel_helpers.string_to_float(report['grossProfit']))
            data[2].append(excel_helpers.string_to_float(report['operatingIncome']))
            data[3].append(excel_helpers.string_to_float(report['ebit']))
            data[4].append(excel_helpers.string_to_float(report['netIncome']))

        worksheet.append(column_headings)
        for row in data:
            worksheet.append(row)

        worksheet.add_table(xltable.Table(
            displayName=table_name,
            # If this isn't specified the program will crash in a cryptic way
            ref='A1:AA6',
            tableStyleInfo=xltable.TableStyleInfo(
                name='TableStyleMedium9',
                showFirstColumn=True,
                showLastColumn=False,
                showRowStripes=True,
                showColumnStripes=False,
            )
        ))

        for i in range(len(column_headings)):
            worksheet.column_dimensions[xlutils.get_column_letter(i + 1)].width = 15

        self.workbook.save(EXCEL_FILENAME)
