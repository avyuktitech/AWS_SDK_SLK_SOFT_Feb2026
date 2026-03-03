import boto3

iam_client = boto3.client('iam')

user_name = 'user1'

tags = [{'Key':'Department', 'Value':'HR'}, {'Key':'Project', 'Value':'Onboarding'}]

iam_client.tag_user(UserName=user_name, Tags=tags)

print('Tag Added')