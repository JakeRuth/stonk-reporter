from stonk_wrapper import financial_data

data = financial_data.FinancialData('APHA')
print (data.income_statement.all_quarterly_revenue)
