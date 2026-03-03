import boto3

db = boto3.client('dynamodb')

response = db.get_item(
    TableName='employee',
    Key={
        'emp_id':{
            'S':'2'
        }
    }
)

print(response['Item'])