import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Users')

    table.update_item(
        Key={
            'id': 1,
        },
        UpdateExpression="set age = :g",
        ExpressionAttributeValues={
            ':g': 24
        },
        ReturnValues="UPDATED_NEW"
    )


