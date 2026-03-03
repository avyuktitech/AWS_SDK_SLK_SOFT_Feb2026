import boto3


iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='testupdated',
    PolicyArn = 'arn:aws:iam::651366224884:policy/pyFullAccess'
)

print(response)