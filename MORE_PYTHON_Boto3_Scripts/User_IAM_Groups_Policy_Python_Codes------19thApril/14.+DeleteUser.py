import boto3


def delete_myuser(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)



delete_myuser('test')