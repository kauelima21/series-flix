import json
import logging
import os
import datetime

from src.handlers.http.games import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    data = json.loads(event['body'])
    params = event.get("pathParameters")
    
    id = params.get("id")

    gamename = data.get('gamename')
    category = data.get('category')
    platform = data.get('platform')
    rating = data.get('rating')
    updatedAt = datetime.datetime.now().isoformat()

    updateExpression = []
    updateExpression.append('gamename = :gamename')
    updateExpression.append('category = :category')
    updateExpression.append('platform = :platform')
    updateExpression.append('rating = :rating')
    updateExpression.append('updatedAt = :updatedAt')
    updateExpression = "SET " + ', '.join(updateExpression)

    expressionAttributeValues = {}
    expressionAttributeValues[':gamename'] = gamename
    expressionAttributeValues[':category'] = category
    expressionAttributeValues[':platform'] = platform
    expressionAttributeValues[':rating'] = rating
    expressionAttributeValues[':updatedAt'] = updatedAt

    result = table.update_item(
        Key = {
            'id': id
        },
        UpdateExpression = updateExpression,
        ExpressionAttributeValues = expressionAttributeValues,
        ReturnValues = "UPDATED_NEW"
    )

    status_code = 200
    return http_response(data=result, status_code=status_code)