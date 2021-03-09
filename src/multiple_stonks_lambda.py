import base64

import multiple_stonks_v1

def lambda_handler(event, context):
    stonk_tickers = event["queryStringParameters"]['ticker'].strip().split(',')
    trimmed_stonk_tickers = [ticker.strip() for ticker in stonk_tickers]
    workbook = multiple_stonks_v1.run(trimmed_stonk_tickers)

    workbook.save('/tmp/spreadsheet.xlsx')

    file_to_return = open('/tmp/spreadsheet.xlsx', 'rb')
    file_to_return_data = file_to_return.read()
    file_to_return.close()

    binary_data = base64.b64encode(file_to_return_data).decode('utf-8')
    return {
        'headers': { "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" },
        'statusCode': 200,
        # might have to decode utf8 as well
        'body': binary_data,
        'isBase64Encoded': True
    }
