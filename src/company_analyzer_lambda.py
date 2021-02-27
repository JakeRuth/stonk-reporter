import base64

from stonks import base_api

from . import company_analyzer_v1

def lambda_handler(event, context):
    stonk_ticker = event["queryStringParameters"]['ticker']

    try:
        workbook = company_analyzer_v1.run(stonk_ticker)
    except base_api.StonkApiException as exc:
        print(str(exc))
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps({
                'error': str(exc),
            }),
        }

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
