import boto3


def list_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="AWS"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('Policy Name : {} Arn : {}'.format(policy_name, Arn))


list_policies()