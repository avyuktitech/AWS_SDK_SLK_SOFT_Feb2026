import boto3


def get_ip(instance_id):
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))



get_ip('i-0cf2faaa79497a515')