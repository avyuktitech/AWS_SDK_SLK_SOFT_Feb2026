# This script Scans SynamoDB

import boto3
AWS_REGION = 'us-east-1'
TABLE_NAME = 'SLkDynamoDBTable222'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

response = table.scan()
print("All Table Scan successful. Items:")
