import logging
import os

from src.handlers.http.games import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def read_game(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    params = event.get("pathParameters")

    id = params.get("id")

    result = table.query(
        KeyConditionExpression = 'id = :id',
        ExpressionAttributeValues = {':id': id}
    )
    
    if not result:
        status_code = 404
        result = f'{id} not found!'
        
    status_code = 200
    return http_response(data=result, status_code=status_code)


def read_games(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()
    logger.info(f'Incoming request is: {event}')
    logger.info(f'result: {result}')
    logger.info(f"result[Items]: {result['Items']}")

    item = result.get("Items")

    if not item:
        status_code = 404
        item = 'Not found!'

    status_code = 200
    return http_response(data=item, status_code=status_code)


def handler(event, context):
    logger.info("TABLE:: %s" % os.getenv('DYNAMODB_TABLE'))
    route = event.get("path")

    if route == '/games':
        return read_games(event)
    return read_game(event)
