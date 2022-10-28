import os
import json
import uuid
import logging


from src.handlers.http.games import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event.get("body"))
    logger.info("BODY:: %s" % data)
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'gamename': data.get('gamename'),
        'category': data.get('category'),
        'platform': data.get('platform'),
        'rating': data.get('rating')
    }
    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
