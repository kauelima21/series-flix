import os
import boto3

def create_table(endpoint_url=None):
    if endpoint_url:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    else:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName=os.environ['DYNAMODB_TABLE'],
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }

        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'LSI_NAME',
                'KeySchema': [
                    {
                        'AttributeName': 'nome',
                        'KeyType': 'HASH'
                    }


                ],
                # Note: since we are projecting all the attributes of the table
                # into the LSI, we could have set ProjectionType=ALL and
                # skipped specifying the NonKeyAttributes
                'Projection': {
                    'ProjectionType': 'ALL'
                   # 'NonKeyAttributes': ['imageid', 'last_like_userid', 'total_likes']
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 123,
                    'WriteCapacityUnits': 123
                }

            }
        ],


        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'nome',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }

    )
    # Wait until the table exists.
    table.wait_until_exists()
    print(table)

