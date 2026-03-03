import boto3


def lambda_handler(event, context):
    db = boto3.resource('dynamodb')

    table = db.Table('Users')

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'id': 1,
                'name': 'parwiz',
                'age': '20'
            }
        )

        batch.put_item(
            Item={
                'id': 2,
                'name': 'john',
                'age': '20'
            }
        )

        batch.put_item(
            Item={
                'id': 3,
                'name': 'abc',
                'age': '37'
            }
        )