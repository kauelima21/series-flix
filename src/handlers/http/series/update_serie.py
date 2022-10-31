import datetime
import json
import logging
import os

from src.handlers.http.series import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    params = event.get("pathParameters")
    id = params.get("id")

    title = data.get("title")
    category = data.get("category")
    launch_date = data.get("launch_date")
    seasons = data.get("seasons")
    rating = data.get("rating")
    synopsis = data.get("synopsis")
    updatedAt = datetime.datetime.now().isoformat()

    updateExpression = []
    updateExpression.append('title = :title')
    updateExpression.append('category = :category')
    updateExpression.append('launch_date = :launch_date')
    updateExpression.append('rating = :rating')
    updateExpression.append('seasons = :seasons')
    updateExpression.append('synopsis = :synopsis')
    updateExpression.append('updatedAt = :updatedAt')
    updateExpression = "SET " + ', '.join(updateExpression)

    expressionAttributeValues = {}
    expressionAttributeValues[':title'] = title
    expressionAttributeValues[':category'] = category
    expressionAttributeValues[':launch_date'] = launch_date
    expressionAttributeValues[':rating'] = rating
    expressionAttributeValues[':seasons'] = seasons
    expressionAttributeValues[':synopsis'] = synopsis
    expressionAttributeValues[':updatedAt'] = updatedAt

    table.update_item(Key={'id': id},
                        UpdateExpression = updateExpression,
                        ExpressionAttributeValues = expressionAttributeValues,
                        ReturnValues="UPDATED_NEW")


    return http_response(data='updated!', status_code=200)
