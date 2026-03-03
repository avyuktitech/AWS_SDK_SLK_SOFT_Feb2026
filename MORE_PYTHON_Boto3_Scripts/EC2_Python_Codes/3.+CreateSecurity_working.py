import boto3


ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description="This is desc111",
    GroupName="pygroup111",
    VpcId='vpc-06d045569e6544444'
)

print(response)