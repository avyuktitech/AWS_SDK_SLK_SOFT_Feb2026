import boto3

# Initialize EC2 client for US East (N. Virginia)
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Describe images compatible with t2.micro
response = ec2_client.describe_images(
    Owners=['amazon'],  # official Amazon AMIs
    Filters=[
        {'Name': 'architecture', 'Values': ['x86_64']},  # t2.micro is x86_64
        {'Name': 'virtualization-type', 'Values': ['hvm']},  # HVM required
        {'Name': 'root-device-type', 'Values': ['ebs']},  # EBS-backed
        {'Name': 'state', 'Values': ['available']},
        {'Name': 'name', 'Values': ['amzn2-ami-hvm-*-x86_64-gp2']}  # Amazon Linux 2
    ]
)

# Print AMI ID and Name (latest first)
images = sorted(response['Images'], key=lambda x: x['CreationDate'], reverse=True)
for image in images:
    print(image['ImageId'], "-", image['Name'], "-", image['CreationDate'])
