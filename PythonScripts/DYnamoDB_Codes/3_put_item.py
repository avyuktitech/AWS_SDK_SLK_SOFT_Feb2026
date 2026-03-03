import boto3

AWS_REGION = 'us-east-1'
TABLE_NAME = 'SampleTable'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

item = {'id': '1', 'name': 'John Doe', 'age': 30}
table.put_item(Item=item)
print('Item inserted:', item)
