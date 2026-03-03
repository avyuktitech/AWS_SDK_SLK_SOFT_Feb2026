import boto3

db = boto3.client('dynamodb')

response = db.update_table(
    TableName='employee',
    BillingMode='PROVISIONED',

    ProvisionedThroughput={
        'ReadCapacityUnits':1,
        'WriteCapacityUnits':1
    }
)

print(response)