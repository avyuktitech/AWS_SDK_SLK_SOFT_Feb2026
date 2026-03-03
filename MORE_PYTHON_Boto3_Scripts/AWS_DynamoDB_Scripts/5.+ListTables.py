import boto3


db = boto3.client('dynamodb')


response = db.list_tables()

print(response['TableNames'])