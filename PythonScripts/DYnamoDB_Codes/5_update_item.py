import boto3

AWS_REGION = 'us-east-1'
TABLE_NAME = 'SampleTable'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

response = table.update_item( # Update item with id '1' to set age to 31
    Key={'id': '1'}, 
    UpdateExpression='SET age = :val1', # Update expression to set age attribute
    ExpressionAttributeValues={':val1': 31}, # Value for the update expression
    ReturnValues='UPDATED_NEW'
)
print('Updated item age:', response['Attributes'])
