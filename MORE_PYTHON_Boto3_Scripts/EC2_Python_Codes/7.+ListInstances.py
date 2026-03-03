import boto3


def get_instances():
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances().get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            public_ip = instance['PublicIpAddress']
            private_ip = instance['PrivateIpAddress']

            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")


get_instances()