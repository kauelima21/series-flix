import datetime
import json
import logging
import os

from src.handlers.http.comments import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    params = event.get("pathParameters")
    id = params.get("id")

    content = data.get("content")

    updatedAt = datetime.datetime.now().isoformat()

    table.update_item(Key={'id': id},
                        UpdateExpression = "SET content = :content, updated_at = :updated_at",
                        ExpressionAttributeValues = {
                            ':content': content,
                            ':updated_at': updatedAt
                        },
                        ReturnValues="UPDATED_NEW")


    return http_response(data='updated!', status_code=200)
