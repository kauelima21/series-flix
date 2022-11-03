import logging
import os
import json

from src.handlers.http.movies import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    params = event.get("pathParameters")
    id = params.get("id")

    resultado = table.get_item(
        Key={
            'id': id
        }
    )

    if "Item" in resultado:
        item = {
            "id": id,
            "nome": data.get('nome'),
            "duration": data.get('duration'),
            "rating": data.get('rating'),
            "gender": data.get('gender')
        }

        retorno = table.put_item(Item=item)
        status_code = 200

        return http_response(data=item, status_code=status_code)
    else:
        status_code = 404
        return http_response(data='Sem resultado', status_code=status_code)
