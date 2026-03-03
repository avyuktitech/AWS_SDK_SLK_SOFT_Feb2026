import boto3

AWS_REGION = 'us-east-1'
TABLE_NAME = 'SampleTable'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

response = table.get_item(Key={'id': '1'})
if 'Item' in response:
    print('Queried item:', response['Item'])
else:
    print('Item not found')
