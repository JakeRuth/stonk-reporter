import boto3
import botocore
import json
import requests


BUCKET_NAME = 'stonk-cache'
s3_client = boto3.client('s3')

class StonkApiException(Exception):
    pass

def DEV_get_cached_api_filename(stonk_ticker, api_call, api_name):
    return 'src/stonks/cached_api_calls/{}_{}_{}.json'.format(stonk_ticker, api_call, api_name).lower()

def DEV_save_api_response(stonk_ticker, api_call, api_name, res_json):
    filename = DEV_get_cached_api_filename(stonk_ticker, api_call, api_name)
    file = open(filename, 'w+')
    file.write(json.dumps(res_json))
    file.close()

def DEV_query_api_cache(stonk_ticker, api_call, api_name):
    filename = DEV_get_cached_api_filename(stonk_ticker, api_call, api_name)
    print('DEV: Looking in cache for {}'.format(filename))
    try:
        with open(filename) as json_file:
            print('DEV: Cache HIT for {}'.format(filename))
            return json.load(json_file)
    except FileNotFoundError:
        print('DEV: No cache found for {}'.format(filename))

def get_cached_api_filename(stonk_ticker, api_call, api_name):
    return '{}_{}_{}.json'.format(stonk_ticker, api_call, api_name).lower()

def save_api_response(stonk_ticker, api_call, api_name, res_json):
    filename = get_cached_api_filename(stonk_ticker, api_call, api_name)
    full_path = '/tmp/{}'.format(filename)
    file = open(full_path, 'w+')
    file.write(json.dumps(res_json))
    file.close()

    s3_client.upload_file(full_path, BUCKET_NAME, filename)

def query_api_cache(stonk_ticker, api_call, api_name):
    filename = get_cached_api_filename(stonk_ticker, api_call, api_name)
    print('Looking in cache for {}'.format(filename))
    try:
        s3_clientobj = s3_client.get_object(Bucket=BUCKET_NAME, Key=filename)
    except botocore.exceptions.ClientError as exc:
        print('No cache found for {}'.format(filename))
        print('Exc: {}'.format(str(exc)))
        return

    print('Cache HIT for {}'.format(filename))
    return json.loads(s3_clientobj['Body'].read().decode('utf-8'))

class BaseStonkApiWrapper:
    def __init__(self, stonk_ticker, api_key, api_name, developer_mode):
        self.stonk_ticker = stonk_ticker
        self.api_key = api_key
        self.api_name = api_name
        self.developer_mode = developer_mode

    def get_json(self, url, api_function):
        # Check cache for file first
        if self.developer_mode:
            cached_response = DEV_query_api_cache(self.stonk_ticker, api_function, self.api_name)
        else:
            cached_response = query_api_cache(self.stonk_ticker, api_function, self.api_name)

        if cached_response:
            return cached_response

        response = requests.get(url).json()
        if self.should_cache_api_response(response):
            if self.developer_mode:
                DEV_save_api_response(self.stonk_ticker, api_function, self.api_name, response)
            else:
                save_api_response(self.stonk_ticker, api_function, self.api_name, response)

        return response

    # this can be overridden for bad api responses that would be very bad to cache for later
    def should_cache_api_response(response):
        return True

    def get_income_statements(self):
        raise NotImplementedError()

    def get_cashflows(self):
        raise NotImplementedError()

    def get_balance_sheets(self):
        raise NotImplementedError()

    def get_company_overview(self):
        raise NotImplementedError()
