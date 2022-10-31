import logging
import os

from src.handlers.http.users import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    return http_response(data=item, status_code=200)