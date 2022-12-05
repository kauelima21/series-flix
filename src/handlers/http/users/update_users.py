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
    params = event.get("pathParameters")
    id = params.get("id")

    username = data.get("username")
    first_name = data.get("first_name")
    surname = data.get("surname")
    age = data.get("age")
    updated_at = datetime.now().isoformat()

    updateExpression = []
    updateExpression.append('username = :username')
    updateExpression.append('first_name = :first_name')
    updateExpression.append('surname = :surname')
    updateExpression.append('age = :age')
    updateExpression.append('updated_at = :updated_at')
    updateExpression = "SET " + ', '.join(updateExpression)

    expressionAttributeValues = {}
    expressionAttributeValues[':username'] = username
    expressionAttributeValues[':first_name'] = first_name
    expressionAttributeValues[':surname'] = surname
    expressionAttributeValues[':age'] = age
    expressionAttributeValues[':updated_at'] = updated_at

    table.update_item(Key={'id': id},
                        UpdateExpression = updateExpression,
                        ExpressionAttributeValues = expressionAttributeValues,
                        ReturnValues="UPDATED_NEW")


    return http_response(data='updated!', status_code=200)
    # item = {
    #     'id': event['pathParameters']['id'],
    #     'username': data.get("username"),
    #     'name': data.get("name"),
    #     'surname': data.get("surname"),
    #     'age': data.get("age"),
    #     'created_at': datetime.now().isoformat(),
    #     'updated_at': datetime.now().isoformat(),
    # }

    # table.put_item(Item=item)

    # return http_response(data=item, status_code=200)
