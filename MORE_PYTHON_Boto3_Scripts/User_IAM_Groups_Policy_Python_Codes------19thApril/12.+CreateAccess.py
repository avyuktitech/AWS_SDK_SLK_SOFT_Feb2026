import boto3

'''
def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)



create_access('testuser')

'''


def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIAZPKDT2P2K2ESBO4H',
        Status='Inactive',
        UserName='testuser'

    )


update_access()




