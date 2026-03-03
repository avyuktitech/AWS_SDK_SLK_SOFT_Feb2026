import boto3

iam_client = boto3.client('iam')

user_name = 'user1'

tag_keys = ['Department', 'Project']

iam_client.untag_user(UserName=user_name, TagKeys=tag_keys)