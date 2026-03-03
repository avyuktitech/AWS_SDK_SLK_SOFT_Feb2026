import boto3

AWS_REGION = 'us-east-1'

dynamodb = boto3.client('dynamodb', region_name=AWS_REGION)

response = dynamodb.create_table(
    TableName='UsersTable',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print('Table created:', response['TableDescription']['TableName'])
