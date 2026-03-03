import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.delete_security_group(
    GroupId='sg-09b9ab986cbea7bcf'
)

print(response)