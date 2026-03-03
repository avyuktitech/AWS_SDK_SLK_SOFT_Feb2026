import boto3


def get_instances():
    ec2_client = boto3.client('ec2')

    # Initialize a list to store instance details
    instance_details = []

    # Retrieve instances with pagination
    paginator = ec2_client.get_paginator('describe_instances')
    for page in paginator.paginate():
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']

                # Safely retrieve PublicIpAddress
                public_ip = instance.get('PublicIpAddress', 'N/A')

                # Safely retrieve PrivateIpAddress
                private_ip = instance.get('PrivateIpAddress', 'N/A')

                # Append instance details to the list
                instance_details.append((instance_id, instance_type, public_ip, private_ip))

    # Print instance details
    for instance_id, instance_type, public_ip, private_ip in instance_details:
        print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")


# Call the function to retrieve and print instance details
get_instances()
