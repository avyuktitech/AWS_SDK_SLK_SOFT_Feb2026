# This scripts queries items from DynamoDB table using boto3 library.
import boto3
AWS_REGION = 'us-east-1'
TABLE_NAME = 'SLkDynamoDBTable222'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)  

response = table.get_item(Key={'Empid': 'E001'})
if 'Item' in response:
    print("Item retrieved successfully:", response['Item']) 
else:
    print("Item not found with Empid: E001")