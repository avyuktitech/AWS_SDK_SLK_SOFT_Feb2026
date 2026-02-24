# This Script  inputs items inti DynamoDB table using boto3 library.

import boto3
AWS_REGION = 'us-east-1'
TABLE_NAME = 'SLkDynamoDBTable222'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

item = {
    'Empid': 'E001',    
    'Name': 'John Doe',
    'Department': 'HR',
    'Salary': 50000
}
table.put_item(Item=item)
print("Item inserted successfully:", item)