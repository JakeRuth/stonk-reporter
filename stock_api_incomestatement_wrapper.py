import os

import openpyxl as xl
from openpyxl.worksheet import table as xltable
from openpyxl import utils as xlutils

class IncomeStatementWrapper:
    def __init__(self, income_statement_json, ticker):
        self.income_statement = income_statement_json
        self.ticker = ticker

    @property
    def create_and_open_yearly_revenue_excel(self):
        annual_reports = self.income_statement['annualReports']
        workbook = xl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'Income Annual'
        worksheet.sheet_properties.tabColor = 'ff9191'
        
        # top left most cell shows ticker + currency
        column_headings = ['{} ({})'.format(self.ticker, annual_reports[0]['reportedCurrency'])]
        data = [
            ['Revenue'],
            ['Gross'],
            ['Op Inc'],
            ['EBIT'],
            ['Net'],
        ]
        for report in annual_reports:
            column_headings.append(report['fiscalDateEnding'])
            data[0].append(int(report['totalRevenue']))
            data[1].append(int(report['grossProfit']))
            data[2].append(int(report['operatingIncome']))
            data[3].append(int(report['ebit']))
            data[4].append(int(report['netIncome']))

        worksheet.append(column_headings)
        for row in data:
            worksheet.append(row)
        
        worksheet.add_table(xltable.Table(
            displayName='Annual_Income',
            # If this isn't specified the program will crash in a cryptic way
            ref='A1:F6',
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

        workbook.save('income_annual_apha.xlsx')
        os.startfile('income_annual_apha.xlsx')
