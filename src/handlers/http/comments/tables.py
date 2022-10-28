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
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
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
