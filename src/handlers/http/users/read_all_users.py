import logging
import os

from src.handlers.http.users import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        result = table.scan()
    
        logger.info(f'Incoming request is: {event}')
        logger.info(f'result: {result}')
        logger.info(f"result[Items]: {result['Items']}")

        item = result.get("Items")

        return http_response(data=item, status_code=200)
    
    except:
        return http_response("Sem resposta", status_code=500)