import boto3



ec2_client = boto3.client('ec2')

response = ec2_client.authorize_security_group_ingress(
    GroupId='sg-09236e1682c8bd3ea',
    IpPermissions=[
        {
            'IpProtocol':'tcp',
            'FromPort':80,
            'ToPort':80,
            'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
        },
{
            'IpProtocol':'tcp',
            'FromPort':22,
            'ToPort':22,
            'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
        }
    ]
)

print(response)