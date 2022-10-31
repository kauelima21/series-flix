import json
import logging
import os
import uuid

from src.handlers.http.movies import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    data = json.loads(event.get("body"))

    logger.info("BODY:: %s" % data)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'nome' : data.get('nome'),
        'duration' : data.get('duration'),
        'rating' : data.get('rating'),
        'gender' : data.get('gender')
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
