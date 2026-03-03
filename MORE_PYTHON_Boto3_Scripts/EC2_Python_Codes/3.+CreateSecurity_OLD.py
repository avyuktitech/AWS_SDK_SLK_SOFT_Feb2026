import boto3



ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description="This is desc",
    GroupName="pygroup",
    VpcId='vpc-027321ec9ba89707b'
)

print(response)