import boto3


ec2_client = boto3.client('ec2')

response = ec2_client.delete_key_pair(
    KeyName='mykey'
)

print(response)