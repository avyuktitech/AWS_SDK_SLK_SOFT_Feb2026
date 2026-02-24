# This scrpt created a DynamoDB table using boto3 library.
import boto3
AWS_Region = 'us-east-1'
dynamodb = boto3.client('dynamodb', region_name=AWS_Region)
response = dynamodb.create_table(
    TableName='SLkDynamoDBTable222',
    KeySchema=[
        {
            'AttributeName': 'Empid',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Empid',
            'AttributeType': 'S'  # String type
        }
    ],
    ProvisionedThroughput={ 
        'ReadCapacityUnits': 5, #5 is the number of read capacity units, which determines how many read operations per second the table can handle.
        'WriteCapacityUnits': 5 #5 is the number of write capacity units, which determines how many write operations per second the table can handle.
    }
)
print("Table created successfully:", response['TableDescription']['TableName'])
