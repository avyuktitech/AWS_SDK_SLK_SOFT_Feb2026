import boto3


def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)





create_group('S3Admins')