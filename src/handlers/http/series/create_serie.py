import json
import logging
import os
import uuid
import datetime

from src.handlers.http.series import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event.get("body"))

    logger.info("BODY:: %s" % data)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'title': data.get('title'),
        'synopsis': data.get('synopsis'),
        'launch_date': data.get('launch_date'),
        'seasons': data.get('seasons'),
        'category': data.get('category'),
        'rating': data.get('rating'),
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
        
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
