from datetime import datetime
import json
import logging
import os

from src.handlers.http.users import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': event['pathParameters']['id'],
        'username': data.get("username"),
        'name': data.get("name"),
        'surname': data.get("surname"),
        'age': data.get("age"),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
