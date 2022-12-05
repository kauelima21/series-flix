import json
import logging
import os
import uuid
from datetime import datetime

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
        'category': data.get("category"),
        'launch_date': data.get("launch_date"),
        'rating': data.get("rating"),
        'seasons': data.get("seasons"),
        'synopsis': data.get("synopsis"),
        'title': data.get("title"),
        'img_src': data.get("img_src"),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat(),
    }

    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
