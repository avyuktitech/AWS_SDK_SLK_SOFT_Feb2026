import boto3

AWS_REGION = 'us-east-1'
TABLE_NAME = 'SampleTable'

dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

# Insert (put) an item
item = {'id': '1', 'name': 'John Doe', 'age': 30}
table.put_item(Item=item)
print('Item inserted:', item)

# Query item by id
response = table.get_item(Key={'id': '1'})
if 'Item' in response:
    print('Queried item:', response['Item'])
else:
    print('Item not found')

# Scan all items
response = table.scan()
print('All items:', response['Items'])

# Update item
response = table.update_item(
    Key={'id': '1'},
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={':val1': 31},
    ReturnValues='UPDATED_NEW'
)
print('Updated item age:', response['Attributes'])

# Delete item
response = table.delete_item(Key={'id': '1'})
print('Item deleted with id 1')
