import logging
import os

import boto3
from src.handlers.http.series.tables import create_table

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if 'LOCALSTACK_HOSTNAME' in os.environ:
    dynamodb_endpoint = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
else:
    dynamodb = boto3.resource('dynamodb')
    dynamodb_endpoint = None


def create_database_if_not_exists():
    existing_tables = [table.name for table in dynamodb.tables.all()]
    table_name = os.environ['DYNAMODB_TABLE']

    logger.info("TABLES:: %s" % existing_tables)
    logger.info("TABLE NAME:: %s" % table_name)

    logger.info(f'existing_tables: {existing_tables}')
    if table_name not in existing_tables:
        create_table(dynamodb_endpoint)


create_database_if_not_exists()
