import os
import json
import uuid
<<<<<<< HEAD:src/handlers/http/series/create_serie.py
import datetime
=======
import logging
>>>>>>> 4294b1ba7d741f7a46d4574291b887b432fd2d29:src/handlers/http/games/create_game.py

from src.handlers.http.games import dynamodb
from src.libraries.utils import http_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    data = json.loads(event.get("body"))
    logger.info("BODY:: %s" % data)
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
<<<<<<< HEAD:src/handlers/http/series/create_serie.py
        'title': data.get('title'),
        'synopsis': data.get('synopsis'),
        'launch_date': data.get('launch_date'),
        'seasons': data.get('seasons'),
        'category': data.get('category'),
        'rating': data.get('rating'),
        "created_at": datetime.datetime.now().isoformat(),
        "updated_at": datetime.datetime.now().isoformat()
        
=======
        'game_name': data.get('game_name'),
        'category': data.get('category'),
        'platform': data.get('platform'),
        'rating': data.get('rating')
>>>>>>> 4294b1ba7d741f7a46d4574291b887b432fd2d29:src/handlers/http/games/create_game.py
    }
    table.put_item(Item=item)

    return http_response(data=item, status_code=200)
