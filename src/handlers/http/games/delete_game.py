import json
import logging
import os

from src.handlers.http.games import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    params = event.get("pathParameters")

    id = params.get("id")

    result = table.delete_item(
        Key = {
            'id': id
        }
    )
    
    status_code = 200
    return http_response(data="success!", status_code=status_code)
