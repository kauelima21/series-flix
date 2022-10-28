import json
import logging
import os
import uuid

from src.handlers.http.series import dynamodb
from src.lib.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event.get("body"))

    logger.info("BODY:: %s" % data)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
