import logging
import os

from src.handlers.http.users import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    params = event.get("pathParameters")
    id = params.get("id")

    try:
        result = table.get_item(
            Key={
                'id': id
            }
        )
    except:
        response = {
            "statusCode": 500,
            'headers': {'Content-Type': 'application/json'},
            "body": "Internal server error"
        }
        return response
        
    if 'Item' in result:
        result = table.delete_item(
            Key={
                'id': id
            }
        )
        print(result)
        
        return http_response(data='deleted!', status_code=200)
