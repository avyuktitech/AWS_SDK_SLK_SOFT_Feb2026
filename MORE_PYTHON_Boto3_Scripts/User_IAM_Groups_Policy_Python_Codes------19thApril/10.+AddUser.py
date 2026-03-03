import boto3


def add_user(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )

    print(response)



add_user('s3user', 'S3Admins')