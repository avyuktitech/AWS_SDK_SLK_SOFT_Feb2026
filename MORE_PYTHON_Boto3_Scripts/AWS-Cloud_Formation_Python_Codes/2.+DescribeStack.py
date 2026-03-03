import boto3


cf_client = boto3.client('cloudformation')

response = cf_client.describe_stacks(
    StackName='dynamostack'
)

print(response)