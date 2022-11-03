import logging
import os

from src.handlers.http.series import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def read_serie(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    print(event)

    params = event.get("pathParameters")
    id = params.get("id")

    result = table.get_item(
        Key={
            'id': id
        }
    )
    item = result.get("Item")
    status_code = 200
    if not item:
        status_code = 404
        item = f'{id} not found!'

    return http_response(data=item, status_code=status_code)


def read_series(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()
    logger.info(f'Incoming request is: {event}')
    logger.info(f'result: {result}')
    logger.info(f"result[Items]: {result['Items']}")

    item = result.get("Items")

    return http_response(data=item, status_code=200)


def handler(event, context):
    print("event", event)
    logger.info("TABLE:: %s" % os.getenv('DYNAMODB_TABLE'))
    route = event.get("path")

    if route == '/series':
        return read_series(event)
    return read_serie(event)
