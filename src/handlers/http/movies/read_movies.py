import logging
import os
from boto3.dynamodb.conditions import Key

from src.handlers.http.movies import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def read_movie(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    params = event.get('pathParameters')
    id = params.get('id')

    result = table.get_item( Key ={"id": id})

    item = result.get("Item")
    status_code = 200
    if not item:
        status_code = 404
        item = f'{id} not found!'

    return http_response(data=item, status_code=status_code)


def read_movies(event):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    print(event)

    filter  = event.get("queryStringParameters")

    if filter is None:
        result = table.scan()
        logger.info(f'Incoming request is: {event}')
        logger.info(f'result: {result}')
        logger.info(f"result[Items]: {result['Items']}")

        item = result.get("Items")

        return http_response(data=item, status_code=200)


    if 'nome' in filter:
        resultado = filter.get('nome')
        query = table.query(IndexName="LSI_NAME",KeyConditionExpression=Key('nome').eq(resultado)) #não quero um matrix, se tiver mais de um matrix, traz os dois
        print(query)
        item = query.get("Items")
        return http_response(data=item, status_code=200)



def handler(event, context):
    print("event", event)
    logger.info("TABLE:: %s" % os.getenv('DYNAMODB_TABLE'))
    route = event.get("path")

    print(route)


    if route == '/movies':
        return read_movies(event)
    return read_movie(event)


