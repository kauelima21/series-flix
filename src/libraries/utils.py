import datetime
import decimal
import json
import logging
import os
from json import dumps

# from pytz import timezone
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def float_to_decimal(s):
    return decimal.Decimal(str(round(float(s), 2)))


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def http_response(data, status_code=422, dump=True, sort=True):
    if dump:
        data = dumps(data, cls=DecimalEncoder, sort_keys=sort)

    return {
        "statusCode": status_code,
        "body": data,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
        },
    }


def msg_response(message) -> dict:
    return {"message": f"{message}"}


class HttpResponse400(Exception):
    CODE = 400


class HttpResponse404(Exception):
    CODE = 404


class HttpResponse403(Exception):
    CODE = 403


class HttpResponse422(Exception):
    CODE = 422


class HttpResponse200(Exception):
    STATUS_CODE = 200


def get_current_time() -> datetime:
    time = datetime.datetime.now()
    return time


def get_dynamodb_endpoint():
    if 'LOCALSTACK_HOSTNAME' in os.environ:
        dynamodb_endpoint = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
    else:
        dynamodb_endpoint = None
    return dynamodb_endpoint


def get_dynamodb():
    if 'LOCALSTACK_HOSTNAME' in os.environ:
        dynamodb_endpoint = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
    else:
        dynamodb = boto3.resource('dynamodb')
    return dynamodb


def create_table(endpoint_url=None):
    if endpoint_url:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    else:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName=os.environ['DYNAMODB_TABLE'],
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }

    )
    # Wait until the table exists.
    table.wait_until_exists()
    logger.info(table)


def create_database_if_not_exists():
    dynamodb = get_dynamodb()
    existing_tables = [table.name for table in dynamodb.tables.all()]
    table_name = os.environ['DYNAMODB_TABLE']
    logger.info(f'existing_tables: {existing_tables}')
    dynamodb_endpoint = get_dynamodb_endpoint()
    if table_name not in existing_tables:
        create_table(dynamodb_endpoint)
