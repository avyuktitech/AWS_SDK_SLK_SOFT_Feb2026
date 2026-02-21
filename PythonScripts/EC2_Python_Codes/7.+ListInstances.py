import boto3

def get_instances():
    ec2_client = boto3.client('ec2', region_name='us-east-1')

    reservations = ec2_client.describe_instances().get('Reservations', [])

    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_id = instance.get('InstanceId')
            instance_type = instance.get('InstanceType')
            public_ip = instance.get('PublicIpAddress', 'N/A')   # Default if missing
            private_ip = instance.get('PrivateIpAddress', 'N/A') # Default if missing

            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")

get_instances()
