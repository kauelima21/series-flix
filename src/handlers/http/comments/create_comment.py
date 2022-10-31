import json
import logging
import os
import uuid
from datetime import datetime

from src.handlers.http.comments import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event.get("body"))

    logger.info("BODY:: %s" % data)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'content': data.get("content"),
        'user_id': data.get("user_id"),
        'model_id': data.get("model_id"),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
